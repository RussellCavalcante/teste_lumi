import pytest
from app.schemas.invoice import Invoice


def test_invoice_schema():
    invoice = Invoice(
        num_client = "1234",
            reference_month = "32131",
            electricity_kWh = "3123131",
            electricity_RS = "3123131",
            sceee_energy_without_ICMS_kWh = "313213",
            sceee_energy_without_ICMS_RS  = "313213",
            compensated_energy_GD_I_kWh = "213132",
            compensated_energy_GD_I_RS  = "213132",
            contrib_municipal_public_light = "1234",
    )

    assert invoice.dict() == {
        "num_client" : "1234",
        "reference_month" : "123412",
        "electricity_kWh" : "131233",
        "electricity_RS " : "131233",
        "sceee_energy_without_ICMS_kWh" : "321313",
        "sceee_energy_without_ICMS_RS " : "321313",
        "compensated_energy_GD_I_kWh" : "3123313",
        "compensated_energy_GD_I_RS " : "3123313",
        "contrib_municipal_public_light" : "312331",
    }


def test_asset_schema_invalid():
    with pytest.raises(ValueError):
         invoice = Invoice(
            num_client = 1234,
            reference_month = 32131,
            electricity_kWh = 3123131,
            electricity_RS = 3123131,
            sceee_energy_without_ICMS_kWh = 313213,
            sceee_energy_without_ICMS_RS  = 313213,
            compensated_energy_GD_I_kWh = 213132,
            compensated_energy_GD_I_RS  = 213132,
            contrib_municipal_public_light = 1234
        )

    # with pytest.raises(ValueError):
    #     invoice = Invoice(
    #         num_client = 1234
    #         reference_month = ""
    #         electricity = ""
    #         sceee_energy_without_ICMS = ""
    #         compensated_energy_GD_I = ""
    #         contrib_municipal_public_light = 1234
    #     )
    
