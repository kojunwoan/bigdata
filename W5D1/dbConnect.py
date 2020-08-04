import cx_Oracle

class DbConnect:
    def __init__(self,user,password,host,dbname,port="1521"):
        # self.connection = cx_Oracle.Connect(user,password,host+":"+port+"/"+dbname)
        self.connection = cx_Oracle.connect(user,password,host+":"+port+"/"+dbname)
        print(self.connection)

    def execute(self,sql):
        self.sql = sql
        cur = self.connection.cursor()
        cur.execute(sql)
        resultList = []
        for x in cur:
            resultList.append(x)
        self.connection.close()
        
        return resultList
if __name__=="__main__":
    db = DbConnect("scott","tiger","192.168.0.68","orcl","1521")
    print(db.execute("select * from dept"))