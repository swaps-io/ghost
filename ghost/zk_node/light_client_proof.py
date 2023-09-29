from fastapi import APIRouter
from pydantic import BaseModel


class LightClientProofSource(BaseModel):
    chainId: str
    txid: str
    logIndex: str


class LightClientProofDestination(BaseModel):
    chainId: str
    lightClient: str


class LightClientProofTarget(BaseModel):
    source: LightClientProofSource
    destination: LightClientProofDestination


class LightClientProofDetailCore(BaseModel):
    blockNumber: int
    transactionIndex: int


class LightClientProofDetailExtra(BaseModel):
    syncCommitteePeriod: int
    rotateStepFinalizedSlot: int
    rotateStepAttestedSlot: int
    rotateStepAttestingSlot: int
    rotateFinalizedSlot: int
    stepTransactionSlot: int
    stepFinalizedSlot: int
    stepAttestedSlot: int
    stepAttestingSlot: int


class LightClientProofDetail(BaseModel):
    core: LightClientProofDetailCore
    extra: LightClientProofDetailExtra | None


class LightClientProofStatus(BaseModel):
    ready: bool
    initReady: bool
    rotateStepReady: bool
    rotateReady: bool
    stepReady: bool
    proofReady: bool


class LightClientProof(BaseModel):
    id: str
    target: LightClientProofTarget
    detail: LightClientProofDetail
    status: LightClientProofStatus
    result: str


class InitiateLightClientProofRequest(LightClientProofTarget):
    pass


class InitiateLightClientProofResponse(LightClientProof):
    pass


class GetLightClientProofResponse(LightClientProof):
    pass


router = APIRouter()


@router.post(
    '/api/proof',
    tags=['Light Client Proof'],
    summary='Initiate light client proof',
    description='Initiates generation of new light client proof (v0)',
    operation_id='initiate_light_client_proof',
)
async def initiate_light_client_proof(request: InitiateLightClientProofRequest) -> InitiateLightClientProofResponse:
    pass


@router.get(
    '/api/proof/{id}',
    tags=['Light Client Proof'],
    summary='Get light client proof',
    description='Returns initiated light client proof (v0) by its ID',
    operation_id='get_light_client_proof',
)
async def get_light_client_proof(id: str) -> GetLightClientProofResponse:
    pass
