from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(300), nullable=True)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists('store.db'):
            db.create_all()
            # Add demo data
            items = [
                Product(name="T-shirt", price=19.99, description="Cool cotton T-shirt", image_url="static/tshirt.jpg"),
                Product(name="Jeans", price=49.99, description="Denim jeans", image_url="static/Jeans.jpg"),
                Product(name="Cap", price=9.99, description="Stylish summer cap", image_url="static/cap.jpg")
            ]
            db.session.add_all(items)
            db.session.commit()

    # Note: Set debug=False in production
    app.run(debug=True)

    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
