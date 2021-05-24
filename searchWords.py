introString=input("Enter your word you want to search")
print(introString)
characterCount = 0
wordCount = 1
for character in introString:
    characterCount=characterCount+1
    if(character==' '):
        wordCount=wordCount+1
print(wordCount)
print(characterCount)