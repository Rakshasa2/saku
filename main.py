from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()


class Word(BaseModel):
    word: str


class Page(BaseModel):
    title: str
    content: str


@app.post("/search/{src}")
def src(src: str, num: int):
    return wikipedia.search(src, results=num)


@app.post("/suggest/word")
def suggest(word: Word):
    return wikipedia.suggest(word)


@app.post("/page/result", response_model=Page)
def return_page(title: Word):
    return wikipedia.page(title)
