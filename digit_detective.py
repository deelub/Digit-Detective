
#Additional features : Levels ; Hint systems,Score system(based on how many tries before getting it right) , Attempts tracker, Custom game mode , HARD MODE -CHALLENGE
def load_game():
  """summary """
  player_name= (input("Hey There!👋🏻 Enter your name ")).title()
  
  
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
  
  return "Loading game..."
      
  
  

def gameplay_config():
  
  """summary """
  
  hints=input(f"Would you like hints during gameplay? (Select a number)\n1.Yes \n2.No \n")
  hints_enabled= False
  
  try:
    if hints=="1":
      hints_enabled=True
      return "yes"
    elif hints=="2":
      hints_enabled=False
      return "no"
    elif  (int(hints) < 1) or (int(hints) > 2):             
      while True:
        print("Invalid option entered,please enter another value")
        hints= input( " ")
  except ValueError:
    while True:
      print("Invalid character entered,please enter another value")
      hints= input( " ")
      
      
  hints_amt= 0
  level=input(f"Would you like hints during gameplay? (Select a number)\n1.Easy \n2.Medium \n3.Hard")
  
  if level=="1":
    hints_amt= 6
  elif level== "2":
    hints_amt=3
  elif level== "3":
    hints_amt=2
  
  
  
  
def play_game():
  """summary"""
  pass

  load_game()
  gameplay_config()



print(gameplay_config())