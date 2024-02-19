from datetime import datetime, timedelta
from fastapi import HTTPException
from jose import JWTError
from starlette import status
from src.routes import jwt


class EmailTokenManager:
    def __init__(self, SECRET_KEY, ALGORITHM):
        self.SECRET_KEY = SECRET_KEY
        self.ALGORITHM = ALGORITHM


def create_email_token(self, data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"iat": datetime.utcnow(), "exp": expire})
    token = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
    return token


def get_email_from_token(self, token: str):
    try:
        payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
        email = payload["sub"]
        return email
    except JWTError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Invalid token for email verification")


