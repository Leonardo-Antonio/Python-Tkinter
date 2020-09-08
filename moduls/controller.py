import moduls.crud as crud

class Controller:
    def __init__(self):
        self.model = crud.CRUD()
    
    def list_user(self):
        return self.model.list_user()
         
    def save_user(self, data):
        if data[0] == "" and data[1] == "" and data[2] == "":
            return [False, "Error", "Llene los campos"]
        else:
            self.model.new_user(data)
            return ['Agregado', f'Usuario {data[0]} añadido']

    def update(self, data):
        if data[6] == "" or data[6] == 0:
            return [False, "Error", "Seleccione un usuario"]
        else :
            self.model.update_user(data)
            return ["Actualizado", f'Datos de usurio {data[0]}']

    def delete(self, id):
        if id == "" or id == 0:
            return [False, "Error", "Seleccione un usuario"]
        else :
            self.model.delete_user(id)
            return ["Eliminado", 'Usurio eliminado']

    def search_user_id(self, id):
        if id == "" or id == 0:
            return "Ingrese el ID"
        else :
            return self.model.search_user(id)
    def close(self):
        self.model.close()
