import os
from random import randint
import pandas as pd
import numpy as nm
from supabase import create_client
from dotenv import load_dotenv
from datetime import datetime
from smtplib import SMTP
from email.mime.text import MIMEText
import smtplib
load_dotenv()

SUPABASE_URL = "https://xzeuuoqcpbhaidfzyxnj.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh6ZXV1b3FjcGJoYWlkZnp5eG5qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzg4NTkwODUsImV4cCI6MjA1NDQzNTA4NX0.Y_liz7tAiguNLm3IoXzIhhZcq-p6Zw5pjvH5gHFhxXM"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def userSignup():
  uuid =  randint(10000, 99999)
  userEmail = input('Enter your email: ')
  userDisplayname = input('Enter your display name: ')
  userPassword = input('Enter your password: ')
  userPasswordConfirm = input('Confirm your password: ')
  created_at = datetime.now().isoformat()
  if userPassword == userPasswordConfirm : 

    try :
      data = supabase.table("users").insert({"user_id": uuid,"name":userDisplayname,"email":userEmail,"password":userPassword,"created_at":created_at}).execute()
      print('Successfully Signed Up')
    except Exception as e :
      print('Signup Error',{e})
  else : 
      print('Password do not match. Please try again.')
    
def userLogin():
  userEmail = input('Enter your email: ')
  userPassword = input('Enter your password: ')
  try:
    response = supabase.table('users').select('*').eq("email",userEmail).execute()

    if response.data : 
      userData = response.data[0]
      storedPassword = userData['password']
      displayName = userData.get('name','No Name')
      storedUuid = userData['user_id']

      if storedPassword == userPassword : 
        print()
        print(f'Sucessfully logged in. Welcome {displayName} {storedUuid}')
        print()
        print('1. Record Transacation')
        print('2. Generate Report')
        print('3. Exit')
        print()

        while True : 
          userChoice = input('Enter your choice : ')
          if userChoice == '1' : 
            transcation(displayName,userEmail)
          elif userChoice == '2' : 
            generateReport(displayName,userEmail)
          elif userChoice == '3' : 
            exit()
          else : 
            print('Invalid Choice')
      else :
        print("Invalid email or password. Please try again.")
    else : 
      print("Invalid email or password. Please try again.")
  except Exception as e:
      print(f"Login error: {e}")
  
def transcation(userDisplayname,userEmail):
  date = datetime.now().isoformat()
  amount = input('Enter the Amount : ')	
  category_name = input('Enter the Category Type : ')	
  merchant = input('Enter the Merchant : ')	
  payment_mode = input('Enter the Payment Mode : ')	
  transaction_type = input('Enter the Transaction Type : ')	

  try :
      data = supabase.table("transactions").insert({
        "name":userDisplayname,
        "date":date,
        "amount":amount,
        "category_name":category_name,
        "merchant":merchant,
        "payment_mode":payment_mode,
        "transaction_type":transaction_type,
        }).execute()
      
      def transactionNotification():
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("x", "x")
        subject = "Transaction Inserted"
        message_body = f"""
                  Hello {userDisplayname},
                  Your transaction has been recorded successfully.
                  "Name":userDisplayname,
                  "Date":date,
                  "Amount":amount,
                  "Category Name":category_name,
                  "Merchant":merchant,
                  "Payment Mode":payment_mode,
                  "Transaction Type":transaction_type,
        """
        message = MIMEText(message_body)
        message["Subject"] = subject
        s.sendmail("systememailn@gmail.com", userEmail, message.as_string())
        print('Your transaction has been recorded successfully.')
      transactionNotification()
  except Exception as e :
      print('Transaction Error',{e})


def generateReport(userDisplayname,userEmail):
    try:
        response = supabase.table('transactions').select('*').eq("name", userDisplayname).execute()
        
        if response.data:
            df = pd.DataFrame(response.data)

            # Renaming columns if they match database structure
            df.rename(columns={
                "id": "Transaction ID",
                "name": "User Name",
                "date": "Date",
                "amount": "Amount",
                "category_name": "Category",
                "merchant": "Merchant",
                "payment_mode": "Payment Mode",
                "transaction_type": "Transaction Type"
            }, inplace=True)

            print(df)

            # Generate a valid filename (remove special characters from timestamp)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_filename = f"{userDisplayname}_report_{timestamp}.csv"

            # Save DataFrame to CSV file
            df.to_csv(report_filename, header=True, index=False)

            
            print(f"File generated: {report_filename}")

            def transactionNotification():
              s = smtplib.SMTP('smtp.gmail.com', 587)
              s.starttls()
              s.login("x", "x")
              subject = "Transaction Report Generated"
              message_body = f"""
                        Hello {userDisplayname},
                        Your Report has been generated successfully.

                        'File Name' : report_filename
              """
              message = MIMEText(message_body)
              message["Subject"] = subject
              s.sendmail("systememailn@gmail.com", userEmail, message.as_string())
              print('Your Report has been generated successfully..')
            transactionNotification()
        else:
            print("No transactions found.")
    
    except Exception as e:
        print(f"Error in generating report: {e}")


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
    print('3. Exit')

    print()

    userChoice = input('Enter your choice : ')
    if userChoice == '1' :
      userLogin()
    elif userChoice == '2' : 
      userSignup()
    elif userChoice == '3' : 
      exit()
    else : 
      print('Invalid Choice')

mainMenu()
