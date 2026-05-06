from database.DB_connect import DBConnect
from database.retailer_DTO import RetailerDTO
from datetime import date
from dataclasses import dataclass

@dataclass
class SaleStatistic:
    retailer_code: int
    product_number: int
    order_method_code: int
    date: date
    quantity: int
    unit_price: float
    unit_sale_price: float
    profit: float


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
        cnx.close()
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

        cursor.close()
        cnx.close()
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

        cursor.close()

        return l

    @staticmethod
    def get_best_sales_filter(year = None, retailer_code = None, product_brand = None, limit = 5) -> list[SaleStatistic]:
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
        SELECT *, (G.Unit_sale_price * G.Quantity) as profit FROM go_daily_sales G
	WHERE YEAR(Date) = COALESCE(%s, YEAR(Date)) AND
		G.Retailer_code = COALESCE(%s, Retailer_code) AND
		 (SELECT Product_brand 
		 FROM go_products P 
		 WHERE P.Product_number = G.Product_number) = COALESCE(%s, (SELECT Product_brand 
		 FROM go_products P 
		 WHERE P.Product_number = G.Product_number))
		 ORDER BY profit DESC;
                """

        data = (year, retailer_code, product_brand)
        cursor.execute(query, data)
        r: list[dict] = cursor.fetchall()
        l: list[SaleStatistic] = []
        cursor.close()
        cnx.close()

        i = 0
        while i < limit and i < len(r):
            row = r[i]
            l.append(SaleStatistic(
                retailer_code=row["Retailer_code"],
                product_number=row["Product_number"],
                order_method_code=row["Order_method_code"],
                date=row["Date"],
                quantity=row["Quantity"],
                unit_price=row["Unit_price"],
                unit_sale_price=row["Unit_sale_price"],
                profit=row["profit"],
            ))
            i += 1

        return l