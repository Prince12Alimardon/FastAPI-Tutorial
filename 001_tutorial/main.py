from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello():
    return {"Text": "Hello Alimardon"}

@app.get('/books')
async def books():
    data = {
        'id': 1,
        "name": "Million dollarlik xatolar",
        'author': 'Jon Kexo',
        'description': 'Biznes va shaxsiy rivojlanishni o\'rgatuchi kitob'
    }
    return data
