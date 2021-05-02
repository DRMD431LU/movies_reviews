from fastapi import FastAPI
from fastapi import HTTPException
from database import database as connection
from database import User, Movie, UserReview
from schemas import UserRequestModel
from schemas import UserResponseModel

app = FastAPI(tittle='Proyecto',
            description='meh',
            version='1'
            )

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    connection.create_tables([User,Movie,UserReview])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

@app.get('/')
async def index():
    return 'fastapi'

@app.get('/about')
async def about():
    return "about"


@app.post('/users', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'El username ya se encuentra en uso')

    hash_password = User.create_password(user.password)
    user = User.create(
        username=user.username,
        password=hash_password
    )
    return user
