/*
 *
 * login-register modal
 * Autor: Creative Tim
 * Web-autor: creative.tim
 * Web script: http://creative-tim.com
 * 
 */
function showRegisterForm(){
    $('.loginBox').fadeOut('fast',function(){
        $('.registerBox').fadeIn('fast');
        $('.login-footer').fadeOut('fast',function(){
            $('.register-footer').fadeIn('fast');
        });
        $('.modal-title').html('Register with');
    }); 
    $('.error').removeClass('alert alert-danger').html('');
       
}
function showLoginForm(){
    $('#loginModal .registerBox').fadeOut('fast',function(){
        $('.loginBox').fadeIn('fast');
        $('.register-footer').fadeOut('fast',function(){
            $('.login-footer').fadeIn('fast');    
        });
        
        $('.modal-title').html('Login with');
    });       
     $('.error').removeClass('alert alert-danger').html(''); 
}

function openLoginModal(){
    showLoginForm();
    setTimeout(function(){
        $('#loginModal').modal('show');    
    }, 230);
    
}
function openRegisterModal(){
    showRegisterForm();
    setTimeout(function(){
        $('#loginModal').modal('show');    
    }, 230);
    
}

/*function loginAjax(){
    /*   Remove this comments when moving to server
    $.post( "/login", function( data ) {
            if(data == 1){
                window.location.replace("/home");            
            } else {
                 shakeModal(); 
            }
        });
    */

/*   Simulate error message from the server 
     shakeModal();
}  */

function shakeModal(){
    $('#loginModal .modal-dialog').addClass('shake');
             $('.error').addClass('alert alert-danger').html("Invalid email/password combination");
             $('input[type="password"]').val('');
             setTimeout( function(){ 
                $('#loginModal .modal-dialog').removeClass('shake'); 
    }, 1000 ); 
}

$(document).ready(function(){
 
 $('#loginform').validate(
 {
  rules: {
    email: {
      required: true,
      email:true
    },
    lastname: {
      required: true
    },
    password: {
      required: true
    }
  },
  messages: {
        email: {
required:"Please enter email address",
 email: "Please enter valid email.",
 }, 
        password: {
            required: "Please provide a password",
            minlength: "Your password must be at least 6 characters long"
        }
  },
  highlight: function(element) {
    //$(element).closest('.form-group').removeClass('success').addClass('error');
$('#loginModal .modal-dialog').addClass('shake');
   setTimeout( function(){ 
                $('#loginModal .modal-dialog').removeClass('shake'); 
    }, 1000 );
  },

 });

}); 



$(document).ready(function(){
 
 $('#regform').validate(
 {
  rules: {
    email: {
      required: true,
      email:true
    },
   
    password1: {
      required: true
    },
 phone: {
      required: true,
      minlength: 10,
      number:true
    },

		    
  },
  messages: {
        email: {
required:"Please enter email address",
 email: "Please enter valid email.",
 }, 
        password1: {
            required: "Please provide a password",
            minlength: "Your password must be at least 6 characters long"
        },
phone: {
            required: "Please enter mobile no.",
            minlength: "Please Enter Valid Mobile No.",
	    number:"Only Number Is Allowed"
        }
  },
  highlight: function(element) {
    //$(element).closest('.form-group').removeClass('success').addClass('error');
$('#loginModal .modal-dialog').addClass('shake');
   setTimeout( function(){ 
                $('#loginModal .modal-dialog').removeClass('shake'); 
    }, 1000 );
  },

 });

});




function email_validate()
{

var regMail = /^([_a-zA-Z0-9-]+)(\.[_a-zA-Z0-9-]+)*@([a-zA-Z0-9-]+\.)+([a-zA-Z]{2,3})$/;

    if(regMail)
    {
    return (true)
    }
   return (false)
} 

function Validate(firstname) {
    firstname.value = firstname.value.replace(/[^a-zA-Z-'\n\r.]+/g, '');
}

function Validate(lastname) {
    lastname.value = lastname.value.replace(/[^a-zA-Z-'\n\r.]+/g, '');
}
function validatephone(phone) 
{
    var maintainplus = '';
    var numval = phone.value
    if ( numval.charAt(0)=='+' )
    {
        var maintainplus = '';
    }
    curphonevar = numval.replace(/[\\A-Za-z!"£$%^&\,*+_={};:'@#~,.Š\/<>?|`¬\]\[]/g,'');
    phone.value = maintainplus + curphonevar;
    var maintainplus = '';
    phone.focus;
}

function checkPass()
{
    //Store the password field objects into variables ...
    var pass1 = document.getElementById('password1');
    var pass2 = document.getElementById('password2');
    //Store the Confimation Message Object ...
    var message = document.getElementById('confirmMessage');
    //Set the colors we will be using ...
    var goodColor = "#66cc66";
    var badColor = "#ff6666";
    //Compare the values in the password field 
    //and the confirmation field
    if(pass1.value == pass2.value){
        //The passwords match. 
        //Set the color to the good color and inform
        //the user that they have entered the correct password 
        pass2.style.backgroundColor = goodColor;
        message.style.color = goodColor;
        message.innerHTML = "Passwords Match"
    }else{
        //The passwords do not match.
        //Set the color to the bad color and
        //notify the user.
        pass2.style.backgroundColor = badColor;
        message.style.color = badColor;
        message.innerHTML = "Passwords Do Not Match!"
    }
} 


//onchange="this.setCustomValidity(validity.valueMissing ? 'Please indicate that you accept the Terms and Conditions' : '');"
//<input type="checkbox"  class="form-control" name="terms"  id="field_terms">I would like to receive ShareAplace messages.
