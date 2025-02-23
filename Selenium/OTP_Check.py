import imaplib
import email
import re

# Email credentials
EMAIL_USER = "gneelakantareddy4143@gmail.com"
EMAIL_PASS = "Neela@123"  # Enable "App Passwords" in Gmail settings


def get_otp_from_email():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

        status, data = mail.search(None, "ALL")
        mail_ids = data[0].split()

        for num in mail_ids[::-1]:  # Check latest emails first
            status, data = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])

            if "OTP" in msg.get_payload():  # Adjust keyword as needed
                otp_match = re.search(r"\b\d{6}\b", msg.get_payload())
                if otp_match:
                    return otp_match.group()

        mail.logout()
    except Exception as e:
        print("Error fetching OTP:", e)
    return None


# Example Usage
otp = get_otp_from_email()
if otp:
    print("Retrieved OTP:", otp)
