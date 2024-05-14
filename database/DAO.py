from database.DB_connect import DBConnect
from modello.Paese import Paese

class DAO():

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM country"
        cursor.execute(query)

        for row in cursor:
            result.append(Paese(row["StateAbb"], row["CCode"], row["StateNme"]))
        cursor.close()
        conn.close()
        return result
