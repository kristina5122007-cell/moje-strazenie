from flask import Flask, render_template, request

app = Flask(__name__)

# Hlavná stránka s tvojimi údajmi
@app.route('/')
def index():
    return render_template('index.html')

# Stránka, ktorá sa zobrazí po odoslaní formulára
@app.route('/kontakt', methods=['POST'])
def kontakt():
    meno = request.form.get('meno')
    email = request.form.get('email')
    sluzba = request.form.get('sluzba')
    sprava = request.form.get('sprava')
    
    # Tu by si mohol dáta uložiť do databázy alebo poslať mailom
    print(f"Nová správa od: {meno} ({email}) - Služba: {sluzba}")
    
    return f"<h3>Ďakujem, {meno}! Tvoja správa ohľadom {sluzba} bola prijatá. Čoskoro sa ti ozvem.</h3>"

if __name__ == '__main__':
    app.run(debug=True)