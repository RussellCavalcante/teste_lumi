import pytest
from passlib.context import CryptContext
from app.db.connection import Session
from app.db.models import Invoice as InvoiceModel


crypt_context = CryptContext(schemes=['sha256_crypt'])

@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()

@pytest.fixture()
def invoice_on_db(db_session):
    Invoices = [
        InvoiceModel(num_client = "12349223",
        reference_month = "32131",
        electricity_kWh = "3123131",
        electricity_RS = "3123131",
        sceee_energy_without_ICMS_kWh = "313213",
        sceee_energy_without_ICMS_RS  = "313213",
        compensated_energy_GD_I_kWh = "213132",
        compensated_energy_GD_I_RS  = "213132",
        contrib_municipal_public_light = "1234",
        file = b"\x50\x4B\x03\x04\x14\x00\x06\x00"  ),
        InvoiceModel(num_client = "12349224",
        reference_month = "32131",
        electricity_kWh = "3123131",
        electricity_RS = "3123131",
        sceee_energy_without_ICMS_kWh = "313213",
        sceee_energy_without_ICMS_RS  = "313213",
        compensated_energy_GD_I_kWh = "213132",
        compensated_energy_GD_I_RS  = "213132",
        contrib_municipal_public_light = "1234",
        file = b"\x50\x4B\x03\x04\x14\x00\x06\x00"  ),
        InvoiceModel(num_client = "12349225",
        reference_month = "32131",
        electricity_kWh = "3123131",
        electricity_RS = "3123131",
        sceee_energy_without_ICMS_kWh = "313213",
        sceee_energy_without_ICMS_RS  = "313213",
        compensated_energy_GD_I_kWh = "213132",
        compensated_energy_GD_I_RS  = "213132",
        contrib_municipal_public_light = "1234",
        file = b"\x50\x4B\x03\x04\x14\x00\x06\x00"),
        InvoiceModel(num_client = "12349226",
        reference_month = "32131",
        electricity_kWh = "3123131",
        electricity_RS = "3123131",
        sceee_energy_without_ICMS_kWh = "313213",
        sceee_energy_without_ICMS_RS  = "313213",
        compensated_energy_GD_I_kWh = "213132",
        compensated_energy_GD_I_RS  = "213132",
        contrib_municipal_public_light = "1234",
        file = b"\x50\x4B\x03\x04\x14\x00\x06\x00"),    
    ]

    for Invoice in Invoices:
        db_session.add(Invoice)
    db_session.commit()

    for Invoice in Invoices:
        db_session.refresh(Invoice)
    
    yield Invoices

    for Invoice in Invoices:
        db_session.delete(Invoice)
    db_session.commit()

