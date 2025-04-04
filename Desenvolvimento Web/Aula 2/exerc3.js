ano = parseInt(prompt("Digite o ano:"));
if((ano % 4 == 0 && ano % 100 != 0)||(ano % 400 == 0)){
    alert("O ano é bissexto")
} else{
    alert("O ano não é bissexto")
}