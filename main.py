import os
from supabase import create_client
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

SUPABASE_URL = "https://xzeuuoqcpbhaidfzyxnj.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh6ZXV1b3FjcGJoYWlkZnp5eG5qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzg4NTkwODUsImV4cCI6MjA1NDQzNTA4NX0.Y_liz7tAiguNLm3IoXzIhhZcq-p6Zw5pjvH5gHFhxXM"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def userSignup():
  userEmail = input('Enter your email: ')
  userDisplayname = input('Enter your display name: ')
  userPassword = input('Enter your password: ')
  userPasswordConfirm = input('Confirm your password: ')
  if userPassword == userPasswordConfirm : 
    try :
      user = supabase.auth.sign_up({
        "email": userEmail,
        "password": userPassword,
        "options": {"data": {"display_name": userDisplayname}}
          })
      print(user)
      print('Successfully Signed Up')
    except Exception as e :
      print('Signup Error',{e})
    
def userLogin():
  userEmail = input('Enter your email: ')
  userPassword = input('Enter your password: ')
  try:
    user = supabase.auth.sign_in_with_password({"email": userEmail, "password": userPassword})
    display_name = user.user.user_metadata.get("display_name", "No Name")  # Fixed display_name retrieval
    print(f'Successfully Logged In. Welcome, {display_name}!')
  except Exception as e:
      print(f"Login error: {e}")
  
def transcation():
  pass

def generateReport():
  pass

def emailNotification():
  pass

def mainMenu():
  while True : 

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