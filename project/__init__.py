from fastapi import FastAPI
from fastapi import HTTPException

from .routers import user_router
from .routers import review_router

from .database import database as connection
from .database import User, Movie, UserReview


app = FastAPI(tittle='Proyecto',
            description='meh',
            version='1'
            )

app.include_router(user_router)
app.include_router(review_router)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    connection.create_tables([User,Movie,UserReview])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
