from fastapi import FastAPI

from .node import app as node_app


app = FastAPI(
    title='Ghost',
    version='v1.0.0',
)

app.mount('/node', node_app)
