from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #hjemside
def index():
    return render_template('index.html')

@app.route('/om_oss') #om oss side
def about():
    return render_template('om_oss.html')

@app.route('/kontakt') #kontakt side
def contact():
    return render_template('kontakt.html')


if __name__ == '__main__':
    app.run(debug=True) # debug slik at vi ikke må restarte siden for hver endring

#