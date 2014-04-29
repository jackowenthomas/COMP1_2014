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
1. Fixed Value - is a variable that is not changed and is initialised without a calculation
2. Stepper - is a variable that is executed in steps through values
3. Most recent holder - is a variable that is the most recent value obtained by input
4. Most wanted holder - is a variable that is holding the most appropriate value that has been encountered so far
5. Gatherer - is a variable that collects individual values and adds them together to show the total.
6. Transformation - is a variable that obtains a new value from a fixed calculation of values of other variables.
7. Follower - is a variable that gets its new value from an old value
8. Temporary - is a variable that holds a value for a short period of time.



##Functions and parameters

1. Passing by value =  When a parameter is passed down from the main memory into a function it creates a copy of that parameter and works on that specific copy in the function
instead of the original so that the original parameter can be used more than once, once it has been changed it is returned as a different value. Integer, float, boolean and string
are passed by value

2. Passing by reference = When a parameter is passed down from the main memory into a function it does not create a copy of that parameter
so it can not be used more than once.

##Question 6 Answers
1. Global Variable - So you can use it anywhere easily.
2. DisplayMenu()
3. GetRank()

##Q6 Pseudocode
FUNCTION DisplayOptions():
	OUTPUT('OPTIONS MENU')
	OUTPUT()
	OUTPUT('1. Set Ace to be HIGH or Low')
	
FUNCTION GetOptionsChoice():
	OptionChoice == INPUT('Select an option from the menu (or enter q to quit): ')
	RETURN OptionChoice
	
FUNCTION SetOptionsChoice(OptionChoice):
	IF OptionChoice = '1':
	 SetAceHighOrLow()

FUNCTION SetAceHighOrLow():
	GLOBAL RankOfAce
	HighOrLow == INPUT('Do you want Ace to be (h)igh or (l)ow: ')
	HighOrLow == HighOrLow.lower()[0]
	IF HighOrLow = 'h':
		RankOfAce == True
		DisplayMenu
	ELIF HighOrLow = 'l':
		RankOfAce == False
		DisplayMenu()

##Testing
###Testing
In the previous section you made significant changes to the program. These changes must be tested to ensure that the program functions correctly. Using the **headings given below** to help you, write a test plan for your changes.

|Test Number|Test Description|Test Data|Type|Expected Result|Actual Result|
|-----------|----------------|---------|----|---------------|-------------|
 hello       my               name      is    jack            thomas