import layout;
import menu;

def menu(name,options):
	clear();
	drawHeader(name);
	showOptions(options);
	drawFooter(name);
	ask(options);
	

def clear():
	for i in range(0,layout.CLEAR_SIZE):
		print "";

def drawHeader(name):
	header = "";
	
	for i in range(0,layout.LENGTH):
		header += layout.PATTERN;
		
	header += " " + layout.MENU_NAME + " ";
	
	for i in range(0,layout.LENGTH):
		header += layout.PATTERN;
	
	print header;

def drawFooter():
	footer = "";
	
	for i in range(0,2*layout.LENGTH+2+len(layout.MENU_NAME)):
		footer += layout.PATTERN;
	
	print footer;
	
def showOptions():
	for i in range(0, len(menu.OPTIONS)):
		print(str(i+1)+") "+menu.OPTIONS[i]["label"]);
		
def ask(options):
	opcao = input("Escolha uma opcao: ") - 1;
	if opcao >= 0 and opcao < len(options):
		options[opcao]["action"]();
	elif opcao == -1:
		return;
	else:
		print "Opcao invalida.";
	pause();
	
def pause():
	raw_input("Pressione ENTER para continuar.");
		
