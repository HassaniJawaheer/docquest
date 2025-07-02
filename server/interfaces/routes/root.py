from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/")
def root():
    return {
        "status": "ok",
        "message": "Bienvenue, DocQuest",
        "version": "1.0."
    }

@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse("server/static/favicon.ico")