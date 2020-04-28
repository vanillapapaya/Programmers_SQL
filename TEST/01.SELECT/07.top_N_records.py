import sys
sys.path.append("..")
import mysql_connect
    
query = """
    
    SELECT NAME
    FROM ANIMAL_INS
    ORDER BY DATETIME
    LIMIT 1

"""

result = mysql_connect.query_result(query)  