// this is javascript lab 1 pain redux



function gen_6nums() {
    low = 1;
    high = 99;
    const ticket = [];
    for (let i = 0; i < 6; i++)
        ticket.push(Math.floor(Math.random() * (1 + high - low)) + low); //IDK
    return ticket;
}

//compare tickets
function match_tracker(gen_6nums) {
    let matches = 0
    let user_ticket = gen_6nums();
    let winning_ticket = gen_6nums();
        for (let i=0; i<6; ++i){
            // console.log(user_ticket[i])
            if (user_ticket[i] == winning_ticket[i])
            matches++;
        }
        return matches
}

// console.log(match_tracker(gen_6nums))


function main(){

    const rewards = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000,
    }
    
  //set everything equl to zero before taking account
    let expenses = 0;
    let rounds = 0;
    let winnings = 0;



    while (rounds <= 99999){
        expenses +=2;
        winnings += rewards[match_tracker(gen_6nums)]; 
        rounds ++;
    }
    console.log(`winnings:${winnings} \nexpenses: ${expenses}\nroi: ${(winnings - expenses)/ expenses}`)
}

main()


