async function cadastrar(){
    
    // puxando os dados do html e salvando nas variáveis
    let nome = document.getElementById("nome").value
    let sobrenome = document.getElementById("sobrenome").value
    let dt_nascimento = document.getElementById("dt_nascimento").value
    let cpf_cnpj = document.getElementById("CPF_CNPJ").value
    let email = document.getElementById("e-mail").value
    let senha = document.getElementById("senha").value
    let termo = document.getElementById("termo").checked

    // volta a estilização padrão da página
    let limpar = [
        document.getElementById("erro").innerHTML = "",
        document.getElementById("nome").style.color = 'black',
        document.getElementById("nome").style.borderColor = 'black',
        document.getElementById("sobrenome").style.color = 'black',
        document.getElementById("sobrenome").style.borderColor = 'black',
        document.getElementById("dt_nascimento").style.color = 'black',
        document.getElementById("dt_nascimento").style.borderColor = 'black',
        document.getElementById("CPF_CNPJ").style.color = 'black',
        document.getElementById("CPF_CNPJ").style.borderColor = 'black',
        document.getElementById("e-mail").style.color = 'black',
        document.getElementById("e-mail").style.borderColor = 'black',
        document.getElementById("senha").style.color = 'black',
        document.getElementById("senha").style.borderColor = 'black'
    ]

    // verificando se os campos estão preenchidos
    if(nome == "" || sobrenome == "" || dt_nascimento == "" || cpf_cnpj == "" || email == "" || senha == "" || termo == false){
        limpar
        document.getElementById("erro").innerHTML = "Preencha todos os campos e aceite os termos"
        document.getElementById("erro").style.color = 'red'
        document.getElementById("nome").style.borderColor = 'red'
        document.getElementById("sobrenome").style.borderColor = 'red'
        document.getElementById("dt_nascimento").style.borderColor = 'red'
        document.getElementById("CPF_CNPJ").style.borderColor = 'red'
        document.getElementById("e-mail").style.borderColor = 'red'
        document.getElementById("senha").style.borderColor = 'red'
        return

    // verificando se o cpf foi inserido no formato válido
    }else if(cpf_cnpj.length < 11 || cpf_cnpj.length > 11 && cpf_cnpj.length < 14 || cpf_cnpj.indexOf(".") != -1 || cpf_cnpj.indexOf("-") != -1){
        limpar
        document.getElementById("erro").innerHTML = "Insira um CPF ou CNPJ válido"
        document.getElementById("erro").style.color = 'red'
        document.getElementById("CPF_CNPJ").style.color = 'red'
        document.getElementById("CPF_CNPJ").style.borderColor = 'red'
        return

    // verificando se o email foi inserido em um formato válido
    }else if(email.indexOf("@") == -1 || email.indexOf(".") == -1) {
        limpar
        document.getElementById("erro").innerHTML = "Insira um email válido"
        document.getElementById("erro").style.color = 'red'
        document.getElementById("e-mail").style.color = 'red'
        document.getElementById("e-mail").style.borderColor = 'red'
        return

    // verificando se a senha tem no min 6 caracteres
    }else if(senha.length < 6){
        limpar
        document.getElementById("erro").innerHTML = "Sua senha deve ter no min 6 caracteres"
        document.getElementById("erro").style.color = 'red'
        document.getElementById("senha").style.color = 'red'
        document.getElementById("senha").style.borderColor = 'red'
        return

    // volta a estilização padrão da página
    }else{
        limpar
    }

    // salvando a api em uma variavel
    let url = 'https://go-wash-api.onrender.com/api/user'

    // criando o corpo da requisição
    let parametros = {
        "name": nome,
        "email": email,
        "user_type_id": 1,
        "password": senha,
        "cpf_cnpj": cpf_cnpj,
        "terms": 1,
        "birthday": dt_nascimento
    }

    // mandando a requisição pra api
    let api = await fetch(url,{
        method: "POST",
        body: JSON.stringify(parametros),
        headers: {
            "Content-Type":"application/json"
        },
    })

    // pegando o resultado da api idependente do resultado
    let response = await api.json()

    // verificando se não teve erro de cadastro
    if (api.ok) {
    
        // mostrando pro usuario que o cadastro dele foi realizado
        alert("Usuario cadastrado com sucesso");
    
        // exibindo o resultado do cadastro no console
        console.log(response);
    
    }else{
    
        // exibindo os erros no console
        console.log(response.data.errors)

        // validando se o email e o cpf ou cnpj ja foram registrados
        if(response.data.errors.email == 'The email has already been taken.' && response.data.errors.cpf_cnpj == 'The cpf cnpj has already been taken.'){
            limpar
            document.getElementById("erro").innerHTML = "O E-mail e o CPF ja existem"
            document.getElementById("erro").style.color = 'red'

        // validando se o email ja foi registrado
        }else if(response.data.errors.email == 'The email has already been taken.'){
            limpar
            document.getElementById("erro").innerHTML = "O E-mail ja existe"
            document.getElementById("erro").style.color = 'red'

        // validando se o CPF ja foi registrado
        }else if(response.data.errors.cpf_cnpj == 'The cpf cnpj has already been taken.'){
            limpar
            document.getElementById("erro").innerHTML = "O CPF ou CNPJ ja existe"
            document.getElementById("erro").style.color = 'red'
        
        // validando se o cpf existe
        }else if(response.data.errors == "cpf_cnpj invalid"){
            document.getElementById("erro").innerHTML = "Insira um CPF ou CNPJ válido"
            document.getElementById("erro").style.color = 'red'
        }
    }
}