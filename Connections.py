import pymysql
from pymysql import connect
from dotenv import dotenv_values

config = dotenv_values('.env')

class PyConnection():
    HOST = config['HOST']
    USER = config['USER']
    PASSWORD = config['PASSWORD']
    DATABASE = config['DATABASE']
    
    @classmethod
    def Cnx(cls):
        try:
            cnx = connect(host=cls.HOST, user=cls.USER, password=cls.PASSWORD, database=cls.DATABASE, cursorclass=pymysql.cursors.DictCursor)
            if cnx:
                return cnx
        except pymysql.Error as e:
            raise Exception(e)
        
    @classmethod
    def insertUser(cls, username, password, is_admin):
        try:
            c = PyConnection()
            conn = c.Cnx()
            with conn.cursor() as cur:
                cur.callproc('insertUser', [username, password, is_admin,])
                conn.commit()
                cur.close()
                conn.close()
        except pymysql.Error as e:
            raise Exception(e)        
        
        
    @classmethod
    def getUsers(cls):
        try:
            c = PyConnection()
            conn = c.Cnx()
            with conn.cursor() as cur:
                cur.callproc('getUsers')
                result = cur.fetchall()
                if result:
                    return result
                else:
                    False
                conn.commit()
                cur.close()
                conn.close()
        except pymysql.Error as e:
            raise Exception(e)    
        
    @classmethod
    def insertCedula(cls, app,apm,nombre,domicilio,colonia,mcpio,cp,local,num_cel,email,l_nac,f_nac,nss,rfc,curp,edo_civil,sexo,matricula,categoria,adsc,turno,t_contr,f_ingr,antiguedad):
        try:
            c = PyConnection()
            conn = c.Cnx()
            with conn.cursor() as cur:
                cur.callproc('insertCedula',[app,apm,nombre,domicilio,colonia,mcpio,cp,local,num_cel,email,l_nac,f_nac,nss,rfc,curp,edo_civil,sexo,matricula,categoria,adsc,turno,t_contr,f_ingr,antiguedad,])
                conn.commit()
                cur.close()
                conn.close()
        except pymysql.Error as e:
            raise Exception(e)
        

    @classmethod
    def listCedula(cls):
        try:
            c = PyConnection()
            conn = c.Cnx()
            with conn.cursor() as cur:
                cur.callproc('listAll')
                ctx = cur.fetchall()
                if ctx:
                    return ctx
                conn.commit()
                cur.close()
                conn.close()
        except pymysql.Error as e:
            raise Exception(e)


        
if __name__ == '__main__':
    conn = PyConnection()
    if conn.Cnx():
        print('Connected')
    
