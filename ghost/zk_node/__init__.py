from fastapi import FastAPI

from .light_client_proof import router as light_client_proof_router
from .block_header_proof import router as block_header_proof_router

app = FastAPI(
    title='Kinetex ZK Node',
    version='v0.1.0',
    description='Kinetex ZK Node APIs',
)

app.include_router(light_client_proof_router)
app.include_router(block_header_proof_router)
