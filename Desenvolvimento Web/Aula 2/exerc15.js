temp = parseInt(prompt("escolha um numero"));
conversao = prompt("Agora escolha C para Celsius e F para Fahrenheit");
Celsius = (temp - 32) * 5 / 9
Fahrenheit = (temp * 9 / 5) + 32
if(conversao == "C" || conversao == "c"){
    alert(temp + " equivale a " + Celsius + "º")
} else if(conversao == "F" || conversao == "f"){
    alert(temp + " equivale a " + Fahrenheit + "º")
} else{
    alert("Respeite as regras!")
}