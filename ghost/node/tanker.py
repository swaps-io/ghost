from enum import Enum

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix='/api/tanker')


class DepositChain(BaseModel):
    chain: str
    liquidation: str


class DepositChainsResponse(BaseModel):
    chains: list[DepositChain]


@router.get(
    '/deposit/chains',
    tags=['Tanker'],
    summary='Get depositable chains',
    description='Returns list of depositable chains & conditions',
    operation_id='get_deposit_chains',
    response_model=DepositChainsResponse,
)
async def get_deposit_chains() -> DepositChainsResponse:
    pass


class DepositToken(BaseModel):
    chain: str
    token: str
    factor: str


class DepositTokensResponse(BaseModel):
    tokens: list[DepositToken]


@router.get(
    '/deposit/tokens',
    tags=['Tanker'],
    summary='Get depositable tokens',
    description='Returns list of depositable assets & conditions',
    operation_id='get_deposit_tokens',
    response_model=DepositTokensResponse,
)
async def get_deposit_tokens() -> DepositTokensResponse:
    pass


class BorrowChain(BaseModel):
    chain: str
    liquidation: str


class BorrowChainsResponse(BaseModel):
    chains: list[BorrowChain]


@router.get(
    '/borrow/chains',
    tags=['Tanker'],
    summary='Get borrowable chains',
    description='Returns list of borrowable chains & conditions',
    operation_id='get_borrow_chains',
    response_model=BorrowChainsResponse,
)
async def get_borrow_chains() -> BorrowChainsResponse:
    pass


class BorrowEstimateRequest(BaseModel):
    chain: str
    amount: str


class BorrowEstimateDeposit(BaseModel):
    chain: str
    cost: str


class BorrowEstimateResponse(BaseModel):
    repayAmount: str
    deposits: list[BorrowEstimateDeposit]


@router.post(
    '/borrow/estimate',
    tags=['Tanker'],
    summary='Estimate borrow',
    description='Returns estimate of borrow with specified params',
    operation_id='estimate_borrow',
    response_model=BorrowEstimateResponse,
)
async def estimate_borrow(request: BorrowEstimateRequest) -> BorrowEstimateResponse:
    pass


class DepositAsset(BaseModel):
    token: str
    amount: str


class BorrowDeposit(BaseModel):
    chain: str
    assets: list[DepositAsset]


class BorrowReceiver(BaseModel):
    address: str
    amount: str


class BorrowCreateRequest(BaseModel):
    chain: str
    borrower: str
    depositor: str
    deposit: BorrowDeposit
    receivers: list[BorrowReceiver]


class BorrowCreateResponse(BaseModel):
    hash: str
    signer: str
    chain: str
    payload: str


@router.post(
    '/borrow',
    tags=['Tanker'],
    summary='Create borrow',
    description='Creates borrow operation to sign from params',
    operation_id='create_borrow',
    response_model=BorrowCreateResponse,
)
async def create_borrow(request: BorrowCreateRequest) -> BorrowCreateResponse:
    pass


class BorrowState(str, Enum):
    CREATED = 'created'
    SUBMITTED = 'submitted'
    CANCELLED = 'cancelled'
    LENT = 'lent'


class BorrowStateUpdate(BaseModel):
    state: BorrowState
    detail: str
    time: str


class BorrowStateUpdates(BaseModel):
    last: BorrowStateUpdate
    all: list[BorrowStateUpdate]


class BorrowStatusResponse(BaseModel):
    hash: str
    updates: BorrowStateUpdates


@router.get(
    '/borrow/{hash}/status',
    tags=['Tanker'],
    summary='Get borrow status',
    description='Gets status that describes state of the borrow',
    operation_id='get_borrow_status',
    response_model=BorrowStatusResponse,
)
async def get_borrow_status(hash: str) -> BorrowStatusResponse:
    pass


class BorrowDepositProof(BaseModel):
    birth: str
    data: str
    result: str
    signature: str


class BorrowSubmitRequest(BaseModel):
    hash: str
    signature: str
    proof: BorrowDepositProof


class BorrowSubmitResponse(BaseModel):
    hash: str


@router.post(
    '/borrow/submit',
    tags=['Tanker'],
    summary='Submit borrow',
    description='Receives signature for pre-created borrow operation',
    operation_id='submit_borrow',
    response_model=BorrowSubmitResponse,
)
async def submit_borrow(request: BorrowSubmitRequest) -> BorrowSubmitResponse:
    pass
