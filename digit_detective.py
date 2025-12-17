import random
#Additional features : Levels ; Hint systems,Score system(based on how many tries before getting it right) , Attempts tracker, Custom game mode , HARD MODE -CHALLENGE
def load_game():
  """summary """
  
  global active_game_template
  
  player_name= (input("Hey There!👋🏻 Enter your name ")).title()
  mysery_num="Enter mystery number"
  active_game_template= """"
  
      _______________Digit Detective {player_name}🔎________________ 
    
       Score: score                          Attempts left: attempts
            
                            
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
  score= 500
  attempts=5
  hint_ls_range=[30,60,90,120,150] #Only five --- we can  siftthrough the range of the number
  if hints_enabled==False:
    hint_count=0
  else:                                       #We can now begin game theory
    mystery_num= random.randrange(150)
    hint_count=6     #how are we goig to give hnint of the numnber if we do not know whta the number is?
    while (attempts >=0) or (mystery_num != guess):#generate the code that after a certain amount of attempt ask if they wante hint
      guess=input("Guess a number in the ranges of 1-150")
      if (hint_count < 6) :
        give_hint= 
      attempts -= 1
      score -= 50
      
    
    print(active_game_template.format(score=score,
                                      attempts=attempts,
                                      mystery_num=mystery_num,))
  

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
      print("INvalid option. \nWhat mode would you like to play? (Select a number)\n1.Easy \n2.Medium \n3.Hard \n")


  

  
  







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
  



print(load_game())