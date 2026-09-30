from fastapi import FastAPI

app = FastAPI(
    title="HireFlow AI Service",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {
        "success": True,
        "message": "HireFlow AI service is running"
    }