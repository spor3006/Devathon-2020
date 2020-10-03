function SubmitButton(){
    var first_name = document.getElementById('first_name').value;
    var last_name = document.getElementById('last_name').value;
    var email = document.getElementById('email').value;
    var mobile = document.getElementById('mobile').value;
    var roll_number = document.getElementById('roll_number').value;
    var username = document.getElementById('username').value;
    var password  = document.getElementById('password').value;

    var data = {
        'username' : username,
        'first_name' : first_name, 
        'last_name' : last_name,
        'email' : email,
        'mobile' : mobile , 
        'roll_number' : roll_number , 
        'password'  : password
    }


    console.log(data)




    var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        document.getElementById("loader").style.visibility = 'hidden';
                        console.log(this.responseText);
                        var response = JSON.parse(this.responseText);
                            if(response['status'] == 'warning'){
                                console.log("query time: " + response['query_time']);
                                var x = document.getElementById("snackbar");
                                x.innerHTML = response['message'];
                                x.style.backgroundColor = "red";    
                                x.className = "show";
                                setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
                            }
                            else if(response['status'] == 'success'){
                                console.log("query time: " + response['query_time']);
                                var x = document.getElementById("snackbar");
                                x.innerHTML = response['message'];
                                x.style.backgroundColor = "green";    
                                x.className = "show";
                                setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
                                window.location.replace(response['url']);

                            }else {
                                console.log(response['console']);
                                var x = document.getElementById("snackbar");
                                x.innerHTML = response['message'];
                                x.style.backgroundColor = "red";    
                                x.className = "show";
                                setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
                                
                            }
                    }
                };
                xhttp.open("POST", "register", true);
                xhttp.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
            xhttp.send(JSON.stringify(data));

}
