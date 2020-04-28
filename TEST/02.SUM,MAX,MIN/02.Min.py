import sys
sys.path.append("..")
import mysql_connect
    
query1 = """

    SELECT DATETIME AS 시간
    FROM ANIMAL_INS
    ORDER BY DATETIME ASC
    LIMIT 1

"""

query2 = """

    SELECT MIN(DATETIME) AS 시간
    FROM ANIMAL_INS

"""

result1 = mysql_connect.query_result(query1)
result2 = mysql_connect.query_result(query2)