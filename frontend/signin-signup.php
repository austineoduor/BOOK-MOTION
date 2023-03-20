<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book-Motion singup</title>
	<link rel="shortcut icon" href="images/book.png">
    <link rel="stylesheet" href="styles/log_in styles.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <div class="signin-signup">

	    <form action="php_file/sign_file/login.php"method="POST" class="sign-in-form">
		<div><?php
			if(isset($Error) && $Error != "")
			{
				echo $Error;
			}
		?></div>
		<h2 class="title">Sign in</h2>
                <div class="input-field">
                    <i class="fas fa-user"></i>
                    <input type="text" name="username" required placeholder="Username">
                </div>
                <div class="input-field">
                    <i class="fas fa-lock"></i>
                    <input type="password" name="password" required placeholder="Password">
                </div>
                <input type="submit" value="Login" class="btn">                
                <p class="account-text">Don't have an account? <a href="#" id="sign-up-btn2">Sign up</a></p>
            </form>

	    <form action="php_file/sign_file/signup.php" method="POST" class="sign-up-form">
		 <div><?php
                        if (isset($Error) && $Error != "")
                        {
                                echo $Error;
                        }
                ?></div>
                <h2 class="title">Sign up</h2>
                <div class="input-field">
                    <i class="fas fa-user"></i>
                    <input type="text" name="username" value="<?=$username?>"required placeholder="Username">
                </div>
                <div class="input-field">
                    <i class="fas fa-envelope"></i>
		    <input type="email" name="email" value="<?$email?>"required placeholder="Email">
                </div>
                <div class="input-field">
                    <i class="fas fa-lock"></i>
                    <input type="password" name="password" required placeholder="Password">
                </div>
                <input type="submit" value="Sign up" class="btn">                
                <p class="account-text">Already have an account? <a href="#" id="sign-in-btn2">Sign in</a></p>
            </form>
        </div>

        <div class="panels-container">
            <div class="panel left-panel">
                <div class="content">
                    <h3>Already a Member of Book-Motion</h3>
                    <p>Sign in to continue your journey of knowledge.</p>
                    <button class="btn" id="sign-in-btn">Sign in</button>
                </div>
                <img src="images/signin.svg" alt="" class="image">
            </div>
            <div class="panel right-panel">
                <div class="content">
                    <h3>New to Book-Motion?</h3>
                    <p>Please sign up to enjoy all benefits.</p>
                    <button class="btn" id="sign-up-btn">Sign up</button>
                </div>
                <img src="images/signup.svg" alt="" class="image">
            </div>
        </div>
    </div>
    <script src="scripts/app.js"></script>
</body>
</html>
