from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Models
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    cash_balance = db.Column(db.Float, default=1000.0)  # Initial cash balance

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String(50), unique=True, nullable=False)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.String(50), unique=True, nullable=False)
    item_id = db.Column(db.String(50), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sales_id = db.Column(db.String(50), unique=True, nullable=False)
    item_id = db.Column(db.String(50), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Create the tables
with app.app_context():
    db.create_all()

# Initialize the company details
def init_company():
    with app.app_context():
        company = Company.query.first()
        if not company:
            new_company = Company(company_name="Namma Kadai", cash_balance=10000.0)
            db.session.add(new_company)
            db.session.commit()

# Call the initialization function
init_company()

# Routes
@app.route("/")
def index():
    return render_template("index.html")

# Add Item
@app.route("/item", methods=["POST"])
def add_item():
    data = request.json
    new_item = Item(
        item_id=data["item_id"],
        item_name=data["item_name"],
        quantity=data["quantity"],
        price=data["price"]
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item added successfully!"}), 201

# Get all items
@app.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    items_list = [
        {"item_id": item.item_id, "item_name": item.item_name, "quantity": item.quantity, "price": item.price}
        for item in items
    ]
    return jsonify(items_list)

# Add Purchase
@app.route("/purchase", methods=["POST"])
def add_purchase():
    data = request.json
    purchase_amount = data["rate"] * data["qty"]

    # Update cash balance
    company = Company.query.first()
    company.cash_balance -= purchase_amount

    # Add to purchases table
    new_purchase = Purchase(
        purchase_id=data["purchase_id"],
        item_id=data["item_id"],
        rate=data["rate"],
        qty=data["qty"],
        amount=purchase_amount
    )
    db.session.add(new_purchase)
    db.session.commit()

    return jsonify({"message": "Purchase recorded successfully!"}), 201

# Add Sales
@app.route("/sales", methods=["POST"])
def add_sales():
    data = request.json
    sales_amount = data["rate"] * data["qty"]

    # Update cash balance
    company = Company.query.first()
    company.cash_balance += sales_amount

    # Add to sales table
    new_sale = Sale(
        sales_id=data["sales_id"],
        item_id=data["item_id"],
        rate=data["rate"],
        qty=data["qty"],
        amount=sales_amount
    )
    db.session.add(new_sale)
    db.session.commit()

    return jsonify({"message": "Sale recorded successfully!"}), 201

# View Report
@app.route("/report", methods=["GET"])
def view_report():
    total_items = Item.query.count()
    total_purchases = Purchase.query.count()
    total_sales = Sale.query.count()
    company = Company.query.first()

    report_data = [
        {"description": "Total Items", "value": total_items},
        {"description": "Total Purchases", "value": total_purchases},
        {"description": "Total Sales", "value": total_sales},
        {"description": "Current Cash Balance", "value": company.cash_balance}
    ]
    return jsonify(report_data)

if __name__ == "__main__":
    app.run(debug=True) 