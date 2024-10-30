from flask import Flask , render_template , request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/base')
def base():
    return render_template('base.html')
@app.route('/register',methods=['GET'])
def register():
    name=request.args.get('name')
    number=request.args.get('number')
    email=request.args.get('email')
    return render_template('register.html',name=name,number=number,email=email)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/product')
def product():
    return render_template('product.html')
@app.route('/contact')
def contact():
    return render_template('contact.html') 
@app.route('/login', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['name'] == 'user' and request.form['password'] == 'yestech':
            return render_template('dashboard.html') 
        else:
            error = "Wrong User Name or Password"
            return render_template('login.html',error=error) 
    else:
        return render_template('login.html')
app.add_url_rule('/home','home',home)
if __name__ == '__main__':
    app.run(debug = True)