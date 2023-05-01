from fastapi import FastAPI, Query, Path, Body, Cookie, Response
from fastapi.responses import JSONResponse, RedirectResponse
from enum import Enum
from pydantic import BaseModel, Required, Field, HttpUrl
from typing import Annotated

application = FastAPI()

fake_db = [{"item_name":"crazy"},{"item_name":"lazy"},{"item_name":"cheesy"},]
class MyChoice(str, Enum):
    yellow = 'yellow'
    blue = 'blue'
    green = 'green'

    def __str__(self) -> str:
        return super().__str__()
class ApiConcert(BaseModel):
    name:str = Field(description='name of the concert', alias=" name of concert")
    description: str | None = Field(min_length=20,max_length=300, alias="put description in")
    ticket_price: float = Field(gt=0,lt=1000, description="must be greater than zero")
    tax: float | None = None
    url: HttpUrl | None = None

    def __str__(self) -> str:
        return super().__str__()

@application.get('/things/')
async def read_things(thing_id: Annotated[str, Path(title="part_of_path")], q_param: Annotated[str | None, Query(alias="thing_query")] = None):
    results = {"thing_id":thing_id}
    if q_param:
        results.update({'q_param':q_param})

@application.get('/concert_program/')
async def get_concert_program(additional_parameter: Annotated[
        str | None, Query(
        min_length=3,
        title="any title",
        description="nothing special",
        alias="my-query",
        deprecated=True,
        include_in_schema=False,
        )
    ] = Required):
    results = {"programs":[{"concert_id":"foo"},{"concert_id":"boo"}]}
    if additional_parameter:
        results.update({'additional_parameter':additional_parameter})
    return results

@application.put('/concerts/{concert_id}')
async def concert_update(concert: ApiConcert, concert_id: int, additional_parameter: str | None = None):
    result = {"concert_id":concert_id, **concert.dict()}
    if additional_parameter:
        result.update({"new param": additional_parameter})
    return result

@application.post('/concerts/create/', response_model= ApiConcert)
async def concert_create(concert:ApiConcert):
    concert_dictionary = concert.dict()
    if concert.tax:
        concert_dictionary.update({"price with tax":concert.ticket_price + concert.tax})
    return concert_dictionary

@application.get('/users/{user_id}/values/{value_id}')
async def get_multiple_data(user_id: int, value_id: int, q_param: str | None = None, is_true: bool = False):
    unit  = {"user":user_id, "value":value_id}
    if q_param:
        unit.update({"q_param":q_param})
    if is_true == True:
        unit.update({"description": "so it is all true"})
    return unit

@application.get('/items_list/')
async def read_db(skip: int = 0, limit: int = 10, q_parameter: str | None = None):
    if q_parameter:
        return {"db_values":fake_db[skip:skip + limit],"q_parameter":q_parameter}
    else:
        return fake_db[skip:skip + limit]

@application.get('/items/{item_id}')
async def check_item(item_id: str):
    return {'item_id':item_id}

@application.get('/colors/{color}')
async def get_color_name(color: MyChoice):
    if color is MyChoice.yellow:
        return {"colour": color, "message":"colour is yellow"}
    elif color.value == 'blue':
        return {"colour": "colour is blue"}
    else:
        return {"colour": "colour is green"}

# @my_app.get('/')
# async def main_page_info():
#     return {'message':"Welcome to home page!"}

# @my_app.get('/api/')
# async def get_data():
#     return {'message':"Hello in API section!"}

# @my_app.put('/api/concerts/')
# async def update_data():
#     return {'message':"Hello World!"}

# @my_app.delete("/api/concert/{concert_id}")
# async def delete_concert(concert_id: str):
#     return {'message':f'concert no.{concert_id} was not found in database'}
    # try:
    #     concert_to_delete = Concert.objects.get(id=concert_id)
    #     concert_to_delete.delete()
    #     return {'message':'concert was removed from database'}
    # except:
    #     return {'message':f'concert no.{concert_id} was not found in database'}
