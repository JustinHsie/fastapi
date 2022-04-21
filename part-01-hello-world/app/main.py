from fastapi import FastAPI, APIRouter

# Instantiate FastAPI object
app = FastAPI(
    title="Recipe API", openapi_url="/openapi.json"
)

# Instantiate APIRouter object
api_router = APIRouter()

# Define GET route by adding decorator to root()
@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}

# Register APIRouter api_router object with FastAPI app object
app.include_router(api_router)

# Runs in debug mode if module is called directly ie run with python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")