import random
#Additional features : Levels ; Hint systems,Score system(based on how many tries before getting it right) , Attempts tracker, Custom game mode , HARD MODE -CHALLENGE


def load_game():
  """summary """
  
  global active_game_template
  
  player_name= (input("Hey There!👋🏻 Enter your name ")).title()
  mysery_num="Enter mystery number"
  active_game_template= """
  
      _______________Digit Detective 🔎________________ 
    
       Score: {score}      Hints:{hints}                Attempts left:{attempts}
            
                            
                      Myster number: {mystery_num}   

    _______________________________________________________________________
  
  
  """
  
  template = """
    _______________Welcome to Digit Detective {player_name}🔎________________ 
    
            The goal of Digit Detective is to guess the number 
            of the round.   
            
            Type in "Next" when you are ready to play
                                           
                            (._.)      
                            <)  )╯     
                             /  \       

    _______________________________________________________________________

  """  #15 underscores
  
  print(template.format(player_name=player_name,))
  play_on=input(" ")
  
  #checking that next is correctly typed in 
  while play_on.lower() != "next":
      print("I don't understand that, It seems that you're not quite ready. Type in 'Next' when you're ready")
      play_on=input(" ")

def gameplay_config():
  
  """summary """
  global hints_enabled
  hints_enabled= False
  hint_amt=0
  
  while True:
    try:
      hints=int(input("Would you like hints during gameplay? (Select a number)\n1.Yes \n2.No \n"))
      
      if hints in (1,2):
        break
      else:
        print("Invalid option entered,please enter another value")
    except ValueError:
      print("Invalid option entered,please enter another value")

    #############FIND PLACEHOLDER FOR THIS CODE HERE##########################
      if hints== 1:   
        hints_enabled= True
      elif hints==2:
        hints_enabled= False
  
  while True:
    try:
      mode=int(input(f"What mode would you like to play? (Select a number)\n1.Easy \n2.Medium \n3.Hard \n"))
      
      if mode in (1,3):
        if mode== 1:
          #easy_mode(hints_enabled)
          easy_mode()
        elif mode== 2:
          hints_amt=3
        elif mode== 3:
          hints_amt=2
      else:
        print("Invalid option, Select a number, 1-3") #Seee the repition on here despite it being rigth after triial and error
        
      # return "loading game..."      #find a way to return the game that is being returned
    except ValueError:
      print("Invalid option. \nWhat mode would you like to play? (Select a number)\n1.Easy \n2.Medium \n3.Hard \n")
  

############# Beginning of easy mode ########################
def easy_mode(): #Change easy mode to be in the range of 75
  
  #Do if hints enabled code
  score= 500
  attempts=5
  hint_ls_range=[16,31,46,61,76] #All hints in coordination with range
  hints_ls=[["You at the very near beginning of numbers","It’s closer to 0 than to 25.","The number is 15 or lower."],
            ["The number is past the very beginning, but the big numbers are still far away","It’s higher than 15, but still below the middle of the range","Your guess should be somewhere between 16 and 30"],
            ["The number is moving closer to the middle, but not quite there yet","It’s above 30, but still below the midpoint of the range","Your guess should be between 31 and 45"], 
            ["The number has crossed the middle, but the highest numbers are still ahead.","It’s above the midpoint, but not near the top.","The number is somewhere between 46 and 60."],
            ["You’re in the higher numbers now, near the end of the range","It’s above 60, but not beyond the maximum.","The number is between 61 and 75"]]
  
  
  
  #Code block for if hints enabled
  if hints_enabled==True:
    hints_amt=3
    for num_range in hint_ls_range:
      if mystery_num <= num_range:
        pos=hint_ls_range.index(num_range) #get the pos to correlate with hint
        break
        # for hints in hints_ls: #going through main hint list             #get the current hint_ls
    
    
  while (attempts >=0) or (mystery_num != guess):#generate the code that after a certain amount of attempt ask if they wante hint
    
    guess=input("Guess a number in the ranges of 1-75 \n")
    
    if guess != mystery_num:
      hints_req= int(input("Wrong answer ❌ \nWould you like to use a hint?(Select a number) \n1.Yes \2.N \n"))
      #checking to see what hint to give base on the range they're in 
      # if hints_req==1:
      if hints_amt <=0: 
        print("No hints left, continue gameplay")
        guess=input("Guess a number in the ranges of 1-75 \n")
      else:
          print(hint_dict.get(hints_amt))
          guess=input("Guess a number in the ranges of 1-75 \n")
      attempts -= 1
      score -= 50
      hints_amt -= 1
        
      print(active_game_template.format(score=score,
                                      attempts=attempts,
                                      hints=hints_amt,
                                      mystery_num=placeholder_mystery_num,))
        
      # elif hints_req==2:
      score-=50
      attempts -= 1
      
      print(active_game_template.format(score=score,
                                    attempts=attempts,
                                    hints=hints_amt,
                                    mystery_num=placeholder_mystery_num,))
            
    elif mystery_num==guess:
      print(active_game_template.format(score=score,
                                          attempts=attempts,
                                          hints=hints_amt,
                                          mystery_num=mystery_num,))

    current_ls=hints_ls[pos]
    # Only take the first 3 hints if you want
    hint_dict = {i+1: hint for i, hint in enumerate(current_ls[:3])}
    
    
    
    
    
  else:#If hints not enabled for the gameplay

    hints_amt="Disabled"
    score-=50
    attempts -= 1
      
    print(active_game_template.format(score=score,
                                    attempts=attempts,
                                    hints=hints_amt,
                                    mystery_num=placeholder_mystery_num,))

  

  mystery_num= random.randrange(75)
  placeholder_mystery_num= "?"
  print(active_game_template.format(score=score,
                                      attempts=attempts,
                                      hints=hints_amt,
                                      mystery_num=placeholder_mystery_num,)) 
    
  

  


  
  







  

  
  







def medium_mode(hints_enabled):
  hint_count= 6
  
  if hints_enabled==False:
    hint_count=0
  else:                                       #We can now begin game theory
    number= random.randrange(1,500)
    


def hard_mode(hints_enabled):
  hint_count= 6
  
  if hints_enabled==False:
    hint_count=0
  else:                                      #We can now begin game theory
    number= random.randrange(1,650)
    

    
   
   
  
  
  
def play_game():
  """summary"""
  pass

  load_game()
  gameplay_config()
  


load_game()
gameplay_config()
print(easy_mode(hints_enabled=True))