import sys
sys.path.append("..")
import mysql_connect
    
query = """

    SELECT ANIMAL_ID, NAME
    FROM ANIMAL_INS
    WHERE INTAKE_CONDITION = "Sick"

"""

result = mysql_connect.query_result(query)  