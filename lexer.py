
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
    ":=":"assign operator"
    }

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


def checkIfShortString(i):
    shortStrings = [""," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    if len(i)>=16:
        output = "short string is too long"
        file2.write(output)
        return

    if(i[0] != "\"" or i[len(i)-1] != "\""):
        output = "string read is: "  + i + " returns LEXICAL ERROR- make sure has opening and closing \""+"\n"
        file2.write(output)
    else:
        for k in range(1, len(i)-1):
            if(i[k] not in shortStrings or i[k] not in numbers or i[k].isspace() == False ):
                output = "string read is: "  + i + " returns LEXICAL ERROR-  only capital letters are allowed and no special characters allowed"+"\n"
                file2.write(output)
                return
            else:
                continue
        output = "string read is: " + i + " - short string"
                

def doCheck(i):
    print("in do check: ", i,"is being checked")
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
    elif i[0] == "\"":
        checkIfShortString(i)
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
    for i in range(0,len(line)):
        # print("word is: ",word)
        # if line[i] == "\"":
        #     l = 0
        #     found = False
        #     for k in range(i,len(line)):
        #         if line[k] != "\"":
        #             l+=1
        #             word+=line[k]
        #         else:
        #             word+=line[k]
        #             found = True
        #             break
        #     if found:
        #         checkIfShortString(word,l)        
        #     i = k
        if(line[i].isspace() or line[i] in symbols):
            if line[i].isspace():
                doCheck(word)
                word = ""
                print("got space")
            elif line[i] in symbols:
                doCheck(word)
                doCheck(line[i])
                word = ""
        else: 
            word+=line[i]

        
        
        # if line[i].isspace() or line[start:3] in symbols or line[i] in symbols or line[i] in numbers:
        #     if line[i].isspace():
        #         print("start assigned at space", i, line[i])
        #         output = "space read\n"
        #         file2.write(output)
        #         start = i+1

        #     elif line[i]==":":
        #         if i+1<len(line) and line[i+1]=="=":
        #             output = "assign operator: "+ line[start:i+1] + "\n"
        #             print("assign Start is: ", i," : ", line[start+1])
        #             file2.write()
        #         else:
        #             output = "lexor error: "+ line[i] + "\n"
        #             file2.write(output)
        #     elif line[i] in symbols:
        #         output = "Symbol: "+ line[i] + "\n"
        #         start = i
        #         print("symbol Start is: ", i," : ", line[start])
        #         file2.write(output)

        #     elif line[i] in numbers:
        #         output = "number: "+ line[i] + "\n"
        #         start = i+1
        #         print("number Start is: ", i," : ", line[start])
        #         file2.write(output)

        #     elif line[start:i] in unaryOperators:
        #         print("checking word: ", line[start:i])
        #         output = "Unary operator: "+ line[start:i] + "\n"
        #         start = i
        #         print("unary Start is: ", i," : ", line[start])
        #         file2.write(output)

            
 