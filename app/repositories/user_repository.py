from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

#this class is used to interact with the User table in the database with methods to create, get, update, and delete users
class UserRepository:

    @staticmethod
    def create(
        db: Session,
        user: UserCreate
    ) -> User:
        db_user = User(
            name=user.name,
            email=user.email,
            phone=user.phone
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def get_all(db: Session) -> list[User]:
        return db.query(User).all()

    @staticmethod
    def get_by_id(
        db: Session,
        user_id: int
    ) -> User | None:
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ) -> User | None:
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        db_user: User,
        user: UserUpdate
    ) -> User:
        if user.name is not None:
            db_user.name = user.name

        if user.email is not None:
            db_user.email = user.email

        if user.phone is not None:
            db_user.phone = user.phone

        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def delete(
        db: Session,
        db_user: User
    ) -> None:
        db.delete(db_user)
        db.commit()

    @staticmethod
    def get_by_phone(
        db: Session,
        phone: str,
    ) -> User | None:
        return (
        db.query(User)
        .filter(User.phone == phone)
        .first()
    )