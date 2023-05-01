from fastapi import FastAPI

app = FastAPI()

concerts = [
    {
     "id":1,
     "concert_pianist": "Piter"
    },
    {
     "id":2,
     "concert_pianist": "Kasia"
    },
    {
     "id":3,
     "concert_pianist": "Pyrć"
    },
]

@app.get('/', tags=['ROOT'])
async def root() -> dict:
    return {"name": "Piter"}

@app.get('/concert/', tags=['getting concerts'])
async def get_concert() -> dict:
    return {'data':concerts}

@app.post('/concert/', tags=['create concert'])
async def create_concert(concert: dict) -> dict:
   concerts.append(concert)
   return {'data':'added succesfully'}

@app.put('/concert/{id}', tags=['update concert'])
async def update_concert(id: int, body: dict) -> dict:
    for concert in concerts:
        if int(concert['id']) == id:
            concert["concert_pianist"] = body["concert_pianist"]
            return {"message":f'concert no.{id} has been updated'}
    return {"message":f'concert no.{id} not found'}

@app.delete('/concert/{id}', tags=['delete concert'])
async def delete_concert(id: int) -> dict:
    for concert in concerts:
        if int(concert['id'])== id:
            concerts.remove(concert)
            return {"message":f'concert no.{id} has been removed'}
    return {"message":f'concert no.{id} not found'}