import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)   #connection
        self.cur=self.conn.cursor()     #cursor
        self.cur.execute('''CREATE TABLE IF NOT EXISTS friends
                         (idn INTEGER PRIMARY KEY, idnum text, name text, dob text, gender text, school text, city text)''')
        self.conn.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM friends")
        rows=self.cur.fetchall()
        return(rows)
    
    def insert(self,idnum,name,dob,gender,school,city):
        self.cur.execute("INSERT INTO friends VALUES (NULL, ?, ?, ?, ?, ?, ?)",(idnum, name, dob, gender,school,city))
        self.conn.commit()
        
    def remove(self,idn):
        self.cur.execute("DELETE FROM friends WHERE idn=?",(idn,))
        self.conn.commit()
    
    def update(self,idn,idnum,name,dob,gender,school,city):
        self.cur.execute("UPDATE friends SET idnum = ?,name=?, dob=?,gender=?,school=?,city=? WHERE idn =?",(idnum,name,dob,gender,school,city,idn))
        self.conn.commit()
    def search(self,idnum):
        self.cur.execute("Select * FROM friends WHERE idnum=?",(idnum,))
        row=self.cur.fetchall()
        return(row)
        self.conn.commit()
    def __del__(self):
        self.conn.close()

        
        
        
#db=Database("Trialdirect1.db")
'''
db.insert("4GB DDR4 Ram","John Doe","Microcenter","140")
db.insert("Asus Mobo","Mike Henery","Microcenter","360")'''
