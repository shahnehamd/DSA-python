<?php
$myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
$txt = "Neha Shah\n";
fwrite($myfile, $txt);
fclose($myfile);
echo "name written in file"
?>