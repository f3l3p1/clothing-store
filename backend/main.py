from fastapi import FastAPI
from routes.product_routes import product_router

app = FastAPI()

app.include_router(product_router)

@app.get("/")
def home():
    return {"message": "Welcome to Clothing Store API"}

# Ejecutar con: uvicorn main:app --reload
