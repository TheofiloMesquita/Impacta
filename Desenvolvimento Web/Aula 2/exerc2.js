idade = parseInt(prompt("Insira sua idade:"))
if (idade < 16){
    alert("Não pode votar");
} else if (idade < 18 || idade > 70){
    alert("Voto Opcional");
} else{
    alert("Voto Obrigatório");
}