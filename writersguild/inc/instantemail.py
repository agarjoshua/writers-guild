# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# fp = open(textfile, 'rb')
# # Create a text/plain message
# msg = MIMEText(fp.read())
# fp.close()

me = 'agarjodongo@gmail.com'
you = 'joshuaagarjj@gmail.com'
# msg['Subject'] = 'The contents of'
# msg['From'] = 'agarj@gmail.com'
# msg['To'] = 'joshuaagarjj@gmail.com'
msg = 'test'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()