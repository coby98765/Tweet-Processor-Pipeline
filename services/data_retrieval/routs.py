from fastapi import FastAPI
from starlette.responses import JSONResponse

from dal import DAL

app = FastAPI()
dal = DAL()

@app.get('/antisemitic')
def get_all_antisemitic():
    try:
        all_data = dal.get_all('antisemitic')
        return JSONResponse(content=all_data)
    except Exception as ex:
        print(ex)
        raise Exception(ex)

@app.get('/not_antisemitic')
def get_all_not_antisemitic():
    try:
        all_data = dal.get_all('not_antisemitic')
        return JSONResponse(content=all_data)
    except Exception as ex:
        print(ex)
        raise Exception(ex)