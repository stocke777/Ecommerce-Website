var updateBtns = document.getElementsByClassName('update-cart');
var incBtns = document.getElementsByClassName('increase');
var decBtns = document.getElementsByClassName('decrease');


for(i = 0; i < incBtns.length; i++){
    incBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        var btn = this.dataset.btn;
        var cname = this.classList;
        var btnclass = cname[cname.length - 1];
        console.log('productId:', productId, "action:", action, "btn is:", btn, cname[cname.length - 1]);

        if(user === "AnonymousUser"){
            console.log("Not loged in")
            window.location.href = "http://127.0.0.1:8000/login";
        }else{
            add_item(productId, action, btnclass)
        }
    })
    console.log("HELI increase")
}

for(i = 0; i < decBtns.length; i++){
    decBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        var btn = this.dataset.btn;
        var cname = this.classList;
        var btnclass = cname[cname.length - 1];
        console.log('productId:', productId, "action:", action, "btn is:", btn, cname[cname.length - 1]);

        if(user === "AnonymousUser"){
            console.log("Not loged in")
            window.location.href = "http://127.0.0.1:8000/login";
        }else{
            remove_item(productId, action, btnclass)
        }
    })
    console.log("HELI decrease")
}


for(i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        var btnclass = "nothing"
        console.log('productId ', productId, "action ", action, "btn", btnclass);

        if(user === "AnonymousUser"){
            console.log("Not loged in")
            window.location.href = "http://127.0.0.1:8000/login";
        }else if (action === "inc" || action === "add"){
            add_item(productId, action, btnclass)
        }else{
            remove_item(productId, action, btnclass)
        }
    })
}

function add_item(productId, action, btnclass){
    if(action === "inc"){
        console.log("we inc boi")
    }else if(action === "add"){
        console.log("we add boi")
    }
    console.log('User is logged in')
    console.log(csrftoken)

    var url = '/add_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })

    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        if(data === "added to cart"){
            console.log('data', data)
        }else{
            console.log("quantity now is ", data)
            document.getElementsByClassName(btnclass)[0].innerHTML = data;
            
        }

    })
}

function remove_item(productId, action, btnclass){
    if(action === "dec"){
        console.log("we dec boi")
    }
    console.log('User is logged in')
    console.log(csrftoken)

    var url = '/remove_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })

    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        if(data === "Item is removed"){
            console.log('data', data)
        }else{
            console.log("quantity now is ", data)
            document.getElementsByClassName(btnclass)[0].innerHTML = data;
            
        }

    })
}