
#Additional features : Levels ; Hint systems,Score system , Attempts tracker, Timer mode, Custom game mode , HARD MODE -CHALLENGE, Achievement system
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
      
  
  

def levels(level):
  hints=input("Would you like hints during gameplay? (Select a number) /n1.Yes /n2.Yes")
  if level.lower()=="easy":
    pass
  elif level.lower()== "medium":
    pass
  elif level.lower()== "medium":

def play_game():
  """summary"""
  pass
  
  load_game()



print(load_game())