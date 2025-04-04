import enum
from datetime import datetime

from sqlalchemy import (
    TIMESTAMP,
    UUID,
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    Integer,
    String,
    text,
    UniqueConstraint
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from .database import Base
from uuid import uuid4

class Gender(enum.Enum):
    male = "male"
    female = "female"

class Action(enum.Enum):
    like = "like"
    dislike = "dislike"

class User(Base):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    city = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    preferably_gender = Column(Enum(Gender), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False) 
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Photos(Base):
    __tablename__ = 'photos'
    photo_id = Column(String, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    photo_url = Column(String, nullable=False)

    user = relationship("User")

class UserChoices(Base):
    __tablename__ = 'user_choices'
    choice_id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    selected_user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    user = relationship("User", foreign_keys=[user_id])
    selected_user = relationship("User", foreign_keys=[selected_user_id])

class History(Base):
    __tablename__ = "history"
    history_id = Column(
        UUID(as_uuid=True), 
        primary_key=True,
        default=uuid4, 
        server_default=text("gen_random_uuid()")  
    )
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    action = Column(Enum(Action), nullable=False)
    selected_user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)

    user = relationship("User", foreign_keys=[user_id])
    selected_user = relationship("User", foreign_keys=[selected_user_id])

    __table_args__ = (
        Index('idx_history_user_pair', 'user_id', 'selected_user_id'),
        Index('idx_history_created_at', 'created_at'),
    )
    
class UserWithPhotos:
    def __init__(self, user:User, photos:Photos):
        self.user_id = user.user_id
        self.username = user.username
        self.age = user.age
        self.gender = user.gender
        self.city = user.city
        self.description = user.description
        self.created_at = user.created_at
        self.preferably_gender = user.preferably_gender
        self.photos = [photos[i].photo_url for i in range(len(photos))] or None


class View(Base):
    __tablename__ = "views"
    viewer_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    viewed_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
# class Match(Base):
#     __tablename__ = 'matches'
    
#     match_id = Column(
#         UUID(as_uuid=True),
#         primary_key=True,
#         default=uuid4,
#         server_default=text("gen_random_uuid()")
#     )
#     user1_id = Column(BigInteger, nullable=False)
#     user2_id = Column(BigInteger, nullable=False)
#     created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
#     __table_args__ = (
#         UniqueConstraint(
#             'user1_id', 
#             'user2_id', 
#             name='unique_user_pair',
            
#             sqlite_where=(user1_id < user2_id)
#         ),
#     )

#     @classmethod
#     def create_sorted_pair(cls, user_a, user_b):
#
#         return cls(
#             user1_id=min(user_a, user_b),
#             user2_id=max(user_a, user_b)
#         )