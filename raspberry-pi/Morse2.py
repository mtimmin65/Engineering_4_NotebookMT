import board
import time
import digitalio 

led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT
  
modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

while True:
  
  print("Enter Morse Code Message, or enter -q to quit")
  MORSE_CODE = { 'A':'.-', 'B':'-...',
  'C':'-.-.', 'D':'-..', 'E':'.',
  'F':'..-.', 'G':'--.', 'H':'....',
  'I':'..', 'J':'.---', 'K':'-.-',
  'L':'.-..', 'M':'--', 'N':'-.',
  'O':'---', 'P':'.--.', 'Q':'--.-',
  'R':'.-.', 'S':'...', 'T':'-',
  'U':'..-', 'V':'...-', 'W':'.--',
  'X':'-..-', 'Y':'-.--', 'Z':'--..',
  '1':'.----', '2':'..---', '3':'...--',
  '4':'....-', '5':'.....', '6':'-....',
  '7':'--...', '8':'---..', '9':'----.',
  '0':'-----', ', ':'--..--', '.':'.-.-.-',
  '?':'..--..', '/':'-..-.', '-':'-....-',
  '(':'-.--.', ')':'-.--.-', ' ':'/',}

  message = input("") 
  message = message.upper() 

  message1 = " " 

  for letter in message: 
    message1 = message1 + (MORSE_CODE[letter]) + " " 

  print(message1)
  

  for character in message1: #loop thru morse message
    if character == ("."):
      led.value = True
      time.sleep(dot_time)
      led.value = False
    if character == ("-"):
      led.value = True
      time.sleep(dash_time)
      led.value = False
    if character == (""):
      led.value = True
      time.sleep(between_letters)
      led.value = False
    if character == ("/"):
      led.value = True
      time.sleep(between_words)
      led.value = False
    time.sleep(between_taps)
   
    # if character is between letters, do a “between letters” pause
    # if it's between words, do a “between words” pause



