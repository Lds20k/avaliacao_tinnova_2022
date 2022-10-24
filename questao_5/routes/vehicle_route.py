from flask import Blueprint, Response, jsonify, request
from domain.vehicle import Vehicle, make_vehicle
from gateway.implementation.vehicle_data import VehicleData
from gateway.interfaces.vehicle_data_interface import VehicleDataInterface

vehicle_data : VehicleDataInterface = VehicleData()

vehicle_route = Blueprint('vehicle_route', __name__, )

OK = 200
CREATED = 201
BAD_REQUEST = 400
NOT_FOUND = 404
UNPROCESSABLE_ENTITY = 422

def make_response(obj, status):
    response = jsonify(obj)
    response.status_code = status
    return response

@vehicle_route.route('/veiculos/<vehicle_id>', methods = ['GET'])
def vehicle_consult(vehicle_id):
    if vehicle_id:
        vehicle = vehicle_data.consult(vehicle_id)
        if vehicle:
            return make_response(
                vehicle,
                OK,
            )
        
        return make_response(
            {"message": "Veiculo não encontrado!"},
            NOT_FOUND,
        )
        
        
@vehicle_route.route('/veiculos', methods = ['GET'])
def vehicle_consult_all():
    brand = request.args.get("marca")
    year = request.args.get("ano")
    color = request.args.get("cor")

    vehicles = None
    try:
        vehicles = vehicle_data.consult_all(brand, year, color)
    except ValueError as err:
        return make_response(
            {
                'message': 'Marca não existe ou está incorreta!',
                'error': str(err)
            },
            BAD_REQUEST
        )
    return make_response(
        vehicles,
        OK
    )


@vehicle_route.route('/veiculos', methods = ['POST'])
def vehicle_register():
    if not request.is_json:
        return make_response(
            {'error': 'Content-Type não suportado!'},
            UNPROCESSABLE_ENTITY
        )
    
    body = request.get_json()

    vehicle = None
    try:
        vehicle = Vehicle(body)
    except KeyError as err:
        return make_response(
            {
                'message': 'Body incorreta!',
                'error': str(err)
            },
            BAD_REQUEST
        )

    try:
        vehicle_data.register(vehicle)
    except ValueError as err:
        return make_response(
            {
                'message': 'Marca não existe ou está incorreta!',
                'error': str(err)
            },
            BAD_REQUEST
        )

    return make_response(
        {'message': 'Registrado com sucesso!'},
        CREATED
    )

@vehicle_route.route('/veiculos/<vehicle_id>', methods = ['PUT', 'PATCH'])
def vehicle_update(vehicle_id):
    if not request.is_json:
        return make_response(
            {'error': 'Content-Type não suportado!'},
            UNPROCESSABLE_ENTITY
        )
    
    body = request.get_json()

    vehicle = None
    if request.method == 'PUT':
        try:
            vehicle = Vehicle(body)
        except KeyError as err:
            return make_response(
                {
                    'message': 'Body incorreta!',
                    'error': str(err)
                },
                BAD_REQUEST
            )
    else:
        try:
            vehicle = make_vehicle(body)
        except KeyError as err:
            return make_response(
                {
                    'message': 'Body incorreta!',
                    'error': str(err)
                },
                BAD_REQUEST
            )
    vehicle.id = vehicle_id

    vehicle_data.update(vehicle)
    return make_response(
        {'message': 'Atualizado com sucesso!'},
        OK
    )

@vehicle_route.route('/veiculos/<vehicle_id>', methods = ['DELETE'])
def vehicle_delete(vehicle_id):   
    vehicle_data.delete(vehicle_id)
    return make_response(
        {'message': 'Veiculo deletado!'},
        OK
    )
    
