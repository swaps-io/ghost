from fastapi import FastAPI

from .node import app as node_app
from .zk_node import app as zk_node_app


app = FastAPI(
    title='Ghost',
    version='v1.0.0',
)

app.mount('/node', node_app)
app.mount('/zk_node', zk_node_app)
