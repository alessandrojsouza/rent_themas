//Load enpoint to list clinets
function loadClients() {
   // document.getElementById('client').innerHTML = "Carregando..."
    fetch('http://127.0.0.1:8000/api/clients/')
        .then(function(resposta){
            return resposta.json();
        })
        .then(function(json){
             showTableClients(json);
        })
        .catch(function(error){
            alert(error);
        })
}

//Save new client in DB
function postClient(){
    
    fetch('http://127.0.0.1:8000/api/clients/',{
        method: 'POST',
        body: JSON.stringify({
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            phone1: document.getElementById('phone1').value,
            phone2: document.getElementById('phone2').value,
        }),
        headers:{
            'Content-Type' : 'application/json'
        }
    });
}


//Mount table of clients
function showTableClients(lista){
    let html = '<thead><tr><th scope="col">#</th><th scope="col">Nome</th><th scope="col">Ações</th><th scope="col"></th></tr></thead>';
    if (lista.length > 0){
        for(let i in lista){
            html += '<tr>' 
            html += '<td>' + lista[i].id + '</td>';
            html += '<td>' + lista[i].name + '</td>';
            html += '<td width="80"><a href="">Excluir</a></td>';
            html += '<td><a href="">Editar</a></td>';
            html += '</tr>'
        }
    } 
    else{
       html ='<p>Nenhum cliente cadastrado!!</p>'
    }
    document.getElementById('tableCients').innerHTML = html;
}

function writeSideBar(){
    document.getElementById('sidebar').innerHTML = '<div><nav class="nav navbar-light" style="background-color: #e3f2fd;">'+
    '<a class="navbar-brand" href="/front_js">&nbsp; RentThemas</a>'+
    '<a class="nav-link" href="/front_js/pages/client/listClient.html">Clientes</a>'+
    '<a class="nav-link" href="/listTheme">Temas</a>'+
    '<a class="nav-link" href="/listItem">Itens</a>'+
    '<a class="nav-link" href="/listRent">Aluguel</a></nav></div>';
}