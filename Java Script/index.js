    //show out put in js 
    alert("Do not enter your password"); // pops up a alert box
    document.write("This is the same thing 2 <br>"); //writes in the page
    document.write("This is the same thing 2");
    console.log("Console output")// writes on the console
    // i can also write code going to SOURCES and then from the left SNIPPETS 



    //data type key word and variable
    var name = "Evan" ,age = 16.456;
    document.write("<br>"+ name+"<br>"+age);//concatenation



    //type casting
    console.log("type of age: "+typeof(age));
    age = toString(age);//string
    console.log("Converted to String: "+typeof(age));
    age = parseInt(age,10);//integer 10 is the base of decimal
    console.log("Converted to Integer: "+typeof(age));
    age = parseFloat(age);//float
    console.log("Converted to Float: "+typeof(age));
    age="16";
    console.log("Converted from String To Number: "+Number(age));//String to number
    console.log("Bool value in Number: "+Number(true));//true = 1 , false = 0
    age = 16.56234;
    console.log("Amnt of digits after point: "+age.toFixed(3));//amount of number after the point and it rounds the number
    console.log("type of age: "+age.toPrecision(3));//it shows exact number from the beginning 



    //js library functions
    var text = "This is js learning";
    var len = text.length;
    document.write(len);
    console.log("Js len lyb for text length: "+len);

    var name1 = prompt("Enter any text :");// user input
    document.write("<br>Then text is : "+name1)
    document.write("<br>nth char in a string: "+name1.charAt(1));
    //more functions
    //x.toUpperCase()
    //x.concat(concat with)
    //x.slice(startIndex,endIndex)




    //operator
    //Arithmetic -> +, -, *, /, %, **(power), ++, --
    //Assignment -> =, +=, -=, *=, /=, %=, 
    //Assignment -> <, <=, >, >=, ==, != ,===(value/data type)


    //IIFE (Immediately Invokeable Function Expressions )
    (function display(){
        console.log("This is IIFE");
    })();
    (function display(message){
        console.log(message);
    })("This is IIFE");

    //Function Expression
    var display2 = function display(){
        console.log("This is IIFE");
    }
    display2();

    var display2 = function display(message){
        console.log(message);
    }
    display2("This is Function Expression");


    let name2 = new Array();
    name2.push("name 1");
    name2.unshift("name 2");//first in push
    name2.length;
    name2.pop;//pop from last
    name2.shift;//pop from first

    //splice can add or remove element in/from array
    //x.splice(add,remove,value/s)  (and will remove from last)
    name2.splice(0,0,"");//adding
    //x.splice(start_index,end_index) to remove
    name2.splice(0,0)//remove


    //var x = x.slice(arr_index) will slice from the mentioned index
    //x.sort()//for alphabet

    //for number sort we have to create anonymous function
    //x.sort(function(a,b){
    //     return a-blur;
    // });

    //DIFFERENT MATH FUNCTION
    //sqrt, abs, sin/cos/tan, pow, floor, ceil, round, max(), random()*X + 1

    //DATE METHOD AND OBJ

    //DOM(Document Object Model)
    //


    