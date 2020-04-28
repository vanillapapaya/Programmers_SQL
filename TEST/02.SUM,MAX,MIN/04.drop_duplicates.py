import sys
sys.path.append("..")
import mysql_connect

query = """

    SELECT COUNT(DISTINCT NAME) as count
    FROM ANIMAL_INS
    WHERE NAME IS NOT NULL

"""

result = mysql_connect.query_result(query)