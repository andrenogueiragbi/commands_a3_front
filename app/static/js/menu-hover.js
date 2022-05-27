//MenuToggle

let toggle = document.querySelector('.toggle');
let navigation = document.querySelector('.navigation');
let main = document.querySelector('.main');



    toggle.onclick = function() {
        navigation.classList.toggle('active');
        main.classList.toggle('active');
    }




list = document.querySelectorAll('.navigation li');

    function ativeLink(){
        list.forEach((item) =>
        item.classList.remove('hovered'));
        this.classList.add('hovered');
    }

    list.forEach((item) =>
        item.addEventListener('mouseover',ativeLink));