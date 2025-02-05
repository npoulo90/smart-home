from fastapi import FastAPI
from fastapi import FastAPI

app = FastAPI(
    title="API Gateway",
    description="Smart Home API Gateway",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "API Gateway Online"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
