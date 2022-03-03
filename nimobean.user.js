// ==UserScript==
// @name         NimoCoinChest
// @namespace    https://fb.com/wolf.xforce
// @version      0.1
// @description  Nimo bean chest auto bet
// @author       Vuu Van Tong
// @match        https://www.nimo.tv/mkt/act/super/coin_box_lottery
// @require      https://code.jquery.com/jquery-3.4.1.min.js
// @grant        GM_setValue
// @grant        GM_getValue
// @grant        GM_deleteValue
// ==/UserScript==
/* Change log */
// V0.1: First release version
// V0.2: Clean up and make a new algo (ôm 8 cầu)

var $ = window.jQuery;
var round = 0;
var count_down = 0;
var placed_bet = false;
var placed_bet_round = 0;
var latest_round = -1;
var bet_available = {
		"box0" : 13,
		"box1" : 14,
		"box2" : 15,
		"box3" : 16,
		"box4" : 17,
		"box5" : 18,
		"box6" : 19,
		"box7" : 20
};


// 23: 500, 24: 1000, 25: 5000, 26: 10000
var box_order = {
		"box0" : [26, 26, 26],      //30000
		"box1" : [26, 26, 26],      //30000
		"box2" : [26, 26, 26],      //30000
		"box3" : [26, 26, 26],      //30000
		"box4" : [26, 25],          //15000
		"box5" : [26],              //10000
		"box6" : [25, 24],          //6000
		"box7" : [24, 24, 24, 23]   //3500
	}

var box_value = {
	"box0" : 30000,
	"box1" : 30000,
	"box2" : 30000,
	"box3" : 30000,
	"box4" : 15000,
	"box5" : 10000,
	"box6" : 6000,
	"box7" : 3500,
}


var last_balance = 0;
var lost_in_row = 0;
var max_lost = 0;
var aimode = false;
var enable_bet = true;
var stop_flag = false;

var cbox_model = `
<div class="cbox" style="position: fixed; z-index: 9999; left : 10px; top: 20px; background-color: black; height: 30px; valign: middle">
<div>
	<input type="button" value="Pause" id="playpause" />
	<select id="coin_p_bet" style="width:60px; display:none">
		<option value="50">50</option>
		<option value="100">100</option>
		<option value="500">500</option>
		<option value="1000">1000</option>
	</select>
	<input type="text" id="curr_round" style="width: 60px" readonly/>
	<input type="text" id="balance" style="width: 80px; display: none" readonly></input>
	<span style="display:none"><input type="checkbox" id="aimode" class="btn" value="AIMODE"  alt="AI MODE AUTOMATIC" ><span style="color:white">Enable AI after losing </span>
	</input><input type="text" id="afterx" value="5" style="width:20px"/></span>
	</div>
	<div>
	<i id="log" style="color:white"></i>
	</div>
	<div>
	<i id="result" style="color:white"></i>
	</div>
</div>
`;

function register_cbox() {
	$("body").append(cbox_model);
	$("#playpause").click(function(e) {
		if(enable_bet) {
			enable_bet = false;
			$("#playpause").val("Play");
			log_w("Next action: stop");
		} else {
			enable_bet = true;
			$("#playpause").val("Pause");
			log_w("Next action: play");
		}
	})
	$("#aimode").on("change", function(e) {
		if ($("#aimode").is(":checked")) {
			aimode = true;
		} else {
			aimode = false;
		}
		log_w("Auto x2 enable? " + aimode);
   });
}

$(document).ready(function(){
	register_cbox();
	if(active_condition()) {
		main_func();
	}
})



function get_balance() {
	var balance = 0;
	try {
		var data = document.getElementsByClassName("nimo-box-lottery__account-bar-account-diamond")[0].children[0].textContent;
		var factor = 1;
		if(data.indexOf("k") != -1) {
			factor = 1000;
		}
		data = data.replace("k","");
		data = data.split(".");
		if(data.length > 1) {
			balance = parseInt(data[0]) * factor + parseInt(data[1])*factor/10;
		} else {
			balance = parseInt(data[0]) * factor;
		}
		return balance;
	} catch(error) {
		//setTimeout(get_balance, 2000)
	}
	return 0;
}

function get_box_id(box07) {
	return bet_available[box07];
}

function timedPromise(ms) {
	return new Promise(function(resolve) {
		setTimeout(function() {
			resolve();
		}, ms);
	})
}

function check_value(box07, expectedVal) {
	var idx = get_box_id(box07) - 13;
	var data = document.getElementsByClassName("nimo-box-lottery__sudoku-box__times n-fx-cc n-fx0")[idx].innerText;
	if(data == expectedVal) {
		return expectedVal;
	} else {
		return data;
	}

}
function click_and_delay(box07, betvalue) {
	return new Promise(function(resolve, reject) {
		set_coin_per_click(betvalue);
		var idx = get_box_id(box07);
		document.getElementsByTagName("picture")[idx].click();
		resolve();
	});
}
function bet(prom, box07, picid) {

}

function start_bet() {
	if(!enable_bet) {
		return false;
	}
	var box_internal_delay = 300;
	var box_ex_delay = 500;
    var start_time = new Date();
	timedPromise(100)
	.then(function() {return click_and_delay("box0", box_order["box0"][0])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box0", box_order["box0"][1])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box0", box_order["box0"][2])})
	.then(function() { return timedPromise(box_ex_delay) })

	.then(function() {return click_and_delay("box1", box_order["box1"][0])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box1", box_order["box1"][1])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box1", box_order["box1"][2])})
	.then(function() { return timedPromise(box_ex_delay) })

	.then(function() {return click_and_delay("box2", box_order["box2"][0])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box2", box_order["box2"][1])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box2", box_order["box2"][2])})
	.then(function() { return timedPromise(box_ex_delay) })

	.then(function() {return click_and_delay("box3", box_order["box3"][0])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box3", box_order["box3"][1])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box3", box_order["box3"][2])})
	.then(function() { return timedPromise(box_ex_delay) })

	.then(function() {return click_and_delay("box4", box_order["box4"][0])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box4", box_order["box4"][1])})
	.then(function() { return timedPromise(box_ex_delay) })

	.then(function() {return click_and_delay("box5", box_order["box5"][0])})
	.then(function() { return timedPromise(box_ex_delay) })

	.then(function() {return click_and_delay("box6", box_order["box6"][0])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box6", box_order["box6"][1])})
	.then(function() { return timedPromise(box_ex_delay) })

	.then(function() {return click_and_delay("box7", box_order["box7"][0])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box7", box_order["box7"][1])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box7", box_order["box7"][2])})
	.then(function() { return timedPromise(box_internal_delay) })
	.then(function() {return click_and_delay("box7", box_order["box7"][3])})
    .then(function() { return calculate_time(start_time)})
	.then(function() { return timedPromise(box_ex_delay) })
    .then(function() { return check_betted_val })
	.catch(err => console.log(err));

}

function check_betted_val() {
    return new Promise(function(resolve, reject) {
		for(var i = 0; i < 8; i++)
        {
            var box_num = "box" + i;
            if(check_value(box_num, box_value[box_num]) != box_value[box_num]) {
                console.log("Please check " + box_num);
                if(stop_flag) {
                    enable_bet = false;
                }
            }
        }
		resolve();
	});
}

function calculate_time(start_time) {
	return new Promise(function(resolve, reject) {
		var end_time = new Date();
        log_w("Total time needed: " + (end_time - start_time)/1000);
		resolve();
	});
}

function set_coin_per_click(coin_value) {
	document.getElementsByTagName("picture")[coin_value].click();
}


function update_count_down_and_round() {
	count_down = document.getElementsByClassName("nimo-box-lottery__countdown__item n-fx0 n-fx-bc")[1].firstElementChild.innerText;
	count_down = count_down.split("s")[0];
	latest_round = document.getElementsByClassName("nimo-box-lottery__countdown__item n-fx0 n-fx-bc")[0].firstElementChild.innerText;
}

function log_result(state) {
	var x = document.getElementById("result");
	var msg = "";
	if(state == "WIN") {
		x.style.color = "green";
		msg = "Congrat!";
	} else if(state == "LOSE") {
		x.style.color = "red";
		msg = "You lost " + lost_in_row + " times cont. (Max: " + max_lost + ")";
	} else {
		x.style.color = "white";
		msg = "Not win not lose, do you enable me?";
	}
	x.innerHTML = msg;
}
function check_win_lose() {
	try {
		var imglink = document.getElementsByClassName("nimo-image nimo-box-lottery__box__img n-fx0")[0].children[0].children[0].getAttribute("srcSet");
		if(imglink.indexOf("box0.") != -1 || imglink.indexOf("box1.") != -1 || imglink.indexOf("box2.") != -1 || imglink.indexOf("box3.") != -1) {
			lost_in_row = lost_in_row + 1;
			// log_w("LOOOOOSE");
			// log_result("LOSE");
		} else {
			if(max_lost < lost_in_row) {
				max_lost = lost_in_row;
			}
			lost_in_row = 0;
			// log_w("WINNNNN");
			// log_result("WIN");
		}
	} catch (error) {

	}
	last_balance = get_balance();
	document.getElementById("balance").value=last_balance;
}
function check_end_round() {
	var cur = document.getElementById("curr_round").value;
	if(latest_round == cur) {
		//log_w("Round: "+ latest_round + " Remaining: " + count_down);
	} else {
		check_win_lose();
		document.getElementById("curr_round").value = latest_round;
	}
	if(last_balance == 0) {
		last_balance = get_balance();
	}
}
function check_ready_and_play() {
	check_end_round();
	if(placed_bet_round == latest_round && placed_bet) {

	} else {
		if(count_down > 10 && !placed_bet) {
			placed_bet = true;
			log_w("Start betting");
			start_bet();
			placed_bet_round = latest_round;
		} else if (count_down <= 10 || placed_bet) {
			placed_bet = false;
			placed_bet_round = latest_round;
		} else {
			log_w("Hhhhm");
			placed_bet = false;
			placed_bet_round = latest_round;
		}
	}
    setTimeout(check_ready_and_play, 1000);
}

function active_condition() {
	return true;
}

function log_w(msg, msg1 = "") {

	var out = "" + msg;
	if(msg1 != "") {
		out = out + " [" + msg1 + "]";
	}
	document.getElementById("log").innerHTML = out;
	console.log(out);
}

function main_func() {
	log_w("Started to obsever");
	setInterval(update_count_down_and_round, 1000);
	check_ready_and_play();
}
