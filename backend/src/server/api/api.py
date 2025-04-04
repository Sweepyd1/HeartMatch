from fastapi import APIRouter

router = APIRouter("/api/users", ["базовый апи"])

@router.get("/get_profile_info"/{id})
async def get_profile_info(user_id:int):
    print(1)



@router.get("/get_my_photos")
async def get_my_photos():
    ...


@router.get("/get_my_statistic")
async def get_my_statistic():
    ...


@router.get("/get_my_history")
async def get_my_history():
    ...


@router.put("/change_profile_info")
async def change_profile_info():
    ...
