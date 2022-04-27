def wordCountFromFile():
    fileName=input("Enter the File Name")
    numberOfWords=0
    fileObject=open(fileName,"r")
    for i in fileName:
        words=i.split()
        numberOfWords= numberOfWords+len(words)
    print(numberOfWords)
wordCountFromFile()
    
