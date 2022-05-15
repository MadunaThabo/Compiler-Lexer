from asyncio.windows_events import NULL
from lexer import Lexer

class Parser:
    def __init__(self):
        pass
    
    def parse(self,fileName="code.txt"):
        tokens = Lexer.run(fileName).tokens
        self.tokenType =  Lexer.run(fileName).tokenTypes
        print("tokens :", tokens, self.tokenType)
        result = self.splProg(tokens)
        print(result)

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
                        return "error: Expected { after main"
                if tokens[i] =="{" and openBracketFound == False:
                    openBracketFound = True
                    indexOpenBracket = i
                if tokens[i] =="halt" and haltFound ==False:
                    haltFound = True
                    indexHalt = i
                    if tokens[i+1] != ";":
                        return "error: Expected ; after halt"
                if tokens[i] ==";" and commaFound ==False:
                    commaFound = True
                    indexComma = i
                if tokens[len(tokens)-1] == "}":
                    closingBracketFound = True
                    indexClosingBracket = len(tokens)-1
                else:
                    return "error: Expected } at the end of program"

            # check all SPLPrgos terminals are found
            if mainFound and openBracketFound and haltFound and commaFound and closingBracketFound == False:
                return "error: not all program terminals( main,{, halt, ; and } ) found"
            # checking for ProcDefs
            list={}
            if(indexMain > 0):
                for index in range(0,indexMain):
                    list[index] = tokens[index]
                print("ProcList", list)
                result = self.procDefs(list, 0)
                if result[0:5] == "error":
                    return result
            
            # check for Algorithm now
            list={}
            realIndex =0
            for index in range(indexOpenBracket+1, indexHalt):
                list[realIndex] = tokens[index]
            result = self.algorithm(list, indexOpenBracket+1)
            if result[0:5] == "error":
                return "error: Algorithm error"
            realIndex +=1
            
            # check for varDecl
            list={}
            realIndex =0
            for index in range(indexComma+1, indexClosingBracket):
                list[realIndex] = tokens[index]
            result = self.varDecl(list, indexComma+1)
            if result[0:5] == "error":
                return "error: VarDecl error"
            realIndex += 1
        else:
            return "error: The program can not have less than 5 tokens"

    def procDefs(self, tokens, indexForTypes):
        commaFound = False
        indexComma = 0
        for i in range(0,len(tokens)):
            if tokens[i] == ",":
                commaFound = True
                indexComma = i
        if(commaFound == False):
            return "error: Expected ,"
        list = {}
        realIndex = 0
        for index in range(0, indexComma):
            list[realIndex] = tokens[index]
            realIndex += 1
        result = self.PD(list, indexForTypes)
        if result[0:5] =="error":
            return result
        if indexComma > len(tokens)-1:
            list = {}
            realIndex = 0
            for index in range(indexComma+1, len(tokens)):
                list[realIndex] = tokens[index]
                realIndex += 1
            result = self.procDefs(list, indexComma+1)
            if result[0:5] == "error":
                return result
        return "continue"

    def PD(self,tokens, indexForTypes):
        semiCollonFound = False
        procFound = False
        userDNameFound = False
        procDefFound = False
        openBracketFound = False
        algorithmFound = False
        returnFound = False
        closingBracketFound = False
        # getting terminal's indexes
        indexSemiCollon = 0
        indexProc = 0
        indexUserDName = 0
        indexOpenBracket = 0
        indexProcDef = 0
        indexAlgorithm = 0
        indexReturn = 0
        indexClosingBracket = 0
        
        for i in range(0,len(tokens)):
            if tokens[i] == "proc" and i == 0 and procFound==False:
                procFound = True
                indexProc = i
                print(self.tokenType)
                print(i+1,"string is",self.tokenType[i+1])
                if self.tokenType[i+1] != "userDefined":
                    return "error: expecting user defined string"
                else:
                    userDNameFound = True
                    indexUserDName = i+1
                    if(tokens[i+2] == "{"):
                        openBracketFound = True
                        indexOpenBracket = i+2
                        #check if we have proc or 
                        if tokens[i+3] == "proc" and procDefFound == False:
                            procDefFound = True
                            indexProcDef = i+3
                            #see if algorithm is next
                            for k in range(i+3, len(tokens)):
                                if  (tokens[k] in {"output","if","do","while","call"} or self.tokenType[i+3] == "userDefined") and algorithmFound == False:
                                    algorithmFound = True
                                    indexAlgorithm = k
                        # algorithm           Assign,Branch,loop, PCsll
            if (tokens[i] in {"output","if","do","while","call"} or self.tokenType[i+3] == "userDefined") and algorithmFound == False:     #probably the token type list ey
                algorithmFound = True
                indexAlgorithm = i+3
            if tokens[i] =="return" and returnFound ==False:
                returnFound =True
                indexReturn = i
                if tokens[i+1] == ";":
                    semiCollonFound = True
                    indexSemiCollon = i+1
                else:
                    return "error: expected ; after return"
            if tokens[len(tokens)-1] =="}":
                closingBracketFound = True
                indexClosingBracket = len(tokens)-1


        print(procFound, userDNameFound, openBracketFound, returnFound, semiCollonFound, closingBracketFound)
        if (procFound and userDNameFound and openBracketFound and returnFound and semiCollonFound and closingBracketFound) == False:
            return "error: PD expects proc userDefinedName { ProcDefs Algorithm return ; VarDecl}"
        
        if procDefFound and algorithmFound:
            list = {}
            realIndex = 0
            for i in range(indexOpenBracket+1, indexAlgorithm):
                list[realIndex] = tokens[i]
            result = self.procDefs(list, indexForTypes + i) #will come back to index for types
            if result[0:5] == "error":
                return result
            list = {}
            realIndex = 0
            for i in range(indexAlgorithm+1, indexReturn):
                list[realIndex] = tokens[i]
            result = self.algorithm(list, indexForTypes + i) #will come back to index for types
            if result[0:5] == "error":
                return result
        elif procDefFound==True and algorithmFound == False:
            list = {}
            realIndex = 0
            for i in range(indexOpenBracket+1, indexAlgorithm):
                list[realIndex] = tokens[i]
            result = self.procDefs(list, indexForTypes + i) #will come back to index for types
            if result[0:5] == "error":
                return result
        elif procDefFound==False and algorithmFound == True:
            list = {}
            realIndex = 0
            for i in range(indexOpenBracket+1, indexReturn):
                list[realIndex] = tokens[i]
            result = self.algorithm(list, indexForTypes + i) #will come back to index for types
            if result[0:5] == "error":
                return result
        return "continue"

    def algorithm(self,tokens,indexForTypes):
       print("algorithm will be implemented soon")
       return "algorithm will be implemented soon"

    def varDecl(self,tokens,indexForTypes):
        # TODO: implement
        print("varDecl Will be implemented soon")
        return "varDecl Will be implemented soon"


    

parser = Parser()
parser.parse()