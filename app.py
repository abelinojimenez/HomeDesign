import mysql.connector
from flask import Flask,request,render_template,redirect,url_for,session
app=Flask(__name__)

def conectarApp(emails,passwords):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario WHERE email='"+emails+"' and clave=sha('"+passwords+"')")
    users=cursor.fetchall()
    if len(users)>0:
        return True
    else:
        return False
def conectarAppAPI(emails,passwords):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario WHERE email='"+emails+"' and clave=sha('"+passwords+"')")
    users=cursor.fetchall()
    #return "1"
    if len(users)>0:
        return str(users[0]['id_usuario'])
    else:
        return "0"
def isRegister(emails):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='optimizationtimeai')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario WHERE email='"+emails+"'")
    users=cursor.fetchall()
    if len(users)<=0:
        return True
    else:
        return False
def idRegisterUser(idUser):
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("Select * from usuario where id_usuario = "+idUser+"")
    userexits=cursor.fetchall()
    if len(userexits)<=0:
        return False
    else:
        return True
@app.route('/api/user',methods=['GET'])
def authUser():
    email=request.args.get('email')
    passwords=request.args.get('password')
    return str(conectarAppAPI(email,passwords))
'''@app.route('/',methods=['GET'])
def index():
        return render_template('index.html')
'''
def datosProyectoLoad(idUser):
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("Select * from proyecto where id_usuario = "+idUser+" order by id_proyecto DESC")
    userexits=cursor.fetchall()
    arrayData=[]
    for i in range(len(userexits)):
            data=[]
            data.append(userexits[i]['id_proyecto'])
            data.append(userexits[i]['nombre_proyecto'])
            arrayData.append(data)
    return arrayData
def datosPresupuestoLoad(idUser,idProyecto):
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("Select * from presupuesto where id_usuario = "+idUser+" and id_proyecto = "+idProyecto+" order by id_presupuesto DESC")
    userexits=cursor.fetchall()
    arrayData=[]
    for i in range(len(userexits)):
            data=[]
            data.append(userexits[i]['id_presupuesto'])
            data.append(userexits[i]['nombre_presupuesto'])
            data.append(userexits[i]['id_proyecto'])
            data.append(userexits[i]['id_usuario']) 
            arrayData.append(data)
    return arrayData
def datosModuloLoad(idUser,id_presupuesto):
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("Select * from modulo where id_usuario = "+idUser+" and id_proyecto = "+session['id_proyecto']+" and id_presupuesto="+id_presupuesto+" order by id_modulo DESC")
    userexits=cursor.fetchall()
    arrayData=[]
    for i in range(len(userexits)):
            data=[]
            data.append(userexits[i]['id_modulo'])
            data.append(userexits[i]['nombre_modulo'])
            data.append(userexits[i]['id_proyecto'])
            data.append(userexits[i]['id_usuario'])
            arrayData.append(data)
    return arrayData
def datosSubModuloLoad(idUser,id_modulo):
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("Select * from submodulo where id_usuario = "+idUser+" and id_proyecto = "+session['id_proyecto']+" and id_presupuesto="+session['id_presupuesto']+" and id_modulo = "+id_modulo+" order by id_sub_modulo DESC")
    userexits=cursor.fetchall()
    arrayData=[]
    for i in range(len(userexits)):
            data=[]
            data.append(userexits[i]['id_sub_modulo'])
            data.append(userexits[i]['nombre_submodulo'])
            data.append(userexits[i]['id_proyecto'])
            data.append(userexits[i]['id_usuario'])
            arrayData.append(data)
    return arrayData
def datosMaterialSubLoad(idUser,id_sub_modulo):
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("Select * from material_sub where id_usuario = "+idUser+" and id_proyecto = "+session['id_proyecto']+" and id_presupuesto="+session['id_presupuesto']+" and id_modulo = "+session['id_modulo']+" and id_sub_modulo = "+id_sub_modulo+" order by id_material_sub DESC")
    userexits=cursor.fetchall()
    arrayData=[]
    for i in range(len(userexits)):
            data=[]
            data.append(userexits[i]['id_material_sub'])
            data.append(userexits[i]['nombre_material'])
            data.append(userexits[i]['id_proyecto'])
            data.append(userexits[i]['id_usuario'])
            arrayData.append(data)
    return arrayData
def datosMaterialesProyectLoad(idUser):
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("Select * from material_proyectos where id_usuario = "+idUser+"  order by id_material_proyectos DESC")
    userexits=cursor.fetchall()
    arrayData=[]
    for i in range(len(userexits)):
            data=[]
            data.append(userexits[i]['id_material_proyectos'])
            data.append(userexits[i]['descripcion'])
            data.append(userexits[i]['unidad'])
            data.append(userexits[i]['precio_unidad'])
            arrayData.append(data)
    return arrayData
def datosListaMaterialesLoad():
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("select lm.id_lista_material,mp.descripcion,mp.unidad,mp.precio_unidad,lm.cantidad from lista_material lm inner join material_proyectos mp on lm.id_material_proyectos=mp.id_material_proyectos WHERE lm.id_usuario="+session['idUsuario']+" and lm.id_proyecto="+session['id_proyecto']+" and lm.id_presupuesto="+session['id_presupuesto']+" and lm.id_modulo="+session['id_modulo']+" and lm.id_sub_modulo="+session['id_sub_modulo']+" and lm.id_material="+session['id_material_sub']+" order by lm.id_lista_material DESC")
    userexits=cursor.fetchall()
    arrayData=[]
    for i in range(len(userexits)):
            data=[]
            data.append(userexits[i]['id_lista_material'])
            data.append(userexits[i]['descripcion'])
            data.append(userexits[i]['unidad'])
            data.append(userexits[i]['precio_unidad'])
            data.append(userexits[i]['cantidad'])
            arrayData.append(data)
    return arrayData

@app.route('/',methods=['POST','GET'])
def index():
    app.secret_key='esta es una clave secreta'
    if request.method=='POST' and request.form['username']!=None:
        email=request.form['username']
        passwords=request.form['password']
        iduser=conectarAppAPI(email,passwords)  
        if iduser!="" and iduser!="0":
            session['idUsuario']=iduser
            datosProyecto=datosProyectoLoad(iduser)
            return render_template('Proyecto_Nuevo.html',idusuario=iduser,datos=datosProyecto,titulo='CREAR NUEVO PROYECTO',rutaAgregar='/nuevoprojecto/')
        else:
            return render_template('index.html',holamundo=" hola mundo")
    elif len(session)>0:
        datosProyecto=datosProyectoLoad(session['idUsuario'])
        return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosProyecto,titulo='CREAR NUEVO PROYECTO',rutaAgregar='/nuevoprojecto/')
    else:
        return render_template('index.html',holamundo="hola mundo")
@app.route('/logout/',methods=['POST','GET'])
def logout():
    session.clear()
    return render_template('index.html',holamundo="hola mundo")
@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/register/')
def signup():
    return render_template('register.html')
@app.route('/registrar/',methods=['POST'])
def registrar():
    emails=request.form['email']
    passwords=request.form['password']
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='optimizationtimeai')
    cursor=connection.cursor(dictionary=True)
    if isRegister(emails):
        cursor.execute("INSERT INTO usuario(email,clave,nombre,apellido,token_unique) values('"+emails+"','"+passwords+"','"+nombre+"','"+apellido+"','ddfg334343d34d')")
        '''
        cursor.execute("update usuario set email='None' where idUsuario=1")
        
        cursor.execute("delete from usuario where idUsuario=1")
        '''
        connection.commit()
    else:
        return "usuario ya registrado"
    
    return "<h>internet conexion "+emails+" "+passwords+"</h>"

@app.route('/nuevoprojecto/',methods=['POST'])
def nuevo_proyecto():
    nombreProyecto=request.form['nombre']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='projectdesign')
    token=request.form['token']
    cursor=connection.cursor(dictionary=True)
    if idRegisterUser(session['idUsuario']) and token=='fdfdsfdshj343245rgtrtgr':
        cursor.execute("INSERT INTO proyecto(id_usuario,nombre_proyecto) values('"+session['idUsuario']+"','"+nombreProyecto+"')")
        connection.commit()
    else:
        return "usuario no valido no puede hacer esta operacion"
    return redirect(url_for('index'))
    #dato=datosProyectoLoad(session['idUsuario'])
    #return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosProyectoLoad(session['idUsuario']),titulo='CREAR NUEVO PROYECTO',rutaAgregar='/nuevoprojecto/',sizedata=len(dato))
    return "<h>internet conexion se registro satisfactoriamente</h>"
@app.route('/nuevopresupuesto/',methods=['POST','GET'])
def nuevo_presupuesto():
    if request.method == 'GET':
        return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosPresupuestoLoad(session['idUsuario'],session['id_proyecto']),titulo=str(session['nombre_proyecto']+'- CREAR NUEVO PRESUPUESTO'),rutaAgregar='/nuevopresupuesto/',sizedata=len(dato))
    nombre_presupuesto=request.form['nombre']
    #nombre_proyecto=session[]
    #id_proyecto=request.form['id_proyecto']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='projectdesign')
    token=request.form['token']
    cursor=connection.cursor(dictionary=True)
    if idRegisterUser(session['idUsuario']) and token=='fdfdsfdshj343245rgtrtgr':
        cursor.execute("INSERT INTO presupuesto(id_proyecto,id_usuario,nombre_presupuesto) values("+session['id_proyecto']+",'"+session['idUsuario']+"','"+nombre_presupuesto+"')")
        connection.commit()
    else:
        return "usuario no valido no puede hacer esta operacion"
    return redirect(url_for('presupuesto'))
    #dato=datosPresupuestoLoad(session['idUsuario'],session['id_proyecto'])
    #return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosPresupuestoLoad(session['idUsuario'],session['id_proyecto']),titulo=str(session['nombre_proyecto']+'- CREAR NUEVO PRESUPUESTO'),rutaAgregar='/nuevopresupuesto/',sizedata=len(dato))
    return "<h>internet conexion se registro satisfactoriamente</h>"
@app.route('/nuevomodulo/',methods=['POST','GET'])
def nuevo_modulo():
    if request.method == 'GET':
        dato=datosModuloLoad(session['idUsuario'],session['id_presupuesto'])
        return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosModuloLoad(session['idUsuario'],session['id_presupuesto']),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'- CREAR NUEVO MODULO'),rutaAgregar='/nuevomodulo/',sizedata=len(dato))
    nombre_modulo=request.form['nombre']
    #nombre_proyecto=session[]
    #id_proyecto=request.form['id_proyecto']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='projectdesign')
    token=request.form['token']
    cursor=connection.cursor(dictionary=True)
    if idRegisterUser(session['idUsuario']) and token=='fdfdsfdshj343245rgtrtgr':
        cursor.execute("INSERT INTO modulo(id_proyecto,id_presupuesto,id_usuario,nombre_modulo) values("+session['id_proyecto']+","+session['id_presupuesto']+",'"+session['idUsuario']+"','"+nombre_modulo+"')")
        connection.commit()
    else:
        return "usuario no valido no puede hacer esta operacion"
    return redirect(url_for('modulo'))
    #dato=datosModuloLoad(session['idUsuario'],session['id_presupuesto'])
    #return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosModuloLoad(session['idUsuario'],session['id_presupuesto']),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'- CREAR NUEVO MODULO'),rutaAgregar='/nuevomodulo/',sizedata=len(dato))
    return "<h>internet conexion se registro satisfactoriamente</h>"
@app.route('/nuevosubmodulo/',methods=['POST'])
def nuevo_submodulo():
    if request.method == 'GET':
         return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosSubModuloLoad(session['idUsuario'],session['id_modulo']),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'-'+session['nombre_modulo']+'- CREAR NUEVO SUBMODULO'),rutaAgregar='/nuevosubmodulo/',sizedata=len(dato))
    nombre_submodulo=request.form['nombre']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='projectdesign')
    token=request.form['token']
    cursor=connection.cursor(dictionary=True)
    if idRegisterUser(session['idUsuario']) and token=='fdfdsfdshj343245rgtrtgr':
        cursor.execute("INSERT INTO submodulo(id_usuario,id_proyecto,id_presupuesto,id_modulo,nombre_submodulo) values("+session['idUsuario']+","+session['id_proyecto']+","+session['id_presupuesto']+","+session['id_modulo']+",'"+nombre_submodulo+"')")
        connection.commit()
    else:
        return "usuario no valido no puede hacer esta operacion"
    return redirect(url_for('submodulo'))
    #dato=datosSubModuloLoad(session['idUsuario'],session['id_modulo'])
    #return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosSubModuloLoad(session['idUsuario'],session['id_modulo']),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'-'+session['nombre_modulo']+'- CREAR NUEVO SUBMODULO'),rutaAgregar='/nuevosubmodulo/',sizedata=len(dato))
@app.route('/edit_costos',methods=['POST','GET'])
def edit_costos():
    return render_template('Proyecto_add_Costo.html')
@app.route('/nuevomaterialsub/',methods=['POST','GET'])
def nuevo_materialsub():
    if request.method == 'GET':
        dato=datosMaterialSubLoad(session['idUsuario'],session['id_sub_modulo'])
        return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosMaterialSubLoad(session['idUsuario'],session['id_sub_modulo']),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'-'+session['nombre_modulo']+'-'+session['nombre_submodulo']+'- CREAR NUEVA LISTA MATERIAL'),rutaAgregar='/nuevomaterialsub/',sizedata=len(dato))
    nombre_material=request.form['nombre']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='projectdesign')
    token=request.form['token']
    cursor=connection.cursor(dictionary=True)
    if idRegisterUser(session['idUsuario']) and token=='fdfdsfdshj343245rgtrtgr':
        cursor.execute("INSERT INTO material_sub(id_sub_modulo,id_modulo,id_proyecto,id_presupuesto,id_usuario,nombre_material) values("+session['id_sub_modulo']+","+session['id_modulo']+","+session['id_proyecto']+","+session['id_presupuesto']+","+session['idUsuario']+",'"+nombre_material+"')")
        connection.commit()
    else:
        return "usuario no valido no puede hacer esta operacion"
    return redirect(url_for('materialsub'))
    #dato=datosMaterialSubLoad(session['idUsuario'],session['id_sub_modulo'])
    #return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosMaterialSubLoad(session['idUsuario'],session['id_sub_modulo']),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'-'+session['nombre_modulo']+'-'+session['nombre_submodulo']+'- CREAR NUEVA LISTA MATERIAL'),rutaAgregar='/nuevomaterialsub/',sizedata=len(dato))
    return "<h>internet conexion se registro satisfactoriamente</h>"
@app.route('/api/proyecto/delete',methods=['POST','GET'])
def deleteProyecto():
    id_proyecto=request.form['id_proyecto']
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("delete from lista_material where id_proyecto="+id_proyecto+"")
    cursor.execute("delete from material_sub where id_proyecto="+id_proyecto+"")
    cursor.execute("delete from submodulo where id_proyecto="+id_proyecto+"")
    cursor.execute("delete from modulo where id_proyecto="+id_proyecto+"")
    cursor.execute("delete from presupuesto where id_proyecto="+id_proyecto+"")
    cursor.execute("delete from proyecto where id_proyecto="+id_proyecto+"")
    connection.commit()
    return redirect(url_for('index'))
@app.route('/api/presupuesto/delete',methods=['POST','GET'])
def deletePresupuesto():
    id_presupuesto=request.form['id_presupuesto']
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("delete from lista_material where id_presupuesto="+id_presupuesto+"")
    cursor.execute("delete from material_sub where id_presupuesto="+id_presupuesto+"")
    cursor.execute("delete from submodulo where id_presupuesto="+id_presupuesto+"")
    cursor.execute("delete from modulo where id_presupuesto="+id_presupuesto+"")
    cursor.execute("delete from presupuesto where id_presupuesto="+id_presupuesto+"")
    connection.commit()
    return redirect(url_for('presupuesto'))
@app.route('/api/modulo/delete',methods=['POST','GET'])
def deletemodulo():
    id_modulo=request.form['id_modulo']
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("delete from lista_material where id_modulo="+id_modulo+"")
    cursor.execute("delete from material_sub where id_modulo="+id_modulo+"")
    cursor.execute("delete from submodulo where id_modulo="+id_modulo+"")
    cursor.execute("delete from modulo where id_modulo="+id_modulo+"")
    connection.commit()
    return redirect(url_for('modulo'))
@app.route('/api/submodulo/delete',methods=['POST','GET'])
def deleteSubmodulo():
    id_submodulo=request.form['id_submodulo']
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("delete from lista_material where id_sub_modulo="+id_submodulo+"")
    cursor.execute("delete from material_sub where id_sub_modulo="+id_submodulo+"")
    cursor.execute("delete from submodulo where id_sub_modulo="+id_submodulo+"")
    connection.commit()
    return redirect(url_for('submodulo'))
@app.route('/api/material/delete',methods=['POST','GET'])
def deleteMaterial():
    id_material_sub=request.form['id_material_sub']
    connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
    cursor=connection.cursor(dictionary=True)
    cursor.execute("delete from lista_material where id_material="+id_material_sub+"")
    cursor.execute("delete from material_sub where id_material_sub="+id_material_sub+"")
    connection.commit()
    return redirect(url_for('materialsub'))
@app.route('/api/presupuesto/',methods=['POST','GET'])
def presupuesto():
    if request.method == 'GET':
         dato=datosPresupuestoLoad(session['idUsuario'],session['id_proyecto'])
         return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosPresupuestoLoad(session['idUsuario'],session['id_proyecto']),titulo=str(session['nombre_proyecto']+'- CREAR NUEVO PRESUPUESTO'),rutaAgregar='/nuevopresupuesto/',sizedata=len(dato))
    idProyecto=request.form['id_proyecto']
    nombre_proyecto=request.form['nombre_proyecto']
    dato=datosPresupuestoLoad(session['idUsuario'],idProyecto)
    session['id_proyecto']=idProyecto
    session['nombre_proyecto']=nombre_proyecto
    return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosPresupuestoLoad(session['idUsuario'],idProyecto),titulo=str(nombre_proyecto+'- CREAR NUEVO PRESUPUESTO'),rutaAgregar='/nuevopresupuesto/',sizedata=len(dato))
@app.route('/api/modulo/',methods=['POST','GET'])
def modulo():
    if request.method == 'GET':
        dato=datosModuloLoad(session['idUsuario'],session['id_presupuesto'])
        return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosModuloLoad(session['idUsuario'],session['id_presupuesto']),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'- CREAR NUEVO MODULO'),rutaAgregar='/nuevomodulo/',sizedata=len(dato))
    id_presupuesto=request.form['id_presupuesto']
    nombre_presupuesto=request.form['nombre_presupuesto']
    dato=datosModuloLoad(session['idUsuario'],id_presupuesto)
    session['id_presupuesto']=id_presupuesto
    session['nombre_presupuesto']=nombre_presupuesto
    return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosModuloLoad(session['idUsuario'],id_presupuesto),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'- CREAR NUEVO MODULO'),rutaAgregar='/nuevomodulo/',sizedata=len(dato))
@app.route('/api/submodulo/',methods=['POST','GET'])
def submodulo():
    if request.method == 'GET':
        dato=datosSubModuloLoad(session['idUsuario'],session['id_modulo'])
        return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosSubModuloLoad(session['idUsuario'],session['id_modulo']),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'-'+session['nombre_modulo']+'- CREAR NUEVO SUBMODULO'),rutaAgregar='/nuevosubmodulo/',sizedata=len(dato))     
    id_modulo=request.form['id_modulo']
    nombre_modulo=request.form['nombre_modulo']
    dato=datosSubModuloLoad(session['idUsuario'],id_modulo)
    session['id_modulo']=id_modulo
    session['nombre_modulo']=nombre_modulo
    return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosSubModuloLoad(session['idUsuario'],id_modulo),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'-'+session['nombre_modulo']+'- CREAR NUEVO SUBMODULO'),rutaAgregar='/nuevosubmodulo/',sizedata=len(dato))
@app.route('/api/materialsub/',methods=['POST','GET'])
def materialsub():
    if request.method == 'GET':
            dato=datosMaterialSubLoad(session['idUsuario'],session['id_sub_modulo'])
            return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosMaterialSubLoad(session['idUsuario'],session['id_sub_modulo']),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'-'+session['nombre_modulo']+'-'+session['nombre_submodulo']+'- CREAR NUEVA LISTA MATERIAL'),rutaAgregar='/nuevomaterialsub/',sizedata=len(dato))

    id_sub_modulo=request.form['id_submodulo']
    nombre_submodulo=request.form['nombre_submodulo']
    dato=datosMaterialSubLoad(session['idUsuario'],id_sub_modulo)
    session['id_sub_modulo']=id_sub_modulo
    session['nombre_submodulo']=nombre_submodulo
    return render_template('Proyecto_Nuevo.html',idusuario=session['idUsuario'],datos=datosMaterialSubLoad(session['idUsuario'],id_sub_modulo),titulo=str(session['nombre_proyecto']+" - "+session['nombre_presupuesto']+'-'+session['nombre_modulo']+'-'+session['nombre_submodulo']+'- CREAR NUEVA LISTA MATERIAL'),rutaAgregar='/nuevomaterialsub/',sizedata=len(dato))

@app.route('/api/listamateriales/',methods=['POST','GET'])
def lista_materiales_add():
    if request.method == 'GET':
            seleccion=datosMaterialesProyectLoad(session['idUsuario'])
            datos=datosListaMaterialesLoad()
            return render_template('Proyecto_add_material.html',seleccion=seleccion,datos=datos,sizeseleccion=len(seleccion),sizedata=len(datos))
    id_material_sub=request.form['id_material_sub']
    nombre_material=request.form['nombre_material']
    session['id_material_sub']=id_material_sub
    session['nombre_material']=nombre_material
    seleccion=datosMaterialesProyectLoad(session['idUsuario'])
    datos=datosListaMaterialesLoad()
    return render_template('Proyecto_add_material.html',seleccion=seleccion,datos=datos,sizeseleccion=len(seleccion),sizedata=len(datos))

@app.route('/materialesproyectos',methods=['GET'])
def materiales_proyectos_show():
    dato=datosMaterialesProyectLoad(session['idUsuario'])
    return render_template('Proyecto_lista_productos.html',datos=dato,sizedata=len(dato))    
@app.route('/addmaterial/',methods=['POST','GET'])
def addsmaterial():
    if request.method == 'GET':
        dato=datosMaterialesProyectLoad(session['idUsuario'])
        return render_template('Proyecto_lista_productos.html',datos=dato,sizedata=len(dato))
    descripcion=request.form['descripcion']
    unidad=request.form['unidad']
    precio_unidad=request.form['precio_unidad']
    token=request.form['token']
    if idRegisterUser(session['idUsuario']) and token=='fdfdsfdshj343245rgtrtgr':
        connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
        cursor=connection.cursor(dictionary=True)
        cursor.execute("INSERT INTO material_proyectos(id_usuario,descripcion,unidad,precio_unidad) values("+session['idUsuario']+",'"+descripcion+"','"+unidad+","+"','"+precio_unidad+"')")
        connection.commit()
    else:
        return "usuario no valido no puede hacer esta operacion"
    return redirect(url_for('materiales_proyectos_show'))
    #dato=datosMaterialesProyectLoad(session['idUsuario'])
    #return render_template('Proyecto_lista_productos.html',datos=dato,sizedata=len(dato))
@app.route('/addlistamaterial/',methods=['POST','GET'])
def addmlistaaterial():
    if request.method == 'GET':
        seleccion=datosMaterialesProyectLoad(session['idUsuario'])
        datos=datosListaMaterialesLoad()
        return render_template('Proyecto_add_material.html',seleccion=seleccion,datos=datos,sizeseleccion=len(seleccion),sizedata=len(datos))    
    id_material_proyectos=request.form['id_material_proyectos']
    cantidad=request.form['cantidad']
    token=request.form['token']
    if idRegisterUser(session['idUsuario']) and token=='fdfdsfdshj343245rgtrtgr':
        session['id_material_proyectos']=id_material_proyectos
        connection=mysql.connector.connect(host='localhost', user='root', password='',database='projectdesign')
        cursor=connection.cursor(dictionary=True)
        cursor.execute("INSERT INTO lista_material(id_usuario,id_Proyecto,id_presupuesto,id_modulo,id_sub_modulo,id_material,id_material_proyectos,cantidad) values("+session['idUsuario']+","+session['id_proyecto']+","+session['id_presupuesto']+","+session['id_modulo']+","+session['id_sub_modulo']+","+session['id_material_sub']+","+id_material_proyectos+",'"+cantidad+"')")
        connection.commit()
    else:
        return "usuario no valido no puede hacer esta operacion"
    seleccion=datosMaterialesProyectLoad(session['idUsuario'])
    return redirect(url_for('lista_materiales_add'))
    #datos=datosListaMaterialesLoad()
    #return render_template('Proyecto_add_material.html',seleccion=seleccion,datos=datos,sizeseleccion=len(seleccion),sizedata=len(datos))    
if __name__ == '__main__':
    app.secret_key='esta es una clave secreta'
    app.run(debug=True)
    #app.run(host= '0.0.0.0',port='5000',debug=True)
    