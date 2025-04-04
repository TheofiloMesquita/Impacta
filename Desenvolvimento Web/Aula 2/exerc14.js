nome = prompt("Insira um nome:");
letra = prompt("Insira uma letra:");
if(letra == nome[0]){
    alert("O nome " + nome + " começa com a letra " + letra);
} else{
    alert("O nome " + nome + " não inicia com a letra " + letra);
}