from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_SSL_MODE = os.getenv("DB_SSL_MODE", "require")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?sslmode={DB_SSL_MODE}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup_event():
    print("\033[92m✅ API funcionando em http://127.0.0.1:8000 🚀\033[0m")

@app.on_event("shutdown")
async def shutdown_event():
    engine.dispose()
    print("⛔ API encerrada e conexão com o banco fechada.")

@app.get("/dataframe_pmdf")
def get_dataframe_pmdf(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT * FROM dataframe_pmdf"))
        records = [dict(row) for row in result.mappings()]
        return {"data": records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar dados: {str(e)}")
