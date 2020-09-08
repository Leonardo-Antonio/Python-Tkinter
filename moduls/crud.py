import mysql.connector

class CRUD:
    def __init__(self):
        self.dbconnection = {
            'host' : 'localhost',
            'user' : 'leo',
            'password' : 'chester',
            'database' : 'bd_task4' 
        }
        self.connect = mysql.connector.connect(**self.dbconnection)
        self.cursor = self.connect.cursor()

    def list_user(self):
        sql = "select id, concat(name,' ',a_p,' ',a_m) ,correo from tb_user"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def new_user(self, data):
        sql = f'insert into tb_user values (null, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(sql, data)
        self.connect.commit()

    def search_user(self, id):
        sql = f'select * from tb_user where id = {id}'
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def delete_user(self, id):
        sql = f'delete from tb_user where id = {id}'
        self.cursor.execute(sql)
        self.connect.commit()

    def update_user(self, data):
        sql = "update tb_user set name=%s, a_p=%s, a_m=%s, edad=%s, correo=%s, telefono=%s where id = %s"
        self.cursor.execute(sql, data)
        self.connect.commit()

    def close(self):
        self.connect.close()
        self.cursor.close()

crud = CRUD()
crud.delete_user(5)