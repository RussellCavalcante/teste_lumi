import pytest
from decouple import config
from datetime import datetime, timedelta
from passlib.context import CryptContext
# from jose import jwt
from fastapi.exceptions import HTTPException
from app.schemas.invoice import Invoice, InvoiceOutput
from app.db.models import Invoice as InvoiceModel
from app.use_cases.invoice import InvoiceUseCases


crypt_context = CryptContext(schemes=['sha256_crypt'])

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')


def test_add_invoice_uc(db_session):
    invoice = Invoice(
        num_client = "12349222",
        reference_month = "32131",
        electricity_kWh = "3123131",
        electricity_RS = "3123131",
        sceee_energy_without_ICMS_kWh = "313213",
        sceee_energy_without_ICMS_RS  = "313213",
        compensated_energy_GD_I_kWh = "213132",
        compensated_energy_GD_I_RS  = "213132",
        contrib_municipal_public_light = "1234",
        file = b"\x50\x4B\x03\x04\x14\x00\x06\x00"  
    )

    uc = InvoiceUseCases(db_session)
    uc.add_invoice(invoice=invoice)

    invoice_on_db = db_session.query(InvoiceModel).all()

    assert invoice_on_db[0].electricity_kWh is not None
    assert invoice_on_db[0].electricity_RS == "3123131"


    for invoice in invoice_on_db:
        db_session.delete(invoice)

    db_session.commit()
    # db_session.delete(invoice_on_db)
    # db_session.commit()

# def test_list_invoices(db_session, invoice_on_db):
#     uc = InvoiceUseCases(db_session=db_session)

#     invoices = uc.list_invoices()

#     assert len(invoices) == 4
#     assert  type(invoices[0]) == InvoiceOutput
#     assert invoices[0].id == invoice_on_db[0].id