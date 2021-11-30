"""sql alchemy orm."""
from sqlalchemy import Column, Integer, String
from .database import Base


class QuestionnaireData(Base):
    __tablename__ = "questionnaire"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    age = Column(Integer)
    gender = Column(String)
    genre = Column(String)
    watch_frequency = Column(Integer)
    introduced_by = Column(String)
    favorite = Column(String)
    sub_dub = Column(String)
    interest_in = Column(String)
