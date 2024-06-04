from fastapi import FastAPI
from app.router.invoice_routes import router as invoice_routes

app = FastAPI()
@app.get('/health-check')
def health_check():
    return True

app.include_router(invoice_routes)