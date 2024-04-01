from fastapi import APIRouter,status,HTTPException
from  models.user import Usuario
from client import db
from schemas.user import user_schema,users_schema

route=APIRouter(responses={404: {"Mensaje":"Ese usuario no existe"}})


@route.post("/crearUsuario",status_code=status.HTTP_201_CREATED)
async def usuario(usuario:Usuario):
    if type(buscarPorNombre(usuario.nombre))==Usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="El usuario ya existe")

    usuario_diccionario=dict(usuario)
    del usuario_diccionario["id"]

    id=db.local.users.insert_one(usuario_diccionario).inserted_id
    usuario_nuevo= user_schema(db.local.users.find_one({"_id":id}))
    
    return Usuario(**usuario_nuevo)


def buscarPorNombre(nombre:str):
    try:
        usuario= db.local.users.find_one({"nombre":nombre})
        usuario_nuevo=Usuario(**user_schema(usuario))
        return usuario_nuevo
    except:
        return "No se ha encontrado el usuario"

@route.get("/usuarios")
async def obtenerTodos():
    return users_schema(db.local.users.find())