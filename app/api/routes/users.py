from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import dependencies
from app.crud import user as crud_user
from app.schemas import user as schemas_user

router = APIRouter()

@router.post("/", response_model=schemas_user.User, status_code=201)
async def create_user(user: schemas_user.UserCreate, db: AsyncSession = Depends(dependencies.get_db)):
    return await crud_user.create_user(db=db, user=user)

@router.get("/", response_model=List[schemas_user.User])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(dependencies.get_db)):
    users = await crud_user.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=schemas_user.User)
async def read_user(user_id: int, db: AsyncSession = Depends(dependencies.get_db)):
    db_user = await crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=schemas_user.User)
async def update_user(user_id: int, user: schemas_user.UserUpdate, db: AsyncSession = Depends(dependencies.get_db)):
    db_user = await crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud_user.update_user(db=db, db_user=db_user, user=user)

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int, db: AsyncSession = Depends(dependencies.get_db)):
    db_user = await crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await crud_user.delete_user(db=db, db_user=db_user)
    return None
