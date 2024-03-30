from fastapi import FastAPI
from Routers import productos,usuarios,seguridad
from fastapi.staticfiles import StaticFiles


app=FastAPI()

app.include_router(productos.router)
app.include_router(usuarios.route) 
app.include_router(seguridad.router)

app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/")
async def inicio():
        return "Has iniciado correctamente el servidor"