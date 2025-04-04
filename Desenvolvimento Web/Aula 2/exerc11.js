base = parseInt(prompt("Insira a base do triângulo"))
lado1 = parseInt(prompt("Insira o lado 1 do triângulo"))
lado2 = parseInt(prompt("Insira o lado 2 do triângulo"))
if(base == lado1 && lado1 == lado2){
    alert("Todos os lados iguais")
}else if(base != lado1 && lado1 != lado2 && base != lado2){
    alert("Todos os lados diferentes")
}else{
    alert("Dois lados iguais")
}