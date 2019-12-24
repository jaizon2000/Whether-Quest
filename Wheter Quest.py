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
              ▀██████▀▄█ ████████▀    ██████████  ▄████████▀     ▄████▀   
                                                                            
                                                                                 
                                                 

                                                                                                             
"""

# RUN
#----------------------------------------------------------------------------------------------------
print(title.center(100))
time.sleep(1)


player = {'name':"", 'decision': {0:'YorN', 1:'YorN', 2:'YorN'}}
questions = {0:"Y: sure y not?\nN: don't worry, I got this :D"}

def name():
    # NAME
    player['name'] = input("Hello, what is your name?\n").capitalize()
    print(f"Welcome, {player['name']}.".center(100))

def instructions():
    # OPEN storyBefore.txt
    intro_file = open("instructions.txt", "r")
    intro_txt_lst = intro_file.read().split('\n')
    intro_file.close()
    
    # OPTIONAL: REMOVE \n
    #while "" in intro_txt_lst:
        #intro_txt_lst.remove("")
    
    num = -1
    for line in intro_txt_lst:
        
        # IF LINE HAS 'DECISION' IN IT, PRINT OUT THE QUESTION
        if line.find('DECISION') > 0:
            num += 1
            question = questions[num]
            # ASK FOR A DECISION
            player["decision"][num] = input(f"{question}\n")
        
        else:
            print(line.center(100))
            
        # DELAY PRINT EVERY LINE
        time.sleep(1.1)
        
    num = -1
    
    # print("hello".ljust(50).center(100)+"\n")
    
    
fquestions = open("questions.txt", "r")
q_lst = fquestions.read().split("\n")
fquestions.close()

num = 0
question = ''
for i in range(len(q_lst)-1):
    if q_lst[i].isdigit():
        question += q_lst[i+1] + "\n"
        question += q_lst[i+2] + "\n"
        print(question)
        question = ''