from fastapi import FastAPI
from Routers import productos,usuarios


app=FastAPI()

app.include_router(productos.router)
app.include_router(usuarios.route) 

@app.get("/")
async def inicio():
        return "Has iniciado correctamente el servidor"