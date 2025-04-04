numero = parseInt(prompt("Insira um numero:"))
if(numero % 3 == 0 && numero % 5 == 0){
    alert("FizzBuzz")
}else if(numero % 3 == 0){
    alert("Fizz")
}else{
    alert("Buzz")
}