from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'spblove123'

users = {'admin': {'password': 'admin_pass'},
         'user1': {'password': 'user1_pass'}}

menu_items = [
    {'id': 1, 'name': 'Dish 1', 'price': 10.99},
    {'id': 2, 'name': 'Dish 2', 'price': 12.99},
    {'id': 3, 'name': 'Dish 3', 'price': 8.99}
]

orders = []

authentication = []

def authenticate(username, password):
    user = users.get(username)
    if user and user['password'] == password:
        return True
    return False

# Маршруты приложения
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if authenticate(username, password):
            authentication.append(str(request.headers.get('User-Agent')))
            return redirect(url_for('menu', username=username))
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html', error=None)

@app.route('/menu/<username>')
def menu(username):
    if str(request.headers.get('User-Agent')) in authentication:
        return render_template('menu.html', username=username, menu=menu_items)

@app.route('/dashboard/<username>')
def dashboard(username):
    if str(request.headers.get('User-Agent')) in authentication:
        return render_template('dashboard.html', username=username, menu=menu_items, orders=orders)

@app.route('/logout')
def logout():
    if str(request.headers.get('User-Agent')) in authentication:
        return redirect(url_for('login'))

@app.route('/order/<username>/<int:item_id>')
def order(username, item_id):
    selected_item = next((item for item in menu_items if item['id'] == item_id), None)
    if selected_item:
        orders.append({'username': username, 'item': selected_item})
    return redirect(url_for('dashboard', username=username))

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

@app.route('/edit_menu')
def edit_menu():
    return render_template('edit_menu.html')
@app.route('/user_table')
def user_table():
    return render_template('user_table.html')

@app.route('/order_list')
def order_list():
    return render_template('order_list.html')

if __name__ == '__main__':
    app.run(debug=True)
