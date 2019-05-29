    var logined = false;

    function Show(){
        document.getElementById('shade').classList.remove('hide');
        document.getElementById('modal').classList.remove('hide');
    }
     function Hide(){
        document.getElementById('shade').classList.add('hide');
        document.getElementById('modal').classList.add('hide');
    }

    function Login(){
    	var useraccount = document.getElementById('account');
    	var userpassword = document.getElementById('password');
        useraccount.focus();
    	var acc = useraccount.value;
    	var psw = userpassword.value;
    	if (acc == "123" && psw == "123") {
    		logined = true;
    		alert('welcome');
    	}
    	else {
    		alert('wrong');
    	}
    }