from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database import get_db
from .. import schemas
from ..repository import user


router = APIRouter(
    prefix = "/user",
    tags = ['Users']
)


@router.post('/', response_model=schemas.ShowUser)
async def create(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def show(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)