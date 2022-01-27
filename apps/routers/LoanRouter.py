import json
from unittest import result
from fastapi import APIRouter, Body, Response
from apps.controllers.LoanController import ControllerLoan as loan

router = APIRouter()

example_input_cif = json.dumps({
    "cif": "1",
}, indent=2)

example_input_ktp = json.dumps({
    "ktp": "3173",
}, indent=2)

example_update_data = json.dumps({
    "phone": "0899800",
    "email": "gmail.com",
    "marital_status": "Single",
    "loan_status": 1
}, indent=2)
example_post_data = json.dumps({
    "loanid": 3000,
    "idno": 1,
    "loan_status": 1,
    "loan_amount": 3000000,
    "loan_tenure": 24,
    "interest": 15,
    "cif": "4000"
}, indent=2)


@router.post("/get_loan_by_cif")
async def get_loan_by_cif(response: Response, input_data=Body(..., example=example_input_cif)):
    result = loan.get_loan_by_cif(input_data=input_data)
    response.status_code = result.status
    return result

@router.post("/get_loan_by_cif_debug")
async def get_loan_by_cif_debug(response: Response, input_data=Body(..., example=example_input_cif)):
    result = loan.get_loan_by_cif_debug(input_data=input_data)
    response.status_code = result.status
    return result

@router.delete("/loan/{ktp}")
async def delete_acc_by_ktp(response: Response, id: int):
    result = loan.delete_acc_by_ktp(id)
    response.status_code = result.status
    return result

@router.get("/loann/{ktp}")
async def show_data(response: Response, id: int):
    result = loan.show_data(id)
    response.status_code = result.status
    return result

@router.put("/edit_data/{ktp}")
async def edit_data(response: Response, id: int, input_data=Body(..., example=example_update_data)):
    result = loan.edit_data(id, input_data=input_data)
    response.status_code = result.status
    return result

@router.post("/loan/")
async def store_data(response: Response, input_data=Body(..., example=example_post_data)):
    result = loan.store_data(input_data=input_data)
    response.status_code = result.status
    return result


