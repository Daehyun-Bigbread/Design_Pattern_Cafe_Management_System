const drinkPrices = {
    coffee: 5,
    latte: 6,
    greenTea: 4,
    blackTea: 4
};

const drinkIngredients = {
    coffee: ['coffee bean: 1', 'water: 200ml'],
    latte: ['coffee bean: 1', 'milk: 100ml', 'water: 100ml'],
    greenTea: ['green tea powder: 1', 'water: 200ml'],
    blackTea: ['black tea: 1', 'water: 200ml']
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

    fetch('/make_payment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ method: method, amount: amount })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            if (data.message === "Payment processed successfully") {
                const paymentHistoryList = document.getElementById('payment-history-list');
                const listItem = document.createElement('li');
                listItem.textContent = `Paid ${amount} using ${method}`;
                paymentHistoryList.appendChild(listItem);
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
    const threshold = parseInt(document.getElementById('inventory-threshold').value);

    if (!item || isNaN(quantity) || quantity <= 0) {
        alert('Please enter a valid item and quantity.');
        return;
    }

    fetch('/add_inventory', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ item: item, quantity: quantity, threshold: threshold })
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
    const item = document.getElementById('inventory-item').value;
    const quantity = parseInt(document.getElementById('inventory-quantity').value);

    if (!item || isNaN(quantity)) {
        alert('Please enter a valid item and quantity.');
        return;
    }

    fetch('/update_inventory', {
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

function updateInventoryHistory() {
    fetch('/get_inventory')
    .then(response => response.json())
    .then(data => {
        const inventoryHistoryList = document.getElementById('inventory-history-list');
        inventoryHistoryList.innerHTML = ''; // Clear existing list
        for (const [item, quantity] of Object.entries(data)) {
            const listItem = document.createElement('li');
            listItem.textContent = `${item}: ${quantity}`;
            inventoryHistoryList.appendChild(listItem);
        }
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
        if (data.message) {
            alert(data.message);
            const drinkHistoryList = document.getElementById('drink-history-list');
            const listItem = document.createElement('li');
            listItem.textContent = data.message;
            drinkHistoryList.appendChild(listItem);
        }
        if (data.inventory) {
            updateInventoryHistory();
        }
    })
    .catch(error => console.error('Error:', error));

    // Set the price and ingredients
    document.getElementById('drink-price').value = drinkPrices[drinkType];
    document.getElementById('drink-price-text').innerText = `${drinkPrices[drinkType]} $`;

    const ingredientsList = document.getElementById('drink-ingredients-list');
    ingredientsList.innerHTML = ''; // Clear existing list
    drinkIngredients[drinkType].forEach(ingredient => {
        const listItem = document.createElement('li');
        listItem.textContent = ingredient;
        ingredientsList.appendChild(listItem);
    });
}

// 초기화 함수
document.addEventListener('DOMContentLoaded', () => {
    updateInventoryHistory();
});
