#!/usr/bin/python

import smtplib

smtpObj = smtplib.SMTP('localhost', 25)
smtpObj.login('username', 'pass')

sender = ''
receivers = ['']

msg = """From: anyone <person@person.com>
To: toPerson <to@toperson.com>
Subject: test

This is a test.
"""

try:
	smtpObj = smtplib.SMTP('localhost', 25)
	smtpObj.sendmail(sender, receivers, msg)
	print "Successfully sent email"
except SMTPException:
	print "Error: unable to send email"

smtpObj.quit()

