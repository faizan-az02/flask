from flask import Blueprint, render_template
from extensions import mysql

bp = Blueprint('display', __name__)

@bp.route('/users')

def show_users():

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM customers")

    users = cur.fetchall()

    cur.close()

    return render_template('users.html', users=users)
