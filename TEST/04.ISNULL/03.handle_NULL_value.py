import sys
sys.path.append("..")
import mysql_connect

query = """

    SELECT ANIMAL_TYPE, IFNULL(NAME, "No name"), SEX_UPON_INTAKE
    FROM ANIMAL_INS
    ORDER BY ANIMAL_ID

"""

result = mysql_connect.query_result(query)
