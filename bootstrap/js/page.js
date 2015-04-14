		$(function(){
			$(".close").click(function(){
				$("#myAlert").alert();
			});
		}); 
        $('ul > li > a[href*=#]').click(function(){
            $('html, body').animate({
                scrollTop: $( $.attr(this, 'href') ).offset().top -80
            }, 500);
        return false;
        });
        $(".alert").hide();        
$(document).ready(function () {
    $('#contact-form').validate({
        rules: {
            name: {
                minlength: 2,
                required: true
            },
            email: {
                required: true,
                email: true
            },
            message: {
                minlength: 2,
                required: true
            }
        },
        highlight: function (element) {
            $(element).closest('.control-group').removeClass('success').addClass('error');
        },
        success: function (element) {
            element.text('OK!').addClass('valid')
                .closest('.control-group').removeClass('error').addClass('success');
        }
    });

});
$("#meuForm").submit(function(event) {
  /* stop form from submitting normally */
  event.preventDefault();
  /* get some values from elements on the page: */
  var $form = $( this ),
	  url = $form.attr( 'action' );
  /* Send the data using post */
	$(".alert").hide();  
	$(".alert-info").show();
	setTimeout(function(){
		$(".alert-info").hide();
		$(".alert-success").show();  
	}, 2000);

});
