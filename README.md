# wt-final-exam-
W.T. QUESTION BANK SOLUTIONS

Q1) Recreate the Image Given below using HTML & CSS. Let the background be of color - #191919 The color of the cirle should be - #F9E492 The color of the triangle must be - #4F77FF The area of intersection of circle & triange must be - #191919 same as that of the background.
<!DOCTYPE html>
<head>
    <title>Shapes</title>
    <style>
    
        .rectangle {
			
            width: 350px;
            height: 295px;
            background-color: #191919;
        }

        .circle {
            position: relative;
            top: 50px;
            left: 90px;
            width: 180px;
            height: 180px;
            border-radius: 50%;
            background-color: #F9E492;
        }

        .triangle {
            position: relative;
            top: 85px;
            right: 43px;
            border-radius: 0px;
            width: 0;
            height: 0;
            border-left: 135px solid transparent;
            border-right: 130px solid transparent;
            border-bottom: 160px solid #4F77FF;
        }

         .cone {
            position: absolute;
			top: 0px;
			right: -75px;
			width: 0;
			height: 0;
			border-left: 76px solid transparent;
			border-right: 76px solid transparent;
			border-bottom: 90px solid #191919;
			border-radius: 50%;
		}
            </style>
</head>
<body>
    <div class="container">
        <div class="rectangle">
            <div class="circle">
                <div class="triangle">
					<div class=cone></div>
				</div>
			</div>
		</div>
	</div>
</body>
</html>

Q2) Create a function to sort a given array into ascending order  
<!DOCTYPE html>
<head>
    <script>
        function sort_array()
		{
			const arr = ["Banana", "Orange", "Apple", "Mango"]; 
			//works for integer array also
			var sorted = arr.sort();
			//var rev_sorted = sorted.reverse();
			return (sorted);
		}
    document.write(sort_array());          
    </script>
    <title>Document</title>
</head>
<body> </body>
</html>

Q3) Complete the square sum function so that it squares each number passed into it and then sums the results together For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
<!DOCTYPE html>
<html>
<head>
    <script>
		function sum_sq(arr)
		{
			var sum = 0;
			for(var i = arr.length - 1; i >= 0; i--)
			{
				sum += Math.pow(arr[i], 2);
				return sum;
			}
		}
		document.write(sum_sq([0,1,2,3,4]));
    </script>
    <title>Document</title>
</head>
<body> </body>
</html>

Q4) Recreate your class Time table using html & css only.
<!DOCTYPE html>
<head>
<style>
	table,th,td{
    border: 1px solid black;
    border-collapse: collapse;
    text-align: center;
    padding: 8px;
	}

	.caption{
    font-weight: 900;
    font-size: larger;
    margin: 10px;
	}

	.row-lunch{
    font-weight: 600;
	}
</style>
    <title>Timetable</title>
</head>
<body>
 <table>
    <caption class="caption">
        TIME TABLE
    </caption>
<thead>
    <tr>
        <th>Day/Period</th>
       <th>I</th>
       <th>II</th>
       <th>III</th>
       <th>12:00- 12:30</th>
       <th>IV</th>
       <th>V</th>
       <th>VI</th>
       <th>VII</th>
    </tr>
</thead>

<tbody>
<tr>
    <td>Monday</td>
   <td>Eng</td>
   <td>Hndi</td>
   <td>Maths</td>
   <td rowspan="6" class="row-lunch">LUNCH</td>
   <td colspan="3">LAB</td>
   <td>Phy</td>
</tr>

<tr>
    <td>Tuesday</td>
    <td colspan="3">LAB</td>
    <td>Eng</td>
    <td>Che</td>
    <td>Sci</td>
    <td>Phy</td>
</tr>

<tr>
    <td>Wednesday</td>
    <td>Math</td>
    <td>Phy</td>
    <td>Eng</td>
    <td>Che</td>
    <td colspan="3">LIBRARY</td>
</tr>

<tr>
    <td>Thrusday</td>
    <td>Math</td>
    <td>Phy</td>
    <td>Eng</td>
    <td colspan="3">LAB</td>
    <td>Math</td>
</tr>

<tr>
    <td>Friday</td>
    <td colspan="3">LAB</td>
    <td>Phy</td>
    <td>Eng</td>
    <td>Che</td>
    <td>Sci</td>
</tr>

<tr>
    <td>Saturday</td>
    <td>Eng</td>
    <td>Phy</td>
    <td>Eng</td>
    <td colspan="3">SEMINAR</td>
    <td>SPORTS</td>
</tr>

</tbody>
 </table>
</body>
</html>

Q5), Q6) Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
<!DOCTYPE html>
<html>
<head>
	<script>
                    	function lovePetals(petals)
                    	{
                                	if (petals % 2 === 0)
                                	{
                                            	return true;
                                	}
                                	else
                                	{
                                	  return false;
                                	}
                    	}
                    	document.write("Flower 1 with 14 petals : " + lovePetals(14))
                    	document.write("<br> Flower 1 with 11 petals : " + lovePetals(11))
        	</script>
    <title>Document</title>
</head>
</html>
 
Q7)
<?php
function greeting(){
    $timeOfDay = date('a');
    if($timeOfDay =='am'){
        return 'GOODMORNING';
   }
    if($timeOfDay =='pm'){
        return'GOODNIGHT';
  }
}
echo greeting();
?>

(OR)

<?php
$hour = date('H');

if ($hour >= 20) {
$greetings = "Good Night";
} elseif ($hour > 17) {
$greetings = "Good Evening";
} elseif ($hour > 11) {
$greetings = "Good Afternoon";
} elseif ($hour < 12) {
$greetings = "Good Morning";
}
echo $greetings;
echo $hour;
?>

Q8) Write a JavaScript function that accepts a string as a parameter and converts the first letter of each word of the string in upper case. Example string : 'the quick brown fox' Expected Output : 'The Quick Brown Fox '
<!DOCTYPE html>
<head>
	<script>
    	const mySentence = "lier lier pants on fire";
    	const words = mySentence.split(" ");
    	const cap_sent = words.map((word) => {
                                            	return word[0].toUpperCase().concat(word.substring(1));
                                	}).join(" ");
                    	document.write(cap_sent);
	</script>
    <title>Document</title>
</head>
<body>
</body>
</html>

Q9) Write a Javascript program to calculate the days left for New Years EVE 2023.
<!DOCTYPE html>
<head>
	<script>
    	var today = new Date();
    	const NewyearDate = new Date("2022-12-31");
                    	const millisec = (10 * 24 * 60 * 60 * 100)
        document.write(Math.ceil((NewyearDate - today) / millisec));
	</script>
    <title>NewYear</title>
</head>
<body>
</body>
</html>

Q10) Write Javascript code to count the no. Of vowels in a string for eg. ‘The Quick Brown Fox’. The output for this should be : 5.
<!DOCTYPE html>
<head>
	<script>
    	var s = "The quick brown fox jumps over euthe lazy dog"
    	function countVowels(s)
                    	{
            	var c = s.match(/[aeiou]/gi);
            	return c === null ? 0 : c.length;
    	}
        document.write(countVowels(s))
	</script>
    <title>Document</title>
</head>
<body>
</body>
</html>

Q11) Write a Javascript function to reverse a string.
<!DOCTYPE html>
<head>
    <script>
        function reverseString(str)
		{
			var newString = "";
			for (var i = str.length - 1; i >= 0; i--)
			{
				newString += str[i];
			}
			return newString;
		}
    document.write(reverseString("hello"));
    </script>
    <title>Document</title>
</head>
<body> </body>
</html>

Q12) Write a Javascript function to validate a palindrome.  
<!DOCTYPE html>
<head>
    <script>
        function reverseString(str)
		{
			var newString = "";
			for (var i = str.length - 1; i >= 0; i--)
			{
				newString += str[i];
			}
			if (newString == str)
			{
				return true;
			}
			else
			{
				return false;
			}
		}
    document.write(reverseString("ll"));
    </script>
    <title>Document</title>
</head>
<body> </body>
</html>

Q13) Write a Javascript function to reverse an Integer.
<!DOCTYPE html>
<head>
    <script>
        function reverse_a_number(n)
		{
			n = n + "";
			return n.split("").reverse().join("");
		}
    document.write(Number(reverse_a_number(51032789)));          
    </script>
    <title>Document</title>
</head>
<body> </body>
</html>

Q14) same as Q8)

Q15) Write a program that prints all the numbers from 1 to 100. for muliples of 3, instead of the number, print 'Fizz' for multiples of 5 print 'Buzz', for numbers which are multiples of both 3 & 5, print 'FizzBuzz'.  
<!DOCTYPE html>
<head>
    <script>
    function fizzBuzz(i)
	{
		for (i = 1; i <= 100; i++)
		{
			if (i % 15 == 0)
				document.write("FizzBuzz" + "<br>");
			else if ((i % 3) == 0)
				document.write("Fizz" + "<br>");
			else if ((i % 5) == 0)
				document.write("Buzz" + "<br>");
			else
				document.write(i + "<br>");
		}
	}
	fizzBuzz(100);
    </script>
    <title>Document</title>
</head>
<body> </body>
</html>

Q16) same as Q9)

Q17) Write a PHP Program to write your full name into a .txt file
<?php
$myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
$txt = "Neha Shah\n";
fwrite($myfile, $txt);
fclose($myfile);
echo "name written in file"
?>

Q20) Write a PHP program to list all the cookies stored on the press of a button.

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

