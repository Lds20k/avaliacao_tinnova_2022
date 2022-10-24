import sqlite3

import globals
from domain.vehicle import Vehicle
from gateway.interfaces.vehicle_data_interface import VehicleDataInterface


class VehicleData(VehicleDataInterface):

    def __execute_query(self, query, row_factory=None):
        conn = sqlite3.connect(globals.database)
        conn.row_factory = row_factory
        
        cursor = conn.cursor()
    
        cursor.execute(query)
        data = cursor.fetchall()

        conn.commit()
        conn.close()
        
        return data

    def consult(self, id):
        query = f"""
        SELECT vh.id, vh.name, br.name, vh.color, vh.year, vh.description, vh.sold, vh.created, vh.updated 
        FROM vehicle vh JOIN brand br
        ON vh.brandid=br.id WHERE vh.id={id}
        """
        return self.__execute_query(query, lambda cursor, row: {
            'id': row[0],
            'nome': row[1], 
            'marca': row[2],
            'cor': row[3],
            'ano': row[4],
            'descricao': row[5],
            'vendido': row[6] == "True",
            'criado': row[7],
            'atualizado': row[8]
        })

    def consult_all(self, brand, year, color):

        query = """
        SELECT vh.id, vh.name, br.name, vh.color, vh.year, vh.description, vh.sold, vh.created, vh.updated 
        FROM vehicle vh JOIN brand br
        ON vh.brandid=br.id
        """
        
        if brand or year or color:
            query += " WHERE"
            flag = False
            if brand:
                brand_id = self.__execute_query(
                    f"SELECT id FROM brand WHERE name='{brand}'",
                    lambda cursor, row: row[0]
                )
                if not brand_id:
                    raise ValueError("Brand is incorrect!")
                
                query += f" vh.brandid='{brand_id[0]}'"
                flag = True
            if year:
                if flag:
                    query += " AND"
                query += f" vh.year='{year}'"
                flag = True
            
            if color:
                if flag:
                    query += " AND"
                query += f" vh.color='{color}'"

        data = self.__execute_query(query, lambda cursor, row: {
            'id': row[0],
            'nome': row[1], 
            'marca': row[2],
            'cor': row[3],
            'ano': row[4],
            'descricao': row[5],
            'vendido': row[6] == "True",
            'criado': row[7],
            'atualizado': row[8]
        })

        return data

    def register(self, vehicle: Vehicle):
        brand_id = self.__execute_query(
            f"SELECT id FROM brand WHERE name='{vehicle.brand}'",
            lambda cursor, row: row[0]
        )

        if brand_id:
            self.__execute_query(f"""
                INSERT INTO vehicle (name, brandid, color, year, description, sold, created, updated) 
                VALUES ('{vehicle.name}', '{brand_id[0]}', '{vehicle.color}', '{vehicle.year}', '{vehicle.description}', '{vehicle.sold}', datetime('now','localtime'), datetime('now','localtime'))
            """)
        else:
            raise ValueError("Brand is incorrect!")
    
    def update(self, vehicle: Vehicle):
        query = "UPDATE vehicle SET"
        flag = False

        if vehicle.name:
            query += f" name='{vehicle.name}'"
            flag = True
        
        if vehicle.brand:
            brand_id = self.__execute_query(
                f"SELECT id FROM brand WHERE name='{vehicle.brand}'",
                lambda cursor, row: row[0]
            )
            if not brand_id:
                raise ValueError("Brand is incorrect!")
            if flag:
                query += ','
            query += f" brandid='{brand_id[0]}'"
            flag = True
        
        if vehicle.color:
            if flag:
                query += ','
            query += f" color='{vehicle.color}'"
            flag = True

        if vehicle.year:
            if flag:
                query += ","
            query += f" year='{vehicle.year}'"
            flag = True
        
        if vehicle.description:
            if flag:
                query += ","
            query += f" year='{vehicle.description}'"
            flag = True
        
        if vehicle.sold:
            if flag:
                query += ","
            query += f" sold='{vehicle.sold}'"
        
        query += f", updated=datetime('now','localtime') WHERE id={vehicle.id}"

        self.__execute_query(query)

    def delete(self, id):
        self.__execute_query(f"DELETE FROM vehicle WHERE id={id}")
