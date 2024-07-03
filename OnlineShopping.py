from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Load products from file
def load_products():
    products = []
    # Check if the file exists before trying to read it
    if os.path.exists('products.txt'):
        with open('products.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    product = {
                        'id': parts[0],
                        'name': parts[1],
                        'price': parts[2],
                        'type': parts[3],
                        'image': parts[4]
                    }
                    products.append(product)
    return products

# Save a new product to the file
def save_product(product):
    # Append a new product to the file with a newline
    with open('products.txt', 'a') as file:
        if os.path.getsize('products.txt') > 0:
            file.write("\n")
        file.write(f"{product['id']},{product['name']},{product['price']},{product['type']},{product['image']}")

        
@app.route('/')
def index():
    products = load_products()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_product = {
            'id': request.form['id'],
            'name': request.form['name'],
            'price': request.form['price'],
            'type': request.form['type'],
            'image': request.form['image']
        }
        save_product(new_product)
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
