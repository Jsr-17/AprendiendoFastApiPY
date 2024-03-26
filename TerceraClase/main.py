from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

class Usuario(BaseModel):
    nombre:str
    edad:int
    pelo:bool
    id:int

usuarios=[Usuario(nombre="Jose",edad=24,pelo=False,id=1),
          Usuario(nombre="Manuel",edad=1,pelo=False,id=2),
          Usuario(nombre="pepe",edad=14,pelo=True,id=3)]

@app.post('/user/',status_code=201)
async def createUser(user: Usuario ):
    if type(buscarPor(user.id)) == Usuario:
       raise HTTPException(status_code=404,detail="El usuario ya existe")
    else:
        usuarios.append(user)
        return "Usuario insertado con exito"

@app.put("/user/")
async def modificarUsuario(user:Usuario ):
    try:
        for index, usuario in enumerate(usuarios):
            if usuario.id== user.id:
                usuarios[index]=user
                return "Usuario cambiado"
    except:
        return "Algo ha fallado"

@app.delete("/user/{id}")
async def eliminaUsuario(user:Usuario):
    try:
        for index, usuario in enumerate(usuarios):
            if usuario.id== user.id:
                del usuarios[index]
                return "Usuario eliminado"
    except:
        return "No ha sido posible eliminar al usuario"



@app.get("/user/")
async def verUsuario():
    return usuarios

def buscarPor(id:int):
    Atributo=filter(lambda atributo:atributo.id==id,usuarios)
    try:
        return list(Atributo)[0]
    except:
        return "Ha ocurrido un error"

