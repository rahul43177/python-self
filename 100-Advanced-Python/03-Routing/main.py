from fastapi import FastAPI , Depends
from routers import books


app = FastAPI()

@app.get("/")
async def health_check():
    return {
        "message" : "Health is fine!"
    }

app.include_router(
    books.router ,
    prefix="/api/v2" ,
    tags=["Books"]
)
