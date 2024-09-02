from flask import Flask, render_template, request

app = Flask(__name__)

# Mock cryptocurrency balances
balances = {
    "Bitcoin": 1.0,
    "Ethereum": 2.0,
    "Litecoin": 3.0,
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Update balances from user input
        for coin in balances.keys():
            try:
                balances[coin] = float(request.form[coin])
            except ValueError:
                pass  # Ignore invalid input
    return render_template('index.html', balances=balances)

if __name__ == '__main__':
    app.run(debug=True)
