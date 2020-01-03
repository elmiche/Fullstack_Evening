// this is unit_converter redux

//Versions 1 - 4 complete

const readline = require('readline-sync');

const user_distance = readline.question('enter the distance: ');
let start_unit = readline.question('Now, enter the starting units(feet, miles, inches, meters, and kilometers): ');
let final_unit = readline.question('Now, what are we converting to (feet, miles, inches, meters, and kilometers): ');

// converts to meters
function convert(a,b,c) {
    new_unit = (a * b) / c
    return new_unit
}


units_m = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000,
    'yards': 0.9144,
    'inches': 0.0254,
   
}


console.log(convert(user_distance, units_m[start_unit], units_m[final_unit]));


