from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.config import LOGGING_CONFIG
from src.adapter.spi.api.api import api_router
from src.core.util.string_util import StringUtil

API_BASE_URL = '/soat-order-payment/v1'

app = FastAPI(title='SOAT Order v1.0')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]    
)
app.include_router(api_router, prefix=API_BASE_URL)

def startUvicorn():
    import uvicorn

    LOGGING_CONFIG["formatters"]["default"]["fmt"] = '%(asctime)s [%(name)s] %(levelprefix)s %(message)s'
    LOGGING_CONFIG["formatters"]["access"]["fmt"] = '%(asctime)s [%(name)s] %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
    uvicorn.run("main:app",host="0.0.0.0", port=8000, reload=True, log_config=LOGGING_CONFIG)

if __name__ == '__main__':
    startUvicorn()
