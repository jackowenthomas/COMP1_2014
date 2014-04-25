#Task Sheet 1 Questions
##Question 3a Answers

1. GetPlayerName()
2. By using the while loop and the length (len) statement it keeps on asking the user until a name is entered
3. ValidName and it's data type is Boolean.

#Pseudocode
FUNCTION GetPlayerName()
	ValidName == False
	PlayerName == INPUT("Please enter your name: ")
	WHILE LENGTH(PlayerName) = 0:
		PlayerName == INPUT("Please enter your name: ")
		ValidName == False
	ValidName == True
	RETURN PlayerName
	
##Question 3b answers
1.GetPlayerName()

##Question 5 answers
1. import datetime
2. displayrecentscore,updaterecentscore,resetrecentscore,playgame
3. You create a datetime object by converting a string to a datetime object using the strptime() function
   datetime.datetime.strptime(date_string, date_time_format) converts a string to a datetime object.
   to display this you use strftime() function, datetime.datetime.strftime("%d/%m/%y")

   
##Additional Questions
##Variable Roles
1. Fixed Value
2. Stepper
3. Most recent holder
4. Most wanted holder
5. Gatherer
6. Transformation
7. Follower
8. Temporary



##Functions and parameters

1. Passing by value =  When a parameter is passed down from the main memory into a function it creates a copy of that parameter and works on that specific copy in the function
instead of the original so that the original parameter can be used more than once, once it has been changed it is returned as a different value. Integer, float, boolean and string
are passed by value

2. Passing by reference = When a parameter is passed down from the main memory into a function it does not create a copy of that parameter
so it can not be used more than once.