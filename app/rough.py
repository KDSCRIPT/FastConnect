from app.config import settings
SQLALCHEMY_DATABASE_URL=f"postgresql+psycopg://{settings.database_username}:{settings.database_password}:{settings.database_port}/{settings.database_name}"
print(SQLALCHEMY_DATABASE_URL)