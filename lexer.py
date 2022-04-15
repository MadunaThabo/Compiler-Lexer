from ast import keyword
from asyncio import constants
import operator


def checkIfUserDefined(i):
    print("will be defined")
    
def checkIfNumber(i):
    if(len(i) > 1 and i[0]=="0"):
        output = "string read is: "  + i + "returns LEXICAL ERROR"+"\n"
        file2.write(output)
        return
    elif(i =="0"):
        output = "Symbol read is: "  + i + " - zero - number\n"
        file2.write(output)
    elif(i[0]=="-"):
        if(len(i)<2 and i[1]=="0"):           #example just a dash
            output = "string read is: "  + i + "returns LEXICAL ERROR"+"\n"
            file2.write(output)
            return 
        
        for k in range(1,len(i)):
            if(i[k].isdigit()==False):
                output = "string read is: "  + i + "returns LEXICAL ERROR"+"\n"
                file2.write(output)
                return      
        output = "Symbol read is: "  + i + " - negative number\n"
        file2.write(output)
    else:
        for k in range(len(i)):
            if(i[k].isdigit()==False):
                output = "string read is: "  + i + "returns LEXICAL ERROR"+"\n"
                file2.write(output)
                return      
        output = "Symbol read is: "  + i + " -positive number\n"
        file2.write(output)
    


def checkIfShortString(i):
    print("will be defined")

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
    token = line.split(" ")
    for i in token:
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
        elif i in types:
            output = "Type read is: "  + i + " - " + types[i] + "\n"
            file2.write(output)
        elif i in keywords:
            output = "Keyword read is: "  + i + " - " + keywords[i] + "\n"
            file2.write(output)
        elif i in symbols:
            output = "Symbol read is: "  + i + " - " + symbols[i] + "\n"
            file2.write(output)
        else:
            checkIfUserDefined(i)
            checkIfNumber(i)
            checkIfShortString(i)
            # i.split("\n")
            # i = i[0]
            # output = "string read is: "  + i + "returns LEXICAL ERROR"+"\n"
            # file2.write(output)
file.close()
file2.close()
