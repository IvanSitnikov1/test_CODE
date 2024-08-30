import requests

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from auth.base_config import current_user
from auth.models import User
from database import get_async_session
from notes.models import note


router = APIRouter(
    prefix='/notes',
    tags=['notes']
)


async def validation_text(text):
    """Функция для валидации текста сервисом Яндекс.Спеллер"""

    url_speller = 'https://speller.yandex.net/services/spellservice.json/checkText'
    response = requests.post(url_speller, data={"text": text})

    for el in response.json():
        text = text.replace(el['word'], el['s'][0])
    return text


@router.post('/')
async def create_note(
        content: str,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    """Эндпоинт для добавления заметки"""

    validated_content = await validation_text(content)
    stmt = insert(note).values(content=validated_content, author_id=user.id)
    await session.execute(stmt)
    await session.commit()

    if validated_content == content:
        return JSONResponse({'success': 'Заметка успешно добавлена'})
    else:
        return JSONResponse({
            'success': 'Заметка успешно добавлена',
            'message': 'Заметка содержала ошибки. Ошибки исправлены, заметка добавлена',
        })


@router.get('/')
async def get_notes(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    """Получение списка заметок пользователя"""

    query = select(note).where(note.c.author_id == user.id)
    result = await session.execute(query)
    result = result.mappings().all()
    return result
