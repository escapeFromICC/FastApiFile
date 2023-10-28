git add .
git commit -m 

git config --global user.name escapeFromICC
git config --global user.email xxx

# FastApiFile
create virtual enviroment:
-- python -m venv tutorial-env

activate:
-- source tutorial-env/bin/activate

install server:
-- pip install uvicorn

install fastapi:
-- pip install fastapi

run terminal:
-- uvicorn main:app --reload

check api:
-- http://localhost:8000/docs

// get method:
1. path parameters:
@app.get('/blog/{id}')
def index(id:int):
    return ("message": f"Blog with id {id}")

2. predefined values: Predefined values with Enum
predefined values with Enum
class BlogType(str, Enum):
    short = 'short'
    stroy = 'stroy'
    howto = 'howto'

@app.get('/blog/type/{type}')
def blog_type(type:BlogType):
    return ("message": f"Blog type {type}")

3. query parameters:
Any function parameters not part of the path
@app.get('/blog/all')
def get_blogs(page, page_size):
   return {'message': f'All {page_size} blogs on page {page}'}

Default values
def get_blogs(page = 1, page_size = 10):
   return {'message': f'All {page_size} blogs on page {page}'}

Optional parameters
from typing import Optional
def get_blogs(page = 1, page_size: Optional[int] = None):
   return {'message': f'All {page_size} blogs on page {page}'}

Query & path parameters
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id:int, comment_id:int, valid:bool = True, username:Optional[str] = None):
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}
