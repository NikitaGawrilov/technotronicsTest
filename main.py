from fastapi import FastAPI

app = FastAPI(
    title='Technotronics Test Case by N. Gavrilov'
)


@app.get('/')
def hello():
    return {'msg': 'hello!'}
