idade = parseInt(prompt("Insira sua idade"))
temAutorizacao = prompt("Tem autorização?")
if(idade >= 18 || temAutorizacao == "sim"){
    alert("Pode acessar")
} else{
    alert("Não pode acessar")
}