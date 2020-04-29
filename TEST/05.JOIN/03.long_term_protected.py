import sys
sys.path.append("..")
import mysql_connect

query = """

    SELECT INS.NAME, INS.DATETIME
    FROM ANIMAL_INS AS INS
    LEFT JOIN ANIMAL_OUTS AS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
    WHERE OUTS.ANIMAL_ID IS NULL
    ORDER BY DATETIME ASC
    LIMIT 3

"""

result = mysql_connect.query_result(query)
