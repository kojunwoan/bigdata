import cx_Oracle

#1. connection 객체 생성
connection = cx_Oracle.connect("scott","tigertiger","orcl.cmseqcexv7bt.ap-northeast-2.rds.amazonaws.com:1521/orcl")
#2. cursor 객체 생성
cur = connection.cursor()
#3. 사용할 sql문 객체
sql1 = "insert into dept values (:deptno, :dname, :loc)"
sql2 = "insert into dept values (:deptno, NULL, :loc)"
sql3 = "insert into dept (deptno, loc) values (:deptno, :loc)"
sql4 = "select * from dept"
#4. 실행
# cur.execute(sql1,[1,"SALEMAN","SEOUL"])
# cur.execute(sql1,[2,None,"BUSAN"])
# cur.execute(sql2,[2,"BUSAN"])
# cur.execute(sql3,[2,"BUSAN"])
cur.execute(sql4)
# connection.commit()
#5. 로직처리
for i in cur:
    print(i)
#6. 자원 반납
connection.close()