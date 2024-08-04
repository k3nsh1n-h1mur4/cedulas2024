from flask import Flask, request, render_template, redirect, jsonify, url_for, flash, Blueprint

from werkzeug.security import generate_password_hash, check_password_hash

from flask_bootstrap import Bootstrap5

from cedula import cedulas

from Connections import PyConnection

from dotenv import dotenv_values
config = dotenv_values(".env")
print(config)

from forms import UsersForm, LoginForm

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = config['SECRET_KEY']
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'morph'
app.register_blueprint(cedulas)
bootstrap = Bootstrap5(app)


@app.route('/')
def index():
    return 'Hola Index'

@app.route('/newUser', methods=['GET', 'POST'])
def newUser():
    form = UsersForm()
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = generate_password_hash(data['password'], method=config['METHOD'], salt_length=int(config['SALT']))
        c = PyConnection()
        #c.Cnx()
        c.insertUser(username, password, data['is_admin'])
        print(password)
    return render_template('index.html', form=form, title='Registro Usuarios')


@app.route('/list')
def list():
    title = 'Listado'
    if request.method == 'GET':
        c = PyConnection()
        rows = c.getUsers()
        if not rows:
            return jsonify({'message': 'NAda por mostrar'})
    return render_template('list.html', rows=rows, title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'LogIn'
    form = LoginForm()
    if request.method == 'POST':
        data = request.form
        username = data['username']
        c = PyConnection()
        conn = c.Cnx()
        with conn.cursor() as cur:
            cur.callproc('getUser', [username,])
            row = cur.fetchone()
            if not row:
                flash('No existe Usuario')
                #return jsonify({'message': 'Usuario no existe'})
            else:
                if row['username'] and check_password_hash(row['password'], data['password']):
                    flash('Credenciales Correctas')
                    #flash('Credenciales Correctas')
                    #return jsonify({'message': 'Credenciales correctas'})
                else:
                    flash('Credenciales Erroneas')
                    #return jsonify({'message': 'Credenciales Erroneas'})
    return render_template('login.html', form=form, title=title)        


app.run(debug=True)
