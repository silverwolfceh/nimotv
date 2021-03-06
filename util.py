import codecs
import json
from datetime import date, datetime
from pytz import timezone
import pytz

def create_dataarray(data):
	return [data]

def create_getGoldBeanLotteryResult(whatround):
	d0 = datetime(2022, 3, 15, tzinfo=timezone("Asia/Shanghai"))
	d1 = datetime.now(timezone("Asia/Shanghai"))
	#d0 = date(2022, 3, 15)
	#d1 = date.today()
	delta = (d1-d0).days
	print(delta, d1)
	data_day = 0x7A + delta
	data_pre = "00031d000102060000020610032c3c406256066e696d6f75696618676574476f6c644265616e4c6f7474657279526573756c747d000101d00800010604745265711d000101c20a0a030000017b67597d2e1620306164373637306532663633643136313761303133303931333139316232616327000001584151414676347674502d63524c786a6a32634a7530774f45384d5a59647a43553341516e563535346a793044436c34734365666a455f59533542514e3336504354637631304e496238756e6c44494451385a4e37415f706e364b4f6d666b5644774f63444f4c65675871517643646366524d75316953433766484f3855395170394758576145493661643043324534447855794a6c6e4663557273504e34796a32534a4845472d57754f336f58424b67626e3969706f424874454a666b313176552d6f31417634506d4c4f45533372326f51694552704139427870696264476e7468676c5a7133394d6341795452683551764d6b6d76307432664579356c56586c334a43507a532d54483455436874494b6a7779534e356f42553851706258614b6132776e6f436b646f392d674e6c4f696c613669544951656b344865594f585650427a356d61784666756b6f4d7373724b485a504a7547361077656226312e302e34266e696d6f545646005604313033336603312e3070638602564e9600a600b0050b1a014a%s11"
	data_day = "{:02x}".format(data_day)
	data_mid = "{:04x}".format(whatround)
	# print(data_mid)
	data_post = "0b210bc00b8c980ca80c2c3625643834336137386630383336356566313a643834336137386630383336356566313a303a314c5c6600"
	data = data_pre % data_day + data_mid + data_post
	b64 = codecs.encode(codecs.decode(data, 'hex'), 'base64').decode()
	return create_dataarray(b64)

def create_getGoldBeanLotteryCurrentRound():
	data = "AAMdAAECBQAAAgUQAyw8QQDHVgZuaW1vdWlmHmdldEdvbGRCZWFuTG90dGVyeUN1cnJlbnRSb3VuZH0AAQHICAABBgR0UmVxHQABAboKCgMAAAF7Z1l9LhYgMGFkNzY3MGUyZjYzZDE2MTdhMDEzMDkxMzE5MWIyYWMnAAABWEFRQUZ2NHZ0UC1jUkx4amoyY0p1MHdPRThNWllkekNVM0FRblY1NTRqeTBEQ2w0c0NlZmpFX1lTNUJRTjM2UENUY3YxME5JYjh1bmxESURROFpON0FfcG42S09tZmtWRHdPY0RPTGVnWHFRdkNkY2ZSTXUxaVNDN2ZITzhVOVFwOUdYV2FFSTZhZDBDMkU0RHhVeUpsbkZjVXJzUE40eWoyU0pIRUctV3VPM29YQktnYm45aXBvQkh0RUpmazExdlUtbzFBdjRQbUxPRVMzcjJvUWlFUnBBOUJ4cGliZEdudGhnbFpxMzlNY0F5VFJoNVF2TWttdjB0MmZFeTVsVlhsM0pDUHpTLVRINFVDaHRJS2p3eVNONW9CVThRcGJYYUthMndub0NrZG85LWdObE9pbGE2aVRJUWVrNEhlWU9YVlBCejVtYXhGZnVrb01zc3JLSFpQSnVHNhB3ZWImMS4wLjQmbmltb1RWRgBWBDEwMzNmAzEuMHBjhgJWTpYApgCwBQsRC8ALjJgMqAwsNiU3NDc0ZWRiMzE3MGQ3YmNhOjc0NzRlZGIzMTcwZDdiY2E6MDoxTFxmAA"
	return create_dataarray(data)

def create_getJackpotInfo():
	data = "AAMdAAEB9AAAAfQQAyw8QEZWBm5pbW91aWYOZ2V0SmFja1BvdEluZm99AAEByAgAAQYEdFJlcR0AAQG6CgoDAAABe2dZfS4WIDBhZDc2NzBlMmY2M2QxNjE3YTAxMzA5MTMxOTFiMmFjJwAAAVhBUUNFbVVIOHh2WlNqQ3BQY0xubkNpMUE3MWE4UjNoMURjazdEUGcwb1RlblV2RGVrMHdPYjZrYmVQeEpJQ1NyZU5SY25Vd1NyazJuS01TVzBSWUIyRHkyaGoxbWdaVmJmX3IwX2xNcXRkYlJzR3JXelFuY2diYjVVcmJ4U0dCQ2I1cjR5UGVBZm5XMDNjN0l1VkFaUzczMUpaRTVoRHgxU2ttc2ZFSlhxYXZjWXV2VVRZcVd0Q3RzWEsyMnVwT0J0NUpHU0wtSW5Xb21hLUVlS2lLdEdXSXAtc1R4cmh1VzhrbXBPMFJMUmdKQkNQMWUxek5wdUNQZUNpdnZWcXFpblh3czlhUW1zRldVQXZaVlljaWtLWnhLVWQ2WFhfZWN6Mm9VbmYwQnZQV0lqSWF0M3hxWHJ3UThWRmRlV085cmR3ZDFpbnpFQ3M0ZGYxU2NGUjVXTWZzTzYQd2ViJjEuMC40Jm5pbW9UVkYAVgQxMDMzZgMyLjFwY4YCVk6WAKYAsAULEQvAC4yYDKgMLDYhZmJlNDA3YjkwNTA4YWMzOS1mYmU0MDdiOTA1MDhhYzM5TA"
	return create_dataarray(data)

def create_onUserHeartBeat():
	data = "AAMdAAECBgAAAgYQAyw8QARWBm5pbW91aWYPT25Vc2VySGVhcnRCZWF0fQABAdkIAAEGBHRSZXEdAAEBywoKAwAAAjf"
	return create_dataarray(data)

def test_util():
	create_getGoldBeanLotteryResult(1)

def create_stats_data(data):
	stats = {
		"box0" : 0,
		"box1" : 0,
		"box2" : 0,
		"box3" : 0,
		"box4" : 0,
		"box5" : 0,
		"box6" : 0,
		"box7" : 0,
		"small" : 0,
		"big"  : 0,
		"total": 0
	}
	
	for d in data:
		if d["BoxVal"] >= 0 and d["BoxVal"] <=7:
			stats["box%d" % d["BoxVal"]] = stats["box%d" % d["BoxVal"]] + 1
		elif d["BoxVal"] == 8:
			stats["small"] = stats["small"] + 1
			stats["box0"] = stats["box0"] + 1
			stats["box1"] = stats["box1"] + 1
			stats["box2"] = stats["box2"] + 1
			stats["box3"] = stats["box3"] + 1
		elif d["BoxVal"] == 9:
			stats["big"] = stats["big"] + 1
			stats["box4"] = stats["box4"] + 1
			stats["box5"] = stats["box5"] + 1
			stats["box6"] = stats["box6"] + 1
			stats["box7"] = stats["box7"] + 1
		else:
			pass
	stats["total"] = len(data)
	data = {}
	data["stats"] = stats
	return json.dumps(data["stats"])

if __name__ == '__main__':
	test_util()