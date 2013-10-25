# In this problem, you'll create a program that guesses a secret number!
# The program works as follows: 
#	you (the user) thinks of an integer between 0 and 100. 
#	The computer makes guesses, and you give it input - 
# is its guess too high or too low? 
# Using bisection search, the computer will guess the user's secret number!

print('Please think of a number between 0 and 100!')
answer =''
low = 0
high = 100
guess = (high + low) / 2

while (answer != 'h' and answer != 'l' and answer != 'c'):
  print('Is your secret number ' + str(guess) + '?')
  answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
  if answer == 'c':
    print('Game over. Your secret number was: ' + str(guess))
    break
  elif answer == 'h':
    high = guess
    answer = ''
  elif answer == 'l':
    low = guess
    answer = ''
  else:
    print('Sorry, I did not understand your input.')
  guess = (high + low) / 2

