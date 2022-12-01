<?php
if(isset($_POST['submit'])){
    $username = htmlentities($_POST['username']);

    $cookiename = setcookie('userName', $username); 

    $cookie=$_COOKIE;
    foreach ($cookie as $key=>$val)
    echo "<br>$key : $val";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>PHP Cookies</title>
</head>
<body>
        <form method="POST" action="<?php echo $_SERVER['PHP_SELF'];?>">
                <input type="text" name="username" placeholder="Enter Username">
                <br>
                <input type="submit" name="submit" value="Submit">
            </form>
        </div>
</body>