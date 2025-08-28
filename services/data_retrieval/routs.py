from fastapi import FastAPI
from manager import Manager

app = FastAPI()
manager = Manager()

@app.get('/antisemitic')
def get_all_antisemitic():
    try:
        return manager.run('antisemitic')
    except Exception as ex:
        print(ex)
        raise Exception(ex)

@app.get('/not_antisemitic')
def get_all_not_antisemitic():
    try:
        return manager.run('not_antisemitic')
    except Exception as ex:
        print(ex)
        raise Exception(ex)