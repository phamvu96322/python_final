from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'supersecret'  # cần thiết cho session

# Sản phẩm mẫu
products = [
    {"id": 1, "name": "Áo thun", "price": 150000, "image": "https://thuthuatnhanh.com/wp-content/uploads/2022/08/ao-thun-in-hinh-theo-yeu-cau.jpg"},
    {"id": 2, "name": "Quần jeans", "price": 300000, "image": "https://bizweb.dktcdn.net/thumb/1024x1024/100/369/522/products/quan-jean-nu-suong-ong-rong-dkmv-thigh-destroyed-jean.png?v=1617941061910"},
    {"id": 3, "name": "Giày thể thao", "price": 500000, "image": "https://2.bp.blogspot.com/-f6WKVS7-ri0/WMeY50UMbNI/AAAAAAAABK8/7kT2o1tj6e43kt_7tnhr4MMLFSX0yWhRgCLcB/s1600/giay-the-thao-cho-nam.jpg"},
]

# Hàm tìm sản phẩm theo ID
def get_product(product_id):
    return next((p for p in products if p["id"] == product_id), None)

@app.route("/")
def index():
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
            total += product["price"]
    return render_template("cart.html", cart=cart_items, total=total)

@app.route("/checkout")
def checkout():
    session.pop("cart", None)
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)