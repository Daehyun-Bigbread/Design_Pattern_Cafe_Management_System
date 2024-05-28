from flask import Flask, request, jsonify
from payment_module import PaymentFactory, FinancialStatementObserver, Payment
from cafe_handler_module import CafeHandler
from inventory_module import InventoryManager

app = Flask(__name__)

payment_handler = CafeHandler()
financial_observer = FinancialStatementObserver()
payment_system = Payment()
payment_system.add_observer(financial_observer)

inventory_manager = InventoryManager()

@app.route('/make_payment', methods=['POST'])
def make_payment():
    data = request.json
    method = data['method']
    amount = data['amount']

    req = {"method": method, "amount": amount}
    payment_system.make_payment(req, payment_handler)
    return jsonify({"message": "Payment processed successfully", "total_payments": payment_handler.payments})

@app.route('/add_inventory', methods=['POST'])
def add_inventory():
    data = request.json
    item = data['item']
    quantity = data['quantity']
    threshold = data['threshold']

    inventory_manager.add_item(item, quantity, threshold)
    return jsonify({"message": "Inventory added successfully", "inventory": inventory_manager.get_inventory()})

@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    data = request.json
    item = data['item']
    quantity = data['quantity']

    inventory_manager.update_inventory(item, quantity)
    return jsonify({"message": "Inventory updated successfully", "inventory": inventory_manager.get_inventory()})

if __name__ == '__main__':
    app.run(debug=True)