from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate

#this class is used to handle the business logic for user operations create, get, update, delete
class UserService:

    @staticmethod
    def create_user(
        db: Session,
        user: UserCreate
    ):
        # Check if email already exists
        existing_email = UserRepository.get_by_email(
            db,
            user.email
        )

        if existing_email:
            raise HTTPException(
                status_code=400,
                detail=f"Email '{user.email}' is already registered."
            )

        # Check if phone already exists
        existing_phone = UserRepository.get_by_phone(
            db,
            user.phone
        )

        if existing_phone:
            raise HTTPException(
                status_code=400,
                detail=f"Phone '{user.phone}' is already registered."
            )

        return UserRepository.create(
            db,
            user
        )

    @staticmethod
    def get_users(
        db: Session
    ):
        return UserRepository.get_all(db)

    @staticmethod
    def get_user(
        db: Session,
        user_id: int
    ):
        user = UserRepository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        return user

    @staticmethod
    def get_user_by_phone(
        db: Session,
        phone: str
    ):
        user = UserRepository.get_by_phone(
            db,
            phone
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        return user

    @staticmethod
    def update_user(
        db: Session,
        user_id: int,
        data: UserUpdate
    ):
        user = UserRepository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        # Check email only if it is being updated
        if data.email is not None:

            existing_email = UserRepository.get_by_email(
                db,
                data.email
            )

            if (
                existing_email
                and existing_email.id != user_id
            ):
                raise HTTPException(
                    status_code=400,
                    detail=f"Email '{data.email}' is already registered."
                )

        # Check phone only if it is being updated
        if data.phone is not None:

            existing_phone = UserRepository.get_by_phone(
                db,
                data.phone
            )

            if (
                existing_phone
                and existing_phone.id != user_id
            ):
                raise HTTPException(
                    status_code=400,
                    detail=f"Phone '{data.phone}' is already registered."
                )

        return UserRepository.update(
            db,
            user,
            data
        )

    @staticmethod
    def delete_user(
        db: Session,
        user_id: int
    ):
        user = UserRepository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        UserRepository.delete(
            db,
            user
        )

        return {
            "message": "User deleted successfully"
        }