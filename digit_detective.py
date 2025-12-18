import random
#Additional features : Levels ; Hint systems,Score system(based on how many tries before getting it right) , Attempts tracker, Custom game mode , HARD MODE -CHALLENGE
def load_game():
  """summary """
  
  global active_game_template
  
  player_name= (input("Hey There!👋🏻 Enter your name ")).title()
  mysery_num="Enter mystery number"
  active_game_template= """"
  
      _______________Digit Detective {player_name}🔎________________ 
    
       Score: score         hints                Attempts left: attempts
            
                            
                         mystery_num     

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
  
  
      
def easy_mode(hints_enabled): 
  
  #Do if hints enabled code
  if hints_enabled==True:
    hints_amt=3
  else:
    hints_amt=0
    
  score= 500
  attempts=5
  hint_ls_range=[31,61,91,121,151] #All hints in coordination with range
  hints_ls=[["The number is 30 or less.","It’s closer to 0 than to 50.","The number is in the first quartile of the range"],  
            ["The number is 60 or less but greater than 30","It’s in the lower half of the range.","It's closer to 50 than to 0"],
            ["It is less than 100","It is greater than 60.","It comes before 90 on the number line"], 
            ["It is less than 100","It is greater than 60.","It comes before 90 on the number line"],
            ["It is less than 100","It is greater than 60.","It comes before 90 on the number line"]]
  

  mystery_num= random.randrange(150)
  placeholder_mystery_num= "?"
  
  while (attempts >=0) or (mystery_num != guess):#generate the code that after a certain amount of attempt ask if they wante hint
    guess=input("Guess a number in the ranges of 1-150")
    
    if guess != mystery_num:
      hints_req= int(input("Would you like a hint?(Select a number) \n1.Yes \2.N \n"))
      #checking to see what hint to give base on the range they're in 
      if hints_req==1:
        for num_range in hint_ls_range:
          if mystery_num in range(num_range):
            pos=hint_ls_range.index(num_range) #get the pos to correlate with hint
            for hints in hints_ls: #going through main hint list             #get the current hint_ls
              current_ls=hints[pos]
              
        hint_dict={
          1: current_ls[0],
          2:current_ls[1],
          3:current_ls[2]
        }
        
        attempts -= 1
        score -= 50
        
        print(active_game_template.format(score=score,
                                      attempts=attempts,
                                      hints=hints,
                                      mystery_num=placeholder_mystery_num,))
        
      elif hints_req==2:
        score-=50
        attempts -= 1
        
        print(active_game_template.format(score=score,
                                      attempts=attempts,
                                      hints=hints,
                                      mystery_num=placeholder_mystery_num,))
        
      else:
        raise ValueError(hints_req= int(input("Would you like a hint?(Select a number) \n1.Yes \2.N \n")))
        
  #Only if the right number is guessed
  print(active_game_template.format(score=score,
                                      attempts=attempts,
                                      hints=hints,
                                      mystery_num=mystery_num,))
  return "bye"



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
          pass
        elif mode== 2:
          hints_amt=3
        elif mode== 3:
          hints_amt=2
      else:
        print("Invalid option, Select a number, 1-3") #Seee the repition on here despite it being rigth after triial and error
        
      # return "loading game..."      #find a way to return the game that is being returned
    except ValueError:
      print("Invalid option. \nWhat mode would you like to play? (Select a number)\n1.Easy \n2.Medium \n3.Hard \n")


  

  
  







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
  



print(easy_mode(hints_enabled=True))