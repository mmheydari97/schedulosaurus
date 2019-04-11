$(document).ready(function(){
            $("#id_title").addClass( "form-control text text-lg").attr("required", false).attr("placeholder", "کار جدید وارد کنید ...");
            $("label[for='id_title']").hide();

            $(".errorlist").hide();

            $("#btn").click(function()
            {
             var new_url="new_packet";
             window.history.pushState("data","Title",new_url);
             document.title="new_packet";
            });

            $(".btn-end").click(function(){
             var new_url="end_task/"+this.value;
             window.history.pushState("data","Title",new_url);
             document.title=new_url;
            });
        });