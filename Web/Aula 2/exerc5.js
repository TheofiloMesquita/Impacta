media = parseFloat(prompt("Insira sua media:"))
if(media >= 7){
    alert("Aprovado")
} else if(media > 4 && media < 7){
    alert("Recuperação")
} else{
    alert("reprovado")
}