"""Database management for Penligent AI"""

from sqlalchemy import create_engine, Column, String, DateTime, JSON, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from typing import Optional
import json

Base = declarative_base()


class ScanModel(Base):
    """SQLAlchemy model for scans"""
    __tablename__ = "scans"

    id = Column(String, primary_key=True)
    target = Column(String, nullable=False)
    scan_type = Column(String, nullable=False)
    status = Column(String, nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    findings = Column(JSON, default=list)
    metadata = Column(JSON, default=dict)


class Database:
    """Database connection and management"""

    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def save_scan(self, scan_data: dict) -> bool:
        """Save scan to database"""
        try:
            session = self.SessionLocal()
            scan = ScanModel(**scan_data)
            session.add(scan)
            session.commit()
            session.close()
            return True
        except Exception as e:
            print(f"Error saving scan: {e}")
            return False

    def get_scan(self, scan_id: str) -> Optional[dict]:
        """Retrieve scan from database"""
        try:
            session = self.SessionLocal()
            scan = session.query(ScanModel).filter(ScanModel.id == scan_id).first()
            session.close()
            return scan
        except Exception as e:
            print(f"Error retrieving scan: {e}")
            return None
