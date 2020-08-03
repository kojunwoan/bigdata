import cx_Oracle

connection = cx_Oracle.connect("scott","tigertiger","orcl.cmseqcexv7bt.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection)

cur = connection.cursor()

query = "select * from dept"
cur.execute(query)

for x in cur:
    print(x)

connection.close()