from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models import Blog
from ..schemas import Blog as Schema


def get_all(db: Session):
    return db.query(Blog).all()


def show(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND 
        # return { 'Detail': f'Blog with the id {id} is not available'}
    return blog


def create(request: Schema, db: Session):
    new_blog = Blog(title=request.title, body=request.body, published=request.published, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def destroy(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
    
    blog.delete(synchronize_session=False)
    db.commit()

    return 'Done'


def update(id: int, request: Schema, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')

    blog.update(request.dict())
    db.commit()

    return 'Updated'