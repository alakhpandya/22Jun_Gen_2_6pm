/*
let btn = document.createElement('button')
let box = document.querySelector('.box')

btn.innerText = 'John Wick'


let first_btn = document.querySelector('button')
let classes = first_btn.getAttribute('class')


box.appendChild(btn)
// console.log(box.getAttribute('id'))
// console.log(box.getAttribute('class'))

// btn.setAttribute('class', 'movie-name')
btn.setAttribute('class', classes)
*/

/*
let hp = document.getElementsByClassName('movie-name')[2]
// hp.setAttribute('class', 'favorite')
// console.log(hp.classList)
hp.classList.add('favorite')
// console.log(hp.classList)

console.log(hp.classList.contains('movie-name'))

hp.classList.remove('movie-name')


let first_btn = document.querySelector('button')
console.log(first_btn.textContent)

first_btn.remove()
*/


// Traversing in the DOM

// Difference between node & element
// let main = document.querySelector('.main')
// console.log(main.childNodes.length)
// console.log(main.childNodes)
// console.log(main.childElementCount);
// console.log(main.children);

// traversing through parent
let hp = document.getElementsByClassName('movie-name')[2]
// console.log(hp.parentElement.parentElement.parentElement.parentElement)
// console.log(hp.parentNode.parentNode.parentNode.parentNode.parentNode)


// traversing through sibling
console.log(hp.previousElementSibling.previousElementSibling)
console.log(hp.previousSibling)

// traversing through children
console.log(hp.firstChild)
console.log(hp.firstElementChild)
console.log(hp.lastChild);
console.log(hp.lastElementChild);