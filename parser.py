from asyncio.windows_events import NULL
from operator import contains
from tokenize import Triple
from lexer import Lexer
from lexer import checkIfUserDefined

class Parser:
    def __init__(self):
        pass
    
    def parse(self,fileName="code.txt"):
        try:
            self.parserOutputfile = open("parserOutput.xml", "w+")
        except IOError:
            print("error: The file does not exist")
            return "error: File not found"
        tokens = Lexer.run(fileName).tokens
        self.parserOutputfile.truncate(0)
        self.tokenType =  Lexer.run(fileName).tokenTypes
        # print("tokens :", tokens, self.tokenType)
        result = self.splProg(tokens, 0)
        print(result)

    def splProg(self, tokens, indentation):
        self.parserOutputfile.write("<splProg>\n")
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
                if tokens[i] =="{" and openBracketFound == False and tokens[i-1]=="main":
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
                result = self.procDefs(list, 0, indentation + 1)
                if result[0:5] == "error":
                    return result
            
            # check for Algorithm now
            list={}
            realIndex =0
            for index in range(indexOpenBracket+1, indexHalt):
                list[realIndex] = tokens[index]
                realIndex +=1
            result = self.algorithm(list, indexOpenBracket+1, indentation+1)
            if result[0:5] == "error":
                return "error: Algorithm error"
            realIndex +=1
            
            # check for varDecl
            list={}
            realIndex =0
            for index in range(indexHalt+2, indexClosingBracket):
                list[realIndex] = tokens[index]
                realIndex +=1
            result = self.varDecl(list, indexComma+1, indentation + 1)
            if result[0:5] == "error":
                return "error: VarDecl error"
            realIndex += 1
        else:
            return "error: The program can not have less than 5 tokens"
        self.parserOutputfile.write("</splProg>\n")

    def procDefs(self, tokens, indexForTypes, indentation):
        print("procdef", tokens)
        tabs = ""
        for i in range(0, indentation):
            tabs += "\t"
        self.parserOutputfile.write(tabs+"<procDefs>\n")
        #split our ProcDefs
        procCount = 0
        procList = []
        indexes =[0]
        tempList = []
        commaFound = False
        indexComma = 0
        for i in range(0, len(tokens)):
            # if i == len(tokens)-1:
            #     indexes.append(i)
            # print("checking", tokens[i], i, procCount)
            if tokens[i]=="{" and tokens[i-2]=="proc":
                procCount +=1
                # print(i, "We at ProcDefs")
            elif tokens[i] == "," and tokens[i-1] =="}":
                # print("closing a proc", i)
                procCount -=1
                if procCount == 0:
                    indexes.append(i)
        realIndex = 0
        print(len(indexes), indexes)
        for i in range(0,len(indexes)):
            if i+1 < len(indexes):
                if i != 0:
                    for j in range(indexes[i]+1,indexes[i+1]+1):
                        tempList.append(tokens[j])
                    procList.append(tempList)
                else:
                    for j in range(indexes[i],indexes[i+1]+1):
                        tempList.append(tokens[j])
                    procList.append(tempList)
                tempList = []
       #call PD 
        ind = 0
        for item in procList:
            if ind == 0:
                result = self.PD(item, indexes[ind], indentation + 1) 
                if result[0:5] == "error":
                    return result
                # else: return "continue"
            else:
                result = self.PD(item, indexes[ind]+1, indentation + 1)
                if result[0:5] == "error":
                    return result
                # else: return "continue"
            ind += 1
        # self.parserOutputfile.write(tabs+"</procDefs>\n")
        return "continue"

  

    def PD(self,tokens, indexForTypes, indentation):
        # TODO: Check when you put another proc after the Thabo proc....something is wrong there might be ProcDefs
        print("PD", tokens)
        tabs = ""
        for i in range(0, indentation):
            tabs += "\t"
        self.parserOutputfile.write(tabs+"<PD>\n")
        # return "will be implemented"
        semiCollonFound = False
        commaFound = False
        procFound = False
        userDNameFound = False
        procDefFound = False
        openBracketFound = False
        algorithmFound = False
        returnFound = False
        closingBracketFound = False
        varDeclFound = False
        # getting terminal's indexes
        indexSemiCollon = 0
        indexProc = 0
        indexUserDName = 0
        indexOpenBracket = 0
        indexProcDef = 0
        indexAlgorithm = 0
        indexReturn = 0
        indexClosingBracket = 0
        indexComma = 0
        indexVarDecl = 0
        endIndexProcDef = 0
        procList = []
        algorithmList = []
        procCount = 0

        #check for proc userDefined and open bracket
        print("index for types: ", indexForTypes)
        if tokens[0] != "proc":
            return "error: string expected to start with proc"
        elif tokens[0] == "proc":
            procFound = True
            indexProc = 0
        if checkIfUserDefined(tokens[1]) !=True:   #self.tokenType[indexForTypes+1] !="userDefined":
            return "error: expected user defined name after proc"
        elif  checkIfUserDefined(tokens[1]) == True:    #self.tokenType[indexForTypes+1] =="userDefined":
            userDNameFound = True
            indexUserDName = 1
        if tokens[2]  != "{":
            return "error: expected { after "+ tokens[1]
        elif tokens[2] == "{":
            openBracketFound = True
            indexOpenBracket = 2
        # Check for procDefs
        if tokens[3] == "proc":
            procDefFound = True
            indexProcDef = 3
            print(tokens[3])
        for i in range(3, len(tokens)):
            if tokens[i] == "return" :
                returnFound = True
                indexReturn = i
        if returnFound == False:
            return "error: expected return not found"
        # check for algorithm I guess
        if procDefFound == True:
            for i in range(3, indexReturn):
                 if tokens[3] in   {"output","if","do","while","call"} or (self.tokenType[indexForTypes+3] == "userDefined" and tokens[i-1] != "proc") :
                    algorithmFound = True
                    indexAlgorithm = i
                    print("got algorithm: ", indexAlgorithm)
        else:
            if tokens[3] in   {"output","if","do","while","call"} or checkIfUserDefined(tokens[3]) == True: #will have to make sure
                algorithmFound = True
                indexAlgorithm = 3

        if tokens[3] == "return":
            algorithmFound = False
            procDefFound = False
            indexAlgorithm = 0
            indexProcDef = 0
         # for i in range(3, len(tokens)):
        #     if tokens[i] == "proc":
        #         procCount += 1
        #     if tokens[i] == "}" and tokens[i+1] == ",":
        #         procCount -+1
        #     if tokens[i] in   {"output","if","do","while","call"} or (i+1 < len(tokens) and self.tokenType[indexForTypes+i] == "userDefined" and tokens[i+1] != "{" and tokens[i-1] != "proc" ) and procCount == 0: #will have to make sure
        #         endIndexProcDef = i-1
        #         algorithmFound = True
        #         indexAlgorithm = i
        #         break

        if tokens[indexReturn+1] == ";":
            semiCollonFound = True
            indexSemiCollon = indexReturn+1
        else: return "error: Expected ; after return not found"
        if tokens[indexSemiCollon+1] != "}":
            varDeclFound = True
            indexVarDecl = indexSemiCollon +1
        if tokens[len(tokens)-2] == "}":
            closingBracketFound = True
            indexClosingBracket = len(tokens)-2
        else: return "error: expected } is not found"
        if tokens[indexClosingBracket+1] == ",":
            commaFound = True
            indexComma = indexClosingBracket + 1
        else: return "error: expected , afte } not found"

        print(indexProc, indexUserDName, indexOpenBracket, indexProcDef, indexAlgorithm, indexReturn, indexSemiCollon, indexClosingBracket)
        print(procFound, userDNameFound, openBracketFound, procDefFound, algorithmFound, returnFound, semiCollonFound, closingBracketFound)

        # have both procDef and  algorithm
        if procDefFound == True and algorithmFound == True:
            tempList = []
            for i in range(indexOpenBracket+1, indexAlgorithm):
                tempList.append(tokens[i])
            # print("procList lists1: ", tempList )
            result = self.procDefs(tempList, indexForTypes + indexOpenBracket+ 1, indentation+1)
            if result[0:5] == "error":
                return result
            tempList = []
            for i in range(indexAlgorithm, indexReturn):
                tempList.append(tokens[i])
            print("algorithm lists1: ", tempList )   
            result = self.algorithm(tempList, indexForTypes + indexAlgorithm+ 1, indentation+1)
            if result[0:5] == "error":
                return result
        # we have procDef and not algorithm
        elif procDefFound ==True and algorithmFound == False:
            tempList = []
            for i in range(indexOpenBracket+1, indexReturn):
                tempList.append(tokens[i])
            # print("procList lists2: ", tempList )
            result = self.procDefs(tempList, indexForTypes + indexOpenBracket+ 1, indentation+1)
            if result[0:5] == "error":
                return result
        # we have no procDef but we have algorithm
        elif procDefFound ==False and algorithmFound == True:
            tempList = []
            for i in range(indexOpenBracket+1, indexReturn):
                tempList.append(tokens[i])
            print("algorithm lists2:.................. ", tempList ) 
            result = self.algorithm(tempList, indexForTypes + indexOpenBracket+ 1, indentation+1)
            if result[0:5] == "error":
                return result

        # for i in range(3, len(tokens)):
        #     if tokens[i] == "proc":
        #         if i ==3:
        #             indexProc = 3
        #             procFound == True
        #         procCount += 1
        #     if tokens[i] == "}" and tokens[i+1] == ",":
        #         procCount -=1
        #     # check for algorithm, will also be used for procDefs
        #     if tokens[i] in   {"output","if","do","while","call"} or (i+1 < len(tokens) and self.tokenType[indexForTypes+i] == "userDefined" and tokens[i+1] != "{" and tokens[i-1] != "proc" ) and procCount == 1: #will have to make sure
        #         algorithmFound = True
        #         indexAlgorithm = i
        #     # make sure it is the last return 
        #     elif tokens[i] == "return" and procCount == 1:
        #         returnFound = True
        #         indexReturn = i
        #         if returnFound == False:
        #             return "error: expecting return in proc scope"
        #         #check if a semicolon follows it
        #         else: 
        #             if tokens[i+1] != ";":
        #                 return "error: expecting ; after return"
        #             elif tokens[i+1] == ";":
        #                 semiCollonFound = True
        #                 indexSemiCollon = i+1
        #     if tokens[i] == "}" and procCount == 0:
        #         closingBracketFound = True
        #         indexClosingBracket = i
        #         if tokens[i+1] != ",":
        #             return "error: expected , after }"
        #         else:
        #             commaFound = True
        #             indexComma = i+1
        # We have procDefs and  algorithm
        # if indexOpenBracket+1 != indexAlgorithm and indexAlgorithm != 0 :
        #     tempList = []
        #     for i in range(indexOpenBracket+1, indexAlgorithm):
        #         tempList.append(tokens[i])
        #     result = self.procDefs(tempList, indexForTypes + indexOpenBracket+ 1, indentation+1)
        #     if result[0:5] == "error":
        #         return result
        #     tempList = []
        #     for i in range(indexAlgorithm, indexReturn):
        #         tempList.append(tokens[i])
        #     result = self.algorithm(tempList, indexForTypes + indexAlgorithm, indentation+1)
        #     if result[0:5] == "error":
        #         return result
        # elif algorithmFound == False and procDefFound == True:
        #     tempList = []
        #     for i in range(indexOpenBracket+1, indexReturn):
        #         tempList.append(tokens[i])
        #     result = self.procDefs(tempList, indexForTypes + indexOpenBracket+ 1, indentation+1)
        #     if result[0:5] == "error":
        #         return result 
        # elif algorithmFound == True and procDefFound == False:
        #     tempList = []
        #     for i in range(indexAlgorithm, indexReturn):
        #         tempList.append(tokens[i])
        #     result = self.algorithm(tempList, indexForTypes + indexAlgorithm, indentation+1)
        #     if result[0:5] == "error":
        #         return result
            # now we take the varDecl
            # if indexSemiCollon + 1 != indexClosingBracket:
            #     tempList = []
            #     for i in range(indexAlgorithm, indexReturn):
            #         tempList.append(tokens[i])
            #     result = self.varDecl(tempList, indexForTypes + indexAlgorithm, indentation+1)
            #     if result[0:5] == "error":
            #         return result
          
        return "continue"

    def algorithm(self,tokens,indexForTypes, indentation):
        print("algorithm will be implemented soon", tokens)
        tabs = ""
        for i in range(0, indentation):
            tabs += "\t"
        self.parserOutputfile.write(tabs+"<Algorithm>\n")
        return "algorithm will be implemented soon"

    def varDecl(self,tokens,indexForTypes, indentation):
        # TODO: implement
        print("varDecl Will be implemented soon", tokens)
        tabs = ""
        for i in range(0, indentation):
            tabs += "\t"
        self.parserOutputfile.write(tabs+"<VarDecl>\n")
        return "varDecl Will be implemented soon"


    

parser = Parser()
parser.parse()