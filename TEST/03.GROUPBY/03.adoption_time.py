import sys
sys.path.append("..")
import mysql_connect

query = """

    SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR
    HAVING HOUR >= 9 AND HOUR <= 19
    ORDER BY HOUR

"""

result = mysql_connect.query_result(query)
