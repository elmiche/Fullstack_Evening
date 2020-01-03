


let countdown = document.querySelector('#countdown');
let c = 5;

setInterval(function() {

countdown.innerText = c;
if (c == 0) {
    let urls = ['http://www.google.com',
            'https://www.powells.com/',
            'http://www.reddit.com',
            'http://wwww.wikipedia.org',
            'https://ohshitgit.com/',
            'https://leafletjs.com/',
            'https://www.leafly.com/'
            ];
    let index = Math.floor(Math.random()*urls.length);

    window.location = urls[index];
}
c -= 1;
}, 1000);

   