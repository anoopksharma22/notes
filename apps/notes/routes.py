from fastapi import APIRouter


router = APIRouter(
    prefix="/notes",
    tags=['notes']
)

@router.get("/")
def return_all_notes():
    print("In note")
    return {
        "all":"notes"
    }