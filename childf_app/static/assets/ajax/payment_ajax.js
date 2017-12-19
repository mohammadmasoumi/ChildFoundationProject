function payment_result() {
    var postUrl = "/payment/";
    amount = $("#amount").val();
    name = $("#name").val();
    national_code = $("#national_code").val();
    email = $("#email").val();
    mobileNo = $("#mobileNo").val();

    message = $("#message").val();
        $.ajax({
        url: postUrl,
               type: 'POST',
               data: {amount:amount, email:email, name:name ,national_code:national_code ,mobileNo:mobileNo},
               traditional: true,
               success: function (result) {
                   var data = JSON.parse(result);
                   swal("", data['html'], data['swal_type'])
               }
    });


}

