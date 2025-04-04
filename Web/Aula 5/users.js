async function save(){
    let name = "Carlos";
    let email = "mitzie1452@uorak.com";
    let userType = 1;
    let password = "123456";
    let termos = 1;
    let birthday = "2000-02-24";
    let cpfCnpj = "82659669000154"
    
    let api = await fetch(
        "https://go-wash-api.onrender.com/api/user",{
            method:"POST",
            body:JSON.stringify({
                "name": name,
                "email": email,
                "user_type_id": userType,
                "password": password,
                "cpf_cnpj": cpfCnpj,
                "terms": termos,
                "birthday": birthday
            }), headers:{
                'Content-Type':'application/json'
            }
        }
    );
    if(api.ok){
        let response = await api.json()
        console.log(response)
        return
    }
    let responseErro = await api.json()
    console.log(responseErro)
}