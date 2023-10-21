<?php
// Get form data
$username = $_POST['name'];
$email = $_POST['email'];

// Establish database connection
$servername = "localhost";
$username = "root";
$password = "03038082StSMy$!S";
$dbname = "dbtest";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connectiondada failed: " . $conn->connect_error);
}

// Insert form data into the database
$sql = "INSERT INTO your_table_name (username, email) VALUES ('$username', '$email')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close the database connection
$conn->close();
?>