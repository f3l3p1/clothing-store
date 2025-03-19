from fastapi import APIRouter
from models.product import Product
from database import products_collection

product_router = APIRouter()

@product_router.get("/products")
def get_products():
    return list(products_collection.find({}, {"_id": 0}))

@product_router.post("/products")
def add_product(product: Product):
    products_collection.insert_one(product.dict())
    return {"message": "Product added successfully"}
