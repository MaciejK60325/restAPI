from fastapi import FastAPI, HTTPException

app = FastAPI(title="Serwis Produktów")

# Przykładowe dane produktów (w pamięci)
products = {
    1: {"id": 1, "name": "Laptop", "price": 4500.00},
    2: {"id": 2, "name": "Smartfon", "price": 2500.00},
    3: {"id": 3, "name": "Monitor", "price": 899.99},
}

@app.get("/products/{id}")
def get_product(id: int):
    product = products.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Uruchomienie serwera: uvicorn product_service:app --host localhost --port 8001
