# Threading
In this program we have created 4 threads input, reversed, capitalize and shift.

# PROCESS OF CODE(EXPLANATION)

#  The code will process in the following way:
  1.	Creating function of input thread “that would take the input of the string from the user”. We have defined that string variable as a global variable.
  2.	Creating reverse function. The reversed function would reverse the string that the user has given.
  3.	Creating capitalize function. The input string given by the user would be capitalized using upper () command. This would automatically convert the string in upper       case letters.
  4.	Creating shift function. In this function we have shifted each character within 2 position ahead. Using the ord command (function returns the number representing         the Unicode code of a specified character).
  5.	We have created the main and have created thread targeting each functions.
  6.	Then we have joined the thread using join () command and start the thread using start () command.
  7.	The output of the code is shown above.
