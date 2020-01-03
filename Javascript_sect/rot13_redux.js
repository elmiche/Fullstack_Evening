//lab 13 rot13 

const readline = require('readline-sync');

let rotation = parseInt(readline.question('enter the rotation: '));
const answer = readline.question('enter a string: ');

let lowerCase = 'abcdefghijklmnopqrstuvwxyz';
    lowerCase = lowerCase.split('')
// let rotCase = 'nopqrstuvwxyzabcdefghijklm';
// let upperCase = lowerCase.toUpperCase();
// how do I include rotCase in the uppercase as well? or do I even need upperCase at all? 



user_rot = '';



if (rotation < 0){
    // let revlowerCase = lowerCase;
    lowerCase = lowerCase.reverse();
    lowerCase = lowerCase.join('');
    console.log(lowerCase);
}

// //callback as demo'ed by
// function rot_item( item, index) {
//     console.log(`index: ${index} value: ${item}`);
// }



for (i = 0; i < answer.length; i++) {
    let index = lowerCase.indexOf(answer[i]);
    // console.log(answer[i]) ------- use to add characters !@#$%^&*&^%$#$%^&* (do an if statement, check if it's in lowercase, if not, add to empty string)
    user_rot += lowerCase[(index + Math.abs(rotation)) %26];
    console.log(user_rot)
}


//TODO: add characters