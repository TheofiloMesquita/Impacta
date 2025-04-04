let numeros = [10,20,30,40,50]
console.log(numeros[2])
//numeros.push(60)
numeros[numeros.length] = 60
console.log(numeros)
for (let i = 0; i < numeros.length; i++){
    console.log(numeros[i])
}
//numeros.shift()

novosNumeros = []
for(let i = 1; i < numeros.length; i++){
    novosNumeros[i - 1] = numeros[i]
}
console.log(novosNumeros)

for (let i = 0; i < numeros.length; i++) {
    if(numeros[i] == 10){
        for (let j = 0; j < numeros.length; j++) {
            numeros[j] = numeros[j+1]
        }
        //numeros.pop()
        numeros.length -=1
    }   
}
console.log(numeros)

frutas = ["laranja", "mamao", "abacaxi", "pera", "uva"]
for(let i = 0; i < frutas.length; i++){
    console.log(frutas[i])
}

lista = [2,5,8,10,15,21]
function pares(num) {
    for(let i = 0; i < lista.length; i++){
        
    }
}
console.log(lista.fil)