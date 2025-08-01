from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
from app import models
from app import utils
from app import oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(tags=["Authentication"])

@router.post("/login",response_model=schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    if not user_credentials.username or not user_credentials.password:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Username and password required")
    
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Invalid Credentials")
    
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}