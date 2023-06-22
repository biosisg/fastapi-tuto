from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


app = FastAPI()


@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    # Only get 10 published blogs

    if published:
        return {
            'data': f'{limit} published blogs from the db'
        }
    return {
        'data': f'{limit} blogs from the db'
    }


@app.get('/blog/unpublished')
def unpubllished():
    return {
        'data': 'All unpublished blogs'
    }


@app.get('/blog/{id}')
def show(id: int):
    # Fetch blog with id = id
    return {
        'data': id
    }


@app.get('/blog/{id}/comments')
def comments(id):
    # Fetch comments of blog with id = id
    return {
        'data': {'1', '2'}
    }


@app.post('/blog')
async def create_blog(blog: Blog):
    return blog
    return {'data': 'Blog is created.'}