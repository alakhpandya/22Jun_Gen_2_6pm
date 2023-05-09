let add_btn = document.querySelector('button');
let input = document.querySelector('input');
let task_name = "";
let main = document.querySelector('.main');
let count = 0;
let task_container, task, hr, target;
let delete_btn_array = [];
let tasks_array = [];

add_btn.addEventListener('click', () => {
    task_name = input.value;
    if (count == 0){
        task_container = document.createElement('div');
        task_container.setAttribute('class', "task-container");
    }
    task = document.createElement('div');
    task.setAttribute('class', 'task');
    
    task.innerHTML = `<p>${task_name}</p>
    <div>
        <i class="fa-solid fa-pen task-options edit-icon"></i>
        <i class="fa-solid fa-check task-options check-icon"></i>
        <i class="fa-solid fa-trash task-options delete-icon"></i>
    </div>`
    if (count > 0){
        hr = document.createElement('hr');
        hr.setAttribute('class', 'task-seperator');
        task_container.appendChild(hr)
    }
    task_container.appendChild(task);
    if (count == 0){
        main.appendChild(task_container);
    }
    count++;
    tasks_array.push(task);
    delete_btn_array.push(task.lastElementChild.lastElementChild);
})

main.addEventListener('click', (e) => {
    // console.log(e.target);
    target = e.target;
    if (target.classList.contains('delete-icon')){
        task.remove();
    }
})