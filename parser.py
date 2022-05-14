from asyncio.windows_events import NULL
from lexer import Lexer

class Parser:
    def __init__(self):
        pass
    
    def parse(self,fileName="code.txt"):
        tokens = Lexer.run(fileName)
        print("tokens :", tokens)
        result = self.splProg(tokens)

    def splProg(self, tokens):
        i=0
        indexMain = 0
        indexOpenBracket = 0
        indexHalt = 0
        indexComma = 0
        indexClosingBracket = 0
        mainFound= False
        openBracketFound = False
        haltFound = False
        commaFound = False
        closingBracketFound = False
        if len(tokens)>=5:
            for i in range(0,len(tokens)):
                if tokens[i] =="main" and mainFound ==False:
                    mainFound = True
                    indexMain = i
                    if tokens[i+1] != "{":
                        print("error: Expected { after main")
                        return "error: Expected { after main"
                if tokens[i] =="{" and openBracketFound == False:
                    openBracketFound = True
                    indexOpenBracket = i
                if tokens[i] =="halt" and haltFound ==False:
                    haltFound = True
                    indexHalt = i
                    if tokens[i+1] != ";":
                        print("error: Expected ; after halt")
                        return "error: Expected ; after halt"
                if tokens[i] ==";" and commaFound ==False:
                    commaFound = True
                    indexComma = i
                if tokens[len(tokens)-1] == "}":
                    closingBracketFound = True
                    indexClosingBracket = len(tokens)-1
                else:
                    print("error: Expected } at the end of program")
                    return "error: Expected } at the end of program"

            # check all SPLPrgos terminals are found
            if mainFound and openBracketFound and haltFound and commaFound and closingBracketFound == False:
                return "error: not all program terminals( main,{, halt, ; and } ) found"
            # checking for ProcDefs
            list={}
            if(indexMain > 0):
                for index in range(0,indexMain):
                    list[index] = tokens[index]
                result = self.procDefs(list)
                if result[0:5] == "error":
                    return "error:ProcDef error"
            
            # check for Algorithm now
            list={}
            realIndex =0
            for index in range(indexOpenBracket+1, indexHalt):
                list[realIndex] = tokens[index]
            result = self.algorithm(list)
            if result[0:5] == "error":
                return "error: Algorithm error"
            realIndex +=1
            
            # check for varDecl
            realIndex =0
            for index in range(indexComma+1, indexClosingBracket):
                list[realIndex] = tokens[index]
            result = self.varDecl(list)
            if result[0:5] == "error":
                return "error: VarDecl error"
            realIndex += 1
        else:
            return "The program can not have less than 5 tokens"

    def procDefs(self, i):
        print("procdefs will be implemented soon")
        return "procdefs will be implemented soon"
        
    def algorithm(self,i):
       print("algorithm will be implemented soon")
       return "algorithm will be implemented soon"

    def varDecl(self,i):
        # TODO: implement
        print("varDecl Will be implemented soon")
        return "varDecl Will be implemented soon"


    

parser = Parser()
parser.parse()