import json
from app import app
from flask import  redirect, url_for, render_template, request, session
from app.controllers.login import makelogin
from app.controllers.register import makeRegister
from app.controllers.APIsearch import searchType
import os
import json


@app.route("/search/<type>",methods=["GET","POST"])
def search(type):

    print(type)

    if(type and "user" in session):

        user = session["user"]

        data = searchType(type)
        print(data)

        if(not data["erro"]):
            
            return render_template("home.html",user=user, data = data['commands'])


    return redirect(url_for("login")) 


@app.route("/login",methods=["GET", "POST"])
def login():

    if session:
        token = session["user"]['token']
        result = search()

        if(token):
            return redirect(url_for("/")) 
  


    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")
    
        statusLogin = makelogin(email,password)

        if not statusLogin['erro']:

            session['user'] = statusLogin

            return redirect(url_for("home"))
        

        return render_template("login.html",erro=True)
   

    return render_template("login.html")


@app.route("/",methods=["GET", "POST"])
def home(): 

    if "user" in session:
        
        user = session["user"]

        data = searchType('linux')
        

        return render_template("home.html",user=user, data = data['commands'])
    

    return redirect(url_for('login'))


@app.route("/logout",methods=["GET"])
def logout():

    print(">>>>>>>>>>>>>",session) 

    session.pop('user', None)
    return redirect(url_for('login'))

@app.route("/register",methods=["GET", "POST"])
def register():

    if session:
        token = session["user"]['token']

        if(token):
            return redirect(url_for("home")) 
  


    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        coupon = request.form.get("coupon")
        company = request.form.get("company")

        print(name,email,password,coupon,company)
    
        statusLogin = makeRegister(name,email,password,coupon,company)

        if not statusLogin['erro']:

            session['user'] = statusLogin

            return redirect(url_for("home"))
        

        return render_template("register.html",erro=True,message=statusLogin['message'])
   

    return render_template("register.html")



@app.route("/teste",methods=["GET"])
def teste():

    return render_template("teste.html")




######################################################

if __name__ == "__main__":
    app.run(port=3000, host='0.0.0.0', debug=True, threaded=True)


    """
    from flask import request

@app.route('/my-route')
def my_route():
  page = request.args.get('page', default = 1, type = int)
  filter = request.args.get('filter', default = '*', type = str)
Examples with the code above:

/my-route?page=34               -> page: 34  filter: '*'
/my-route                       -> page:  1  filter: '*'
/my-route?page=10&filter=test   -> page: 10  filter: 'test'
/my-route?page=10&filter=10     -> page: 10  filter: '10'
    """