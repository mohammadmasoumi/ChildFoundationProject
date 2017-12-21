function forget_password() {
    var postUrl = "/forget_password/";
    username = $("#username").val();
    email = $("#email").val();

        $.ajax({
        url: postUrl,
               type: 'POST',
               data: {username:username, email:email},
               traditional: true,
               success: function (result) {
                   var data = JSON.parse(result);
                   swal("", data['html'], data['swal_type'])
               }
    });


}

