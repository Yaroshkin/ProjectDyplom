$(document).ready(function (){
    let form = $('#form_buy');
    console.log(form);
    form.on('submit',function (e){
        e.preventDefault();
        console.log('123');
        let number = $('#number').val();
        console.log(number);
        let submit_btn = $('#submit_btn');
        let id_prod = submit_btn.data("id_prod");
        let name_prod = submit_btn.data("name_prod");
        let price_prod = submit_btn.data("price_prod");
        console.log(id_prod)
        console.log(name_prod)
        console.log(price_prod)
        $('.cart_prod ul').append('<li>'+name_prod+ ', '  + number+ 'шт. ' + 'по ' + price_prod+ ' грн ' +
    '<a class="delete-item" href="">x</a>' + ' </li>');
    });

    function showcart(){
        $('.cart_prod').removeClass('hidden ')
    }
    $('.cart-container').on('click', function (e){
        e.preventDefault();
        showcart();
    });
    $('.cart-container').mouseover(function (){
        showcart();
    });
    // $('.cart-container').mouseout(function (){
    //    showcart();
    // });

    $(document).on('click','delete-item', function (e){
        e.preventDefault()
        $(this).closest('li').remove();
    })
});