/*
Coding like poetry should be short and concise. ― Santosh Kalwar
It’s not a bug; it’s an undocumented feature. ― Anonymous
First, solve the problem. Then, write the code. – John Johnson
Code is like humor. When you have to explain it, it’s bad. – Cory House
Make it work, make it right, make it fast. – Kent Beck
Clean code always looks like it was written by someone who cares. — Robert C. Martin
Of course, bad code can be cleaned up. But it’s very expensive.” — Robert C. Martin

Programming is the art of algorithm design and the craft of debugging errant code. – Ellen Ullman
Programming today is a race between software engineers striving to build bigger and better idiot-proof programs and the Universe trying to produce bigger and better idiots. So far, the Universe is winning. ― Rick Cook
Any fool can write code that a computer can understand. Good programmers write code that humans can understand. ― Martin Fowler
Experience is the name everyone gives to their mistakes. – Oscar Wilde
Programming is the art of telling another human being what one wants the computer to do. ― Donald Ervin Knuth
Confusion is part of programming. ― Felienne Hermans
No matter which field of work you want to go in, it is of great importance to learn at least one programming language. ― Ram Ray
*/

/*
strategy - 1: 
let
quote_list = ["q0", "q1", "q2", "q3", "q4"],
author_list = ["a0", "a1", "a2", "a3", "a4"]

index = Math.floor(Math.random() * 5);

console.log(quote_list[index], author_list[index]);


strategy - 2:
let 
quotes = [
    {quote: "q0", author : "a0"},
    {quote: "q1", author : "a1"},
    {quote: "q2", author : "a2"},
    {quote: "q3", author : "a3"},
    {quote: "q4", author : "a4"}
],

index = Math.floor(Math.random() * 5),
q = quotes[index]["quote"],
a = quotes[index]["author"];

console.log(q, a);
*/

const quotes = [
    {
        quote: "Coding like poetry should be short and concise.",
        author : "Santosh Kalwar"
    },
    {
        quote: "No matter which field of work you want to go in, it is of great importance to learn at least one programming language.",
        author : "Ram Ray"
    },
    {
        quote: "Q",
        author : "A"
    },
    {
        quote: "Q",
        author : "A"
    },
    {
        quote: "Q",
        author : "A"
    },
    {
        quote: "Q",
        author : "A"
    },
    {
        quote: "Q",
        author : "A"
    },
    {
        quote: "Q",
        author : "A"
    },
    {
        quote: "Q",
        author : "A"
    },
    {
        quote: "Q",
        author : "A"
    },
    {
        quote: "Q",
        author : "A"
    },
    {
        quote: "Q",
        author : "A"
    },
    {
        quote: "Q",
        author : "A"
    },
    {
        quote: "Q",
        author : "A"
    }
];

let index, q, a;
const btn = document.getElementById('btn');
const quo = document.getElementById('quote1');
const auth = document.getElementById('author1');

btn.addEventListener('click', () => {
    index = Math.floor(Math.random() * 5),
    q = quotes[index]["quote"],
    a = quotes[index]["author"];
    quo.innerText = q;
    auth.innerText = a;
})