import time

title = u"""
 ▄█     █▄     ▄█    █▄       ▄████████     ███        ▄█    █▄       ▄████████    ▄████████ 
███     ███   ███    ███     ███    ███ ▀█████████▄   ███    ███     ███    ███   ███    ███ 
███     ███   ███    ███     ███    █▀     ▀███▀▀██   ███    ███     ███    █▀    ███    ███ 
███     ███  ▄███▄▄▄▄███▄▄  ▄███▄▄▄         ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███     ███ ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀         ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███     ███   ███    ███     ███    █▄      ███       ███    ███     ███    █▄  ▀███████████ 
███ ▄█▄ ███   ███    ███     ███    ███     ███       ███    ███     ███    ███   ███    ███ 
 ▀███▀███▀    ███    █▀      ██████████    ▄████▀     ███    █▀      ██████████   ███    ███ 
                                                                                  ███    ███ 
             ████████▄   ███    █▄     ▄████████    ▄████████     ███     
             ███    ███  ███    ███   ███    ███   ███    ███ ▀█████████▄ 
             ███    ███  ███    ███   ███    █▀    ███    █▀     ▀███▀▀██ 
             ███    ███  ███    ███  ▄███▄▄▄       ███            ███   ▀ 
             ███    ███  ███    ███ ▀▀███▀▀▀     ▀███████████     ███     
             ███    ███  ███    ███   ███    █▄           ███     ███     
             ███  ▀ ███  ███    ███   ███    ███    ▄█    ███     ███     
              ▀██████▀▄█ ████████▀    ██████████  ▄████████▀     ▄████▀"""

# RUN
#----------------------------------------------------------------------------------------------------
print(title.center(100))
time.sleep(1)


player = {'name':"", 
          'decision': {0:'YorN', 1:'YorN', 2:'YorN'}
          }
questions = {0:"Y: sure y not?\nN: don't worry, I got this :D"
             }

def name():
    # NAME
    player['name'] = input("Hello, what is your name?\n").capitalize()
    print(f"Welcome, {player['name']}.".center(100))

def instructions():
    # OPEN instructionstxt
    finstructions = open("instructions.txt", "r")
    intro_txt_lst = finstructions.read().split('\n')
    finstructions.close()
    
    # OPTIONAL: REMOVE \n ****************
    #while "" in intro_txt_lst:
        #intro_txt_lst.remove("")
    
    num = -1
    for line in intro_txt_lst:
        
        # IF LINE HAS 'DECISION' IN IT, PRINT OUT THE QUESTION
        if line.find('DECISION') > 0:
            num += 1
            question = questions[num]
            # ASK FOR A DECISION and put in player decision dict
            player["decision"][num] = input(f"{question}")
        
        else:
            print(line.center(100))
            
        # DELAY PRINT EVERY LINE
        time.sleep(1.1)
        
    num = -1

    


# OPEN questions.txt
fquestions = open("questions.txt", "r")
q_lst = fquestions.read().split("\n")
fquestions.close()

# PRINT THE QUESTIONS 
num = 0
question = ''
for i in range(len(q_lst)-1):
    
    if q_lst[i].isdigit():
        # put YES/NO question into 1 string
        question += q_lst[i+1] + "\n"
        question += q_lst[i+2] + "\n"
        #print(question)
        
        # put question into dictionary
        questions[num] = question
        
        num += 1
        question = ''

# OPEN story.txt
fstory = open("story.txt", "r")
story_lst = fstory.read().split("\n")
fstory.close() 

def print_lines(story_lst): 
    
    # PRINT story.txt while asking for input on questions
    num = 0
    for line in story_lst:
        if line.find("DECISION") > 0:
            question = questions[num]
            player['decision'][num] = input(f"{question}")
            num += 1
         
        else: 
            print(line.center(100))
            time.sleep(.7)  # Delay of each printed line 
    