let add_btn = document.querySelector('button');
let input = document.querySelector('input');
let task_name = "";
let main = document.querySelector('.main');
var count = 0;
let task_container, task, hr, target;
let delete_btn_array = [], check_btn_array = [], edit_btn_array = [];
let tasks_array = [];
var delete_icon, check_icon, edit_icon, index, new_text;

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
        tasks_array[count-1].appendChild(hr)
    }
    task_container.appendChild(task);
    if (count == 0){
        main.appendChild(task_container);
    }
    count++;
    tasks_array.push(task);
    delete_icon = document.getElementsByClassName('delete-icon');
    delete_btn_array.push(delete_icon[count-1]);
    
    check_icon = document.getElementsByClassName('check-icon');
    check_btn_array.push(check_icon[count-1]);
    
    edit_icon = document.getElementsByClassName('edit-icon');
    edit_btn_array.push(edit_icon[count-1]);
    console.log(tasks_array);
    // console.log(delete_btn_array);

    input.value = "";
})

main.addEventListener('click', (e) => {
    // console.log(e.target);
    target = e.target;
    if (target.classList.contains('delete-icon')){
        index = delete_btn_array.indexOf(target);
        tasks_array[index].remove();
        count--;
        if (count == 0){
            task_container.remove();
        }
        if (count == 1){
            tasks_array[0].lastElementChild.remove();
        }
    }
    if (target.classList.contains('check-icon')){
        index = check_btn_array.indexOf(target);
        tasks_array[index].firstElementChild.style.textDecoration = 'line-through';
    }
    if (target.classList.contains('edit-icon')){
        index = edit_btn_array.indexOf(target);
        new_text = prompt("Modified task:");
        tasks_array[index].firstElementChild.innerText = new_text;
    }
})