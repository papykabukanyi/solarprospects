from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD

app = Flask(__name__)

def send_email(name, phone, email, message):
    msg = MIMEText(f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}")
    msg['Subject'] = 'Incoming Solar Professional!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())

@app.route("/", methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        message = request.form['message']
        # Process form data (e.g., store in database, send email, etc.)
        send_email(name, phone, email, message)
        return render_template('emailsent.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)