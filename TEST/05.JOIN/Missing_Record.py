import pymysql
import pandas as pd
    
query = """

    SELECT OUTS.ANIMAL_ID, OUTS.NAME
    FROM ANIMAL_INS AS INS
    RIGHT JOIN ANIMAL_OUTS AS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
    WHERE INS.ANIMAL_ID IS NULL
    ORDER BY OUTS.ANIMAL_ID

"""

# Connect to the database
conn = pymysql.connect(host = '192.168.0.2',
                       user = 'vanillapapaya',
                       password = 'qhans7810!',
                       db = 'AAC',
                       charset = 'utf8')

try:
    with conn.cursor() as cursor:
        
        # Show your query result
        cursor.execute(query)
        result = pd.read_sql(query, conn)
        conn.commit()
        cursor.close()

finally:
    conn.close()