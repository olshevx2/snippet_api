from fastapi import FastAPI
from api.routes import router
from db.database import engine, Base

app = FastAPI(title="Snippets API")
app.include_router(router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def read_root():
    return {"message": "Snippets API is running"}