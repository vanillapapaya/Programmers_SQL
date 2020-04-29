import sys
sys.path.append("..")
import mysql_connect

query = """

    SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME, INS.SEX_UPON_INTAKE, OUTS.SEX_UPON_OUTCOME
    FROM ANIMAL_INS AS INS
    JOIN ANIMAL_OUTS AS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
    WHERE (INS.SEX_UPON_INTAKE LIKE "Intact%")
    # AND (OUTS.SEX_UPON_OUTCOME NOT LIKE "Intact%")

"""

result = mysql_connect.query_result(query)


# 문제에서와 달리 본래 데이터의 동물들은 보호소에 들어올 때 중성화를 받지 않았으면 보호소를 나갈 때에도 중성화를 받지 않았음.
# 문제를 만들기 위해 본래 데이터를 바꾼걸로 보임
