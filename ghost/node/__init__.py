from fastapi import FastAPI

from .proofer import router as proofer_router
from .tanker import router as tanker_router

app = FastAPI(
    title='Kinetex Node',
    version='v1.0.0',
    description='Kinetex Node APIs',
)

app.include_router(proofer_router)
app.include_router(tanker_router)
