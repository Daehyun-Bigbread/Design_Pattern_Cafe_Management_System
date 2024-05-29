let totalAmount = 0;
let totalSales = 0;
let paymentTotals = {
    creditCard: 0,
    debitCard: 0,
    cash: 0,
    gift: 0
};
let drinkCounts = {
    coffee: 0,
    latte: 0,
    greenTea: 0,
    blackTea: 0
};

const drinkPrices = {
    coffee: 5,
    latte: 6,
    greenTea: 4,
    blackTea: 4
};

function setPaymentMethod(method) {
    document.getElementById('payment-method').value = method;
}

function makePayment() {
    const method = document.getElementById('payment-method').value;
    const amount = parseFloat(document.getElementById('payment-amount').value);

    if (!method || isNaN(amount) || amount <= 0) {
        alert('Please enter a valid payment method and amount.');
        return;
    }

    if (amount < totalAmount) {
        alert('Insufficient amount to cover the total price.');
        return;
    }

    const paymentDetails = {
        method: method,
        amount: totalAmount,
        drinkCounts: drinkCounts
    };

    fetch('/make_payment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(paymentDetails)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            if (data.message === "Payment processed successfully") {
                const paymentHistoryList = document.getElementById('payment-history-list');
                const listItem = document.createElement('li');
                
                let drinksPurchased = Object.entries(drinkCounts)
                    .filter(([drink, count]) => count > 0)
                    .map(([drink, count]) => `${count} ${drink.charAt(0).toUpperCase() + drink.slice(1)}`)
                    .join(', ');
                
                if (drinksPurchased !== '') {
                    listItem.textContent = `Paid ${totalAmount}$ using ${method} | Buy ${drinksPurchased}`;
                    paymentHistoryList.appendChild(listItem);
                }
                
                // Update total sales
                totalSales = data.total_sales;
                document.getElementById('total-sales').textContent = `${totalSales}$`;
                
                // Update payment totals
                paymentTotals = data.payment_totals;
                updateTotalSales();

                // Reset total amount
                totalAmount = 0;
                document.getElementById('total-amount').value = totalAmount;
            }
        }
    })
    .catch(error => console.error('Error:', error));
}

function setInventoryItem(item) {
    document.getElementById('inventory-item').value = item;
}

function addInventory() {
    const item = document.getElementById('inventory-item').value;
    const quantity = parseInt(document.getElementById('inventory-quantity').value);

    if (!item || isNaN(quantity) || quantity <= 0) {
        alert('Please enter a valid item and quantity.');
        return;
    }

    fetch('/add_inventory', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ item: item, quantity: quantity })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            updateInventoryHistory();
        }
    })
    .catch(error => console.error('Error:', error));
}

function updateInventory() {
    updateInventoryHistory();
}

function updateInventoryHistory() {
    fetch('/get_inventory')
    .then(response => response.json())
    .then(data => {
        document.getElementById('coffee-bean-quantity').textContent = data['coffee bean'] || 0;
        document.getElementById('milk-quantity').textContent = `${data['milk'] || 0} ml`;
        document.getElementById('green-tea-powder-quantity').textContent = data['green tea powder'] || 0;
        document.getElementById('water-quantity').textContent = `${data['water'] || 0} ml`;
        document.getElementById('black-tea-quantity').textContent = data['black tea powder'] || 0;
    })
    .catch(error => console.error('Error:', error));
}

function makeDrink(drinkType) {
    fetch('/make_drink', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ drink_type: drinkType })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            const drinkHistoryList = document.getElementById('drink-history-list');
            const listItem = document.createElement('li');
            listItem.textContent = data.message;
            drinkHistoryList.appendChild(listItem);
        } else {
            alert(data.message);
        }
        if (data.inventory) {
            updateInventoryHistory();
        }
    })
    .catch(error => console.error('Error:', error));

    // Update total amount and drink counts
    totalAmount += drinkPrices[drinkType];
    document.getElementById('total-amount').value = totalAmount;
    drinkCounts[drinkType]++;
    updateDrinkHistory();
}

function updateDrinkHistory() {
    document.getElementById('coffee-count').textContent = drinkCounts.coffee;
    document.getElementById('latte-count').textContent = drinkCounts.latte;
    document.getElementById('green-tea-count').textContent = drinkCounts.greenTea;
    document.getElementById('black-tea-count').textContent = drinkCounts.blackTea;
}

function updateTotalSales() {
    document.getElementById('credit-card-total').textContent = `${paymentTotals.creditCard}$`;
    document.getElementById('debit-card-total').textContent = `${paymentTotals.debitCard}$`;
    document.getElementById('cash-total').textContent = `${paymentTotals.cash}$`;
    document.getElementById('gift-card-total').textContent = `${paymentTotals.gift}$`;
    document.getElementById('total-sales').textContent = `${totalSales}$`;
}

// 초기화 함수
document.addEventListener('DOMContentLoaded', () => {
    updateInventoryHistory();
    fetch('/get_total_sales')
        .then(response => response.json())
        .then(data => {
            totalSales = data.total_sales;
            paymentTotals = data.payment_totals;
            drinkCounts = data.drink_counts;
            updateTotalSales();
            updateDrinkHistory();
        })
        .catch(error => console.error('Error:', error));
});

