from database.DB_connect import DBConnect
from database.retailer_DTO import RetailerDTO


class StatisticsDAO:
    """DAO to handle all the statistics loading from the database"""
    def __init__(self):
        pass

    @staticmethod
    def load_years_list() -> list[int]:
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
        SELECT DISTINCT(YEAR(Date)) AS distinct_years FROM go_daily_sales;"""

        cursor.execute(query)
        l = []
        for v in cursor:
            l.append(v["distinct_years"])

        cursor.close()

        return l

    @staticmethod
    def load_brand_list() -> list[str]:
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
        SELECT DISTINCT(Product_brand) FROM go_products;"""

        cursor.execute(query)

        l = []
        for row in cursor:
            l.append(row["Product_brand"])

        return l

    @staticmethod
    def load_retailer_list() -> list[RetailerDTO]:
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                SELECT *
                FROM go_retailers;"""

        cursor.execute(query)

        l = []
        for row in cursor:
            l.append(RetailerDTO(
                row["Retailer_code"],
                row["Retailer_name"],
                row["Type"],
                row["Country"]
            ))

        return l