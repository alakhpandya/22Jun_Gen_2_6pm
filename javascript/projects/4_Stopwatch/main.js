const play_pause_btn = document.getElementById('btn-1');
const reset_btn = document.getElementById('btn-2');
const time_box = document.querySelector('.time-box');
let ms = 0, s = 0, m = 0, h = 0;
let timer = null, playing = false;


// use of setInterval
/*
var i = 0;
const stopwatch = () => {
    console.log(i);
    i++;
}

stopwatch();
stopwatch();
setInterval(stopwatch, 1000);
*/

const stopwatch = () => {
    ms++;
    // console.log(ms);
    if (ms == 100){
        ms = 0;
        s++;
        if (s == 60){
            s = 0;
            m++;
            if (m == 60){
                m = 0;
                h++;
            }
        }
    }
    time_box.innerHTML = `<span id="hour">${h.toString().padStart(2, '0')}</span>
    <span>:</span>
    <span id="min">${m.toString().padStart(2, '0')}</span>
    <span>:</span>
    <span id="sec">${s.toString().padStart(2, '0')}</span>
    <span>:</span>
    <span id="msec">${ms.toString().padStart(3, '0')}</span>`
}

play_pause_btn.addEventListener('click', () => {
    if (!playing){
        timer = setInterval(stopwatch, 10);
        playing = true;
        play_pause_btn.innerHTML = `<i class="fa-solid fa-pause">`;
    }
    else{
        clearInterval(timer);
        playing = false;
        play_pause_btn.innerHTML = `<i class="fa-solid fa-play">`;
    }
});

reset_btn.addEventListener('click', () => {
    ms = 0, s = 0, m = 0, h = 0; 
    time_box.innerHTML = `<span id="hour">${h.toString().padStart(2, '0')}</span>
    <span>:</span>
    <span id="min">${m.toString().padStart(2, '0')}</span>
    <span>:</span>
    <span id="sec">${s.toString().padStart(2, '0')}</span>
    <span>:</span>
    <span id="msec">${ms.toString().padStart(3, '0')}</span>`
})