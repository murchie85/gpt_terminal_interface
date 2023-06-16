import openai
import getch
import os
from termcolor      import colored, cprint 
from art            import *
import os
import subprocess

# UPDATE ME TO YOUR KEY
keyLocation    = '/Users/adammcmurchie/code/gpt/.key.txt'

# VARIABLES
OPENAI_API_KEY = open(keyLocation,'r').read()
openai.api_key = OPENAI_API_KEY
temperature    = 1.2
max_tokens     = 4096
promptFile     = 'promptFile.txt'
convoHistory   = 'convoHistory.txt'





def welcome():
    os.system('clear')
    welcomeMessage=text2art("Welcome")
    wmessage=text2art("Harness V 0.1")
    cprint(welcomeMessage,'cyan')
    cprint(wmessage,'cyan')
welcome()


def getModelType():
    modelTypes     = ["gpt-3.5-turbo","gpt-4"]
    print("""
    1. GPT-3.5
    2. GPT-4
    """)
    modelChoiceIndex = ''
    while(type(modelChoiceIndex) != int):
        print("Please choose a model.")
        modelChoiceIndex = getch.getch()
        try:
            modelChoiceIndex = int(modelChoiceIndex)
        except:
            print('Please select a number.')
            print(type(modelChoiceIndex))

    welcome()
    modelType = modelTypes[modelChoiceIndex-1]

    print('\n\n\n')
    cprint(modelType + ' selected.\n','white')
    input("\nPress any key to continue")
    welcome()
    cprint(modelType + ' selected.\n','white')

    return(modelType)

def getSystemMessage():
    systemType     = ["You are a beta reader, proof reader and book critic.", 
                      "You are a helpfull assistant,",
                      "You are a coding assistant."]

    for i in range(1,len(systemType)+1):
        print(str(i) + '. ' + str(systemType[i-1]))


    sysMsgIndex = ''
    while(type(sysMsgIndex) != int):
        print("Please choose a model.")
        sysMsgIndex = getch.getch()
        try:
            sysMsgIndex = int(sysMsgIndex)
        except:
            print('Please select a number.')
            print(type(sysMsgIndex))

    welcome()
    systemMessage = systemType[sysMsgIndex-1]

    print('\n\n\n')
    cprint(systemMessage + ' selected.\n','white')
    input("\nPress any key to continue")

    welcome()

    return(systemMessage)



def createPrompt():
    indx = ''
    while(type(indx) != int):
        print("How Do you want to respond?")
        print('[1]: Type here in terminal')
        print('[2]: Paste into a doc')
        
        indx = getch.getch()
        try:
            indx = int(indx)
        except:
            print('Please select a number.')
            print(type(indx))

    if(indx==1):
        print('\n\n')
        promptMessage = input("Please type your reply here. \n\n")
    elif(indx==2):
        print('empty prompt file')
        with open(promptFile, 'w') as file:
            file.write('')
        
        subprocess.run(['subl', promptFile])
        cprint("Press enter when complete",'yellow')
        input('Complete?\n')
        promptMessage = open(promptFile,'r').read()
    else:
        print('No choice selected')
        exit()



    return(promptMessage)



def callModel(modelType,systemMesssage,userMessage,debug=False):

    messageList = [
        {"role": "system", "content": systemMesssage},
        {"role": "user", "content": userMessage}
    ]
    if(debug):
        print("Message List is: ")
        print(messageList)

    # Call the GPT-4 model
    response = openai.ChatCompletion.create(
        model=modelType,
        messages=messageList
    )

    currentResponse = response['choices'][0]['message']['content'].lstrip()

    # Print the response
    if(debug):
        print('---   response-----\n\n\n')
        cprint(response,'blue')
    if(debug):
        print('---parsed response-----\n\n\n')
    
    cprint(currentResponse,'white')

    return(currentResponse)



modelType      = getModelType()
systemMesssage = getSystemMessage()
promptMessage  = createPrompt()


msgHistory = promptMessage
while(True):
    response    = callModel(modelType,systemMesssage,msgHistory)
    msgHistory += response + '\n'

    # SAVING CONVO HISTORY
    with open(convoHistory, 'w') as file:
        file.write(msgHistory)

    # GET USER NEXT PROMPT
    promptMessage  = createPrompt()
    msgHistory += promptMessage + '\n'




