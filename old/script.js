// const ws = new WebSocket('wss://a4345916-ws.master.live/?baseinfo=AwAAAXtnWX0uFiAwYTQ3Njk0ZTUwMjI0YzYxMjIxMjRhNjE0YjYxMTEzZCYQd2ViaDUmMC4wLjEmbmltbzYMTklNTyZWTiYxMDY2RgBWAGx2AIcAAAa0aHV5YV91YT13ZWJoNSYwLjAuMSZuaW1vOyBfX3lhbWlkX25ldz1DOTg3OUUyRDgyODAwMDAxOTMxRjdBNUMxNTk2RkZFMDsgX2dhPUdBMS4xLjE3NzY3ODc0MTcuMTYzMjM3OTQ3MzsgZ3VpZD0wYTQ3Njk0ZTUwMjI0YzYxMjIxMjRhNjE0YjYxMTEzZDsgdGhlbWU9MjsgaHV5YV91YT13ZWJoNSYwLjAuMSZuaW1vOyBsYW5nPTEwNjY7IGNjb3VudHJ5PVZOOyBjbGFuZz0xMDY2OyB1ZGJfZ3VpZGRhdGE9MGNiMDA4YzZmZGFiNDM0ZjhiYjcwZDJmNTAyZmVlNDY7IGNvdW50cnk9Vk47IF9feWFzbWlkPTAuNjUyOTE3ODg3NzE3MTIyNzsgeWFfcG9wdXBfbG9naW5fZnJvbT1sb2dpbl9idDsgeWFfbG9naW5fbW9kZT1QaG9uZU51bTsgdWRiX2JpenRva2VuPUFRQ0lIYlpuQ195MmlxYWhvOGw2cGhQTEdvdms2MDFIdENHUllmOGxuTE1qeDVadUtDR2YyRWJkeFMzcEctZUhGUFgzeVpGQkFMMjNNQlE3LUVVaHR2RzRqN2M2aG50ZUJ1RkxuR0dfcUViWElBWTVuLVktLXN1dWx1eDBfMllybng2Z1lRdG5DZm9SUXlIVFBRY0dlLTU2dElzd2NQZFNDbkZIZ25nSkhjZGt1Mzh6UnJKUi02X2Z6Q2xhaWtQdEZsNTdiX253QlQ5RkE5X2lMRXFFbGNRODh1Zmhmd05oRUpEcDR0TkNzQmxFYmloTGRuXzF3OGxaUjczRTBwT3ZxRDcyY2FBS0Z1R2R5REp3ZVJWZjQ2Nkh5U2xvb21BRUdfMlJFdms0b1BDd3FlSzFqMkRUTmpKcDREekszYXp6YzJ5V013NjUxcXdTNVpVTzhJRmRqTG5LOyB1ZGJfY3JlZD1DakN0M28zS2htQ1pkeHBaSUpjQlhhR1VjZGU5aWErU2txelNGY2ZwOERnMW1WSHB1cTByTDcyWENRVDMzR1B2aGFmSmU5V002eGxEQ1dXbTlCRVc5ZURYZzZrYmM4eFVQVHNXUUlpVW5LOStvZz09OyB1ZGJfb3JpZ2luPTA7IHVkYl9zdGF0dXM9MTsgdWRiX3VpZD0xNjI5NTI2NTIzMTgyOyB1ZGJfdmVyc2lvbj0yLjE7IHl5dWlkPTE2Mjk1MjY1MjMxODI7IHZlcnNpb249Mi4xOyBiaXpUb2tlbj1BUUNJSGJabkNfeTJpcWFobzhsNnBoUExHb3ZrNjAxSHRDR1JZZjhsbkxNang1WnVLQ0dmMkViZHhTM3BHLWVIRlBYM3laRkJBTDIzTUJRNy1FVWh0dkc0ajdjNmhudGVCdUZMbkdHX3FFYlhJQVk1bi1ZLS1zdXVsdXgwXzJZcm54NmdZUXRuQ2ZvUlF5SFRQUWNHZS01NnRJc3djUGRTQ25GSGduZ0pIY2RrdTM4elJySlItNl9mekNsYWlrUHRGbDU3Yl9ud0JUOUZBOV9pTEVxRWxjUTg4dWZoZndOaEVKRHA0dE5Dc0JsRWJpaExkbl8xdzhsWlI3M0UwcE92cUQ3MmNhQUtGdUdkeURKd2VSVmY0NjZIeVNsb29tQUVHXzJSRXZrNG9QQ3dxZUsxajJEVE5qSnA0RHpLM2F6emMyeVdNdzY1MXF3UzVaVU84SUZkakxuSzsgdXNlcmlkPTE3NzcxMzMwNDsgdXNlck5hbWU9JUUwJUI5JTk2JURCJUEzJURCJTlDS2glQzMlQjNpOyB1ZGJVc2VySWQ9MTYyOTUyNjUyMzE4MjsgaXNBbmNob3I9MTsgYXZhdGFyVXJsPWh0dHBzOi8vc2VydmVyLWF2YXRhci5uaW1vc3RhdGljLnR2LzE2Mjk1MjY1MjMxODIvMjAyMjAzMDExNjQ2MTQzMzg5MzIwXzE2Mjk1MjY1MjMxODJfYXZhdGFyLnBuZzsgX195YW9sZHl5dWlkPTE2Mjk1MjY1MjMxODI7IF95YXNpZHM9X19yb290c2lkJTNEQzlCQUU3RjMwMTUwMDAwMTQyMzExMTAwMUFGNjlDODA7IHlhX2VpZD11bmRlZmluZWQ7IF9feWFvbGRjaWQ9OyBfZ2FfUTlGODY4WVg3Uj1HUzEuMS4xNjQ2MjI0MDExLjE3OC4wLjE2NDYyMjQwNjIuOTsgX2dhX1I4OEY4NFNIVzk9R1MxLjEuMTY0NjIzNTE3MC4xMTEuMS4xNjQ2MjM1MzAzLjYw');
const ws = new WebSocket('wss://a4345916-ws.master.live/');
ws.binaryType = 'arraybuffer';

const max_msg = 10;
const packages = {
	hello: [
		`AAMdAAEAiwAAAIsQAyw8QP9WBmxhdW5jaGYId3NMYXVuY2h9AABmCAABBgR0UmVxHQAAWQoDAAABe2dZfS4WIDBhNDc2OTRlNTAyMjRjNjEyMjEyNGE2MTRiNjExMTNkJhB3ZWJoNSYwLjAuMSZuaW1vNgxOSU1PJlZOJjEwNjZKBgAWACYANgBGAAsLjJgMqAwsNgBM`,
		`AAodAAEHBwMAAAF7Z1l9LhYQd2ViaDUmMC4wLjEmbmltbycAAAa1aHV5YV91YT13ZWJoNSYwLjAuMSZuaW1vOyBfX3lhbWlkX25ldz1DOTg3OUUyRDgyODAwMDAxOTMxRjdBNUMxNTk2RkZFMDsgX2dhPUdBMS4xLjE3NzY3ODc0MTcuMTYzMjM3OTQ3MzsgZ3VpZD0wYTQ3Njk0ZTUwMjI0YzYxMjIxMjRhNjE0YjYxMTEzZDsgdGhlbWU9MjsgaHV5YV91YT13ZWJoNSYwLjAuMSZuaW1vOyBsYW5nPTEwNjY7IGNjb3VudHJ5PVZOOyBjbGFuZz0xMDY2OyB1ZGJfZ3VpZGRhdGE9MGNiMDA4YzZmZGFiNDM0ZjhiYjcwZDJmNTAyZmVlNDY7IGNvdW50cnk9Vk47IF9feWFzbWlkPTAuNjUyOTE3ODg3NzE3MTIyNzsgeWFfcG9wdXBfbG9naW5fZnJvbT1sb2dpbl9idDsgeWFfbG9naW5fbW9kZT1QaG9uZU51bTsgdWRiX2JpenRva2VuPUFRQ0lIYlpuQ195MmlxYWhvOGw2cGhQTEdvdms2MDFIdENHUllmOGxuTE1qeDVadUtDR2YyRWJkeFMzcEctZUhGUFgzeVpGQkFMMjNNQlE3LUVVaHR2RzRqN2M2aG50ZUJ1RkxuR0dfcUViWElBWTVuLVktLXN1dWx1eDBfMllybng2Z1lRdG5DZm9SUXlIVFBRY0dlLTU2dElzd2NQZFNDbkZIZ25nSkhjZGt1Mzh6UnJKUi02X2Z6Q2xhaWtQdEZsNTdiX253QlQ5RkE5X2lMRXFFbGNRODh1Zmhmd05oRUpEcDR0TkNzQmxFYmloTGRuXzF3OGxaUjczRTBwT3ZxRDcyY2FBS0Z1R2R5REp3ZVJWZjQ2Nkh5U2xvb21BRUdfMlJFdms0b1BDd3FlSzFqMkRUTmpKcDREekszYXp6YzJ5V013NjUxcXdTNVpVTzhJRmRqTG5LOyB1ZGJfY3JlZD1DakN0M28zS2htQ1pkeHBaSUpjQlhhR1VjZGU5aWErU2txelNGY2ZwOERnMW1WSHB1cTByTDcyWENRVDMzR1B2aGFmSmU5V002eGxEQ1dXbTlCRVc5ZURYZzZrYmM4eFVQVHNXUUlpVW5LOStvZz09OyB1ZGJfb3JpZ2luPTA7IHVkYl9zdGF0dXM9MTsgdWRiX3VpZD0xNjI5NTI2NTIzMTgyOyB1ZGJfdmVyc2lvbj0yLjE7IHl5dWlkPTE2Mjk1MjY1MjMxODI7IHZlcnNpb249Mi4xOyBiaXpUb2tlbj1BUUNJSGJabkNfeTJpcWFobzhsNnBoUExHb3ZrNjAxSHRDR1JZZjhsbkxNang1WnVLQ0dmMkViZHhTM3BHLWVIRlBYM3laRkJBTDIzTUJRNy1FVWh0dkc0ajdjNmhudGVCdUZMbkdHX3FFYlhJQVk1bi1ZLS1zdXVsdXgwXzJZcm54NmdZUXRuQ2ZvUlF5SFRQUWNHZS01NnRJc3djUGRTQ25GSGduZ0pIY2RrdTM4elJySlItNl9mekNsYWlrUHRGbDU3Yl9ud0JUOUZBOV9pTEVxRWxjUTg4dWZoZndOaEVKRHA0dE5Dc0JsRWJpaExkbl8xdzhsWlI3M0UwcE92cUQ3MmNhQUtGdUdkeURKd2VSVmY0NjZIeVNsb29tQUVHXzJSRXZrNG9QQ3dxZUsxajJEVE5qSnA0RHpLM2F6emMyeVdNdzY1MXF3UzVaVU84SUZkakxuSzsgdXNlcmlkPTE3NzcxMzMwNDsgdXNlck5hbWU9JUUwJUI5JTk2JURCJUEzJURCJTlDS2glQzMlQjNpOyB1ZGJVc2VySWQ9MTYyOTUyNjUyMzE4MjsgaXNBbmNob3I9MTsgYXZhdGFyVXJsPWh0dHBzOi8vc2VydmVyLWF2YXRhci5uaW1vc3RhdGljLnR2LzE2Mjk1MjY1MjMxODIvMjAyMjAzMDExNjQ2MTQzMzg5MzIwXzE2Mjk1MjY1MjMxODJfYXZhdGFyLnBuZzsgX195YW9sZHl5dWlkPTE2Mjk1MjY1MjMxODI7IF95YXNpZHM9X19yb290c2lkJTNEQzlCQUU3RjMwMTUwMDAwMTQyMzExMTAwMUFGNjlDODA7IHlhX2VpZD11bmRlZmluZWQ7IF9feWFvbGRjaWQ9OyBfZ2FfUjg4Rjg0U0hXOT1HUzEuMS4xNjQ2MTQ3MDU1LjEwOS4xLjE2NDYxNDcwODEuMzQ7IF9nYV9ROUY4NjhZWDdSPUdTMS4xLjE2NDYxNDcwMjEuMTc3LjEuMTY0NjE0NzI2Ny40NzYgMGE0NzY5NGU1MDIyNGM2MTIyMTI0YTYxNGI2MTExM2RAAVYMTklNTyZWTiYxMDY2LDYATA==`,
	],
	info: [
		`UGFjb3RlIG9taXRpZG8=`,
		`UGFjb3RlIG9taXRpZG8=`,
		`AAMdAAECBAAAAgQQAyw8QANWBm5pbW91aWYLT25Vc2VyRXZlbnR9AAEB2wgAAQYEdFJlcR0AAQHNCgoDAAACN/6lECAWIDBhNDc2OTRmYTMzNTU1NWZhMTAyYmMxMGJkMTA0NWVhJwAAAVhBUUJvNTc2anpQbUREYW9Meldhb2haWDRZa2NJeTRRUWZDMTRwdGZvdG5fdkVCWWVDSzRZRUtEQVMxTy05LVhjMHF6NXNycW1zbk94MjJvWG5oeEdscE9COWdReGEtcFU2Z2tTZGRVZHF5Nm5kMUNicERtSFlHemd1Yl9HZlpxUnBLUFlwdUR6SjFlWFBsakp4eC1veER6bDl3YlBjVUtMUmN6UURLdlJCZ0NCQXZTa293VGNodG9EcExvb00ycjR3OXBPSmZJbmhiQUFDTEtLVWtOcWtZNWMwNGVUTVczdGVjTllOQ0gydndmN01qRlFTZ1JxTkQyNW5hTjFzR25GZi1HSmNsaTY3Z1BQc21KVkhuSlNfd0w4TFFwTWdjZ29ERUJSS2l6czI4NHB5TlJDZzFwZzdfZGF5dDhyQVNqT1c3c0Zpem96MW1TTHFtdzZFOFJxaXhBSzYQd2ViJjEuMC40Jm5pbW9UVkYAVgQxMDQ2ZgMxLjBwY4YCQlKWAKYAsAQLEAEjAAACN/6lECAzAAAAAXGHPMBAAQuMmAyoDCw2IWY1NzNjMjRlOGZlNzA1OTEtZjU3M2MyNGU4ZmU3MDU5MUw=`,
		`AAMdAAECBgAAAgYQAyw8QARWBm5pbW91aWYPT25Vc2VySGVhcnRCZWF0fQABAdkIAAEGBHRSZXEdAAEBywoKAwAAAjf+pRAgFiAwYTQ3Njk0ZmEzMzU1NTVmYTEwMmJjMTBiZDEwNDVlYScAAAFYQVFCbzU3Nmp6UG1ERGFvTHpXYW9oWlg0WWtjSXk0UVFmQzE0cHRmb3RuX3ZFQlllQ0s0WUVLREFTMU8tOS1YYzBxejVzcnFtc25PeDIyb1huaHhHbHBPQjlnUXhhLXBVNmdrU2RkVWRxeTZuZDFDYnBEbUhZR3pndWJfR2ZacVJwS1BZcHVEekoxZVhQbGpKeHgtb3hEemw5d2JQY1VLTFJjelFES3ZSQmdDQkF2U2tvd1RjaHRvRHBMb29NMnI0dzlwT0pmSW5oYkFBQ0xLS1VrTnFrWTVjMDRlVE1XM3RlY05ZTkNIMnZ3ZjdNakZRU2dScU5EMjVuYU4xc0duRmYtR0pjbGk2N2dQUHNtSlZIbkpTX3dMOExRcE1nY2dvREVCUktpenMyODRweU5SQ2cxcGc3X2RheXQ4ckFTak9XN3NGaXpvejFtU0xxbXc2RThScWl4QUs2EHdlYiYxLjAuNCZuaW1vVFZGAFYEMTA0NmYDMS4wcGOGAkJSlgCmALAECxMAAAI3/qUQICMAAAABcYc8wDABC4yYDKgMLDYhMTQ3NzgzMThhYjIwZDcxNC0xNDc3ODMxOGFiMjBkNzE0TA==`,
		`AAMdAAEAjAAAAIwQAyw8QP9WBmxhdW5jaGYMcXVlcnlIdHRwRG5zfQAAYwgAAQYEdFJlcR0AAFYKAwAAAjf+pRAgFhB3ZWJoNSYwLjAuMSZuaW1vKQACBhBjZG4ud3VwLmh1eWEuY29tBhJjZG53cy5hcGkuaHV5YS5jb202DE5JTU8mQlImMTA0NkYAC4yYDKgMLDYATA==`,
	],
	jackpot: [
		`AAMdAAEB9AAAAfQQAyw8QEZWBm5pbW91aWYOZ2V0SmFja1BvdEluZm99AAEByAgAAQYEdFJlcR0AAQG6CgoDAAABe2dZfS4WIDBhZDc2NzBlMmY2M2QxNjE3YTAxMzA5MTMxOTFiMmFjJwAAAVhBUUNFbVVIOHh2WlNqQ3BQY0xubkNpMUE3MWE4UjNoMURjazdEUGcwb1RlblV2RGVrMHdPYjZrYmVQeEpJQ1NyZU5SY25Vd1NyazJuS01TVzBSWUIyRHkyaGoxbWdaVmJmX3IwX2xNcXRkYlJzR3JXelFuY2diYjVVcmJ4U0dCQ2I1cjR5UGVBZm5XMDNjN0l1VkFaUzczMUpaRTVoRHgxU2ttc2ZFSlhxYXZjWXV2VVRZcVd0Q3RzWEsyMnVwT0J0NUpHU0wtSW5Xb21hLUVlS2lLdEdXSXAtc1R4cmh1VzhrbXBPMFJMUmdKQkNQMWUxek5wdUNQZUNpdnZWcXFpblh3czlhUW1zRldVQXZaVlljaWtLWnhLVWQ2WFhfZWN6Mm9VbmYwQnZQV0lqSWF0M3hxWHJ3UThWRmRlV085cmR3ZDFpbnpFQ3M0ZGYxU2NGUjVXTWZzTzYQd2ViJjEuMC40Jm5pbW9UVkYAVgQxMDMzZgMyLjFwY4YCVk6WAKYAsAULEQvAC4yYDKgMLDYhZmJlNDA3YjkwNTA4YWMzOS1mYmU0MDdiOTA1MDhhYzM5TA==`
	]
};
const type_package = {
	newMsg: "781d",
	newFollow: "009c",
	like: "7a1d",
	onLive: /[a-f0-9]{2}1d/,
	onLive2: "d91d",
	trevo: "281d"
};

let box_mensagens = [];
let cache_onLive = [];
let last_result = 0;

ws.onopen = function(evt) {
	loopPackage(packages.hello);
	console.log("Connected to server");
	setInterval(function() {
					loopPackage(packages.jackpot);
				}, 5000);
	setInterval(function() {
		document.getElementById("clitime").innerHTML = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Ho_Chi_Minh' });
	}, 1000);
}

ws.onclose = function(event) {
	console.log("WebSocket is closed now.");
};

ws.onerror = function(event) {
	console.error("WebSocket error observed:", event);
};
function send_data(data) {
	var srv = "https://pgsharpmail.silverwolfceh.repl.co/jpres"
	var http = new XMLHttpRequest;
	http.open("POST", srv, !0);
	http.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    http.setRequestHeader("Content-Type", "application/json");
	http.onreadystatechange = function() {
		if (4 == http.readyState && 200 == http.status) {
			var a = http.responseText;
			console.log("Send data " + a);
		} else if (4 == http.readyState) {
			console.log("Error " + http.status);
		}
    };
    http.send(data);
	console.log(data);
}

function log_data(jstype, jpval, win1 = "", win2 = "") {
	var obj = new Object();
	obj.time = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Ho_Chi_Minh' });
	obj.type = jstype;
	obj.winner1 = win1
	obj.winner2 = win2
	obj.jpvalue = jpval
	send_data(JSON.stringify(obj))
}
function log_jp_time(time, winner1, winner2, type = "small") {
	var mm = time.getMonth() + 1;
	var dd = time.getDate();
	var yyyy = time.getFullYear();
	var hh = time.getHours();
	var mmm = time.getMinutes();
	var ss = time.getSeconds();
	if(type == "small" ){
		var msg = dd + "-" + mm + "-" + yyyy + " " + hh + ":" + mmm + ":" + ss;
		console.log("Small JP at: " + msg);
	}
	
}

var pack_receiv = 0;
ws.onmessage = function(event) {
	pack_receiv += 1;

	const data = event.data;
	const dtView = new DataView(data);
	let package = readPackage(dtView, 0);
	
	// First time server communication
	if(package == '0004 1d00 006d 0000 006d 1003 2c3c 40ff') 
	{
		let intervalSendMsg = setInterval(function() {
			if(pack_receiv == 1) {
				console.log("Started JP thread");
				loopPackage(packages.info);
				
				pack_receiv = 0;
				clearInterval(intervalSendMsg);
				// Ping
				setInterval(function() {                
					ws.send(sendData(packages.info[3], true));
				}, 30000);
			}
	  }, 10);
	}
  
	// Check only jackpot response

  let header_pack = null;
  if(header_pack = package.match(/0004 1d00 0101 [0-9a-f]{2}00 0001 [0-9a-f]{2}10 032c 3c40/)) 
  {
	//console.log("Jackpot response");
	let hexresult = readPackage(dtView, 4).substr(-6, 6).replace(" ","");
	let curresult = parseInt(hexresult, 16);
	document.getElementById("jpval").innerHTML = curresult;
	if(curresult < last_result) {
		// Jackpot time
		//log_jp_time(new Date(), "0", "0");
		log_data("smalljp", curresult, "", "")
		
	} else {
		log_data("smallrealtime", curresult, "", "")
	}
	console.log("Delta: " + (curresult - last_result));
	last_result = curresult;
  }

};

function readPackage(package, block) {
	let maxByte = 16;
	let package_tmp = '';
	let i_pos = block > 0 ? (block * maxByte) : 0;
	
	for(let i=i_pos > 0 ? i_pos : 0, ii=0; ii<maxByte; i++) {
		ii++;
		if(i+1 >= package.byteLength) {
			break;
		}

		let hex = package.getUint8(i).toString(16);
		package_tmp += hex.length == 1 ? 0x0 + hex : hex;
	}

	return package_tmp.replace(/([0-9a-f]{4})/gi, '$1 ').trim();
}

function loopPackage(package) {
	for(let i=0; i<package.length; i++) {
		ws.send(sendData(package[i], true));
	}
}

function sendData(data, base64 = false) {
	const buf = new ArrayBuffer(data.length);
	const bufView = new Uint8Array(buf);
	
	if(base64) {
		data = decodeBase64(data);
	}

	for (let i=0, strLen=data.length; i < strLen; i++) {
		bufView[i] = data[i].charCodeAt();
	}
	
	return bufView;
}

function encodeBase64(data) {
	if (typeof btoa === "function") {
		return btoa(data);
	} else if (typeof Buffer === "function") {
		return Buffer.from(data, "utf-8").toString("base64");
	} else {
		throw new Error("Failed to determine the platform specific encoder");
	}
}

function decodeBase64(data) {
	if (typeof atob === "function") {
		return atob(data);
	} else if (typeof Buffer === "function") {
		return Buffer.from(data, "base64").toString("utf-8");
	} else {
		throw new Error("Failed to determine the platform specific decoder");
	}
}

function a2hex(str) {
  let arr = [];
  
  for (let i = 0, l = str.length; i < l; i ++) {
	let hex = Number(str.charCodeAt(i)).toString(16);
	arr.push(hex);
  }
  
  return arr.join('');
}

function hex2a(hexx) {
	let hex = hexx.toString("utf-8");
	let str = '';
	
	for (let i = 0; i < hex.length; i += 2) {
		str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
	}
	
	return decode_utf8(str);
}

function encode_utf8(s) {
	return unescape(encodeURIComponent(s));
}

function decode_utf8(s) {
	return decodeURIComponent(escape(s));
}