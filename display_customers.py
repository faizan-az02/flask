from flask import Blueprint, render_template
from extensions import db
from models import Customer, Order, Address

bp = Blueprint('display', __name__)

@bp.route('/users')
def show_users():
    users = Customer.query.all()
    # Prepare a list of dicts with user info, orders, and addresses
    user_data = []
    for user in users:
        orders = Order.query.filter_by(customer_id=user.id).all()
        addresses = Address.query.filter_by(customer_id=user.id).all()
        user_data.append({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'orders': orders,
            'addresses': addresses
        })
    return render_template('users.html', users=user_data)
