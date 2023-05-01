let show_modal = document.querySelector('.box-2')
let close_modal = document.querySelector('button')
let modal = document.querySelector('.box-1')
let body = document.querySelector('body')
let show_modal_btn = document.getElementById('show-modal-btn')

show_modal.addEventListener('click', () => {
    modal.style.display = "block";
})

close_modal.addEventListener('click', () => {
    modal.style.display = "none";
})

body.addEventListener('click', (e) => {
    if (e.target != modal && e.target != show_modal_btn){
        modal.style.display = "none";
    }
})