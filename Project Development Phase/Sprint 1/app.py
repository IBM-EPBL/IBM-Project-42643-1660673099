from flask import Flask,render_template

app=Flask(__name__)

@app.route('/Dashboard')
def Dashboard():
    return render_template("Dashboard.html")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)