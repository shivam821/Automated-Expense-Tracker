# Automated Expense Tracker
 A simple, automated expense tracking system with transaction logging and report generation.

## Introduction
 The Automated Expense Tracker is a Python-based application that allows users to record transactions, generate expense reports, and receive email notifications. It leverages Supabase for database management, pandas for data handling, and smtplib for sending email alerts.

## Features
1. User Signup & Login (with unique user IDs)
2. Transaction Recording (store amount, category, merchant, payment mode, and type)
3. Expense Report Generation (download transaction history as a CSV file)
4. Email Notifications (get alerts for transactions and reports)

## Explanation of Features:

### User Authentication:
1. Users can register with their email and password.
2. Secure authentication using a Supabase database.

### Transaction Logging:
1. Users enter transaction details (amount, category, merchant, etc.).
2. Data is stored in the Supabase database.

### Report Generation:
1. Users can download a CSV report of their expenses.
2. The report contains details of all transactions made.

### Email Alerts:
1. Users receive an email after successfully adding a transaction.
2. A notification is sent when a report is generated.

## Installation & Deployment:
### To run this project locally, follow these steps:
### Prerequisites:
1. Python 3.x installed
2. Supabase account & API credentials
4. Environment variables configured (.env file)
### Setup Instructions:
1. Clone the repository:
    git clone https://github.com/yourusername/automated-expense-tracker.git
    cd automated-expense-tracker
2. Install dependencies:
    pip install -r requirements.txt
3. Set up environment variables in a .env file:
    SUPABASE_URL=your_supabase_url
    SUPABASE_KEY=your_supabase_api_key
4. Run the script:
    python main.py
   
### For deployment:

1. Clone the Repository
    Obtain the project files by cloning the repository from GitHub:
    git clone https://github.com/your-repo-name.git
    cd your-repo-name
2. Create a Virtual Environment
    Set up a virtual environment to manage dependencies and prevent conflicts:
    python -m venv venv

    Activate the virtual environment:
    1. Windows:
        venv\Scripts\activate
    2. Mac/Linux:
        source venv/bin/activate
3. Install Dependencies
    Inside the virtual environment, install all required dependencies:
    pip install -r requirements.txt
4. Initialize the Database
    If using Supabase, set up your PostgreSQL database by running the initialization script:
    python init_db.py
5. Set Up Environment Variables
    Create a .env file to store sensitive information like API keys, SMTP credentials, and database URLs. Example:
    DATABASE_URL=your_supabase_url
    SMTP_SERVER=smtp.example.com
    EMAIL_USER=your_email@example.com
    EMAIL_PASSWORD=your_secure_password
6. Run the Application
    Start the application using:
    python app.py

## Tools/Technology Used:

1. Python – Core programming language for backend logic.
2. Supabase – Database as a Service (PostgreSQL-based).
3. pandas – Used for data analysis and CSV report generation.
4. dotenv – For environment variable management and security.
5. smtplib & email.mime – For email notifications via SMTP.

## Conclusion

The Automated Expense Tracker simplifies personal finance management by allowing users to log transactions, generate reports, and receive email notifications effortlessly. With a secure database and intuitive interface, this tool helps users track their spending habits and make informed financial decisions.

Future improvements may include graphical analytics, budgeting features, and multi-user support. Contributions and feedback are welcome to enhance its functionality! 🚀
