import cx_Oracle

connection = cx_Oracle.connect("scott","tigertiger","orcl.cmseqcexv7bt.ap-northeast-2.rds.amazonaws.com:1521/orcl")
connection2 = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")

# print(connection)
cur = connection.cursor()
cur2 = connection2.cursor()

sql = """
select empno, ename, job, deptno
from emp
where deptno = :deptno
"""

sql2 = """
insert into member (id, pw, name, grade)
values ("junwoan","1q2w3e4r","kojunwoan",5)
"""

sql3 = """
select * from member
"""
#바인드 변수 사용시 :콜론 사용

#바인드 변수를 실행시 넘겨줌
cur.execute(sql,deptno=10)
cur2.execute(sql2)
connection.commit()


for empno, ename, job, deptno in cur:
    print("{}\t{}\t{}\t{}".format(empno,ename,job,deptno))

connection.close()