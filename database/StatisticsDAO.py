from database.DB_connect import DBConnect


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
