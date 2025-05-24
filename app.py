from flask import Flask, render_template, redirect, url_for, request, session
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'supersecret'  # cần thiết cho session

# Cấu hình SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model sản phẩm
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    image = db.Column(db.String(300))

# Flask-Admin
admin = Admin(app, name='Quản trị cửa hàng', template_mode='bootstrap4')
admin.add_view(ModelView(Product, db.session))

# Tạo database nếu chưa có
with app.app_context():
    db.create_all()

# Hàm tìm sản phẩm theo ID
def get_product(product_id):
    return Product.query.get(product_id)

@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)

@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(product_id)
    session.modified = True
    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    cart_items = []
    total = 0
    for pid in session.get("cart", []):
        product = get_product(pid)
        if product:
            cart_items.append(product)
            total += product.price
    return render_template("cart.html", cart=cart_items, total=total)

@app.route("/checkout")
def checkout():
    session.pop("cart", None)
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
