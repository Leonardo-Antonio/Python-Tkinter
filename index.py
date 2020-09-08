import moduls.gui as gui
import moduls.controller as controller

ctlr =  controller.Controller()

text = ("Nombre :", "Apellido paterno :", "Apellido materno :","Edad :", "Correo :", "Teléfono :")
btn_name = ("Add", "Update", "Delete", "Search", "Clear")

Main = gui.Interface()
Main.label_title("Agenda con archivos", "red", 0, 0)

for x in range(5):
    Main.label_text(text[x], "black", x+1, 0)
Main.label_text("Teléfono :", "black", 1, 3)

text_var = [ gui.StringVar() for i in range(6) ]  

def list_users_table():
    Main.dataGrid(ctlr.list_user())
list_users_table()

#ID seleccionado 
ID = 0

def save():
    data = [ text_var[i].get() for i in range(6) ]
    rspt = ctlr.save_user(data)
    if rspt[0] == False:
        Main.msj_success(rspt[1], rspt[2])
    else:
        Main.msj_success(rspt[0], rspt[1])
        list_users_table()

def update():
    data = [ i.get() for i in text_var ]
    data.append(ID)
    rspt = ctlr.update(data)
    if rspt[0] == False:
        Main.msj_err(rspt[1], rspt[2])
    else:
        Main.msj_success(rspt[0],rspt[1])
        list_users_table()

def delete():
    rspt = ctlr.delete(Main.select_user()[1])
    if(rspt[0] == False):
        Main.msj_err(rspt[1], rspt[2])
    else:
        Main.msj_success(rspt[0],rspt[1])
        list_users_table()

def clear():
    Main.clear(text_var)


def search():
    rspt = Main.select_user()
    global ID 
    ID = rspt[1]
    if rspt[0] == False:
        Main.msj_err(rspt[1], rspt[2])
    else:
        data = ctlr.search_user_id(Main.select_user()[1])
        for i in range(6):
            text_var[i].set(data[i+1])

func = [save, update, delete, search, clear]

for i in range(5):
    Main.text_box( i+1, 1, text_var[i] )
    Main.btn( btn_name[i], 10, 0, i, 1, func[i])
Main.text_box(1, 4, text_var[5])

Main.close()
