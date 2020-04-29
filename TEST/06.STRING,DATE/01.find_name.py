import sys
sys.path.append("..")
import mysql_connect

query = """

    SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
    FROM ANIMAL_INS
    WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")

"""

result = mysql_connect.query_result(query)
