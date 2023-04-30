from fastapi import FastAPI

my_app = FastAPI()

@my_app.get('/api/')
async def get_data():
    return {'message':"Hello World!"}

@my_app.put('/api/concerts/')
async def update_data():
    return {'message':"Hello World!"}

@my_app.get("/api/concert/{concert_id}")
async def delete_concert(concert_id: str):
    return {'concert_id':concert_id}
