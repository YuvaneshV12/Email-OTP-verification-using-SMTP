import smtplib
import random
from email.mime.text import MIMEText
from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Your Gmail credentials
sender_email = "noreplyotpgova@gmail.com"
password = "cvvjgllllyouffhw"  # Use the generated app password

# Function to generate OTP
def generate_otp():
    otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
    return otp

# Function to send OTP email
def send_otp(receiver_email, otp_code):
    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp_code}"

    # Construct the email
    message = MIMEText(body, "plain")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:  # Use SMTP_SSL for SSL connection
            server.login(sender_email, password)  # Login with your email and app password
            server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
            print("OTP sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        receiver_email = request.form["email"]
        # Here you can add database checks for username and password if required
        if username and password:  # Assuming basic validation here
            # Generate OTP and send it to the provided email
            otp_code = generate_otp()
            session['otp_code'] = otp_code  # Store OTP in session for validation
            session['receiver_email'] = receiver_email  # Store receiver email
            send_otp(receiver_email, otp_code)
            return redirect(url_for("verify"))
        else:
            return render_template_string(LOGIN_TEMPLATE, error="Invalid credentials")

    return render_template_string(LOGIN_TEMPLATE)

@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        otp_code = request.form["otp_code"]
        # Validate OTP
        if otp_code == str(session.get('otp_code')):
            return redirect(url_for("success"))
        else:
            return render_template_string(VERIFY_TEMPLATE, error="Invalid OTP")

    return render_template_string(VERIFY_TEMPLATE)

@app.route("/success")
def success():
    return "OTP Verified Successfully!"

# HTML Template for Login Page
LOGIN_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-xl shadow-lg w-96">
        <h2 class="text-3xl font-semibold mb-6 text-center text-gray-700">Login</h2>
        <form method="POST">
            <div class="mb-4">
                <label for="username" class="block text-gray-600">Username:</label>
                <input type="text" name="username" id="username" class="mt-2 p-2 w-full border border-gray-300 rounded" required>
            </div>
            <div class="mb-4">
                <label for="password" class="block text-gray-600">Password:</label>
                <input type="password" name="password" id="password" class="mt-2 p-2 w-full border border-gray-300 rounded" required>
            </div>
            <div class="mb-4">
                <label for="email" class="block text-gray-600">Email:</label>
                <input type="email" name="email" id="email" class="mt-2 p-2 w-full border border-gray-300 rounded" required>
            </div>
            {% if error %}
            <div class="text-red-500 text-center mb-4">{{ error }}</div>
            {% endif %}
            <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded mt-4 hover:bg-blue-600">Login and Receive OTP</button>
        </form>
    </div>
</body>
</html>
"""

# HTML Template for OTP Verification Page
VERIFY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OTP Verification</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-xl shadow-lg w-96">
        <h2 class="text-3xl font-semibold mb-6 text-center text-gray-700">OTP Verification</h2>
        <form method="POST">
            <div class="mb-4">
                <label for="otp_code" class="block text-gray-600">Enter OTP:</label>
                <input type="text" name="otp_code" id="otp_code" class="mt-2 p-2 w-full border border-gray-300 rounded" required>
            </div>
            {% if error %}
            <div class="text-red-500 text-center mb-4">{{ error }}</div>
            {% endif %}
            <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded mt-4 hover:bg-blue-600">Verify OTP</button>
        </form>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
