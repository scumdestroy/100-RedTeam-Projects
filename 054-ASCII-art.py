# Here's a cheating lame way to do it.
#import pyfiglet
#def print_intense_ascii_art(text):
#   ascii_art = pyfiglet.figlet_format(text, font='big')
#   print(ascii_art)
#user_input = input("Enter a string: ")
#print_intense_ascii_art(user_input)


# This other way took an eternity actually, so nvm, but here are the non-tedious parts.

def print_lit_ascii_art(text):
    characters = {
        'A': r"""
 @@@@@@      
@@@@@@@@     
@@!  @@@     
!@!  @!@     
@!@!@!@!     
!!!@!!!!     
!!:  !!!     
:!:  !:!     
::   :::     
 :   : :     
   """,
   'B': r"""
             
@@@@@@@   
@@@@@@@@  
@@!  @@@  
!@   @!@  
@!@!@!@   
!!!@!!!!  
!!:  !!!  
:!:  !:!  
 :: ::::  
:: : ::   
   """,
  # ETC ETC ETC...
   
      'Z': r"""
                
@@@@@@@@  
@@@@@@@@  
     @@!  
    !@!   
   @!!    
  !!!     
 !!:      
:!:       
 :: ::::  
: :: : :  
"""
    }

    for char in text:
        if char.isalpha():
            char = char.upper()
            if char in characters:
                print(characters[char])
        else:
            print()

user_input = input("Enter a string: ")
print_lit_ascii_art(user_input)
