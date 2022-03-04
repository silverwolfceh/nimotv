from ws4py.client.threadedclient import WebSocketClient
import base64 as b64
import re
from functools import reduce
import struct
from threading import Thread
import time
import datetime

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
	],
	"jackpot" : [
		'AAMdAAEB9AAAAfQQAyw8QEZWBm5pbW91aWYOZ2V0SmFja1BvdEluZm99AAEByAgAAQYEdFJlcR0AAQG6CgoDAAABe2dZfS4WIDBhZDc2NzBlMmY2M2QxNjE3YTAxMzA5MTMxOTFiMmFjJwAAAVhBUUNFbVVIOHh2WlNqQ3BQY0xubkNpMUE3MWE4UjNoMURjazdEUGcwb1RlblV2RGVrMHdPYjZrYmVQeEpJQ1NyZU5SY25Vd1NyazJuS01TVzBSWUIyRHkyaGoxbWdaVmJmX3IwX2xNcXRkYlJzR3JXelFuY2diYjVVcmJ4U0dCQ2I1cjR5UGVBZm5XMDNjN0l1VkFaUzczMUpaRTVoRHgxU2ttc2ZFSlhxYXZjWXV2VVRZcVd0Q3RzWEsyMnVwT0J0NUpHU0wtSW5Xb21hLUVlS2lLdEdXSXAtc1R4cmh1VzhrbXBPMFJMUmdKQkNQMWUxek5wdUNQZUNpdnZWcXFpblh3czlhUW1zRldVQXZaVlljaWtLWnhLVWQ2WFhfZWN6Mm9VbmYwQnZQV0lqSWF0M3hxWHJ3UThWRmRlV085cmR3ZDFpbnpFQ3M0ZGYxU2NGUjVXTWZzTzYQd2ViJjEuMC40Jm5pbW9UVkYAVgQxMDMzZgMyLjFwY4YCVk6WAKYAsAULEQvAC4yYDKgMLDYhZmJlNDA3YjkwNTA4YWMzOS1mYmU0MDdiOTA1MDhhYzM5TA'
	],
	"heatbeat" : [
		'AAMdAAECBgAAAgYQAyw8QARWBm5pbW91aWYPT25Vc2VySGVhcnRCZWF0fQABAdkIAAEGBHRSZXEdAAEBywoKAwAAAjf+pRAgFiAwYTQ3Njk0ZmEzMzU1NTVmYTEwMmJjMTBiZDEwNDVlYScAAAFYQVFCbzU3Nmp6UG1ERGFvTHpXYW9oWlg0WWtjSXk0UVFmQzE0cHRmb3RuX3ZFQlllQ0s0WUVLREFTMU8tOS1YYzBxejVzcnFtc25PeDIyb1huaHhHbHBPQjlnUXhhLXBVNmdrU2RkVWRxeTZuZDFDYnBEbUhZR3pndWJfR2ZacVJwS1BZcHVEekoxZVhQbGpKeHgtb3hEemw5d2JQY1VLTFJjelFES3ZSQmdDQkF2U2tvd1RjaHRvRHBMb29NMnI0dzlwT0pmSW5oYkFBQ0xLS1VrTnFrWTVjMDRlVE1XM3RlY05ZTkNIMnZ3ZjdNakZRU2dScU5EMjVuYU4xc0duRmYtR0pjbGk2N2dQUHNtSlZIbkpTX3dMOExRcE1nY2dvREVCUktpenMyODRweU5SQ2cxcGc3X2RheXQ4ckFTak9XN3NGaXpvejFtU0xxbXc2RThScWl4QUs2EHdlYiYxLjAuNCZuaW1vVFZGAFYEMTA0NmYDMS4wcGOGAkJSlgCmALAECxMAAAI3/qUQICMAAAABcYc8wDABC4yYDKgMLDYhMTQ3NzgzMThhYjIwZDcxNC0xNDc3ODMxOGFiMjBkNzE0TA=='
	]
}

TYPE_COM_START = r'00041d00006\w0000006\w10032c3c40ff'
TYPE_JACK_RESP = r'00041d000101\w\w000001\w\w10032c3c40'
TYPE_UNKN_DATA = 'UNKNOWN OR DONT CARE'
WS_CONN = None
LAST_JP_VAL = 0

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

def send_heatbeat():
	while True:
		time.sleep(10)
		send_package(packages["heatbeat"])

def send_jackpot():
	while True:
		time.sleep(3)
		send_package(packages["jackpot"])
		

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

	def opened(self):
		global WS_CONN
		print("Connected")
		WS_CONN = self
		self.loop_package(packages["hello"])

	def closed(self, code, reason=None):
		print("Closed down", code, reason)

	def header_parser(self, hdrrow):
		#print(hdrrow)
		if re.search(TYPE_COM_START, hdrrow):
			return TYPE_COM_START
		elif re.search(TYPE_JACK_RESP, hdrrow):
			
			return TYPE_JACK_RESP
		else:
			return TYPE_UNKN_DATA

	def received_message(self, m):
		dv = DataView(m.data)
		first_row = dv.get_row(0)
		pck_type = self.header_parser(first_row)
		#00041d00006d0000006d10032c3c40ff
		#00041d00006c0000006c10032c3c40ff
		if pck_type == TYPE_COM_START:
			print("Communication started. Send request open")
			send_package( packages["info"])
			Thread(target=send_heatbeat).start()
			Thread(target=send_jackpot).start()
		elif pck_type == TYPE_JACK_RESP:
			global LAST_JP_VAL
			data_row = dv.get_row(4)
			jackval = int(data_row[-5:], 16)
			if jackval < LAST_JP_VAL:
				jptime = time.time()
				jptimefull = datetime.datetime.now("Asia/Ho_Chi_Minh")
				print("Jackpot at %s with val %d" % (jptimefull, jackval))
			else:
				print("Current Jackpot val: ", jackval)
			LAST_JP_VAL = jackval
		else:
			pass


if __name__ == '__main__':
	try:
		ws = NimoCli('wss://a4345916-ws.master.live/', protocols=['http-only', 'chat'])
		ws.connect()
		ws.run_forever()
	except KeyboardInterrupt:
		ws.close()
