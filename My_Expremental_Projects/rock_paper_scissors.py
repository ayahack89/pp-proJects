import random
computer_list = ['Rock','Paper','Scissor']
#Game rules....
'''Rock Vs paper >> Paper wins 
Rock Vs Scissor >> Rock wins 
Paper Vs Scissor >> Scissor wins'''

while  True:
    computer_count=0
    usercount = 0
    user_input = int(input('''
    
    Game Start......
    1 Yes|Start
    2 No|Exit 
    Put number press enter:
    
    '''))
    if user_input ==1:
        for game in range(1,6):
            user_play = int(input('''
            
            1 Rock
            2 Paper
            3 Scissor
            
            '''))
            if user_play == 1:
                userchoice ='Rock'
            elif user_play == 2:
                userchoice ='Paper'
            elif user_play == 3:
                userchoice ='Scissor'
            else:
                print("Its a invalid number.")
            
            computer_coice = random.choice(computer_list)
            if computer_coice == userchoice:
                print("Computer_Choice",computer_coice)
                print("User_Choice",userchoice)
                print("GAME DRAW")
                computer_count = computer_count+1
                usercount = usercount +1
            elif (userchoice == 'Rock' and computer_coice == 'Scissor') or (userchoice 
            == 'Scissor' and computer_coice =='paper') or (userchoice == 'Paper' and computer_coice 
            == 'Rock'):
                print("YOU WIN")
                usercount = usercount + 1
            else:
                print("Computer Value",computer_coice)
                print("User value",userchoice)
                print("Computer Win")
                computer_count = computer_count + 1
            # print(userchoice)
            # print(computer_coice)
    else:
        break

        



    


