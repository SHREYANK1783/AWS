from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Stocker"

@app.route('/dashboard_admin')
def dashboard_admin():
    return render_template('dashboard_admin.html')

@app.route('/dashboard_trader')
def dashboard_trader():
    return render_template('dashboard_trader.html')

@app.route('/buy_stock')
def buy_stock():
    return render_template('buy_stock.html')

@app.route('/sell_stock')
def sell_stock():
    return render_template('sell_stock.html')

@app.route('/service_details_5')
def service_details_5():
    return render_template('service_details_5.html')

if __name__ == '__main__':
    app.run(debug=True)