# Sistema de Documentação de Comandos Front-End

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://a3-commands.herokuapp.com/login)

A Sistema está em nuvem na plataforma [Heroku], a Front-and foi desenvolvida com o Framework [flask.js] usando python.

## Instalação
Clone o repositório no GIT.

```
git clone https://github.com/andrenogueiragbi/commands_a3_front
```
Entre do repositório.

```
cd commands_a3_front
```
Instalar virtualenv.

```
pip install virtualenv
```

Criar um ambiente virtual para o python.

```
virtualenv nome_da_virtualenv
```

Ativar ambiente virtual.
```
source nome_da_virtualenv/bin/activate 
```

Instalar as dependências.
```
pip3 install -r requirements.txt
```

Exportar variável app.
```
export FLASK_APP=main.py
```

Exportar variável env.
```
 export FLASK_ENV=development
```

Rodar a aplicação na porta 3000.
```
flask run --host 0.0.0.0 --port=3000
```



## Autores

- [@andrenogueiragbi](https://github.com/andrenogueiragbi)

- [@RonaldoThierre](https://github.com/RonaldoThierre)

## licença

MIT

 
   [flask.js]: <https://flask.palletsprojects.com/en/2.1.x/>
   [heroku]: <https://www.heroku.com/>
   
   