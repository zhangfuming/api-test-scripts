__author__ = 'zhangfuming'


# Import smtplib for the actual sending function
import smtplib

from email.mime.text import MIMEText

msg = MIMEText("test")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % "test"
msg['From'] = "fuming.zhang@baidao.com"
msg['To'] = "fuming.zhang@baidao.com"

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('mail.baidao.com',25)
s.login("fuming.zhagn@baidao.com", "******")
s.sendmail("fuming.zhang@baidao.com", ["fuming.zhang@baidao.com"], msg.as_string())
s.quit()