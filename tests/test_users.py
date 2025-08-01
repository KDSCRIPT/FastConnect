from app import schemas
from app.config import settings
import jwt
import pytest

def test_create_user(client):
    res=client.post("/users/",json={"email":"hello1234@gmail.com","password":"password123"})
    new_user=schemas.UserOut(**res.json())
    assert new_user.email=="hello1234@gmail.com"
    assert res.status_code==201

def test_login_user(client,test_user):
    res=client.post("/login",data={"username":test_user["email"],"password":test_user["password"]})
    login_res=schemas.Token(**res.json())
    payload=jwt.decode(login_res.access_token,settings.secret_key,algorithms=[settings.algorithm])
    id:str=payload.get("user_id")
    assert id==test_user["id"]
    assert login_res.token_type=="bearer"
    assert res.status_code==200

@pytest.mark.parametrize("email,password,status_code,detail",[("wrongmail@gmail.com","password123",401,"Invalid Credentials"),("hello1234@gmail.com","wrongpassword",401,"Invalid Credentials"),("wrongmail@gmail.com","wrongpassword",401,"Invalid Credentials"),(None,"password123",422,"Username and password required"),("hello1234@gmail.com",None,422,"Username and password required")])
def test_incorrect_login(test_user,client,email,password,status_code,detail):
    res=client.post("/login",data={"username":email,"password":password})
    assert res.status_code==status_code
    assert res.json().get("detail")==detail