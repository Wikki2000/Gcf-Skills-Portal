#!/usr/bin/env python3
"""Models class for storing trainer and his voluntary skills."""
from sqlalchemy import Column, String, DateTime
from models.base_model import Base, BaseModel
from datetime import datetime


class Trainer(BaseModel, Base):
    """Class definition of Trainer and  voluntary skills."""

    __tablename__ = "trainers"

    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(100), nullable=False)
    create_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    skills = Column(String(600), nullable=False)
