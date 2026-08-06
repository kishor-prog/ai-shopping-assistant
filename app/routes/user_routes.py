from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_order_db
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
)
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_order_db),
):
    return UserService.create_user(
        db,
        user,
    )


@router.get("/", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_order_db),
):
    return UserService.get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_order_db),
):
    return UserService.get_user(
        db,
        user_id,
    )

@router.get("/phone/{phone}", response_model=UserResponse)
def get_user_by_phone(
    phone: str,
    db: Session = Depends(get_order_db),
):
    return UserService.get_user_by_phone(
        db,
        phone,
    )


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_order_db),
):
    return UserService.update_user(
        db,
        user_id,
        user,
    )


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_order_db),
):
    return UserService.delete_user(
        db,
        user_id,
    )