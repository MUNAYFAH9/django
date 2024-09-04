
function add_to_cart(id)
{
    var cart=document.getElementById('cart')
    var ajaxurl="/add_to_cart/";
    $.ajax({

        headers: { "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content") },
        url:ajaxurl,
        data:{id:id},
        method:"post",

        success:function(response){
            cart.innerHTML=response.count
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: "تم الإضافة الى السلة بنجاح",
                showConfirmButton: false,
                timer: 1500
              });
          
        }

    });
}
