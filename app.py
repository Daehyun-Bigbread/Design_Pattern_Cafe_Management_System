from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from payment_module import PaymentFactory, FinancialStatementObserver, Payment
from cafe_handler_module import CafeHandler
from inventory_module import InventoryManager
from drink_module import DrinkFactory

app = Flask(__name__)
CORS(app)  # 모든 출처에서의 요청을 허용

payment_factory = PaymentFactory()
payment_handler = CafeHandler()
financial_observer = FinancialStatementObserver()
payment_system = Payment()
payment_system.add_observer(financial_observer)

inventory_manager = InventoryManager()
drink_factory = DrinkFactory()

total_sales = 0
payment_totals = {
    "creditCard": 0,
    "debitCard": 0,
    "cash": 0,
    "gift": 0
}

drink_counts = {
    "coffee": 0,
    "latte": 0,
    "greenTea": 0,
    "blackTea": 0
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make_drink', methods=['POST'])
@cross_origin()
def make_drink():
    data = request.json
    drink_type = data['drink_type'].replace(" ", "").lower()
    
    try:
        drink = drink_factory.create_drink(drink_type)
        result = drink.make(inventory_manager)
        if "is made" in result:
            drink_counts[drink_type] += 1
            return jsonify({"message": result, "inventory": inventory_manager.get_inventory(), "drink_counts": drink_counts, "success": True})
        return jsonify({"message": result, "success": False})
    except ValueError as e:
        return jsonify({"message": str(e), "success": False}), 400

@app.route('/make_payment', methods=['POST'])
@cross_origin()
def make_payment():
    data = request.json
    method = data['method']
    amount = data['amount']
    drink_counts = data['drinkCounts']

    try:
        payment_strategy = payment_factory.create_payment(method)
        payment_system.make_payment(amount, payment_strategy)
        global total_sales
        total_sales += amount
        payment_totals[method] += amount
        return jsonify({
            "message": "Payment processed successfully",
            "total_sales": total_sales,
            "payment_totals": payment_totals,
            "drink_counts": drink_counts
        })
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@app.route('/get_inventory', methods=['GET'])
@cross_origin()
def get_inventory():
    return jsonify(inventory_manager.get_inventory())

@app.route('/add_inventory', methods=['POST'])
@cross_origin()
def add_inventory():
    data = request.json
    item = data['item']
    quantity = data['quantity']

    inventory_manager.add_item(item, quantity)
    return jsonify({"message": "Inventory added successfully", "inventory": inventory_manager.get_inventory()})

@app.route('/update_inventory', methods=['POST'])
@cross_origin()
def update_inventory():
    data = request.json
    item = data['item']
    quantity = data['quantity']

    inventory_manager.update_inventory(item, quantity)
    return jsonify({"message": "Inventory updated successfully", "inventory": inventory_manager.get_inventory()})

@app.route('/get_total_sales', methods=['GET'])
@cross_origin()
def get_total_sales():
    return jsonify({"total_sales": total_sales, "payment_totals": payment_totals, "drink_counts": drink_counts})

if __name__ == '__main__':
    app.run(debug=True)
