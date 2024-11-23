
Namma Kadai is a web-based inventory and sales management application. It enables users to manage items, record purchases and sales, and track financial metrics, such as cash balance and stock levels.

Features:

Add Items
Add new items to the inventory with details such as ID, name, quantity, and price.

View Items
Display all items in the inventory with their details.

Make Purchases
Record purchases with quantity and rate, and update inventory stock and company cash balance.

Record Sales
Log sales transactions, update stock, and increase the company's cash balance.

View Reports
Summarize inventory statistics, total purchases, total sales, and the current cash balance.

Technology Stack:
Backend: Flask (Python)
Database: SQLite
Frontend: HTML, CSS, JavaScript
Styling: Custom CSS
Installation
Prerequisites
Python 3.x
Pip (Python package manager)
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/namma-kadai.git
cd namma-kadai
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open the app in your browser:

arduino
Copy code
http://127.0.0.1:5000
API Endpoints
1. Add Item
POST /item
Add a new item to the inventory.
Body (JSON):

json
Copy code
{
  "item_id": "item1",
  "item_name": "Laptop",
  "quantity": 10,
  "price": 50000
}
2. Get Items
GET /items
Fetch all items in the inventory.

3. Add Purchase
POST /purchase
Record a purchase.
Body (JSON):

json
Copy code
{
  "purchase_id": "pur1",
  "item_id": "item1",
  "qty": 5,
  "rate": 48000
}
4. Add Sales
POST /sales
Record a sale.
Body (JSON):

json
Copy code
{
  "sales_id": "sale1",
  "item_id": "item1",
  "qty": 3,
  "rate": 52000
}
5. View Report
GET /report
Fetch a summary of inventory, purchases, sales, and the company's cash balance.

Project Structure
php
Copy code
Namma-Kadai/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Frontend HTML file
├── static/
│   ├── styles.css         # Styling for the frontend
│   └── script.js          # Frontend JavaScript logic
├── database.db            # SQLite database file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
Screenshots
Home Page
Displays navigation links and welcome message.

Add Item
Form to add items to the inventory.

View Report
Shows key metrics like total items, sales, purchases, and cash balance.

Contributing
Contributions are welcome! Follow these steps:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Add feature"
Push to your branch:
bash
Copy code
git push origin feature-name