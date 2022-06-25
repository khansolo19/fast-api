from fastapi import BackgroundTasks, UploadFile, File, APIRouter, Form, HTTPException
from services import write_video
from models import Video, User
from schemas import UploadVideo


video_router = APIRouter()
 
@video_router.post('/video')
async def upload_video(
    backgroun_tasks: BackgroundTasks,
    title: str = Form(...), 
    description: str = Form(...),
    file: UploadFile = File(...)
):
    file_name = f'media/{file.filename}'
    if file.content_type == 'video/mp4':
        backgroun_tasks.add_task(write_video, file_name, file)
    else:
        raise HTTPException(status_code=418, detail='It`s not mp4')
    info = UploadVideo(title=title, description=description)
    # user = await User.objects.first() user = user
    return await Video.objects.create(video = file.filename, **info.dict())
    


@video_router.get('/video/{pk}', response_model=Video)
async def get_video(pk: int):
    return await Video.objects.select_related('user').get(pk=pk)


