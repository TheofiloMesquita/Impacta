numero = parseInt(prompt("Informe uma Categoria:"));
num1 = "R$ 10,00";
num2 = "R$ 20,00";
num3 = "R$ 30,00";
invalido = "Categoria não encontrada";
if(numero == 1){
    alert("O preço do produto é" + num1)
} else if(numero == 2){
    alert("O preço do produto é" + num2)
} else if(numero == 3){
    alert("O preço do produto é" + num3)
} else{
    alert("Categoria não encontrada")
}