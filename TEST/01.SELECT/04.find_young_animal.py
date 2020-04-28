import sys
sys.path.append("..")
import mysql_connect
    
query = """

    SELECT ANIMAL_ID, NAME
    FROM ANIMAL_INS
    WHERE INTAKE_CONDITION <> "Aged"
    ORDER BY ANIMAL_ID

"""

result = mysql_connect.query_result(query)  