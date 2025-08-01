from fastapi import Response,status,HTTPException,Depends,APIRouter
from app.database import get_db
from sqlalchemy.orm import Session,joinedload
from sqlalchemy import func
from app import models
from app import schemas
from typing import List,Optional
from app import oauth2


router=APIRouter(prefix="/posts",tags=["Posts"])
@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.PostOut])
def get_posts(db:Session= Depends(get_db),current_user:int=Depends(oauth2.get_current_user),limit:int=10,skip:int=0,search:Optional[str]=""):
    #cursor.execute("""SELECT * FROM posts""")
    #posts=cursor.fetchall()
    #posts=db.query(models.Post).filter(models.Post.owner_id==current_user.id).all()
    # posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    results=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return results

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db:Session= Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    #new_post=cursor.fetchone()
    #conn.commit()
    # new_post=models.Post(title=post.title,content=post.content,published=post.published)
    new_post=models.Post(owner_id=current_user.id,**post.model_dump())#convert to dict and unpack 
    db.add(new_post)
    db.commit()
    db.refresh(new_post)#retrieve new post and store in new_post
    return new_post

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.PostOut)
def get_post(id:int,db:Session= Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # post=db.query(models.Post).filter(models.Post.id==id).first()

    post=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    #cursor.execute("""SELECT * from posts WHERE id=%s""",(str(id),))
    #post=cursor.fetchone()
    if not post:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"post with id: {id} was not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
    return post

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session= Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #cursor.execute("""DELETE FROM posts WHERE id = %s returning *""",(str(id),))
    #deleted_post=cursor.fetchone()
    #conn.commit()
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id: {id} does not exist")
    
    if post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not authorized to perform required action")

    post_query.delete(synchronize_session=False)
    db.commit()
    # my_posts.pop(index)
    # return {"message":"Post was successfully deleted"} 204 should be blank response hence this is wrong. Error called content is too long is thrown in old fastapi
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",status_code=status.HTTP_200_OK, response_model=schemas.Post)
def update_post(id:int,post:schemas.PostCreate,db:Session= Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #cursor.execute("""UPDATE posts SET title=%s,content=%s,published=%s WHERE id= %s RETURNING *""",(post.title,post.content,post.published,str(id)))
    #updated_post=cursor.fetchone()
    #conn.commit()
    post_query=db.query(models.Post).options(joinedload(models.Post.owner)).filter(models.Post.id==id)
    original_post=post_query.first()
    if original_post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id: {id} does not exist")
    
    if original_post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not authorized to perform required action")
    post_query.update(post.model_dump(),synchronize_session=False)        
    db.commit()
    db.refresh(original_post)  # Refresh to include updated values + relationships
    return original_post