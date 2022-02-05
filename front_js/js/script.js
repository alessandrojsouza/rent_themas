function loadClients() {
    fetch('http://127.0.0.1:8000/api/clients')
        .then(function(resposta){
            console.log(resposta)
        })
        .catch(function(error){
            console.log("Deu pau!!")
        })
}