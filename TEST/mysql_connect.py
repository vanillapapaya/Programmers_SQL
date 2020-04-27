import pymysql
import pandas as pd

def query_result(query):
    
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
            print(result)
            conn.commit()
            cursor.close()
    
    finally:
        conn.close()
        
    return result