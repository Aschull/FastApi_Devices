from common.utils import converte_data
from domain.device_domain import Device
from models.models import Dispositivos
from fastapi import APIRouter

router = APIRouter()


@router.get("/device/")
def list_all():
    dispositivos = Dispositivos.query.all()
    response = [
        {'id': i.id, 'nome': i.nome, 'latitude': i.latitude, 'longitude': i.longitude,
         'data_hora': converte_data(i.data_hora)} for i in dispositivos]
    return response


@router.get("/device/{id}")
def list_by_id(id: int):
    dispositivos = Dispositivos.query.filter_by(id=id).first()
    try:
        response = {
            'id': dispositivos.id,
            'nome': dispositivos.nome,
            'idade': dispositivos.latitude,
            'longitude': dispositivos.longitude,
            'data_hora': converte_data(dispositivos.data_hora)
        }
    except AttributeError:
        response = {
            'status': 'error',
            'mensagem': 'Dispositivo não encontrado!'
        }
    return response


@router.post("/insertDevice")
def insert_device(device: Device):
    dispositivos = Dispositivos(nome=device.nome, latitude=device.latitude, longitude=device.longitude)
    dispositivos.save()
    response = {
        'id': dispositivos.id,
        'nome': dispositivos.nome,
        'latitude': dispositivos.latitude,
        'longitude': dispositivos.longitude,
        'data_hora': dispositivos.data_hora
    }
    return response


@router.delete("/device/{id}")
def delete_by_id(id):
    dispositivos = Dispositivos.query.filter_by(id=id).first()
    try:
        dispositivos.delete()
        response = {
            'status': 'sucess',
            'mensagem': 'Dispositivo {} excluído com sucesso!'.format(dispositivos.id)
        }
    except AttributeError:
        response = {
            'status': 'error',
            'mensagem': 'Dispositivo não encontrado!'
        }
    return response
