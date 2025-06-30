from flask import Flask, render_template, request, redirect, session
from extensions import db
from display_customers import bp
from models import Customer, Order, Address
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

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
app.secret_key = 'c7e2b1f4a8d9e3c5f6b7a2d4e9c1f3b8a5d6c2e7b4f1a9c3e8d2b5a7f6c4e1b9'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{password}@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register Blueprint from display_customers.py
app.register_blueprint(bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']
        item_name = request.form['item_name']
        total_price = request.form['total_price']
        address_line = request.form['address_line']
        city = request.form['city']
        country = request.form['country']

        if password != confirm_password:
            error = 'Passwords do not match.'
            return render_template('register.html', error=error)

        password_hash = generate_password_hash(password)
        customer = Customer(name=name, password_hash=password_hash, email=email)
        db.session.add(customer)
        db.session.commit()

        order = Order(customer_id=customer.id, item_name=item_name, total_price=total_price)
        db.session.add(order)
        address = Address(customer_id=customer.id, address_line=address_line, city=city, country=country)
        db.session.add(address)
        db.session.commit()

        return redirect('/login')
    return render_template('register.html', error=error)

@app.route('/login', methods=['GET', 'POST'])

def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Customer.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            return redirect('/welcome')
        else:
            error = 'Invalid email or password.'
    return render_template('login.html', error=error)


@app.route('/welcome')
def welcome():
    user_name = session.get('user_name')
    if not user_name:
        return redirect('/login')
    return render_template('welcome.html', user_name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
