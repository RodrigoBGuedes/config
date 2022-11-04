$(document).ready(function () {
    $('input').on('keypress', function (event) {
        var regex = new RegExp("^[a-zA-Z0-9]+$");
        var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
        if (!regex.test(key)) {
            event.preventDefault();
            return false;
        }
    });
});

$(document).ready(function () {
    $('input:visible:enabled:first').focus();
});

setTimeout(function () {
    if ($('#msg').length > 0) {
        $('#msg').remove();
    }
}, 2500)