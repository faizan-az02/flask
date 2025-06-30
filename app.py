from flask import Flask, render_template, request, redirect
from extensions import db
from display_customers import bp
from models import Customer, Order, Address

def get_pass(filepath = "C:/Faizan/Misc/Github/password.txt"):

    try:

        with open(filepath, 'r') as file:

            line = file.readline().strip()

            return line
        
    except FileNotFoundError:

        print(f"Error: File '{filepath}' not found.")

        return None

password = get_pass()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{password}@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register Blueprint from display_customers.py
app.register_blueprint(bp)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        item_name = request.form['item_name']
        total_price = request.form['total_price']
        address_line = request.form['address_line']
        city = request.form['city']
        country = request.form['country']

        customer = Customer(name=name, email=email)
        db.session.add(customer)
        db.session.commit()

        order = Order(customer_id=customer.id, item_name=item_name, total_price=total_price)
        db.session.add(order)
        address = Address(customer_id=customer.id, address_line=address_line, city=city, country=country)
        db.session.add(address)
        db.session.commit()

        return redirect('/users')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
