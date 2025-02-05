from fastapi import APIRouter

router = APIRouter(
    prefix="/devices",
    tags=["devices"]
)

@router.get("/")
async def get_devices():
    return {"devices": []}

@router.get("/{device_id}")
async def get_device(device_id: str):
    return {"device_id": device_id, "status": "online"}