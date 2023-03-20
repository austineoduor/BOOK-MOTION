<?php 
	require "php_file/private/autoload.php";
	$user_data = check_login($con);
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Librarify</title>
        <link rel="icon" type="image/png" href="images/book.png">
        <link rel="stylesheet" type="text/css" href="styles/userPage.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <body>
        <header>
            <div class="container">
                <nav class="navAlign">
                    <div class="logo_home">
                        <img  class="nav_img" src="images/book.png" alt="logo" onerror="this.style.display = 'none'">
                        <div class="home">
                        <a href="index.php"><i class="fa fa-home"></i>Home</a>
                        </div>
                    </div>
                    <div class="navList">
                        <ul>
                            <li><a href="landing_page.php"><i class="fa fa-book"></i>About</a></li>
                            <li><a href="php_file/sign_file/logout.php"><i class="fa fa-sign-out"></i>Logout</a></li>
                        </ul>
                    </div>
                </nav>
            </div>
        </header>
        <section class="container">
            <div>
                <img src="" alt="" onerror="this.style.display = 'none'">
            </div>
            <div>
                <img src="" alt="" onerror="this.style.display = 'none'">
            </div>
            <div>
                <img src="" alt="" onerror="this.style.display = 'none'">
            </div>
            <div>
                <img src="" alt="" onerror="this.style.display = 'none'">
            </div>
            <div>
                <img src="" alt="" onerror="this.style.display = 'none'">
            </div>
            <div>
                <img src="" alt="" onerror="this.style.display = 'none'">
            </div>
            <div>
                <img src="" alt="" onerror="this.style.display = 'none'">
            </div>
            <div>
                <img src="" alt="" onerror="this.style.display = 'none'">
            </div>
            <div>
                <img src="" alt="" onerror="this.style.display = 'none'">
            </div>
            <div>
                <img src="" alt="" onerror="this.style.display = 'none'">
            </div>
        </section>
        <section class="container">
            <div>
                <h1>Recommended Books</h1>
            </div>
            <div>
                <h2>Coming Soon</h2>
            </div>
        </section>
    </body>
    <footer>
        <section class="footer_container">
            <div class="container fut">
                <div class="fut">
                    <h1 class="fut_h1">&copy;<em>2022 All Rights Reserverd</em></h1>
                    <div class="footerIcons">
                        <a href="#"><i class="fa fa-twitter"></i> Librarify</a>
                        <a href="#"><i class="fa fa-instagram"></i> Librarify</a>
                        <a href="#"><i class="fa fa-facebook"></i> Librarify</a>
                    </div>
                </div>
            </div>
        </section>
    </footer>
</html>
