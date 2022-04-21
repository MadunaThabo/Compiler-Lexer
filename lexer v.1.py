# from ast import keyword
# from asyncio import constants



def checkIfUserDefined(i):
    letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    if(i[0].isdigit()==True and i[0] not in letters):
        output = "string read is: "  + i + " returns LEXICAL ERROR\n"
        file2.write(output)
        return
    else:
        for k in range(0,len(i)):
            if(i[k] in letters):
                continue
            elif(i[k] in numbers):
                continue
            else:
                output = "string read is: " + i + "returns Lexical Error\n"
                file2.write(output)
                return
        output = "Symbol read is: "  + i + " - User Defined name\n"
        file2.write(output)
            


                
    
def checkIfNumber(i):
    if(len(i) > 1 and i[0]=="0"):
        output = "Number read is: "  + i + "returns LEXICAL ERROR"+"\n"
        file2.write(output)
        return
    elif(i =="0"):
        output = "Number read is: "  + i + " - zero - number\n"
        file2.write(output)
    elif(i[0]=="-"):
        if(len(i)<2 and i[1]=="0"):           #example just a dash
            output = "Number read is: "  + i + "returns LEXICAL ERROR"+"\n"
            file2.write(output)
            return 
        
        for k in range(1,len(i)):
            if(i[k].isdigit()==False):
                output = "Number read is: "  + i + "returns LEXICAL ERROR"+"\n"
                file2.write(output)
                return      
        output = "Number read is: "  + i + " - negative number\n"
        file2.write(output)
    else:
        for k in range(len(i)):
            if(i[k].isdigit()==False):
                output = "string read is: "  + i + "returns LEXICAL ERROR"+"\n"
                file2.write(output)
                return     
        output = "Symbol read is: "  + i + " - positive number\n"
        file2.write(output)
    


def checkIfShortString(i):
    shortStrings = [""," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]

    if(i[0] != "\"" or i[len(i)-1] != "\""):
        output = "string read is: "  + i + " returns LEXICAL ERROR- make sure has opening and closing \""+"\n"
        file2.write(output)
    else:
        for l in range(0, len(i)-1):
            if(i[l] not in shortStrings or i[l] not in numbers ):
                output = "string read is: "  + i + " returns LEXICAL ERROR-  only capital letters are allowed and no special characters allowed"+"\n"
                file2.write(output)
            else:
                output = i + "short string will be defined\n"
                file2.write(output)
                print(i,"short string will be defined")

file = open("code.txt", 'r')

dataType = {
    "num":"number",
    "string":"text string",
    "bool":"boolean"}
binaryOperators = {
    "and":"and operator",
    "or":"or operator",
    "eq":"equal operator",
    "larger":"larger operator",
    "add":"addition operator",
    "sub":"subtraction operator",
    "mult":"multiplication operator"}
unaryOperators = {
    "input":"input operation",
    "not":"not operation",
    ":=":"assign operator"}
constants = {
    "true":"true boolean",
    "false":"false boolean"}
keywords = {
    "main":"main keyword",
    "if":"if keyword",
    "then":"then keyword",
    "else":"else keyword",
    "do":"do keyword",
    "until":"until keyword",
    "while":"while keyword",
    "output":"output keyword",
    "halt":"halt keyword",
    "return":"return keyword",
    "proc":"procedure keyword"}
types = {
    "arr":"array"}
symbols = {
    ";":"semicolon",
    "{":"open curly bracket",
    "}":"close curly bracket",
    "[":"open square bracket",
    "]":"close square bracket",
    "(":"open bracket",
    ")":"close bracket",
    ",":"comma"
    }

output = ""
file2 = open("output.txt", "a+")
file2.truncate(0)
topology = file.readlines()
for line in topology:
    line = line.rstrip()
    token = line.split(" ")
    for i in token:
        if i in dataType:
            output = "DataType read is: " + i + " - " + dataType[i] + "\n"
            file2.write(output)
            continue
        elif i in binaryOperators:
            output = "Binary Operator read is: "  + i + " - " + binaryOperators[i] + "\n"
            file2.write(output)
            continue
        elif i in unaryOperators:
            output = "Unary Operators read is: "  + i + " - " + unaryOperators[i] + "\n"
            file2.write(output)
            continue
        elif i in constants:
            output = "Constant read is: "  + i + " - " + constants[i] + "\n"
            file2.write(output)
            continue
        elif i in types:
            output = "Type read is: "  + i + " - " + types[i] + "\n"
            file2.write(output)
            continue
        elif i in keywords:
            output = "Keyword read is: "  + i + " - " + keywords[i] + "\n"
            file2.write(output)
            continue
        elif i in symbols:
            output = "Symbol read is: "  + i + " - " + symbols[i] + "\n"
            file2.write(output)
            continue
        elif (i[0] == "\""):
            checkIfShortString(i)
        elif i[0].isdigit() or i[0]=="-":
            checkIfNumber(i)
        else:
            checkIfUserDefined(i)
    
file.close()
file2.close()
