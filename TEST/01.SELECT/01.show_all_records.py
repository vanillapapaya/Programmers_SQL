import sys
sys.path.append("..")
import mysql_connect
    
query = """

    SELECT *
    FROM ANIMAL_INS
    ORDER BY ANIMAL_ID

"""

result = mysql_connect.query_result(query)