function resend_sms() {
    swal({
        title: '<p class="swal-text">ارسال مجدد کد</p>',
        text:'<p class="swal-text">آیا موافق ارسال مجدد کد فعال سازی هستید؟</p>',
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'بله',
        cancelButtonText:'خیر',
        confirmButtonClass: 'btn btn-success',
        cancelButtonClass: 'btn btn-danger'
    }).then(function(isConfirm) {
           if (isConfirm) {
             var postUrl = "/sms/";
             $.ajax({
               url: postUrl,
               type: 'POST',
               data: {},
               traditional: true,
               success: function (result) {
                 swal("", result, "success")
               }
              });
              }
            })





}

