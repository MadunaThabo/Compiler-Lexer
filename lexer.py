class Lexer:
    def run(fileName="code.txt"):
        file = open(fileName, 'r')
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

        tokens =[]
        errorLine = 0
        def checkIfNumber(i):
            # TODO: check if only a dash
            if(len(i) > 1 and i[0]=="0"):
                output = "Number read is: "  + i + "returns LEXICAL ERROR"+"\n"
                file2.write(output)
                print(output, "on line",errorLine); quit()
                return
            elif(i =="0"):
                output = "Number read is: "  + i + " - zero - number\n"
                file2.write(output)
                tokens.append(i)
            elif(i[0]=="-"):
                if(len(i)<2 and i[1]=="0"):           #example just a dash
                    output = "Number read is: "  + i + "returns LEXICAL ERROR"+"\n"
                    file2.write(output)
                    print(output, "on line",errorLine); quit()
                    return 
                
                for k in range(1,len(i)):
                    if(i[k].isdigit()==False):
                        output = "Number read is: "  + i + "returns LEXICAL ERROR"+"\n"
                        file2.write(output)
                        print(output, "on line",errorLine); quit()
                        return      
                output = "Number read is: "  + i + " - negative number\n"
                file2.write(output)
                tokens.append(i)
            else:
                for k in range(len(i)):
                    if(i[k].isdigit()==False):
                        output = "string read is: "  + i + "returns LEXICAL ERROR"+"\n"
                        file2.write(output)
                        print(output, "on line",errorLine); quit()
                        return     
                output = "Symbol read is: "  + i + " - positive number\n"
                file2.write(output)
                tokens.append(i)

        def checkIfUserDefined(i):
            letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            numbers = ["0","1","2","3","4","5","6","7","8","9"]
            if(i[0].isdigit()==True and i[0] not in letters):
                output = "string read is: "  + i + " returns LEXICAL ERROR\n"
                file2.write(output)
                print(output, "on line",errorLine); quit()
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
                        print(output, "on line",errorLine); quit()
                        return
                output = "Symbol read is: "  + i + " - User Defined name\n"
                file2.write(output)
                tokens.append(i)

        def checkIfShortString(i, stringLen):
            shortStrings = [""," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            numbers = ["0","1","2","3","4","5","6","7","8","9"]
            if stringLen>=16:
                output = "short string read "+i+" is too long\n"
                file2.write(output)
                print(output, "on line",errorLine); quit()
                return

            elif(i[0] != "\"" or i[len(i)-1] != "\""):
                output = "string read is: "  + i + " returns LEXICAL ERROR- make sure has opening and closing \""+"\n"
                file2.write(output)
                print(output, "on line",errorLine); quit()
            else:
                for k in range(1, len(i)-1):
                    if(i[k] in shortStrings or i[k] in numbers or i[k].isspace()):
                        continue
                    else:
                        output = "string read is: "  + i + " returns LEXICAL ERROR-  only capital letters and numbers are allowed and no special characters allowed"+"\n"
                        file2.write(output)
                        print(output, "on line",errorLine); quit()
                        return
                output = "string read is: " + i + " - short string\n"
                tokens.append(i)
                file2.write(output)
                        
        def doCheck(i):
            if(len(i)<=0):
                return
            if i in dataType:
                output = "DataType read is: " + i + " - " + dataType[i] + "\n"
                file2.write(output)
                tokens.append(i)
            elif i in binaryOperators:
                output = "Binary Operator read is: "  + i + " - " + binaryOperators[i] + "\n"
                file2.write(output)
                tokens.append(i)
            elif i in unaryOperators:
                output = "Unary Operators read is: "  + i + " - " + unaryOperators[i] + "\n"
                file2.write(output)
                tokens.append(i)
            elif i in constants:
                output = "Constant read is: "  + i + " - " + constants[i] + "\n"
                file2.write(output)
                tokens.append(i)
            elif i in keywords:
                output = "Keyword read is: "  + i + " - " + keywords[i] + "\n"
                file2.write(output)
                tokens.append(i)
            elif i in symbols:
                output = "Symbol read is: "  + i + " - " + symbols[i] + "\n"
                file2.write(output)
                tokens.append(i)
            elif i[0].isdigit() or i[0]=="-":
                checkIfNumber(i)
            # elif i[0] == "\"":
            #     checkIfShortString(i)
            elif i[0] in letters:
                checkIfUserDefined(i)
            else:
                output = "symbol read is: " + i + " is undefined\n"
                file2.write(output)
                print(output, "on line",errorLine); quit()

        output =""
        file2 = open("output.txt", "a+")
        file2.truncate(0)
        topology = file.readlines()
        for line in topology:
            errorLine +=1
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
                        tokens.append(line[i]+line[i+1])
                        last = i+2
                        word=""
                elif line[i] == "\"":
                    l = 0
                    found = False
                    last=0
                    for k in range(i,len(line)):
                        if line[k] != "\"":
                            l+=1
                            word+=line[k]
                            last = k
                        else:
                            word+=line[k]
                            found = True
                            last = k
                            if(k >i):
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
                        # tokens.append(line[i])
                        doCheck(word)
                        word = ""
                    elif line[i] in symbols:
                        doCheck(word)
                        doCheck(line[i])
                        word = ""
                elif i ==len(line)-1:
                    doCheck(word+line[i])
                else: 
                    word+=line[i]
        return tokens