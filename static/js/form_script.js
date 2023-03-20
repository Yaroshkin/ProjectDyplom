$(document).ready(function () {
        let form = $('#form_buy');

        function cartUpdate(id_prod, number, is_delete) {
            let data = {};
            data.id_prod = id_prod;
            data.number = number;
            let csrf_token = $('#form_buy [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;

            if (is_delete){
                data["is_delete"] = true;
            }

            let url = form.attr("action");
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    console.log("OK");
                    if (data.prod_total || data.prod_total == 0) {
                        $('#cart_total_nmb').text("(" + data.prod_total + ")");
                        $('.cart_prod ul').html("");
                        $.each(data.prod, function (k, v) {
                            $('.cart_prod ul').append('<li>' + v.name + ', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + ' грн ' +
                                '<a class="delete-item" href="" data-id_prod="'+ v.id +'">x</a>' +
                                ' </li>');
                        })
                    }

                },
                error: function () {
                    console.log("error")
                }
            });

        }

        form.on('submit', function (e) {
            e.preventDefault();
            let number = $('#number').val();
            let submit_btn = $('#submit_btn');
            let id_prod = submit_btn.data("id_prod");
            let name_prod = submit_btn.data("name_prod");
            let price_prod = submit_btn.data("price_prod");


            cartUpdate(id_prod, number, is_delete = false);


        });

        function showcart() {
            $('.cart_prod').toggleClass('hidden ')
        }


        $('.cart-container').mouseover(function () {
            showcart();
        });
        $('.cart-container').mouseout(function (){
           showcart();
        });

        $(document).on('click', '.delete-item', function (e) {
            e.preventDefault()
            id_prod = $(this).data("id_prod")
            number = 0
            cartUpdate(id_prod, number, is_delete = true);
        })

    function CalcCart(){
        let total_order = 0;
        $('.total_prod').each(function (){
            total_order += parseFloat($(this).text());
        })
        $('#total_order').text(total_order.toFixed(2))
    }

        $(document).on('change', ".prod-cart-nmb", function (){
            let current_nmb = $(this).val();
            let cur_tr = $(this).closest('tr');
            let current_price = parseFloat(cur_tr.find('.prod-price').text());
            let total_amount = current_nmb*current_price;
            cur_tr.find('.total_prod').text(total_amount.toFixed(2));
            CalcCart();
    })


    CalcCart();
})
