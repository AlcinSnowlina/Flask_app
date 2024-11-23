document.addEventListener("DOMContentLoaded", () => {
    const items = []; // Array to store items
    const purchases = []; // Array to store purchases
    let totalAmount = 1000; // Initial total amount

    // Add Item Form Handling
    const addItemForm = document.getElementById("addItemForm");
    const itemsList = document.getElementById("itemsList");

    addItemForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const itemId = document.getElementById("item_id").value.trim();
        const itemName = document.getElementById("item_name").value.trim();
        const quantity = parseInt(document.getElementById("quantity").value);
        const price = parseFloat(document.getElementById("price").value);

        if (itemId && itemName && quantity > 0 && price > 0) {
            // Add the item to the array
            items.push({ id: itemId, name: itemName, quantity, price });

            // Update the items list
            displayItems();

            // Clear form fields
            addItemForm.reset();
        } else {
            alert("Please fill in all fields correctly.");
        }
    });

    function displayItems() {
        itemsList.innerHTML = ""; // Clear existing items
        if (items.length === 0) {
            itemsList.innerHTML = "<p>No items added yet.</p>";
        } else {
            const ul = document.createElement("ul");
            items.forEach((item) => {
                const li = document.createElement("li");
                li.textContent = `ID: ${item.id}, Name: ${item.name}, Quantity: ${item.quantity}, Price: ₹${item.price.toFixed(2)}`;
                ul.appendChild(li);
            });
            itemsList.appendChild(ul);
        }
    }

    // Add Purchase Form Handling
    const addPurchaseForm = document.getElementById("addPurchaseForm");

    addPurchaseForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const purchaseId = document.getElementById("purchase_id").value.trim();
        const purchaseItemId = document.getElementById("purchase_item_id").value.trim();
        const qty = parseInt(document.getElementById("qty").value);
        const rate = parseFloat(document.getElementById("rate").value);

        const item = items.find((item) => item.id === purchaseItemId);

        if (rate <= 0 || qty <= 0) {
            alert("Please enter valid rate and quantity.");
            return;
        }

        // Handle new or existing items
        if (item) {
            if (item.quantity < qty) {
                alert("Insufficient stock.");
                return;
            }
            item.quantity -= qty; // Deduct stock for existing item
        }

        const purchaseTotal = rate * qty;

        if (purchaseTotal > totalAmount) {
            alert("Insufficient balance.");
            return;
        }

        totalAmount -= purchaseTotal; // Deduct purchase amount from total balance

        // Add the purchase to the array
        purchases.push({ id: purchaseId, itemId: purchaseItemId, qty, rate });

        // Update items list
        displayItems();

        // Clear form fields
        addPurchaseForm.reset();
    });

    // View Report Handling
    const viewReportButton = document.getElementById("viewReportButton");
    const reportDiv = document.getElementById("report");

    viewReportButton.addEventListener("click", () => {
        reportDiv.innerHTML = ""; // Clear existing report
        if (purchases.length === 0) {
            reportDiv.innerHTML = "<p>No purchases made yet.</p>";
        } else {
            const ul = document.createElement("ul");
            purchases.forEach((purchase) => {
                const li = document.createElement("li");
                li.textContent = `Purchase ID: ${purchase.id}, Item ID: ${purchase.itemId}, Quantity: ${purchase.qty}, Rate: ₹${purchase.rate.toFixed(2)}, Total: ₹${(purchase.rate * purchase.qty).toFixed(2)}`;
                ul.appendChild(li);
            });
            reportDiv.appendChild(ul);
        }

        // Display balance amount
        const balanceDiv = document.createElement("div");
        balanceDiv.textContent = `Balance Amount: ₹${totalAmount.toFixed(2)}`;
        balanceDiv.style.marginTop = "20px";
        balanceDiv.style.fontWeight = "bold";
        reportDiv.appendChild(balanceDiv);
    });
});
