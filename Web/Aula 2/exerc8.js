idade = parseInt(prompt9("Insira sua idade:"));
if(idade<5 && idade>65){
    alert("Gratuito")
} else if(idade<=12){
    alert("Meia Tarifa")
} else{
    alert("Tarifa Completa")
}