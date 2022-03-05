import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class sqldb:
	def __init__(self):
		self.conn = sqlite3.connect('jp.db')
		self.conn.row_factory = dict_factory

	def get_record(self, numrec = 100):
		sql = "SELECT jptime, jptimeful, jpval, win1, win2 FROM smalljp ORDER BY ID desc limit %d" % numrec;
		cursor = self.conn.execute(sql)
		return cursor
	

	def save_record(self, data):
		sql = "INSERT INTO smalljp(jptime, jptimeful, jpval, win1, win2) VALUES(%d, '%s', %d, '%s', '%s')" % (data["jptime"], data["jptimeful"], data["jpval"], data["win1"], data["win2"])
		print(sql)
		self.conn.execute(sql)
		self.conn.commit()  
	
	def __del__(self):
		self.conn.close()

	def close(self):
		self.conn.close()