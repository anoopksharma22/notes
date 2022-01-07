from fastapi import APIRouter


router = APIRouter(
    prefix="/notes",
    tags=['notes']
)

@router.get("/")
def return_all_notes():
    return {
        "all":"notes"
    }