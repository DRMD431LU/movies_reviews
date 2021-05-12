from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import HTTPException

from .routers import user_router
from .routers import review_router

from .database import database as connection
from .database import User, Movie, UserReview


app = FastAPI(tittle='Proyecto',
            description='meh',
            version='1'
            )

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)
api_v1.include_router(review_router)
app.include_router(api_v1)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    connection.create_tables([User,Movie,UserReview])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
