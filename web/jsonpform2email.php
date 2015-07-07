<?php
header('Content-type: application/x-javascript');
/* validate email address using regular expression */
function validateEmail($address){
	$pattern = '/^(?!(?:(?:\\x22?\\x5C[\\x00-\\x7E]\\x22?)|(?:\\x22?[^\\x5C\\x22]\\x22?)){255,})(?!(?:(?:\\x22?\\x5C[\\x00-\\x7E]\\x22?)|(?:\\x22?[^\\x5C\\x22]\\x22?)){65,}@)(?:(?:[\\x21\\x23-\\x27\\x2A\\x2B\\x2D\\x2F-\\x39\\x3D\\x3F\\x5E-\\x7E]+)|(?:\\x22(?:[\\x01-\\x08\\x0B\\x0C\\x0E-\\x1F\\x21\\x23-\\x5B\\x5D-\\x7F]|(?:\\x5C[\\x00-\\x7F]))*\\x22))(?:\\.(?:(?:[\\x21\\x23-\\x27\\x2A\\x2B\\x2D\\x2F-\\x39\\x3D\\x3F\\x5E-\\x7E]+)|(?:\\x22(?:[\\x01-\\x08\\x0B\\x0C\\x0E-\\x1F\\x21\\x23-\\x5B\\x5D-\\x7F]|(?:\\x5C[\\x00-\\x7F]))*\\x22)))*@(?:(?:(?!.*[^.]{64,})(?:(?:(?:xn--)?[a-z0-9]+(?:-+[a-z0-9]+)*\\.){1,126}){1,}(?:(?:[a-z][a-z0-9]*)|(?:(?:xn--)[a-z0-9]+))(?:-+[a-z0-9]+)*)|(?:\\[(?:(?:IPv6:(?:(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){7})|(?:(?!(?:.*[a-f0-9][:\\]]){7,})(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){0,5})?::(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){0,5})?)))|(?:(?:IPv6:(?:(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){5}:)|(?:(?!(?:.*[a-f0-9]:){5,})(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){0,3})?::(?:[a-f0-9]{1,4}(?::[a-f0-9]{1,4}){0,3}:)?)))?(?:(?:25[0-5])|(?:2[0-4][0-9])|(?:1[0-9]{2})|(?:[1-9]?[0-9]))(?:\\.(?:(?:25[0-5])|(?:2[0-4][0-9])|(?:1[0-9]{2})|(?:[1-9]?[0-9]))){3}))\\]))$/iD';
	if (preg_match($pattern, $address) === 1) {
		return true;
	}
	
	return false;
}
$to_email = "sheum1@tcnj.edu"; // put your email address here - this is the address to which the email will be sent
$from = (isset($_REQUEST["from"])) ? $_REQUEST["from"] : ''; // sender
$subject = (isset($_REQUEST["subject"])) ? $_REQUEST["subject"] : ''; // email subject
$message = (isset($_REQUEST["message"])) ? $_REQUEST["message"] : ''; // email text message
$callback = (isset($_REQUEST["callback"])) ? $_REQUEST["callback"] : ''; // javascript callback function
	
// Check if the "from" input field is filled out
if (!empty($from) && validateEmail($from)) {
			
	// message lines should not exceed 70 characters (PHP rule), so wrap it
	$message = wordwrap($message, 70);
	
	// send mail ( to, subject, message, headers )
	if(mail($to_email,$subject,$message,"From: ".$from."\n")){
			echo $callback."([{status:'success',from:'".$from."',subject:'".$subject."',message:'".$message."'}])";
	} else {
			echo $callback."([{status:'failed to send',message:'Couldn\'t send mail.'}])";
	};
} else {
	echo $callback."([{status:'invalid email',message:'Invalid email address.'}])";
}
?>