// Audioオブジェクトを作成
let ad = new Audio("cut_audio/0.wav");

ad.volume = 0.1; // ボリューム

// 再生ボタン
let elem_go = document.getElementById("go");
elem_go.addEventListener("click", function(){
	ad.play();  // 再生
	ad.loop = false; 
}, false);

// ストップボタン
let elem_stop = document.getElementById("stop");
elem_stop.addEventListener("click", function(){
	ad.pause();          // 一時停止
	ad.currentTime = 0;  // 次は最初（先頭）から再生する
}, false);