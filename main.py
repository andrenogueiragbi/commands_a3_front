import re
from app import app
from flask import  redirect, url_for, render_template, request, session,flash
from app.controllers.login import makelogin
from app.controllers.register import makeRegister
from app.controllers.APIcommands import searchCommandSpecific,saveCommand, deleteCommand,updateCommand
from app.controllers.APItype import searchTypeCommands
import json


@app.route("/search/<type>",methods=["GET","POST"])
def search(type):



    if(type and "user" in session):

        user = session["user"]

        data = searchCommandSpecific(type)            
        types = searchTypeCommands()


        if(not data["erro"]):
            
            return render_template("home.html",user=user, data = data['commands'],types = types['types'])


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
        

        return render_template("login.html",erro=True,message=statusLogin['message'])
   

    return render_template("login.html")


@app.route("/",methods=["GET", "POST"])
def home(): 

    if "user" in session:
        
        user = session["user"]

        data = searchCommandSpecific('Linux')
        types = searchTypeCommands()
        

        return render_template("home.html",user=user, data = data['commands'],types = types['types'])
    

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



@app.route("/commandDelete/<id>/",methods=["GET", "POST"])
def commandDelete(id):


    if "user" in session and id:
        
        user = session["user"]

        id = id.split('-')

        resultsave = deleteCommand(int(id[0]))

        if(resultsave['erro']):

            flash(f"O {resultsave['message']}!")





        return redirect(url_for(f'search',type=id[1]))
    

    return redirect(url_for('login'))




@app.route("/save",methods=["GET", "POST"])
def saveCommands(): 

    if "user" in session:
        
        user = session["user"]

        if request.method == "POST":

            id = request.form.get("id").split('-')
            pagNewComands = id[1]
            title = request.form.get("title")
            description = request.form.get("description")
            commands = request.form.get("commands")
            tags = request.form.get("tags")
            creator = request.form.get("creator")

            print(pagNewComands,'...')

            resultsave = saveCommand(int(id[0]),title,description,commands,tags,creator)

            if(resultsave['erro']):

                flash(f"O {resultsave['message']}!")



        
            return redirect(url_for(f'search',type=id[1]))

    

    return redirect(url_for('login'))





@app.route("/update/<idCommands>",methods=["GET", "POST"])
def updateCommands(idCommands): 

    if "user" in session:
        
        user = session["user"]

        if request.method == "POST":

            id = request.form.get("id").split('-')

            print('array',id)

            print('o id  type_id é esse:', id[0])
            print('o id idCommands da url é esse:', idCommands)




            pagNewComands = id[1]
            title = request.form.get("title")
            description = request.form.get("description")
            commands = request.form.get("commands")
            tags = request.form.get("tags")
            creator = request.form.get("creator")


            resultsave = updateCommand(idCommands,int(id[0]),title,description,commands,tags,creator)

          
            if(resultsave['erro']):

                flash(f"O {resultsave['message']}!")




        
            return redirect(url_for(f'search',type=pagNewComands))

    

    return redirect(url_for('login'))


######################################################

if __name__ == "__main__":
    app.run(debug=True)


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