// another javascript lab

// button event

let bt = document.querySelector('.task-submit');


bt.addEventListener('click', () => {
    // alert('Task added')
    addnewtask()
})

// let submitTask = () => {
// userInput = document.querySelector('.task-input').value
// console.log(userInput)

// }



let addnewtask = () => {
    let newDivclass = ['task-1-incompletes'];
    userInput = document.querySelector('.task-input').value
    let newDiv = document.createElement('div')
    newDiv.classList = newDivclass
    newDiv.innerText = userInput
    document.querySelector('.incomplete-task-list').append(newDiv)
    
}
let incompleteItems = document.querySelector('.incomplete-task-list')

incompleteItems.addEventListener('click', event => {
    event.target.remove('task-1-incompletes')
    // event.target.add('task-2-completes');
    document.querySelector('.completed-task-list').append(event.target);

    console.log(event.target)
})

let rmCompleted = document.querySelector('.completed-task-list')

rmCompleted.addEventListener('click', event => {
    event.target.remove('task-2-completes')
    
})
