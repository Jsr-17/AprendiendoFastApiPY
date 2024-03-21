from fastapi import FastAPI
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
@app.get("/users")
async def obtenerUsuarios():
    return usuarios

@app.get("/obtenerUsuarioId/{id}")
async def obtenerporId(id:int):
    idUsuario=filter(lambda idUsuario: idUsuario.id==id,usuarios)
    try:
        return list(idUsuario)[0]
    except:
        return "Ha ocurrido un error"

@app.get("/obtenerUsuarioNombre/{nombre}")
async def obtenerporNombre(nombre:str):
    nombreUsuario=filter(lambda nombreUsuario:nombreUsuario.nombre==nombre,usuarios)
    try:
        return list(nombreUsuario)[0]
    except:
        return "Ha ocurrido algun error"
    

@app.get("/user/")
async def user(id:int):
    return buscarPor(id)




def buscarPor(id:int):
    Atributo=filter(lambda atributo:atributo.id==id,usuarios)
    try:
        return list(Atributo)[0]
    except:
        return "Ha ocurrido un error"

