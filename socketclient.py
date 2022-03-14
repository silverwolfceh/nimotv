from ws4py.client.threadedclient import WebSocketClient
import base64 as b64
import re
from functools import reduce
import struct
from threading import Thread
import time
from datetime import datetime,timezone
from sqldb import *
from util import *
from pytz import timezone
import pytz
import json

packages = {
	"hello" : [
		'AAMdAAEAiwAAAIsQAyw8QP9WBmxhdW5jaGYId3NMYXVuY2h9AABmCAABBgR0UmVxHQAAWQoDAAABe2dZfS4WIDBhNDc2OTRlNTAyMjRjNjEyMjEyNGE2MTRiNjExMTNkJhB3ZWJoNSYwLjAuMSZuaW1vNgxOSU1PJlZOJjEwNjZKBgAWACYANgBGAAsLjJgMqAwsNgBM',
		'AAodAAEHBwMAAAF7Z1l9LhYQd2ViaDUmMC4wLjEmbmltbycAAAa1aHV5YV91YT13ZWJoNSYwLjAuMSZuaW1vOyBfX3lhbWlkX25ldz1DOTg3OUUyRDgyODAwMDAxOTMxRjdBNUMxNTk2RkZFMDsgX2dhPUdBMS4xLjE3NzY3ODc0MTcuMTYzMjM3OTQ3MzsgZ3VpZD0wYTQ3Njk0ZTUwMjI0YzYxMjIxMjRhNjE0YjYxMTEzZDsgdGhlbWU9MjsgaHV5YV91YT13ZWJoNSYwLjAuMSZuaW1vOyBsYW5nPTEwNjY7IGNjb3VudHJ5PVZOOyBjbGFuZz0xMDY2OyB1ZGJfZ3VpZGRhdGE9MGNiMDA4YzZmZGFiNDM0ZjhiYjcwZDJmNTAyZmVlNDY7IGNvdW50cnk9Vk47IF9feWFzbWlkPTAuNjUyOTE3ODg3NzE3MTIyNzsgeWFfcG9wdXBfbG9naW5fZnJvbT1sb2dpbl9idDsgeWFfbG9naW5fbW9kZT1QaG9uZU51bTsgdWRiX2JpenRva2VuPUFRQ0lIYlpuQ195MmlxYWhvOGw2cGhQTEdvdms2MDFIdENHUllmOGxuTE1qeDVadUtDR2YyRWJkeFMzcEctZUhGUFgzeVpGQkFMMjNNQlE3LUVVaHR2RzRqN2M2aG50ZUJ1RkxuR0dfcUViWElBWTVuLVktLXN1dWx1eDBfMllybng2Z1lRdG5DZm9SUXlIVFBRY0dlLTU2dElzd2NQZFNDbkZIZ25nSkhjZGt1Mzh6UnJKUi02X2Z6Q2xhaWtQdEZsNTdiX253QlQ5RkE5X2lMRXFFbGNRODh1Zmhmd05oRUpEcDR0TkNzQmxFYmloTGRuXzF3OGxaUjczRTBwT3ZxRDcyY2FBS0Z1R2R5REp3ZVJWZjQ2Nkh5U2xvb21BRUdfMlJFdms0b1BDd3FlSzFqMkRUTmpKcDREekszYXp6YzJ5V013NjUxcXdTNVpVTzhJRmRqTG5LOyB1ZGJfY3JlZD1DakN0M28zS2htQ1pkeHBaSUpjQlhhR1VjZGU5aWErU2txelNGY2ZwOERnMW1WSHB1cTByTDcyWENRVDMzR1B2aGFmSmU5V002eGxEQ1dXbTlCRVc5ZURYZzZrYmM4eFVQVHNXUUlpVW5LOStvZz09OyB1ZGJfb3JpZ2luPTA7IHVkYl9zdGF0dXM9MTsgdWRiX3VpZD0xNjI5NTI2NTIzMTgyOyB1ZGJfdmVyc2lvbj0yLjE7IHl5dWlkPTE2Mjk1MjY1MjMxODI7IHZlcnNpb249Mi4xOyBiaXpUb2tlbj1BUUNJSGJabkNfeTJpcWFobzhsNnBoUExHb3ZrNjAxSHRDR1JZZjhsbkxNang1WnVLQ0dmMkViZHhTM3BHLWVIRlBYM3laRkJBTDIzTUJRNy1FVWh0dkc0ajdjNmhudGVCdUZMbkdHX3FFYlhJQVk1bi1ZLS1zdXVsdXgwXzJZcm54NmdZUXRuQ2ZvUlF5SFRQUWNHZS01NnRJc3djUGRTQ25GSGduZ0pIY2RrdTM4elJySlItNl9mekNsYWlrUHRGbDU3Yl9ud0JUOUZBOV9pTEVxRWxjUTg4dWZoZndOaEVKRHA0dE5Dc0JsRWJpaExkbl8xdzhsWlI3M0UwcE92cUQ3MmNhQUtGdUdkeURKd2VSVmY0NjZIeVNsb29tQUVHXzJSRXZrNG9QQ3dxZUsxajJEVE5qSnA0RHpLM2F6emMyeVdNdzY1MXF3UzVaVU84SUZkakxuSzsgdXNlcmlkPTE3NzcxMzMwNDsgdXNlck5hbWU9JUUwJUI5JTk2JURCJUEzJURCJTlDS2glQzMlQjNpOyB1ZGJVc2VySWQ9MTYyOTUyNjUyMzE4MjsgaXNBbmNob3I9MTsgYXZhdGFyVXJsPWh0dHBzOi8vc2VydmVyLWF2YXRhci5uaW1vc3RhdGljLnR2LzE2Mjk1MjY1MjMxODIvMjAyMjAzMDExNjQ2MTQzMzg5MzIwXzE2Mjk1MjY1MjMxODJfYXZhdGFyLnBuZzsgX195YW9sZHl5dWlkPTE2Mjk1MjY1MjMxODI7IF95YXNpZHM9X19yb290c2lkJTNEQzlCQUU3RjMwMTUwMDAwMTQyMzExMTAwMUFGNjlDODA7IHlhX2VpZD11bmRlZmluZWQ7IF9feWFvbGRjaWQ9OyBfZ2FfUjg4Rjg0U0hXOT1HUzEuMS4xNjQ2MTQ3MDU1LjEwOS4xLjE2NDYxNDcwODEuMzQ7IF9nYV9ROUY4NjhZWDdSPUdTMS4xLjE2NDYxNDcwMjEuMTc3LjEuMTY0NjE0NzI2Ny40NzYgMGE0NzY5NGU1MDIyNGM2MTIyMTI0YTYxNGI2MTExM2RAAVYMTklNTyZWTiYxMDY2LDYATA'
	],
	"info" : [
		'UGFjb3RlIG9taXRpZG8=',
		'UGFjb3RlIG9taXRpZG8=',
		'AAMdAAECBAAAAgQQAyw8QANWBm5pbW91aWYLT25Vc2VyRXZlbnR9AAEB2wgAAQYEdFJlcR0AAQHNCgoDAAACN/6lECAWIDBhNDc2OTRmYTMzNTU1NWZhMTAyYmMxMGJkMTA0NWVhJwAAAVhBUUJvNTc2anpQbUREYW9Meldhb2haWDRZa2NJeTRRUWZDMTRwdGZvdG5fdkVCWWVDSzRZRUtEQVMxTy05LVhjMHF6NXNycW1zbk94MjJvWG5oeEdscE9COWdReGEtcFU2Z2tTZGRVZHF5Nm5kMUNicERtSFlHemd1Yl9HZlpxUnBLUFlwdUR6SjFlWFBsakp4eC1veER6bDl3YlBjVUtMUmN6UURLdlJCZ0NCQXZTa293VGNodG9EcExvb00ycjR3OXBPSmZJbmhiQUFDTEtLVWtOcWtZNWMwNGVUTVczdGVjTllOQ0gydndmN01qRlFTZ1JxTkQyNW5hTjFzR25GZi1HSmNsaTY3Z1BQc21KVkhuSlNfd0w4TFFwTWdjZ29ERUJSS2l6czI4NHB5TlJDZzFwZzdfZGF5dDhyQVNqT1c3c0Zpem96MW1TTHFtdzZFOFJxaXhBSzYQd2ViJjEuMC40Jm5pbW9UVkYAVgQxMDQ2ZgMxLjBwY4YCQlKWAKYAsAQLEAEjAAACN/6lECAzAAAAAXGHPMBAAQuMmAyoDCw2IWY1NzNjMjRlOGZlNzA1OTEtZjU3M2MyNGU4ZmU3MDU5MUw=',
		'AAMdAAECBgAAAgYQAyw8QARWBm5pbW91aWYPT25Vc2VySGVhcnRCZWF0fQABAdkIAAEGBHRSZXEdAAEBywoKAwAAAjf+pRAgFiAwYTQ3Njk0ZmEzMzU1NTVmYTEwMmJjMTBiZDEwNDVlYScAAAFYQVFCbzU3Nmp6UG1ERGFvTHpXYW9oWlg0WWtjSXk0UVFmQzE0cHRmb3RuX3ZFQlllQ0s0WUVLREFTMU8tOS1YYzBxejVzcnFtc25PeDIyb1huaHhHbHBPQjlnUXhhLXBVNmdrU2RkVWRxeTZuZDFDYnBEbUhZR3pndWJfR2ZacVJwS1BZcHVEekoxZVhQbGpKeHgtb3hEemw5d2JQY1VLTFJjelFES3ZSQmdDQkF2U2tvd1RjaHRvRHBMb29NMnI0dzlwT0pmSW5oYkFBQ0xLS1VrTnFrWTVjMDRlVE1XM3RlY05ZTkNIMnZ3ZjdNakZRU2dScU5EMjVuYU4xc0duRmYtR0pjbGk2N2dQUHNtSlZIbkpTX3dMOExRcE1nY2dvREVCUktpenMyODRweU5SQ2cxcGc3X2RheXQ4ckFTak9XN3NGaXpvejFtU0xxbXc2RThScWl4QUs2EHdlYiYxLjAuNCZuaW1vVFZGAFYEMTA0NmYDMS4wcGOGAkJSlgCmALAECxMAAAI3/qUQICMAAAABcYc8wDABC4yYDKgMLDYhMTQ3NzgzMThhYjIwZDcxNC0xNDc3ODMxOGFiMjBkNzE0TA==',
		'AAMdAAEAjAAAAIwQAyw8QP9WBmxhdW5jaGYMcXVlcnlIdHRwRG5zfQAAYwgAAQYEdFJlcR0AAFYKAwAAAjf+pRAgFhB3ZWJoNSYwLjAuMSZuaW1vKQACBhBjZG4ud3VwLmh1eWEuY29tBhJjZG53cy5hcGkuaHV5YS5jb202DE5JTU8mQlImMTA0NkYAC4yYDKgMLDYATA==',
	]
}

TYPE_COM_START = r'00041d00006\w0000006\w10032c3c40ff'
TYPE_DATA_START = r'00041d0001.*'
TYPE_UNKN_DATA = 'UNKNOWN OR DONT CARE'

DATA_JACKPOT_INFO = "506f74496e666f" #PotInfo, row2
DATA_BEAN_RESULT = "4265616e4c6f74" #BeanLot, row2
DATA_BEAN_ROUND = "526f756e64" #Round

BOX_INPR = ["BOX1_X5", "BOX2_X5", "BOX3_X5", "BOX4_X5", "BOX5_X10", "BOX6_X15", "BOX7_X25", "BOX8_X45", "BOX1234", "BOX5678"]

WS_CONN = None
LAST_JP_VAL = 0
CUR_ROUND = -1
SQL_DB_INS = None

class DataView:
	def __init__(self, array, bytes_per_element=1):
		"""
		bytes_per_element is the size of each element in bytes.
		By default we are assume the array is one byte per element.
		"""
		self.array = array
		self.bytes_per_element = 1

	def __get_binary(self, start_index, byte_count, signed=False):
		integers = [self.array[start_index + x] for x in range(byte_count)]
		bytes = [integer.to_bytes(self.bytes_per_element, byteorder='little', signed=signed) for integer in integers]
		return reduce(lambda a, b: a + b, bytes)

	def get_uint_16(self, start_index):
		bytes_to_read = 2
		return int.from_bytes(self.__get_binary(start_index, bytes_to_read), byteorder='little')

	def get_uint_8(self, start_index):
		bytes_to_read = 1
		return int.from_bytes(self.__get_binary(start_index, bytes_to_read), byteorder='little')


	def get_hex(self, start_index):
		return "{:02x}".format(self.get_uint_8(start_index))

	def get_row(self, row_num):
		offset = row_num * 16
		data = ""
		try:
			for i in range(0, 16):
				data += "{:02x}".format(self.get_uint_8(offset + i))
		except:
			pass
		return data

	def get_float_32(self, start_index):
		bytes_to_read = 4
		binary = self.__get_binary(start_index, bytes_to_read)
		return struct.unpack('<f', binary)[0] # <f for little endian


def parse(byte_array):
	d = DataView(byte_array)
	return {
		"headerSize": d.get_uint_8(0),
		"numverOfPlanes": d.get_uint_16(1),
		"width": d.get_uint_16(3),
		"hieght": d.get_uint_16(5),
		"offset": d.get_uint_16(7),
	}

def send_package(package):
	for p in package:
		p += '=' * (-len(p) % 4)
	if WS_CONN != None:
		WS_CONN.send(b64.b64decode(p), binary = True)
	else:
		print("Not initialize WS")

def reset_global():
	global WS_CONN, LAST_JP_VAL, CUR_ROUND
	WS_CONN = None
	LAST_JP_VAL = 0
	CUR_ROUND = -1


def send_heatbeat():
	while True:
		time.sleep(10)
		send_package(create_onUserHeartBeat())

def send_jackpot():
	while True:
		time.sleep(1)
		send_package(create_getJackpotInfo())

def send_beanlot():
	while True:
		time.sleep(1)
		send_package(create_getGoldBeanLotteryResult(CUR_ROUND))

def send_beancurrentround():
	while True:
		send_package(create_getGoldBeanLotteryCurrentRound())	
		time.sleep(1)
	

def process_bean_lottery(dv, pck_type):
	global CUR_ROUND
	if pck_type == DATA_BEAN_ROUND:
		data_row = str(dv.get_row(5))
		roundnum = int(data_row[19:22], 16)
		if CUR_ROUND == -1 and roundnum > 0:
			CUR_ROUND = roundnum
			time.sleep(3)
			send_package(create_getGoldBeanLotteryResult(roundnum-1))
			print("Round: ", roundnum)
		elif roundnum > CUR_ROUND:
			time.sleep(3)
			send_package(create_getGoldBeanLotteryResult(roundnum-1))
			CUR_ROUND = roundnum
			print("Round: ", roundnum)
		else:
			# Same round
			pass
	elif pck_type == DATA_BEAN_RESULT:
		boxval = -1
		data_row = str(dv.get_row(5))
		print(data_row)
		if int(data_row[0:4], 16) == 0x0C29:
			numbox = int(data_row[7:8])
			print("Numbox: ", numbox)
			if numbox == 4:
				if data_row.find("0c2900040c000100020003") != -1:
					boxval = 8
				else:
					boxval = 9
			elif numbox == 1:
				if data_row.find("0c2900010c3900030") != -1:
					boxval = 0
				else:
					boxval = int(data_row[11:12], 16)
			else:
				print("Numbox: ", numbox)
		elif int(data_row[0:4], 16) == 0x190c:
			boxval = 0
		else:
			print("DATA_BEAN_RESULT WRONG")
		if boxval >= 0 and boxval < len(BOX_INPR):
			print("Box Val: ", BOX_INPR[boxval])
			


def data_callback(dtype, data):
	# Dummy function
	pass

def sk_closed():
	# Dummy function
	pass

class NimoCli(WebSocketClient):
	def decode_base64(self, data, altchars=b'+/'):
		data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
		missing_padding = len(data) % 4
		if missing_padding:
			data += b'='* (4 - missing_padding)
		return b64.b64decode(data, altchars)

	def loop_package(self, package):
		for p in package:
			p += '=' * (-len(p) % 4)
			self.send(b64.b64decode(p), binary = True)


	def set_datacallback(self, fcallback):
		self.fcallback = fcallback

	def set_closecallback(self, fcallback):
		self.closecallback = fcallback

	def opened(self):
		global WS_CONN
		print("Connected")
		WS_CONN = self
		self.loop_package(packages["hello"])

	def closed(self, code, reason=None):
		print("Closed down", code, reason)
		reset_global()
		self.closecallback()

	def package_parser(self, dv):
		hdrrow = dv.get_row(0)
		if re.search(TYPE_COM_START, hdrrow):
			return TYPE_COM_START
		elif re.search(TYPE_DATA_START, hdrrow):
			# print("DATA")
			pack_2 = dv.get_row(2)
			pack_3 = dv.get_row(3)
			# print(pack_2)
			# print(pack_3)
			if str(pack_2).find(DATA_JACKPOT_INFO) != -1:
				return DATA_JACKPOT_INFO
			elif str(pack_3).find(DATA_BEAN_ROUND) != -1:
				return DATA_BEAN_ROUND
			elif str(pack_2).find(DATA_BEAN_RESULT) != -1:
				return DATA_BEAN_RESULT
			else:
				return TYPE_UNKN_DATA
		else:
			return TYPE_UNKN_DATA


	def received_message(self, m):
		dv = DataView(m.data)

		pck_type = self.package_parser(dv)
		# print(pck_type)
		if pck_type == TYPE_COM_START:
			print("Communication started. Send request open")
			send_package( packages["info"])
			Thread(target=send_heatbeat).start()
			Thread(target=send_beancurrentround).start()
			# if CUR_ROUND == -1:
			# 	send_package(create_getGoldBeanLotteryCurrentRound())
		elif pck_type == DATA_BEAN_ROUND or pck_type == DATA_BEAN_RESULT:
			process_bean_lottery(dv, pck_type)
		elif pck_type == DATA_JACKPOT_INFO:
			global LAST_JP_VAL
			data_row = dv.get_row(4)
			jackval = int(data_row[-5:], 16)
			if jackval < LAST_JP_VAL:
				jptime = int(time.time())
				jptimefull = datetime.now(timezone("Asia/Ho_Chi_Minh"))
				print("Jackpot at %s with val %d" % (jptimefull, jackval))
				data = {
					"jptime" : str(jptime),
					"jptimeful" : str(jptimefull),
					"jpval" : jackval,
					"win1" : "",
					"win2" : ""
				}

				self.fcallback("smalljp", json.dumps(data))
				db = sqldb()
				db.save_record(data)
				db.close()

			else:
				jptime = int(time.time())
				jptimefull = datetime.now(timezone("Asia/Ho_Chi_Minh"))
				data = {
					"jptime" : str(jptime),
					"jptimeful" : str(jptimefull),
					"jpval" : jackval,
					"win1" : "",
					"win2" : ""
				}
				if LAST_JP_VAL != jackval:
					self.fcallback("smallrt", json.dumps(data))
					print("Current Jackpot val: %d. Delta: %d" % (jackval, jackval - LAST_JP_VAL))
			LAST_JP_VAL = jackval
		else:
			pass

def run_socket_client(fcallback_data, fcallback_close):
	try:
		ws = NimoCli('wss://a4345916-ws.master.live/', protocols=['http-only', 'chat'])
		ws.set_datacallback(fcallback_data)
		ws.set_closecallback(fcallback_close)
		ws.connect()
		ws.run_forever()
	except KeyboardInterrupt:
		ws.close()

if __name__ == '__main__':
	run_socket_client(data_callback, sk_closed)
