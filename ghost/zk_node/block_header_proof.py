from enum import Enum

from fastapi import APIRouter
from pydantic import BaseModel


class BlockHeaderProofSource(BaseModel):
    chainId: str
    txid: str
    logIndex: str


class BlockHeaderProofDestination(BaseModel):
    chainId: str
    adapters: list[str] | None
    checkpointSource: str | None


class BlockHeaderProofTarget(BaseModel):
    source: BlockHeaderProofSource
    destination: BlockHeaderProofDestination


class BlockHeaderTransferProvider(str, Enum):
    LAYER_ZERO = 'layer-zero',
    AXELAR = 'axelar',
    HYPERLANE = 'hyperlane',
    CELER = 'celer',
    ZETACHAIN = 'zeta',
    WORMHOLE = 'wormhole',
    LOCAL = 'local',


class BlockHeaderTransfer(BaseModel):
    adapterAddress: str
    reporterAddress: str
    provider: BlockHeaderTransferProvider
    storage: str


class CheckpointDetail(BaseModel):
    checkpointIndex: int
    checkpointSize: int


class ProofDetailCore(BaseModel):
    blockNumber: int
    transactionIndex: int


class ProofType(str, Enum):
    BLOCK_HEADER = 'block-header'
    CHECKPOINT = 'checkpoint'


class BlockHeaderProofDetail(BaseModel):
    core: ProofDetailCore
    proofType: ProofType
    transfers: list[BlockHeaderTransfer]
    checkpoint: CheckpointDetail | None


class BlockHeaderProtocolTransferDetail(BaseModel):
    gas: str
    fee: str
    txid: str


class BlockHeaderProtocolTransferStatus(BaseModel):
    blockReportReady: bool
    blockReceiveReady: bool
    provider: BlockHeaderTransferProvider
    detail: BlockHeaderProtocolTransferDetail | None


class BlockHeaderProofStatus(BaseModel):
    ready: bool
    initReady: bool
    transfers: list[BlockHeaderProtocolTransferStatus]
    proofReady: bool


class BlockHeaderProof(BaseModel):
    id: str
    target: BlockHeaderProofTarget
    detail: BlockHeaderProofDetail
    status: BlockHeaderProofStatus
    result: str


class InitiateBlockHeaderProofRequest(BlockHeaderProofTarget):
    pass


class InitiateBlockHeaderProofResponse(BlockHeaderProof):
    pass


class GetBlockHeaderProofResponse(BlockHeaderProof):
    pass


router = APIRouter()


@router.post(
    '/api/hashi/proof',
    tags=['Block Header Proof'],
    summary='Initiate block header proof',
    description='Initiates generation of new block header proof (v1). Optionally via checkpoint (v2)',
    operation_id='initiate_block_header_proof',
)
async def initiate_block_header_proof(request: InitiateBlockHeaderProofRequest) -> InitiateBlockHeaderProofResponse:
    pass


@router.get(
    '/api/hashi/proof/{id}',
    tags=['Block Header Proof'],
    summary='Get block header proof',
    description='Returns initiated block header proof (v1/v2) by its ID',
    operation_id='get_block_header_proof',
)
async def get_block_header_proof(id: str) -> GetBlockHeaderProofResponse:
    pass
