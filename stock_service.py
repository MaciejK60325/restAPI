
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="Serwis Magazynowy")

# Przykładowe stany magazynowe
stock = {
    1: {"productId": 1, "quantity": 15},
    2: {"productId": 2, "quantity": 30},
    3: {"productId": 3, "quantity": 0},
}

PRODUCT_SERVICE_URL = "http://localhost:8001/products/{}"

@app.get("/stock/{productId}")
def get_stock(productId: int):
    # Sprawdzenie czy produkt istnieje w Serwisie Produktów
    product_response = requests.get(PRODUCT_SERVICE_URL.format(productId))
    if product_response.status_code == 404:
        raise HTTPException(status_code=404, detail="Product not found in catalog")
    elif product_response.status_code != 200:
        raise HTTPException(status_code=502, detail="Error communicating with Product Service")

    # Zwrócenie stanu magazynowego
    product_stock = stock.get(productId)
    if not product_stock:
        return {"productId": productId, "quantity": 0}
    return product_stock

    # Uruchomienie serwera: uvicorn stock_service:app --host localhost --port 8002