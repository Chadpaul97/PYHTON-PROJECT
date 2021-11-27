
var slider_img = document.querySelector('.slider-img');
var images = ['hotdeals.png', 'newproducts.png', 'clearence.png', 'holidaysale.png'];
var i = 0;

function prev(){
	if(i <= 0) i = images.length;	
	i--;
	return setImg();
}

function next(){
	if(i >= images.length-1) i = -1;
	i++;
	return setImg();
}

function setImg(){
	return slider_img.setAttribute('src', "/flask_app/static/images/products/slidingimg/"+images[i]);
	
}


function show_email(){
    document.getElementById("email").innerHTML = "Homestore@email.com";
}
function show_address(){
	document.getElementById("find").innerHTML = "123 Home Store St.";
}
function show_phonenumber(){
	document.getElementById("call").innerHTML = "123-456-7890";
}