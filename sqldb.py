import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class sqldb:
	def __init__(self):
		self.dbname = "jp.db"
		self.tablname = "smalljp"
		self.conn = sqlite3.connect(self.dbname)
		self.conn.row_factory = dict_factory

	def get_record(self, numrec = 100):
		pass
	

	def save_record(self, data):
		sql = "INSERT INTO smalljp(jptime, jptimeful, jpval, win1, win2) VALUES(%d, '%s', %d, '%s', '%s')" % (int(data["jptime"]), data["jptimeful"], int(data["jpval"]), data["win1"], data["win2"])
		print(sql)
		self.conn.execute(sql)
		self.conn.commit()  
	
	def __del__(self):
		self.conn.close()

	def close(self):
		self.conn.close()


class jpdb(sqldb):
	def __init__(self):
		self.dbname = "jp.db"
		self.tablname = "smalljp"
		super().__init__()

	def get_record(self, numrec = 100):
		sql = "SELECT jptime, jptimeful, jpval, win1, win2 FROM smalljp ORDER BY ID desc limit %d" % numrec;
		cursor = self.conn.execute(sql)
		return cursor

	def save_record(self, data):
		sql = "INSERT INTO smalljp(jptime, jptimeful, jpval, win1, win2) VALUES(%d, '%s', %d, '%s', '%s')" % (int(data["jptime"]), data["jptimeful"], int(data["jpval"]), data["win1"], data["win2"])
		print(sql)
		self.conn.execute(sql)
		self.conn.commit()  


class beanlotdb(sqldb):
	def __init__(self):
		self.dbname = "jp.db"
		self.tablname = "beanlot"
		super().__init__()

	def get_record(self, numrec = 1000):
		sql = "SELECT * FROM %s ORDER BY ID desc limit %d" % (self.tablname, numrec)
		cursor = self.conn.execute(sql)
		return cursor

	def save_record(self, data):
		s

