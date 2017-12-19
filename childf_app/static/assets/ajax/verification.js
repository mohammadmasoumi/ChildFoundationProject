function verification_entered_code() {
        var postUrl = "/verification/";
        code = $("#verification-code").val();

        $.ajax({
            url: postUrl,
            type: 'POST',
            data: {'code': code},
            traditional: true,
            dataType: 'html',
            success: function (result) {
                var data = JSON.parse(result);
                if (data['result'] == 1) {
                    console.log(data['result']);
                    swal("", data['html'], "success")
                }
            }

        });

       }