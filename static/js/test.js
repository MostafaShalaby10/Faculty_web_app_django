var one = document.getElementById('one')
var two = document.getElementById('two')
var three = document.getElementById('three')
var four = document.getElementById('four')

var current = 1 

function next()
{
    switch(current) {
        case 1: 
        one.removeAttribute("class") ; 
        one.setAttribute("class" , "hide")
        two.removeAttribute("class")
        two.setAttribute("class" , "apper")
        current = 2 ; 
        break;

        case 2:
        two.removeAttribute("class") ; 
        two.setAttribute("class" , "hide")
        three.removeAttribute("class")
        three.setAttribute("class" , "apper")
        current = 3 ; 
        break;
        
        case 3: 
        three.removeAttribute("class") ; 
        three.setAttribute("class" , "hide")
        four.removeAttribute("class")
        four.setAttribute("class" , "apper")
        current = 4 ; 
        break;

        case 4:
        four.removeAttribute("class") ; 
        four.setAttribute("class" , "hide")
        one.removeAttribute("class")
        one.setAttribute("class" , "apper")
        current = 1 ; 
        break;
    }
}

function previous()
{
    switch(current) {
        case 1: 
        one.removeAttribute("class") ; 
        one.setAttribute("class" , "hide")
        four.removeAttribute("class")
        four.setAttribute("class" , "apper")
        current = 4 ; 
        break;

        case 2:
        two.removeAttribute("class") ; 
        two.setAttribute("class" , "hide")
        one.removeAttribute("class")
        one.setAttribute("class" , "apper")
        current = 1 ; 
        break;
            
        case 3: 
        three.removeAttribute("class") ; 
        three.setAttribute("class" , "hide")
        two.removeAttribute("class")
        two.setAttribute("class" , "apper")
        current = 2 ; 
        break;

        case 4:
        four.removeAttribute("class") ; 
        four.setAttribute("class" , "hide")
        three.removeAttribute("class")
        three.setAttribute("class" , "apper")
        current = 3 ; 
        break;
    }
}