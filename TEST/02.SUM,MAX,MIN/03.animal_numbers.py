import sys
sys.path.append("..")
import mysql_connect

query = """

    SELECT COUNT(*)
    FROM ANIMAL_INS

"""

result = mysql_connect.query_result(query)