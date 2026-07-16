import os
import csv
import io
import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USERNAME = os.environ.get("SMTP_USERNAME", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")


def send_result_email(student_name, student_email, marks):
    subject = "Your Exam Result"
    body = f"Dear {student_name},\n\nYour result has been published.\nMarks: {marks}\n\nRegards,\nExam Cell"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USERNAME
    msg["To"] = student_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, student_email, msg.as_string())


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_csv():
    file = request.files.get("csv_file")
    if not file or file.filename == "":
        flash("Please select a CSV file to upload.")
        return redirect("/")

    stream = io.StringIO(file.stream.read().decode("utf-8"))
    reader = csv.DictReader(stream)

    sent_count = 0
    failed = []

    for row in reader:
        name = row.get("name", "").strip()
        email = row.get("email", "").strip()
        marks = row.get("marks", "").strip()

        if not name or not email or not marks:
            continue

        try:
            send_result_email(name, email, marks)
            sent_count += 1
        except Exception as e:
            failed.append(f"{email} ({str(e)})")

    flash(f"Processed CSV. Emails sent: {sent_count}. Failed: {len(failed)}")
    return redirect("/")


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)