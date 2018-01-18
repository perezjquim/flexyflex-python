import random;

def randgen():
	print "Generated random number: " + str(random.random());

def guessaguess():
	LOW = 1;
	HIGH = 5;
	solution = random.randint(LOW,HIGH);
	print "The objective of this game is to guess a number that's between " + str(LOW) + " and " + str(HIGH);
	while (raw_input("Pick a number between " + str(LOW) + " and " + str(HIGH) + ": ") != str(solution)):
		continue;
	print "YOU GOT IT!";
	
def smalltalk():
	print "Hello darling!";
	raw_input();
	print "How are you?";
	raw_input();
	print "Glad! I am fine too!";
	raw_input();
	print "Ok! Bye!";

OPTIONS = [
	{ "label" : "Random number generator",	"action": randgen },
	{ "label" : "Guess-a-guess",						"action": guessaguess },
	{ "label" : "Small talk with a dumb bot",	"action": smalltalk }
];



