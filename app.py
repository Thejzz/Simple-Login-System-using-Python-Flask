from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Mock database for storing user credentials
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        
        # Check if the user already exists
        if name in users:
            flash('Username already exists!', 'warning')
            return redirect(url_for('register'))
        
        # Hash the password and save user details in the users dictionary
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        users[name] = {'name': name, 'password': hashed_password}
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        
        # Verify if the user exists and if the password matches
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            error = "Incorrect username or password"
    
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out!', 'info')
    return redirect(url_for('login'))

app.add_url_rule('/home', 'home', home)

if __name__ == '__main__':
    app.run(debug=True)
