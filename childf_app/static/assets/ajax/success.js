function successful() {
    var postUrl = "/contact_us/";
    name = $("#name").val();
    email = $("#email").val();
    message = $("#message").val();
        $.ajax({
        url: postUrl,
               type: 'POST',
               data: {name:name, email:email, message:message},
               traditional: true,
               success: function (result) {
                   var data = JSON.parse(result);
                   swal("", data['html'], data['swal_type'])
               }
    });


}

