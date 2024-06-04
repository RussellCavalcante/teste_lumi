from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, func, LargeBinary
# from sqlalchemy.orm import relationship
from app.db.base import Base


class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    num_client = Column('num_client', String, nullable=True, unique=True)
    reference_month = Column('reference_month', String, nullable=True)
    electricity_kWh = Column('electricity_kWh', String, nullable=True)
    electricity_RS = Column('electricity_RS', String, nullable=True)
    sceee_energy_without_ICMS_kWh = Column('sceee_energy_without_ICMS_kWh', String, nullable=True)
    sceee_energy_without_ICMS_RS = Column('sceee_energy_without_ICMS_RS', String, nullable=True)
    compensated_energy_GD_I_kWh = Column('compensated_energy_GD_I_kWh', String, nullable=True)
    compensated_energy_GD_I_RS = Column('compensated_energy_GD_I_RS', String, nullable=True)
    contrib_municipal_public_light = Column('contrib_municipal_public_light', String, nullable=True)
    file = Column("file", LargeBinary, nullable=True)
