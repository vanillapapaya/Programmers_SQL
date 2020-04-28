import sys
sys.path.append("..")
import mysql_connect
    
query = """

    SELECT NAME, DATETIME
    FROM ANIMAL_INS
    ORDER BY ANIMAL_ID DESC

"""

result = mysql_connect.query_result(query)