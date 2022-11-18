from flask import Flask,render_template,redirect, url_for, request, session
import ibm_db
COS_ENDPOINT="https://s3.jp-tok.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID="eMcex_1Ai5Ee0zdY02faN3xOI11a0n00ousBac2XmyeT"
COS_INSTANCE_CRN="crn:v1:bluemix:public:cloud-object-storage:global:a/fd8584e5ab4b4110b3cdf639fd12266c:43ac326a-7436-4af1-ab27-4359450ec159::"


conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32459;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=pwk11780;PWD=9iemmWzszDMP5WQf",'','')



app=Flask(__name__)

@app.route('/home1')
def home1():
    return render_template("home1.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/value_insert', methods = ['GET', 'POST'])
def value_insert():
    Email = request.form['Email']
    password = request.form['password']
    rpassword = request.form['rpassword']
    
    insert_sql = "INSERT INTO signup VALUES (?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, Email)
    ibm_db.bind_param(prep_stmt, 2, password)
    ibm_db.bind_param(prep_stmt, 3, rpassword)
    ibm_db.execute(prep_stmt)
   
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/signin', methods=['Post', 'Get'])
def signin():
    
        return render_template("signin.html")

@app.route('/features')
def features():
    return render_template("features.html")


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)