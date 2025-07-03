from fastapi import FastAPI

app = FastAPI(
    title="Techeron API",
    description="FastAPI + Swagger + ECS CI/CD Demo",
    version="1.0.0"
)

# Root endpoint
@app.get("/", tags=["System"])
def read_root():
    return {"message": "Welcome to Techeron FastAPI!"}

# Health check endpoint
@app.get("/health", tags=["System"])
def health_check():
    """
    Health check endpoint to verify if the API is alive.
    """
    return {"status": "alive"}

# Math endpoint
@app.get("/add", tags=["Math"])
def add_numbers(a: int, b: int):
    """
    Add two numbers and return the result.
    Example: /add?a=5&b=3 returns {"result": 8}
    """
    return {"result": a + b}

