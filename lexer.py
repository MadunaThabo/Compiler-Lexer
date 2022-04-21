
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

output =""
file2 = open("output.txt", "a+")
file2.truncate(0)
topology = file.readlines()
for line in topology:
    line = line.rstrip()
    start = 0
    print("reading ", line," ",len(line))
    for i in range(0,len(line)):
        if line[i].isspace():
            file2.write(output)
            start = i+1
            continue 
        elif line[start:i] == "\"":
            print("will define short string soon")
            start = i
            continue
        elif line[start:i] in symbols:
            output = "sysmbol read "  + line[start:i] + " " + symbols[line[start:i]] + " \n"
            file2.write(output)
            start = i
            continue
 