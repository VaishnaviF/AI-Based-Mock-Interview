# importing the package  
import language_tool_python  
  
def grammer_check(my_text):
    my_tool = language_tool_python.LanguageTool('en-US')  
    my_matches = my_tool.check(my_text)  
    # defining some variables  
    myMistakes = []  
    myCorrections = []  
    startPositions = []  
    endPositions = []  
    # using the for-loop  
    for rules in my_matches:  
        if len(rules.replacements) > 0:  
            startPositions.append(rules.offset)  
            endPositions.append(rules.errorLength + rules.offset)  
            myMistakes.append(my_text[rules.offset : rules.errorLength + rules.offset])  
            myCorrections.append(rules.replacements[0])  
      
    # creating new object  
    my_NewText = list(my_text)   
      
    # rewriting the correct passage  
    for n in range(len(startPositions)):  
        for i in range(len(my_text)):  
            my_NewText[startPositions[n]] = myCorrections[n]  
            if (i > startPositions[n] and i < endPositions[n]):  
                my_NewText[i] = ""  
      
    my_NewText = "".join(my_NewText)  
      
    # printing the text  
    return my_NewText


if __name__ == '__main__':
    my_text = """LanguageTool provides utility for check grammaring and spelling errors."""   
    grammer_check(my_text)
