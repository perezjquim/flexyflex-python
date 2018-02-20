import layout;
import menu;
import messages;

def menu(name,options):
	clear();
	drawHeader(name);
	showOptions(options);
	drawFooter(name);
	ask(name,options);

def clear():
	for i in range(0,layout.CLEAR_SIZE):
		print "";

def drawHeader(name):
	header = "";
	
	for i in range(0,layout.LENGTH):
		header += layout.PATTERN;
		
	header += " " + name + " ";
	
	for i in range(0,layout.LENGTH):
		header += layout.PATTERN;
	
	print header;

def drawFooter(name):
	footer = "";
	
	for i in range(0,2*layout.LENGTH+2+len(name)):
		footer += layout.PATTERN;
	
	print footer;
	
def showOptions(options):
	for i in range(0, len(options)):
		print(str(i+1)+") "+options[i]["label"]);
	print("0) " + messages.EXIT);
		
def ask(name,options):
	opcao = input(messages.ASK) - 1;
	if opcao >= 0 and opcao < len(options):
		options[opcao]["action"]();
	elif opcao == -1:
		return;
	else:
		print messages.INVALID;
	pause();
	menu(name,options);
	
def pause():
	raw_input(messages.PAUSE);
		
