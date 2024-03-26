from fastapi import APIRouter

router=APIRouter(prefix="/productos",
                 tags=["productos"],
                 responses={404:{"Mensaje":"Ese producto no existe"}})

productos= ["Almejas","Croquetas","Morcilla","Rabo de toro"]
@router.get("/")
async def ObtenerProductos():
    return productos

@router.get("/{id}")
async def ObtenerProductoId(id:int):
    return productos[id]

