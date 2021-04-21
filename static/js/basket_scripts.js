window.onload = function () {
    $('#form-reg').on('click', '#rgst', function (event) {
        //alert('Подтверждение для регистрации отправлено')
        
        }
    )
    console.log('DOM loaded');
    $('#dataTable').on('click', '#quamtity', function (event) {
        console.log(event.target);
        $.ajax({
            url: '/clientdevicelist/change/' + event.target.name + '/quantity/' + event.target.value + '/',
            success: function (data) {
                console.log(data)
            }
        });
    })
};

