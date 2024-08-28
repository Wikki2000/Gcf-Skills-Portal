#!/usr/bin/env python3
"""Models class for storing learner and it's skills."""
from sqlalchemy import Column, String, JSON, DateTime
from models.base_model import Base, BaseModel
from datetime import datetime


class Learner(BaseModel, Base):
    """Class definition of learners and skills."""

    __tablename__ = "learners"

    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(100), nullable=False)
    create_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    skills = Column(JSON, nullable=False)
    other_skills = Column(String(100))
