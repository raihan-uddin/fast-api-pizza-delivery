from fastapi import APIRouter

auth_router = APIRouter(
    prefix="/auth",
    tags=['authentication']
)


@auth_router.get('/')
async def hello():
    return {"message": "Hello World from auth"}
