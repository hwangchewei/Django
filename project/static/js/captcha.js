function myfunction(params) {
    // alert('aaa')
    var captcha_btn = document.getElementById('captcha-btn')
    var ajax_func = new XMLHttpRequest
    var email = document.getElementById('email').value
    if (!email) {
        alert('no email')
    } else {
        ajax_func.open('GET','captcha?email='+email,'true')
        ajax_func.send()
        
        captcha_btn.disabled = true
        var wait_time = 10
        var counttime = setInterval(function () {
            document.getElementById('captcha-btn').innerHTML = wait_time;
            if (wait_time == 0) {
                clearInterval(counttime)
                document.getElementById('captcha-btn').innerHTML = 'Button'
                captcha_btn.disabled = false
            }
            wait_time--
        }, 1000)
        alert('captcha?email='+email)

    }

}