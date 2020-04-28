import sys
sys.path.append("..")
import mysql_connect

query = """

    SELECT ANIMAL_TYPE, COUNT(*)
    FROM ANIMAL_INS
    GROUP BY ANIMAL_TYPE
    ORDER BY FIELD(ANIMAL_TYPE, "Cat", "Dog")

"""

result = mysql_connect.query_result(query)