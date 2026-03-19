from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
#соединение с бд
engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False}
)
#настроить соединение и сессии с бд 
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)
Base = declarative_base() #создан чтоб писать модели 

def get_db():
    #создаем сессию 
    db = SessionLocal()
    #попытка передать сессию
    try:
        yield db
    finally:
        db.close()

def init_bd():
    Base.metadata.create_all(bind=engine)