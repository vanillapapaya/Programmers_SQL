import sys
sys.path.append("..")
import mysql_connect

query = """

    SELECT ANIMAL_ID
    FROM ANIMAL_INS
    WHERE NAME IS NULL

"""

result = mysql_connect.query_result(query)
