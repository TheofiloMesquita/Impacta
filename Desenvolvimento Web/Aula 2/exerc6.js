num1 = parseInt(prompt("Digite o primeiro numero"));
num2 = parseInt(prompt("Digite o segundo numero"));
num3 = parseInt(prompt("Digite o terceiro numero"));

if(num1>num2){
    if(num1>num3){
        alert("o 1º numero é o maior")
    } else{
        alert("O 3º numero é o maior")
    }
} else if(num2>num3){
    alert("O 2º numero é o maior")
} else{
    alert("O 3º numero é o maior")
}