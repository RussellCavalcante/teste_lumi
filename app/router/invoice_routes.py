from fastapi import APIRouter, File, UploadFile,  Depends, Response, status, Query
from sqlalchemy.orm import Session
from app.schemas.invoice import Invoice, InvoiceOutput
from app.router.deps import get_db_session
from app.use_cases.invoice import InvoiceUseCases
from fastapi_pagination import Page

# dependencies=[Depends(auth)]
router = APIRouter(prefix='/invoice', tags=['Invoice'])


@router.post('/add', status_code=status.HTTP_201_CREATED, description="Add new asset")
def add_invoice(
    invoice: Invoice,
    db_session: Session = Depends(get_db_session)
):
    uc = InvoiceUseCases(db_session=db_session)
    uc.add_invoice(invoice=invoice)
    return Response(status_code=status.HTTP_201_CREATED)


@router.post('/uploadfile', status_code=status.HTTP_201_CREATED, description='Add new Measurements')
def create_upload_file(
    file: UploadFile = File(...),
    db_session: Session = Depends(get_db_session)
):
    uc = InvoiceUseCases(db_session=db_session)
    uc.add_file_invoice(
        file=file
    )

    return Response(status_code=status.HTTP_201_CREATED)


@router.get('/list', response_model=Page[InvoiceOutput], description="List assets")
def list_categories(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(50, ge=1, le=100, description="Size of page"),
    db_session: Session = Depends(get_db_session)
):
    uc = InvoiceUseCases(db_session=db_session)
    response = uc.list_invoices(page=page, size=size)

    return response


# @router.delete('/delete/{id}', description="Delete asset")
# def delete_Asset(
#     id: int,
#     db_sesion: Session = Depends(get_db_session)
# ):
#     uc = AssetUseCases(db_session=db_sesion)
#     uc.delete_Asset(id=id)

#     return Response(status_code=status.HTTP_200_OK)
