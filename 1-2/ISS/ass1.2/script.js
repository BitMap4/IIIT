var commands = {
    help: `<span class="red">help</span> - list of commands<br>
    <span class="red">about</span> - about me<br>
    <span class="red">education</span> - my educational background<br>
    <span class="red">achievements</span> - my achievements<br>
    <span class="red">skills</span> - my skills<br>
    <span class="red">blog</span> - link to my blog<br>`,
    about: `Undergrad at IIIT Hyderabad. Born in 2006 in UP, India.<br>
    `,
    education: `Currently pursuing <span class="red">CLD</span> (Dual degree: Btech in Computer Science 
    and MS by Research in Computational Linguistics) at IIIT Hyderabad.
    I finished my schooling from <span class="red">Amity International School</span> and 
    studied in <span class="red">DPS Indirapuram</span> till class 11.`,
    achievements: `<span class="red">JEE Mains 2023</span> - AIR 4230<br>
    <span class="red">JEE Advanced 2023</span> - AIR 5244<br>
    <span class="red">IOQM 2022</span> - Qualified<br>
    <span class="red">IOQM 2019</span> - Qualified<br>
    <span class="red">UGEE 2023</span> - AIR 93<br>`,
    skills: `<span class="red">Python</span>, <span class="red">C</span>, <span class="red">JavaScript</span>, <span class="red">HTML</span>, <span class="red">CSS</span>, <span class="red">Node.js</span>, <span class="red">SQL</span>`,
    blog: `Visit my <a href="blog/index.html" target="_blank"><span class="red">blog</span></a><br>
    Some of my recent posts:<br>
    <a href="blog/posts/1.html">First post</a><br>
    <a href="blog/posts/2.html">Second post</a>`
}
var count = 1;
var terminal = document.getElementById('terminal');
var input = document.getElementById(`typed-${count}`);
var themeToggle = document.getElementById('theme-toggle');
var current = document.getElementById('current');
var inputs = document.getElementsByTagName('input');
var header = document.getElementById('header');
var pfp = document.getElementById('pfp');
var navbar = document.getElementById('navbar');
var Name = document.getElementById('name');
var pages = document.getElementById('pages');

// var text = 'ABHYUDIT SINGH';
// Name.innerHTML = '';
// var i = 0;
// const addCharacter = () => {
//     if (i < text.length) {
//         Name.innerHTML += text[i];
//         i++;
//     } else clearInterval(intervalId);
// }
// const intervalId = setInterval(addCharacter, 100);

if (input) terminal.addEventListener('click', function(){
    input.focus();
});

// input.style.width = `${terminal.offsetWidth - 170}px`;
// input.focus();
const execute = (command) => {
    if (window.location.href.includes('blog')) window.location.href = '/index.html';
    input.disabled = true;
    if (command == null) {command = input.value;}
    else {input.value = command}
    var output = document.createElement('div');
    output.classList.toggle('output');
    output.id = `output-${count}`;
    output.innerHTML = (commands[command])?commands[command]:`${command}: command not found`;
    terminal.appendChild(output);
    count++;
    var newInput = document.createElement('div');
    newInput.classList.toggle('command');
    newInput.id = `command-${count}`;
    newInput.innerHTML = `<span class="user">abhyudit@IIIT</span>:<span class="pwd">~</span>$ <input id="typed-${count}"></input>`;
    terminal.appendChild(newInput);
    input = document.getElementById(`typed-${count}`);
    input.style.width = `${terminal.offsetWidth - 210}px`;
    input.focus();
}
window.addEventListener('keyup', (e) => {
    if(e.key === 'Enter'){execute(null)}
});

const toggle = () => {
    if(current.innerHTML === '🌙'){
        current.innerHTML = '☀️';
        themeToggle.style.justifyContent = 'flex-end';
        // modify root variables
        document.documentElement.style.setProperty('--accent', '#B8C0E0');
        document.documentElement.style.setProperty('--text', '#20111B');
        document.documentElement.style.setProperty('--accent-text', '#3A94C5');
    } else {
        current.innerHTML = '🌙';
        themeToggle.style.justifyContent = 'flex-start';
        // modify root variables
        document.documentElement.style.setProperty('--accent', '#282a36');
        document.documentElement.style.setProperty('--text', '#f8f8f2');
        document.documentElement.style.setProperty('--accent-text', '#8BE9FD');
    }
}
themeToggle.addEventListener('click', toggle);

const transformHeader = () => {
    if(header.getBoundingClientRect().top <= 20 || 'blog' in window.URL) {
        header.style.width = '100vw';
        // delete pfp
        if (header.children[0] === pfp) {
            header.removeChild(pfp);
        }
        // insert pfp in #navbar at the beginning if img not in navbar
        if (navbar.children[0] !== pfp) {
            navbar.insertBefore(pfp, navbar.children[0]);
        }
        navbar.style.display = 'flex';
        navbar.style.flexDirection = 'row';
        Name.style.fontSize = '18px';
        header.style.backgroundColor = 'var(--accent)';
        header.style.borderBottom = '1px solid var(--accent-text)';
        header.style.position = 'fixed';
        header.style.top = `0`;
        header.style.paddingTop = `20px`;
        if (terminal) terminal.style.paddingTop = `${header.offsetHeight}px`
        pages.style.display = 'flex';
        if (header.classList[0] == 'not-navbar') {
            header.classList.toggle('not-navbar');
            header.classList.toggle('navbar');
        }
    }
}
// detect when the header is at the top, but it may get to the top without scrolling
const observer = setInterval(transformHeader, 100);
// stop the observer when the page is close
window.addEventListener('beforeunload', function(){
    clearInterval(observer);
});