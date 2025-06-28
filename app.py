from flask import Flask, render_template, request, redirect
from extensions import mysql
from display_customers import bp

def get_pass(filepath="C:/Faizan/Misc/Github/password.txt"):

    try:

        with open(filepath, 'r') as file:

            return file.readline().strip()
        
    except FileNotFoundError:

        print(f"Error: File '{filepath}' not found.")

        return None

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = get_pass()
app.config['MYSQL_DB'] = 'test'

mysql.init_app(app)

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

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()

        customer_id = cur.lastrowid

        cur.execute("INSERT INTO orders (customer_id, item_name, total_price) VALUES (%s, %s, %s)",
                    (customer_id, item_name, total_price))
        cur.execute("INSERT INTO addresses (customer_id, address_line, city, country) VALUES (%s, %s, %s, %s)",
                    (customer_id, address_line, city, country))
        
        mysql.connection.commit()
        
        cur.close()

        return redirect('/users')

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
