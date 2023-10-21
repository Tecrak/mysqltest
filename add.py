if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $servername = "127.0.0.1:3306";
    $username = "root";
    $password = "03038082StSMy$!S";
    $database = "dbtest";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $database);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed fuck: " . $conn->connect_error);
    }

    // Sanitize user input to prevent SQL Injection
    $name = mysqli_real_escape_string($conn, $_POST['name']);
    $email = mysqli_real_escape_string($conn, $_POST['email']);

    // Insert data into the database
    $sql = "INSERT INTO user_data (name, email) VALUES ('$name', '$email')";

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error fuck: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}