
file = open("code.txt", 'r')
numbers = ["0","1","2","3","4","5","6","7","8","9"]
letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
capitalLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

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
   }

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
    "proc":"procedure keyword",
    "arr":"array"}

symbols = {
    ";":"semicolon",
    "{":"open curly bracket",
    "}":"close curly bracket",
    "[":"open square bracket",
    "]":"close square bracket",
    "(":"open bracket",
    ")":"close bracket",
    ",":"comma",
    }

assign = {
    ":=":"assign operator"
    }

def checkIfNumber(i):
    # TODO: check if only a dash
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

def checkIfShortString(i, stringLen):
    shortStrings = [""," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    if stringLen>=16:
        output = "short string is too long"
        file2.write(output)
        return

    elif(i[0] != "\"" or i[len(i)-1] != "\""):
        output = "string read is: "  + i + " returns LEXICAL ERROR- make sure has opening and closing \""+"\n"
        file2.write(output)
    else:
        for k in range(1, len(i)-1):
            if(i[k] in shortStrings or i[k] in numbers or i[k].isspace()):
                continue
            else:
                output = "string read is: "  + i + " returns LEXICAL ERROR-  only capital letters and numbers are allowed and no special characters allowed"+"\n"
                file2.write(output)
                return
        output = "string read is: " + i + " - short string\n"
        file2.write(output)
                
def doCheck(i):
    if(len(i)<=0):
        return
    if i in dataType:
        output = "DataType read is: " + i + " - " + dataType[i] + "\n"
        file2.write(output)
    elif i in binaryOperators:
        output = "Binary Operator read is: "  + i + " - " + binaryOperators[i] + "\n"
        file2.write(output)
    elif i in unaryOperators:
        output = "Unary Operators read is: "  + i + " - " + unaryOperators[i] + "\n"
        file2.write(output)
    elif i in constants:
        output = "Constant read is: "  + i + " - " + constants[i] + "\n"
        file2.write(output)
    elif i in keywords:
        output = "Keyword read is: "  + i + " - " + keywords[i] + "\n"
        file2.write(output)
    elif i in symbols:
        output = "Symbol read is: "  + i + " - " + symbols[i] + "\n"
        file2.write(output)
    elif i[0].isdigit() or i[0]=="-":
        checkIfNumber(i)
    # elif i[0] == "\"":
    #     checkIfShortString(i)
    elif i[0] in letters:
        checkIfUserDefined(i)
    else:
        output = "symbol read is: " + i + " is undefined\n"
        file2.write(output)

output =""
file2 = open("output.txt", "a+")
file2.truncate(0)
topology = file.readlines()
for line in topology:
    line = line.rstrip()
    word = ""
    last=-1
    for i in range(0,len(line)):
        if i<= last:
            continue
        elif line[i] == ":":
            if line[i+1] == "=":
                output = "symbol read is: := - assign operation\n"
                file2.write(output)
                last = i+2
                word=""
        elif line[i] == "\"":
            print("checking for short string", word)
            l = 0
            found = False
            last=0
            for k in range(i,len(line)):
                print(line[k]+"this is our character", found)
                if line[k] != "\"":
                    l+=1
                    word+=line[k]
                    last = k
                else:
                    word+=line[k]
                    found = True
                    last = k
                    if(k >i):
                        print("Checking why we here ", k)
                        break
                   
            if found:
                checkIfShortString(word,l) 
            else:
                output = "No closing \" for "+word
                file2.write(output)       
            i = last
            word=""
        elif(line[i].isspace() or line[i] in symbols):
            if line[i].isspace():
                doCheck(word)
                word = ""
            elif line[i] in symbols:
                doCheck(word)
                doCheck(line[i])
                word = ""
        else: 
            word+=line[i]

            
 