import sys
sys.path.append("..")
import mysql_connect
    
query = """

    SELECT ANIMAL_ID, NAME, DATETIME
    FROM ANIMAL_INS
    ORDER BY NAME ASC, DATETIME DESC

"""

result = mysql_connect.query_result(query)  