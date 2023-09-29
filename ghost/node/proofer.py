from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix='/api/proofer')


class ProofCore(BaseModel):
    chain: str
    target: str
    data: str


class Proof(ProofCore):
    birth: str
    result: str


class ProofVerifyRequest(BaseModel):
    proofs: list[Proof]


class ProofVerdict(BaseModel):
    proof: Proof
    ok: bool
    error: str
    signature: str


class ProofVerifyResponse(BaseModel):
    verdicts: list[ProofVerdict]


@router.post(
    '/verify',
    tags=['Proofer'],
    summary='Verify proofs',
    description='Returns verification verdicts of requested data view proofs',
    operation_id='verify_proofs',
    response_model=ProofVerifyResponse,
)
async def verify_proofs(request: ProofVerifyRequest) -> ProofVerifyResponse:
    pass


class Provable(ProofCore):
    pass


class ProofCreateRequest(BaseModel):
    proofs: list[Provable]


class ProofCreateResponse(ProofVerifyResponse):
    pass


@router.post(
    '/create',
    tags=['Proofer'],
    summary='Create proofs',
    description='Creates proof for requested data and returns verification verdict for it',
    operation_id='create_proofs',
    response_model=ProofCreateResponse,
)
async def create_proofs(request: ProofCreateRequest) -> ProofCreateResponse:
    pass
