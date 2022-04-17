from fastapi import FastAPI


'''
Что бы запустить нужно выполнить команду:
docker run -it -p 8000:8000 app
'''

app=FastAPI()

@app.get("/ping/", status_code=200)
def root():
    return {"message": "pong"}

