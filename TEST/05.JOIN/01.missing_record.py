import sys
sys.path.append("..")
import mysql_connect
    
query = """

    SELECT OUTS.ANIMAL_ID, OUTS.NAME
    FROM ANIMAL_INS AS INS
    RIGHT JOIN ANIMAL_OUTS AS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
    WHERE INS.ANIMAL_ID IS NULL
    ORDER BY OUTS.ANIMAL_ID

"""

result = mysql_connect.query_result(query)