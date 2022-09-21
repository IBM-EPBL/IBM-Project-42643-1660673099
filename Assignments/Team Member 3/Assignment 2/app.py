from flask import Flask,redirect,url_for,render_template,request,make_response

app=Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return render_template('home.html',name=name)
@app.route('/admin')
def admin():
    return render_template('index.html')
@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('hello_world',name=name))
@app.route('/page/<int:postID>')
def page(postID):
    return render_template('page.html',page=postID)
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['fname']
        password=request.form['lname']
        return "Username is "+user+"and the password is"+password
    if request.method=='GET':
        return render_template('login.html')
@app.route('/signup')
def signup():
        return render_template('signup.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/signin')
def signin():
    return render_template('signin.html')
@app.route('/about')
def about():
    return render_template('about.html')
if __name__=='__main__':
    app.run(host='192.168.226.179',port=8080,debug=True)
