#!/usr/bin/env python

# sending an HTML email with an embedded image and a text message

import time

# importing the libraries needed to send an email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# defining the sending and receiving email addresses
strFrom = 'p1.raspb3rry@gmail.com'
strTo = 'email@address.com'

# creating the root message and filling in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Security image'

# sending from and to to the above mentioned email addresses
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# encapsulating the plain and HTML versions of the message body in an 'alternative' part
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('text message')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('There was motion sensed by the system at the below mentioned time.<br><img src="cid:image1"><br>', 'html')
msgAlternative.attach(msgText)

# the image is in the current directory
fp = open('security_image.jpg', 'rb')

# opening the image and assigning it to a variable
msgImage = MIMEImage(fp.read())
fp.close()

# defining the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# sending the email with the SMTP library
import smtplib

# specife the port
# port 587 is open by default on Gmail
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()

# login to the sender Gmail account
smtp.login('p1.raspb3rry@gmail.com', 'malnapi2016')

# send the email according to the above specified parameters
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.close()

# sleep for 2 seconds after it has sent an email so no multiple emails are sent about the same person
time.sleep(2)
