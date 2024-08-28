#!/usr/bin/env python3
"""Models class for storing Admin users."""
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel


class Admin(BaseModel, Base):
    """Class definition of admin users."""

    __tablename__ = "admins"

    username = Column(String(100), nullable=False, unique=True)
    passkey = Column(String(100), nullable=False)
