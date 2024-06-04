from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Invoice as InvoiceModel
from app.main import app
import json
import base64

client = TestClient(app)
# headers = {"Authorization": "Bearer token"}
# client.headers = headers

def test_add_invoice_route(db_session):
    body = {
        "num_client" : "1234",
        "reference_month" : "123412",
        "electricity_kWh" : "131233",
        "electricity_RS " : "131233",
        "sceee_energy_without_ICMS_kWh" : "321313",
        "sceee_energy_without_ICMS_RS " : "321313",
        "compensated_energy_GD_I_kWh" : "3123313",
        "compensated_energy_GD_I_RS " : "3123313",
        "contrib_municipal_public_light" : "312331",
        "file": base64.b64encode(b"\x50\x4B\x03\x04\x14\x00\x06\x00").decode("utf-8")
    }
    
    response = client.post('/invoice/add', json=body)

    print(response)
    input()

    assert response.status_code == status.HTTP_201_CREATED
    
    asset_on_db = db_session.query(InvoiceModel).all()
    assert len(asset_on_db) == 1
    db_session.delete(asset_on_db[0])
    db_session.commit()


def test_list_invoice_route(invoice_on_db):
    response = client.get('/invoice/list')

    print(response)

    input()
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert len(data["items"]) == 4
    # assert data["items"][0] == {
    #     "name": asset_on_db[0].name,
    #     "id": asset_on_db[0].id
    # }
    