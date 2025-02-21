import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

@asynccontextmanager
async def lifespan(app):
    logger.info('Iniciando app')
    yield
    logger.info('Finalizando app')

app = FastAPI(lifespan=lifespan)

@app.get('/check')
def check():
    logger.info('APP OK')
    return{'status': 'ok'}