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
		