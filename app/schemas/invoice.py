from app.schemas.base import CustomBaseModel


class Invoice(CustomBaseModel):
    num_client : str
    reference_month : str
    electricity_kWh : str
    electricity_RS  : str
    sceee_energy_without_ICMS_kWh: str
    sceee_energy_without_ICMS_RS : str
    compensated_energy_GD_I_kWh : str
    compensated_energy_GD_I_RS  : str
    contrib_municipal_public_light : str
    file: bytes

class InvoiceOutput(Invoice):
    id : int
    electric_power_consumption : str
    
  