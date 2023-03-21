<style>
    input {
        display:block;
    }
    td.parameter{
        text-align:right;
    }
</style>

<form method="post" action="index.php">

<label>Seconds before passing each request:</label>    
<input type="number" id="SECONDS_BEFORE_PASSING_REQUEST" name="SECONDS_BEFORE_PASSING_REQUEST" value="<?php if(isset($_POST['SECONDS_BEFORE_PASSING_REQUEST'])) {echo $_POST['SECONDS_BEFORE_PASSING_REQUEST'];} ?>" />

<label>URL to pass the request to:</label>    
<input type="text" id="DESTINATION_URL" name="DESTINATION_URL" value="<?php if(isset($_POST['DESTINATION_URL'])) {echo $_POST['DESTINATION_URL'];} ?>"/>

<label>How many attempts should fail before a success:</label>
<input type="number" id="FAILED_ATTEMPTS_BEFORE_SUCCESS" name="FAILED_ATTEMPTS_BEFORE_SUCCESS" value="<?php if(isset($_POST['FAILED_ATTEMPTS_BEFORE_SUCCESS'])) {echo $_POST['FAILED_ATTEMPTS_BEFORE_SUCCESS'];} ?>"/>

<input type="submit" value="Submit" name="submit"/>

</form>
<?php

?>

<?php
       if(isset($_POST['submit']))
       {

            $myfile = fopen("config", "w") or die("Unable to open file!");

            $txt = $_POST['SECONDS_BEFORE_PASSING_REQUEST'];
            $txt .= "\n";
            $txt .= $_POST['DESTINATION_URL'];
            $txt .= "\n";
            $txt .= $_POST['FAILED_ATTEMPTS_BEFORE_SUCCESS'];
            fwrite($myfile, $txt);
            fclose($myfile);


            echo"<h1>Saved Configuration</h1><br>";
            echo "<table border='1'>";
            echo "<thead>";
            echo "<th>Parameter</th>";
            echo "<th>Value</th>";
            echo "</thead>";
            echo "<tr>";
            echo "<td class='parameter'>Seconds before passing request</td>";
            echo "<td>".$_POST['SECONDS_BEFORE_PASSING_REQUEST']."</td>";
            echo "</tr>";
            echo "<tr>";
            echo "<td class='parameter'>Destination URL</td>";
            echo "<td>".$_POST['DESTINATION_URL']."</td>";
            echo "</tr>";
            echo "<tr>";
            echo "<td class='parameter'>Failed attempts before success</td>";
            echo "<td>".$_POST['FAILED_ATTEMPTS_BEFORE_SUCCESS']."</td>";
            echo "</tr>";
            echo "<tr>";
            echo "</table>";
        }
    ?>