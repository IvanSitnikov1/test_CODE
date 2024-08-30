from sqlalchemy import MetaData, Table, Column, Integer, Text, ForeignKey

from auth.models import user
from database import metadata


note = Table(
    'note',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('content', Text()),
    Column("author_id", Integer, ForeignKey("user.id")),
)
