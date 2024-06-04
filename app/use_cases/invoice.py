from sqlalchemy.orm import Session
from app.db.models import Invoice as InvoiceModel
from app.schemas.invoice import Invoice, InvoiceOutput
from fastapi.exceptions import HTTPException
from fastapi import status
from fastapi_pagination import Params
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi import File
import pandas as pd
from io import BytesIO
import PyPDF2
import re



class InvoiceUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def add_invoice(self, invoice: Invoice):
        invoice_model = InvoiceModel(**invoice.dict())
        self.db_session.add(invoice_model)
        self.db_session.commit()

    def list_invoices(self, page: int = 1, size: int = 50):
        Invoices_on_db = self.db_session.query(InvoiceModel)
        params = Params(page=page, size=size)
        return paginate(Invoices_on_db, params=params)
    
    



    def add_file_invoice(self, file:File):
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Arquivo deve ser um CSV")
        # try:

        print("file >>>>", type(file))
        # input()
        

        with BytesIO(file.file.read()) as bytes_io:
            pdf_reader = PyPDF2.PdfReader(bytes_io)

            faturaTexto = ""
            # Obter o número de páginas do PDF
            # num_pages = pdf_reader.pages
            
            # Iterar sobre cada página e extrair texto
            for page in pdf_reader.pages:
                text = page.extract_text()
                faturaTexto += text

            
            # Extraindo os dados
            dados = extrair_dados(faturaTexto)

            # Criando o DataFrame
            df = pd.DataFrame([dados])

            # Exibindo o DataFrame
            print(df.columns)

            # f =  open(file.file, "rb") 

            file_content = file.file.read()
            # file_data = f.read()

            print(file_content)
            input()
            
            for _, row in df.iterrows():
                invoice = Invoice(
                    num_client=row["Nº DO CLIENTE"],
                    reference_month=row["Mês de Referência"],
                    electricity_kWh=row["Energia Elétrica - Quantidade (kWh)"],
                    electricity_RS=row["Energia Elétrica - Valor (R$)"],
                    sceee_energy_without_ICMS_kWh=row["Energia SCEE s/ICMS - Quantidade (kWh)"],
                    sceee_energy_without_ICMS_RS=row["Energia SCEE s/ICMS - Valor (R$)"],
                    compensated_energy_GD_I_kWh=row["Energia Compensada GD I - Quantidade (kWh)"],
                    compensated_energy_GD_I_RS=row["Energia Compensada GD I - Valor (R$)"],
                    contrib_municipal_public_light=row["Contrib Ilum Publica Municipal - Valor (R$)"],
                    file=file_content
                    # Adicione as outras colunas aqui conforme necessário
                )
                print()
            self.db_session.add(invoice)
        
            self.db_session.commit() 

            # Função para extrair dados usando regex
    
        # df = pd.read_csv(file.file, delimiter=',', header=None)
        # json_list = []
        # for index, row in df.iterrows():
        #     if row[0] == 'Invoice_id':
        #         continue
        #     data_dict = {
        #         'id': row[0],
        #         'name': row[1],
        #     }
        #     json_data = json.dumps(data_dict)
        #     json_list.append(json_data)
        
        # for json_data in json_list:
        #     json_object = json.loads(json_data)

        #     Invoice_model = InvoiceModel(**json_object)
        #     self.db_session.add(Invoice_model)
        #     self.db_session.commit()
        
        # except pd.errors.EmptyDataError:
        #     raise HTTPException(status_code=400, detail="Arquivo CSV vazio ou nao possui Invoice")


    # def delete_Invoice(self, id: int):
    #     Invoice_model = self.db_session.query(InvoiceModel).filter_by(id=id).first()
    #     if not Invoice_model:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invoice not found')
        
    #     self.db_session.delete(Invoice_model)
    #     self.db_session.commit()

    def serialize_invoice(self, invoice_model: InvoiceModel):
        return InvoiceOutput(**invoice_model.__dict__)

def extrair_dados(texto):
    # Padrões regex para os dados
    padrao_cliente = re.compile(r'Nº DA INSTALAÇÃO\s+(\d{10})')
    padrao_referencia = re.compile(r'Valor a pagar \(R\$\)\s+(\w{3}/\d{4})')
    padrao_energia_eletrica = re.compile(r'Energia Elétrica kWh\s+(\d+)\s+[\d,\.]+\s+([\d,\.]+)')
    padrao_energia_scee = re.compile(r'Energia SCEE ISENTA kWh\s+(\d+)\s+[\d,\.]+\s+([\d,\.]+)')
    padrao_energia_compensada = re.compile(r'Energia compensada GD I kWh\s+(\d+)\s+[\d,\.]+\s+([-,\d\.]+)')
    padrao_ilum_publica = re.compile(r'Contrib Ilum Publica Municipal\s+([\d,\.]+)')
    
    # Extraindo dados
    cliente = padrao_cliente.search(texto)
    referencia = padrao_referencia.search(texto)
    energia_eletrica = padrao_energia_eletrica.search(texto)
    energia_scee = padrao_energia_scee.search(texto)
    energia_compensada = padrao_energia_compensada.search(texto)
    ilum_publica = padrao_ilum_publica.search(texto)
    
    # Verificando se os padrões foram encontrados e extraindo os dados
    dados = {}
    if cliente:
        dados['Nº DO CLIENTE'] = cliente.group(1)
    if referencia:
        dados['Mês de Referência'] = referencia.group(1)
    if energia_eletrica:
        dados['Energia Elétrica - Quantidade (kWh)'] = energia_eletrica.group(1)
        dados['Energia Elétrica - Valor (R$)'] = energia_eletrica.group(2)
    if energia_scee:
        dados['Energia SCEE s/ICMS - Quantidade (kWh)'] = energia_scee.group(1)
        dados['Energia SCEE s/ICMS - Valor (R$)'] = energia_scee.group(2)
    if energia_compensada:
        dados['Energia Compensada GD I - Quantidade (kWh)'] = energia_compensada.group(1)
        dados['Energia Compensada GD I - Valor (R$)'] = energia_compensada.group(2)
    if ilum_publica:
        dados['Contrib Ilum Publica Municipal - Valor (R$)'] = ilum_publica.group(1)
    
    return dados