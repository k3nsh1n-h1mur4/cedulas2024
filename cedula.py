from flask import Blueprint, request, abort, render_template

from forms import cedulaForm

from Connections import PyConnection 

cedulas = Blueprint('cedulas', __name__, template_folder='cedulasTemplate', url_prefix='/cedulas')



@cedulas.route('/regCedula', methods=['GET', 'POST'])
def newCedula():
    if request.method == 'GET':
        form = cedulaForm()
        
    title = 'Registro de Cédula'
    error = None
    if request.method == 'POST':
        form = cedulaForm()
        data = request.form
        app = data['app']
        apm = data['apm']
        nombre = data['nombre']
        domicilio = data['domicilio']
        colonia =data['colonia'] 
        mcpio = data['mcpio']
        cp = data['cp']
        local = data['local']
        num_cel = data['num_cel']
        email = data['email']
        l_nac = data['l_nac']
        f_nac = data['f_nac']  
        nss = data['nss']  
        rfc = data['rfc']  
        curp = data['curp']  
        edo_civil = data['edo_civil']  
        sexo = data['sexo']  
        matricula = data['matricula']
        categoria = data['categoria']
        adsc = data['adsc']
        turno = data['turno']
        t_contr = data['t_contr']
        f_ingr = data['f_ingr']
        antiguedad = data['antiguedad']
        #print(app,apm,nombre)
        c = PyConnection()
        c.insertCedula(app.upper(), apm.upper(), nombre.upper(), domicilio.upper(), colonia.upper(), mcpio.upper(), cp, local.upper(), num_cel, email, l_nac.upper(), f_nac, nss, rfc.upper(), curp.upper(), edo_civil, sexo, matricula, categoria, adsc, turno, t_contr, f_ingr, antiguedad)

    return render_template('registro.html', title=title, form=form)
    
