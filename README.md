# OTP-Based Login and Verification System

This project is a Flask-based web application for implementing an OTP-based login and verification system. It uses Gmail SMTP for sending OTPs to the user's email, and Tailwind CSS for a modern, responsive UI.

## Features
- User login with a username, password, and email address.
- OTP generation and email delivery using Gmail's SMTP server.
- OTP verification process for enhanced security.
- Tailwind CSS for responsive and visually appealing design.

## Prerequisites
1. Python 3.7 or higher
2. Flask
3. smtplib
4. email.mime
5. Tailwind CSS (via CDN in the templates)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/otp-flask-app.git
    cd otp-flask-app
    ```

2. Install the required Python libraries:
    ```bash
    pip install flask
    ```

3. Set up your Gmail account:
   - Enable **2-Step Verification** for your Google account.
   - Generate an **App Password** for your account and replace it in the script:
     ```python
     password = "your_app_password"
     ```

## Usage

1. Run the Flask app:
    ```bash
    python app.py
    ```

2. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

3. Use the login form to:
   - Enter your username, password, and email address.
   - Receive an OTP in your email inbox.
   - Verify the OTP to access the success page.
