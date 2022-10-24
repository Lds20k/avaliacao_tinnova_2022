import datetime

class Vehicle:
    id: int
    name: str
    brand: str
    color: str
    year: int
    description: str
    sold: bool
    created: datetime
    updated: datetime

    def __init__(self, vehicle=None) -> None:
        if not vehicle:
            return
        
        self.name = vehicle["nome"]
        self.brand = vehicle["marca"].lower()
        self.color = vehicle["cor"]
        self.year = vehicle["ano"]
        self.description = vehicle["descricao"]
        self.sold = vehicle["vendido"]
    
    def empty(self):
        return not self.name and not self.brand and not self.color and not self.year and not self.description and not self.sold

def make_vehicle(vehicle):
    vehicle["default"] = None

    obj = Vehicle()
    obj.name: str = vehicle.get("nome")
    obj.brand: str = vehicle.get("marca")
    if obj.brand:
        obj.brand = obj.brand.lower()
    obj.color: str = vehicle.get("cor")
    obj.year: int = vehicle.get("ano")
    obj.description: str = vehicle.get("descricao")
    obj.sold: bool = vehicle.get("vendido")

    if obj.empty():
        raise KeyError("Empty data!")
    return obj