from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def home():
    
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # Print to console
        print("User Registration:")
        print("Name:", name)
        print("Email:", email)
        print("Username:", username)
        print("Password:", password)

        return "Form submitted! Check console."

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
