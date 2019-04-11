$(document).ready(function(){
            $("input").addClass( "form-control text text-lg");
            $("label").hide();
            $("#id_first_name").attr('placeholder', 'نام خود را وارد کنید :');
            $("#id_last_name").attr('placeholder', 'نام خانوادگی خود را وارد کنید :');
            $("#id_username").attr('placeholder', 'نام کاربری :').val("");
            $("#id_password").attr('placeholder', 'رمز عبور :').val("");
            $("#id_email").attr('placeholder', 'ایمیل :');
            $("#id_phone_number").attr('placeholder', 'شماره تلفن :');
});