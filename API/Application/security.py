from Models import actors, token, users

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from datetime import datetime, timedelta
from typing import Annotated

secretKey = "5db9eaaa921532ec48984fecfa927349a96f75973edf5991de686f1259a56d261"
algorithm = "HS256"
accessTokenExpireMinutes = 30
