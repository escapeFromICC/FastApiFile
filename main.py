from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/')
def index():
    return 'hello world...'

@app.get('/hello')
def index():
    return 'hello'

# @app.get('/blog/all')
# def get_all_blogs(page, page_size):
#     return {'message': f'All {page_size} blogs on page {page}'}

@app.get('/blog/all')
def get_all_blogs(page = 1, page_size:Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}

@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id:int, comment_id:int, valid:bool = True, username:Optional[str] = None):
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

@app.get('/blog/{id}')
def get_blog(id:int):
    return {'message':f'Blog with id {id}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type:BlogType):
    return {'message':f'Blog type {type}'}




