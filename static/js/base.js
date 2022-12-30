//slider ---------------------------------------------------------------------------------------------
const cajade4img = document.querySelector("#slider");
let cajadeimgindividual = document.querySelectorAll(".slider__section");
//con esta optenemos la posicion de la caja de una img si queremos buscar una img mayor se pone coma ejem ,2
let ultima_caja_img = cajadeimgindividual[cajadeimgindividual.length -1];
const btnlef = document.querySelector("#btn-left");
const btnright = document.querySelector("#btn-right");

//con esto ponemos la ultima caja como primera ahora tenemos que poner -100% en el css
cajade4img.insertAdjacentElement('afterbegin',ultima_caja_img)//esto solo se ejecuta la primera ves


function moverderecha(){
    primera_caja_img = document.querySelectorAll(".slider__section")[0];//este nos da la img 4 la primera ves ya que la movimos anterior mente a la primera posicion
    cajade4img.style.marginLeft = "-200%";//este es para que la img sig se ponga  en la que se ve 
    cajade4img.style.transition = "all 0.5s";
    setTimeout(function(){
        //ponemos la primera caja al final la primera ves el la 4
       cajade4img.insertAdjacentElement('beforeend',primera_caja_img);
        cajade4img.style.marginLeft = "-100%"
        cajade4img.style.transition = "none";
    },500);
}

function moverizquierda(){
    let cajadeimgindividual = document.querySelectorAll(".slider__section");
    let ultima_caja_img = cajadeimgindividual[cajadeimgindividual.length -1];
    cajade4img.style.transition = "all 0.5s";
    cajade4img.style.marginLeft = "0";
    setTimeout(function(){
        cajade4img.insertAdjacentElement('afterbegin',ultima_caja_img)
         cajade4img.style.marginLeft = "-100%";
         cajade4img.style.transition = "none";
    },500);
}

btnright.addEventListener("click",function(){
    moverderecha();
});

btnlef.addEventListener("click",function(){
    moverizquierda();
});


setInterval(function(){
    moverderecha();
},7000); 