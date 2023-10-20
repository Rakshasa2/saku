from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI()
class  WikiInput(BaseModel):
    name: str
    quantity: int


@app.get("/route")
def wiki():
    return wikipedia.search("Bill", results=2)


@app.post("/wiki/{name}")
def wiki_search(name, quantity: WikiInput):
    return wikipedia.search(name, results=quantity)

@app.get("/wikipedia/{name}")
def wiki_suggest(name: str):
    return wikipedia.suggest(name)

@app.get("/name")
def wiki_summary(name:str):
    return wikipedia.summary(name)
