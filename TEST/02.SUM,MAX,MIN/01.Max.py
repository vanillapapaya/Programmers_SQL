import sys
sys.path.append("..")
import mysql_connect
    
query1 = """

    SELECT DATETIME AS 시간
    FROM ANIMAL_INS
    ORDER BY DATETIME DESC
    LIMIT 1

"""

query2 = """

    SELECT MAX(DATETIME) AS 시간
    FROM ANIMAL_INS

"""

result1 = mysql_connect.query_result(query1)
result2 = mysql_connect.query_result(query2)