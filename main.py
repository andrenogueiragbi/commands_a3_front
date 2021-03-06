from app import app
from flask import redirect, url_for, render_template, request, session, flash
from app.controllers.login import makelogin
from app.controllers.register import makeRegister,createTicket
from app.controllers.APIcommands import searchCommandSpecific, saveCommand, deleteCommand, updateCommand
from app.controllers.APItype import searchTypeCommands
from app.controllers.APiuser import searchUser,saveNewUser,deleteUser,updateUser,searchUserId
import json
import time
""" import logging

logging.basicConfig(level=logging.DEBUG) """

# ROTA DE CRIAR NOVO TICKET
@app.route("/newticket/", methods=["GET", "POST"])
def newticket():

    # VERIFICA SE USUÁRIO ESTAR LOGADO
    if "user" in session:

        user = session["user"]
        token = user.get('token')

        # PEGANDO DADOS PARA ATUALIZAR COMANDO
        if request.method == "POST":

            email = request.form.get("email")

            # CHAMANDO API PARA CRIAR TIKET
            resultsave = createTicket(email,token)



            # FAZENDO VALIDAÇÃO DA API DEPOIS DE CRIADO TICKET
            if(resultsave['erro']):
                flash(f"Erro: {resultsave['message']}!", 'danger')
                return redirect(url_for(f'config'))
            else:

                flash(f"Sucesso: Ticket criado pra o {resultsave['tiketNew']['email_user']} - NÚMERO: {resultsave['tiketNew']['number']}", 'success')
                return redirect(url_for(f'config'))

    return redirect(url_for('login'))




# ROTA DE ATULIZAR PERFIL
@app.route("/userUpdatePerfil/<idUser>", methods=["GET", "POST"])
def userUpdatePerfil(idUser):

    # VERIFICA SE USUÁRIO ESTAR LOGADO
    if "user" in session:

        user = session["user"]
        token = user.get('token')

        # PEGANDO DADOS PARA ATUALIZAR PERFIL
        if request.method == "POST":

            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")
            level = request.form.get("level")
            company = request.form.get("company")


            # CHAMANDO API PARA ATUALIZAR PERFIL
            resultsave = updateUser(idUser, name,email,password,level,company,token)

            # FAZENDO VALIDAÇÃO DA API AO ATUALIZAR PERFIL
            if(resultsave['erro']):
                flash(f"Erro: {resultsave['message']}!", 'danger')
                return redirect(url_for(f'config'))
            else:

                flash(f"Sucesso: User {name} atualizado!", 'success')
                return redirect(url_for(f'config'))

    return redirect(url_for('login'))



# ROTA DE ATULIZAR USUÁRIO
@app.route("/updateUser/<idUser>", methods=["GET", "POST"])
def userUpdate(idUser):

    # VERIFICA SE USUÁRIO ESTAR LOGADO
    if "user" in session:

        user = session["user"]
        token = user.get('token')

        # PEGANDO DADOS PARA ATUALIZAR USUÁRIO
        if request.method == "POST":

        
            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")
            level = request.form.get("level")
            company = request.form.get("company")


            # CHAMANDO API PARA ATUALIZAR USUÁRIO
            resultsave = updateUser(idUser, name,email,password,level,company,token)


            # FAZENDO VALIDAÇÃO DA API AO ATULIZAR USUÁRIO
            if(resultsave['erro']):

                flash(f"Erro: {resultsave['message']}!", 'danger')
                return redirect(url_for(f'config'))

            else:

                flash(f"Sucesso: User {name} atualizado!", 'success')
                return redirect(url_for(f'config'))

    return redirect(url_for('login'))




#ROTA DE APAGAR USUÁRIO
@app.route("/userDelete/<id>/", methods=["GET", "POST"])
def userDelete(id):

    # VERIFICA SE USUÁRIO ESTAR LOGADO E SE TEM ID PARA APAGAR
    if "user" in session and id:

        user = session["user"]
        token = user.get('token')


        # CHAMANDO API PARA APAGAR USUÁRIO
        resultdelete = deleteUser(int(id), token)


        # SE TIVER ERRO DA API AO APAGAR USUÁRIO
        if(resultdelete['erro']):

            flash(
                f"Erro: Usuário de id: {id} não pode ser apagado!", 'danger')
            return redirect(url_for(f'config'))

        # SE TIVER SUCESSO API AO APAGAR USUÁRIO
        flash(f"Sucesso: Usuário de id: {id} apagado!", 'success')
        return redirect(url_for(f'config'))

    return redirect(url_for('login'))



# ROTA PARA SALVAR USUÁRIO
@app.route("/newUser", methods=["GET", "POST"])
def newUser():

    # VERIFICA SE USUÁRIO ESTAR LOGADO
    if "user" in session:
        user = session["user"]
        token = user.get('token')

        # PEGANDO DADOS DO NOVO USUÁRIO A SER GRAVADO
        if request.method == "POST":

            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")
            level = request.form.get("level")
            company = request.form.get("company")

            # CHAMANDO API PARA SALVAR USUÁRIO
            resultsave = saveNewUser(name,email,password,int(level),company,token)

            

            # FAZENDO VALIDAÇÃO DA API AO SALVAR USUÁRIO
            if(resultsave['erro']):
                flash(f"Erro: {resultsave['message']}!", 'danger')
                return redirect(url_for(f'config'))

            else:
                flash(f"Sucesso: Usuário {name} criado!", 'success')
                return redirect(url_for(f'config'))

    return redirect(url_for('login'))




# ROTA DIRECIONANDO PARA CONFIGURAÇÃO ADMIN
@app.route("/config/", methods=["GET", "POST"])
def config():
    # VERIFICA SE USUÁRIO ESTAR LOGADO
    if "user" in session:

        # PEGANDO DADOS DO USUÁRIO LOGADO
        user = session["user"]
        token = user.get('token')


        # CHAMANDO API E PEGANDO DADOS
        dataUsers = searchUser(token)
        dataUserID = searchUserId(int(user['user']['id']),token)




        if dataUserID['users']['level'] == 1:
            return redirect(url_for('login'))





        return render_template("config.html",dataUsers=dataUsers['users'], idUser=dataUserID['users'])

    # SE O USUÁRIO NÃO TIVER LOGADO, ENVIA PARA O TELA LOGIN
    return redirect(url_for('login'))


# ROTA PRINCIPAL DIRECIONANDO PARA HOME
@app.route("/", methods=["GET", "POST"])
def home():

    # VERIFICA SE USUÁRIO ESTAR LOGADO
    if "user" in session:

        # PEGANDO DADOS DO USUÁRIO LOGADO
        user = session["user"]
        token = user.get('token')

        # CHAMANDO API E PEGANDO DADOS
        data = searchCommandSpecific('Linux', token)
        types = searchTypeCommands(token)

        return render_template("home.html", user=user, data=data['commands'], types=types['types'])

    # SE O USUÁRIO NÃO TIVER LOGADO, ENVIA PARA O TELA LOGIN
    return redirect(url_for('login'))


# ROTA PARA BUSCAR POR TIPO DE COMANDOS POR PARAMETRO
@app.route("/search/<type>", methods=["GET", "POST"])
def search(type):

    # VERIFICA SE USUÁRIO ESTAR LOGADO E SE TEM TIPO EM PARAMETRO
    if(type and "user" in session):

        # PEGANDO DADOS DO USUÁRIO LOGADO
        user = session["user"]
        token = user.get('token')

        # CHAMANDO API E PEGANDO DADOS
        data = searchCommandSpecific(type, token)
        types = searchTypeCommands(token)

        # VERIFICA SE NÃO TEVE ERRO NA API EXTERNA ENTÃO APRESENTA PÁGINA E DADOS
        if(not data["erro"] or not types["erro"]):
            return render_template("home.html", user=user, data=data['commands'], types=types['types'])

        # QUANDO TEVE ERRO NA API EXTERNA.
        flash(f"Erro: Falha no servidor!", 'danger')
        return redirect(url_for(f'search', type))

    # SE O USUÁRIO NÃO TIVER LOGADO, ENVIA PARA O TELA LOGIN
    return redirect(url_for("login"))


# ROTA DE FAZER LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    # VERIFICA SE USUÁRIO ESTAR LOGADO, SE SIM JA MANDA PARA HOME
    if session and request.method == "GET":
        token = session["user"]['token']

        if(token):
            return render_template("login.html")

    # PEGANDO DADOS DE LOGIN
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        # CHAMANDO A API PARA FAZER LOGIN
        statusLogin = makelogin(email, password)


        # QUANDO O LOGIN É AUTORIZADO COM SUCESSO
        if not statusLogin['erro']:

            # JOGA OS DADOS COMO O TOKEM PARA DENTRO DA SESSÃO
            session['user'] = statusLogin
            user = session["user"]

            data = searchCommandSpecific('Linux', statusLogin['token'])
            types = searchTypeCommands(statusLogin['token'])

            return render_template("home.html", user=user, data=data['commands'], types=types['types'])

        # QUANDO O LOGIN NÃO É AUTORIZADO COM FALHA
        return render_template("login.html", erro=True, message=statusLogin['message'])

    return render_template("login.html")


# RODA PARA SAIR/LOGOUT
@app.route("/logout", methods=["GET"])
def logout():

    # DELATA A SESSÃO DO USUARIO
    session.pop('user', None)
    return redirect(url_for('login'))

# ROTA DE REDISTRO DE NOVO USUARIO


@app.route("/register", methods=["GET", "POST"])
def register():

    # VERIFICA SE USUÁRIO ESTAR LOGADO, SE SIM JA MANDA PARA HOME
    if session:
        token = session["user"]['token']
        if(token):
            return redirect(url_for("home"))

    # PEGANDO DADOS PARA NO CADASTRO DE USUÁRIO
    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        coupon = request.form.get("coupon")
        company = request.form.get("company")


        # CHAMANDO API PARA REGISTRAR NOVO USUÁRIO
        statusLogin = makeRegister(name, email, password, coupon, company)

        # SE NÃO HAVER ERRO ENVIA PARA TELA HOME
        if not statusLogin['erro']:

            session['user'] = statusLogin
            return redirect(url_for("home"))

        # SE HAVER ALGUM ERRO NO RETORNO DA API
        return render_template("register.html", erro=True, message=statusLogin['message'])

    return render_template("register.html")


# ROTA DE APAGAR UM COMANDO USANDO ID POR PARAMETRO
@app.route("/commandDelete/<id>/", methods=["GET", "POST"])
def commandDelete(id):

    # VERIFICA SE USUÁRIO ESTAR LOGADO E SE TEM ID PARA APAGAR
    if "user" in session and id:

        user = session["user"]
        token = user.get('token')

        id = id.split('-')

        # CHAMANDO API PARA APAGAR COMANDO
        resultsave = deleteCommand(int(id[0]), token)

        # SE TIVER ERRO DA API AO APAGAR COMANDO
        if(resultsave['erro']):

            flash(
                f"Erro: Comando de id: {id[0]} não pode ser apagado!", 'danger')
            return redirect(url_for(f'search', type=id[1]))

        # SE TIVER SUCESSO API AO APAGAR COMANDO
        flash(f"Sucesso: Comando de id: {id[0]} apagado!", 'success')
        return redirect(url_for(f'search', type=id[1]))

    return redirect(url_for('login'))



#ROTA DE ATULIZAR COMANDO
@app.route("/update/<idCommands>",methods=["GET", "POST"])
def updateCommands(idCommands): 

    #VERIFICA SE USUÁRIO ESTAR LOGADO
    if "user" in session:
        
        user = session["user"]
        token = user.get('token')

        #PEGANDO DADOS PARA ATUALIZAR COMANDO
        if request.method == "POST":

            id = request.form.get("id").split('-')
            pagNewComands = id[1]
            title = request.form.get("title")
            description = request.form.get("description")
            commands = request.form.get("commands")
            tags = request.form.get("tags")
            creator = request.form.get("creator")

            #CHAMANDO API PARA ATUALIZAR COMANDO
            resultsave = updateCommand(idCommands,int(id[0]),title,description,commands,tags,creator,token)

            #FAZENDO VALIDAÇÃO DA API AO ATULIZAR COMANDO
            if(resultsave['erro']):

                flash(f"Erro: {resultsave['message']}!",'danger')
                return redirect(url_for(f'search',type=pagNewComands))
            else:

                flash(f"Sucesso: Comando {title} atualizado!",'success')
                return redirect(url_for(f'search',type=pagNewComands))

    





# ROTA PARA SALVAR COMANDO
@app.route("/save", methods=["GET", "POST"])
def saveCommands():

    # VERIFICA SE USUÁRIO ESTAR LOGADO
    if "user" in session:
        user = session["user"]
        token = user.get('token')

        # PEGANDO DADOS DO NOVO COMANDO A SER GRAVADO
        if request.method == "POST":

            id = request.form.get("id").split('-')
            pagNewComands = id[1]
            title = request.form.get("title")
            description = request.form.get("description")
            commands = request.form.get("commands")
            tags = request.form.get("tags")
            creator = request.form.get("creator")

            # CHAMANDO API PARA SALVAR NO COMANDO
            resultsave = saveCommand(
                int(id[0]), title, description, commands, tags, creator, token)

            # FAZENDO VALIDAÇÃO DA API
            if(resultsave['erro']):
                flash(f"Erro: {resultsave['message']}!", 'danger')
                return redirect(url_for(f'search', type=id[1]))

            else:
                flash(f"Sucesso: Comando {title} criado!", 'success')
                return redirect(url_for(f'search', type=id[1]))

    return redirect(url_for('login'))


# PONTO INICIAL DO APP
if __name__ == "__main__":
    app.run(debug=True)


# ALGUNS EXEMPLOS DE PARAMETRO PARA FLASK
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
