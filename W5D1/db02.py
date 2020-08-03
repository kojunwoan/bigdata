import cx_Oracle

connection = cx_Oracle.connect("scott","tigertiger","orcl.cmseqcexv7bt.ap-northeast-2.rds.amazonaws.com:1521/orcl")

# print(connection)
cur = connection.cursor()

sql = """
select empno, ename, job, deptno
from emp
where deptno = :deptno
"""
#바인드 변수 사용시 :콜론 사용

#바인드 변수를 실행시 넘겨줌
cur.execute(sql,deptno=10)

for empno, ename, job, deptno in cur:
    print("{}\t{}\t{}\t{}".format(empno,ename,job,deptno))

connection.close()