Aby uruchomić serwery należy najpierw pobrać potrzebne biblioteki:

pip install fastapi uvicorn requests

Serwis produktow uruchamiamy poprzez python -m uvicorn product_service:app --host localhost --port 8001 w terminalu
a serwis magazynowy python -m uvicorn stock_service:app --host localhost --port 8002

Sprawdzic produkt lub ilosc w magazynie mozemy za pomoc curla
np. curl http://localhost:8002/stock/99 lub curl http://localhost:8002/stock/1
lub w przeglądarce http://localhost:8002/stock/99 