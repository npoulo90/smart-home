from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)

@router.post("/token")
async def get_token():
    return {"access_token": "test_token", "token_type": "bearer"}