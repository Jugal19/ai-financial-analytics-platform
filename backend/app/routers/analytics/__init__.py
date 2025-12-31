from fastapi import APIRouter

router = APIRouter(prefix="/analtics", tags=["analytics"])

from .summary import *
from .categories import *
from .trends import *