from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    count: int
    price: int
    description: Optional[str] = None


class Product_in(BaseModel):
    id: int
    name: str
    count: int
    price: int
    description: Optional[str] = None


# @app.post('/product', response_model=Product)
# async def post_product(product: Product_in):
#     return product


@app.post('/product/', response_model=Product, response_model_include={'description'})
async def post_product(product: Product_in):
    return product
