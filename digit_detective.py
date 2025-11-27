
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
  
  return template.format(player_name=player_name,)





def play_game():
    pass



#print(load_game())