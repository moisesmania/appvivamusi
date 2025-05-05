from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {
    "joao": "senha123",
    "maria": "abc456"
}

# Estrutura para guardar bandas e músicas
bands_db = bands_db = {
    'Banda X': ['Música 1', 'Música 2'],
    'Banda Y': ['Música A']
}


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('user_home'))
    else:
        return render_template('index.html', error="Credenciais inválidas.")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/user')
def user_home():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('user_home.html', bands=bands_db)

@app.route('/add_band', methods=['POST'])
def add_band():
    if 'username' not in session:
        return redirect(url_for('index'))
    band_name = request.form['band_name']
    if band_name and band_name.strip():
        bands_db[band_name] = []
    return redirect(url_for('user_home'))

@app.route('/delete_band/<band_name>')
def delete_band(band_name):
    bands_db.pop(band_name, None)
    return redirect(url_for('user_home'))

@app.route('/edit_band/<old_name>', methods=['POST'])
def edit_band(old_name):
    new_name = request.form['new_band_name']
    if new_name and new_name.strip():
        bands_db[new_name] = bands_db.pop(old_name)
    return redirect(url_for('user_home'))

@app.route('/add_music/<band_name>', methods=['POST'])
def add_music(band_name):
    music_name = request.form['music_name']
    if music_name and music_name.strip():
        bands_db[band_name].append(music_name)
    return redirect(url_for('user_home'))

@app.route('/delete_music/<band_name>/<int:music_index>')
def delete_music(band_name, music_index):
    if 0 <= music_index < len(bands_db.get(band_name, [])):
        bands_db[band_name].pop(music_index)
    return redirect(url_for('user_home'))

@app.route('/edit_music/<band_name>/<int:music_index>', methods=['POST'])
def edit_music(band_name, music_index):
    new_music_name = request.form['new_music_name']
    if new_music_name and new_music_name.strip():
        bands_db[band_name][music_index] = new_music_name
    return redirect(url_for('user_home'))

if __name__ == "__main__":
    app.run(debug=True)
