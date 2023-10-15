//COM

//select element by ID
let hName = document.getElementById("heading1");
hName.innerHTML="hello";

//select element by tag name
let hName2 = document.getElementsByTagName("h2")[0];
hName2.innerHTML = "h22"

//select element by class name
let hName3 = document.getElementsByClassName("heading3")[0];
hName3.innerHTML = "h3"

// we can do all the works by querySelector
//for id "#xxx"
//for class ".xxx"
//for tag "tang name"
document.querySelector("#pid").innerHTML = "this one is short";


let textBoxValue = 0;
document.getElementById("myButton").onclick = function(){
    textBoxValue = document.getElementById("myText").value;
    console.log(textBoxValue);
}

let number;
document.getElementById("decrease").onclick = function(){
    textBoxValue -= 1;
    document.getElementById("counterLabel").innerHTML = textBoxValue;
}
document.getElementById("reset").onclick = function(){
    textBoxValue = 0;
    document.getElementById("counterLabel").innerHTML = textBoxValue;
}
document.getElementById("increase").onclick = function(){
    textBoxValue += 1;
    document.getElementById("counterLabel").innerHTML = textBoxValue;
}