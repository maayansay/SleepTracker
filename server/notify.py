import sys
import json
import os
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from twilio.rest import Client

# Load issue body JSON from GitHub Action input
data = json.loads(sys.argv[1])
participant_id = data['participant_id']
timestamp = data['timestamp']

# Load participant info from CSV
df = pd.read_csv('data/participants.csv')
row = df[df['participant_id'] == participant_id].iloc[0]
email = row['email']
whatsapp = row['whatsapp']

# Append to log CSV
log_df = pd.read_csv('data/sleep_log.csv')
log_df = pd.concat([log_df, pd.DataFrame([[timestamp, participant_id]], columns=['timestamp', 'participant_id'])])
log_df.to_csv('data/sleep_log.csv', index=False)

# Send email notification
msg = MIMEText(f"Participant {participant_id} went to sleep at {timestamp}")
msg['Subject'] = f"Sleep Log - {participant_id}"
msg['From'] = os.environ['EMAIL_USER']
msg['To'] = email

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASS'])
    server.send_message(msg)

# Send WhatsApp message via Twilio
client = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_TOKEN'])
client.messages.create(
    from_='whatsapp:+14155238886',  # Twilio sandbox default
    to=whatsapp,
    body=f"Participant {participant_id} went to sleep at {timestamp}"
)
