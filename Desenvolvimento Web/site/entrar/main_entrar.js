// Garantindo que tudo foi carregado no html
document.addEventListener('DOMContentLoaded', function() {
    let senha = document.getElementById("senha");
    let iconSenha = document.getElementById("icon-senha");
    
    function mostrar_senha() {
        if (senha.type === "password") {
            senha.setAttribute("type", "text");
            iconSenha.src = "../imgs/hide.png";
        } else {
            senha.setAttribute("type", "password");
            iconSenha.src = "../imgs/show.png";
        }
    }
    
    // Tornar a função acessível globalmente se necessário
    window.mostrar_senha = mostrar_senha;
});

async function entrar() {

    // puxando os dados do html
    let email = document.getElementById("email").value
    let senha = document.getElementById("senha").value

    // verificando se o email e senha estão preenchidos
    if(email == "" || senha == ""){
        document.getElementById("erro").innerHTML = "Preencha todos os campos"
        document.getElementById("erro").style.color = 'red'
        document.getElementById("email").style.borderColor = 'red'
        document.getElementById("senha").style.borderColor = 'red'
        return

    // verificando se o email foi inserido no formato válido
    } else if (email.indexOf("@") == -1 || email.indexOf(".") == -1) {
        document.getElementById("erro").innerHTML = "Insira um email válido"
        document.getElementById("erro").style.color = 'red'
        return
    }

    // salvando a api em uma váriavel
    let url = "https://go-wash-api.onrender.com/api/login"

    // criando o corpo da requisição
    let parametros = {
        "email": email,
        "password": senha,
        "user_type_id": 1
    }

    // fazendo a requisição
    let api = await fetch(url,{
        method: "POST",
        body: JSON.stringify(parametros),
        headers: {
            "Content-Type":"application/json"
        }
    })

    // verificando se teve erros
    if (api.ok) {
        
        // salvando a resposta da api
        let response = await api.json()

        // avisando o usuario
        alert("Logado com sucesso!!!")

        // exibindo o resultado da api no console
        console.log(response);

    // erro de login ou senha
    } else{
        document.getElementById("erro").innerHTML = "E-mail ou senha não encontrados"
        document.getElementById("erro").style.color = 'red'
    }
}