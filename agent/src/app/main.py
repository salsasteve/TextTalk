from fastapi import FastAPI
from app.api.api_v1.api import router as api_router
from mangum import Mangum

app = FastAPI(title="Agent API", version=0.1, docs_url="/api/v1/docs", redoc_url="/api/v1/redoc")


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)
