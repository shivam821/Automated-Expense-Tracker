def userSignup():
  userEmail = input('Enter your email: ')
  userDisplayname = input('Enter your display name: ')
  userPassword = input('Enter your password: ')
  userPasswordConfirm = input('Confirm your password: ')
  if userPassword == userPasswordConfirm : 
    print('You have successfully signed up!')
    
def userLogin():
  userEmail = input('Enter your email: ')
  userPassword = input('Enter your password: ')
  
def transcation():
  pass

def generateReport():
  pass

def emailNotification():
  pass

def mainMenu():

  print('#######################################')
  print('Automated Expense Tracker')
  print()
  print('Main Menu')
  print('#######################################')  
  print()

  print('1. Login')
  print('2. Signup')
  print('3. Record Transacation')
  print('4. Generate Report')
  print('5. Exit')

  print()

  userChoice = input('Enter your choice : ')
  if userChoice == '1' :
    userLogin()
  elif userChoice == '2' : 
    userSignup()
  elif userChoice == '3' :
    transcation()
  elif userChoice == '4' :
    generateReport()
  elif userChoice == '5' : 
    exit()
  else : 
    print('Invalid Choice')

mainMenu()