from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #hjemside
def index():
    return render_template('index.html')

@app.route('/om_oss') #om oss side
def about():
    return render_template('om_oss.html')

@app.route('/kontakt') #kontakt side
def kontact():
    kontaktliste = [
        {"navn": "Kjartan Lang Holmen", "alder": "Hvem vet?", "fag": "God IT mann, er lat IT mann", "tlf": "+47 987 65 432", "bilde": "Kjartan.jpeg"},
        {"navn": "Ebbe Gassed On Zelow", "alder": "17", "fag": "230mg koffein om kvelden er bra :P", "tlf": "+47 245 23 678", "bilde": "ebbe.png"},
        {"navn": "Nikolai Haukland", "alder": "17", "fag": "Klarer ikke sitte vanlig", "tlf": "+47 234 56 789", "bilde": "nikolai.png"}, 
        {"navn": "Ludvig Haukland", "alder": "17", "fag": "Det er bare sånn det blir!", "tlf": "+47 123 45 678", "bilde": "ludvig.png"}
    ]
    return render_template('kontakt.html', kontaktliste=kontaktliste)


if __name__ == '__main__':
    app.run(debug=True) # debug slik at vi ikke må restarte siden for hver endring

#