<?php 
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "db_diagnostic";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Error al conectar a la base de datos: ");
} 

?>