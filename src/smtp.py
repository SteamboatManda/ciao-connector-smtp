#!/usr/bin/python -u
###
# This file is part of Arduino Ciao
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Copyright 2016 Arduino Srl (http://www.arduino.org/)
#
# authors:
# 	sergio@arduino.org
#
# notes: if you want to use gmail remember to turn on access for less
#	secure apps here: https://www.google.com/settings/u/2/security/lesssecureapps
###

import smtplib, ciaotools, os
from email.mime.text import MIMEText

# DEFINE CONNECTOR HANDLERS AND FUNCTIONS

def sendEmail(to, subject, body):
	#create email message
	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = smtp_sender
	msg['To'] = to

	try:
		if smtp_ssl:
			smtpserver = smtplib.SMTP_SSL(smtp_host, smtp_port)
			smtpserver.login(smtp_user, smtp_pwd)
		else:
			if smtp_tls:
				smtpserver = smtplib.SMTP(smtp_host, smtp_port)
				smtpserver.ehlo()
				smtpserver.starttls()
				smtpserver.ehlo()
				smtpserver.login(smtp_user, smtp_pwd)
			else:
				if smtp_auth:
					smtpserver = smtplib.SMTP(smtp_host, smtp_port)
					smtpserver.login(smtp_user, smtp_pwd)
				else:
					smtpserver = smtplib.SMTP(smtp_host, smtp_port)

		smtpserver.sendmail(smtp_sender, [to], msg.as_string())
		smtpserver.close()

	except Exception, e:
		logger.error("Error seding Email[%s] to %s: %s" %( subject, to, str(e) ) )

def handler(entry):
	if entry["type"] == "out":
		sendEmail(entry["data"][0], entry["data"][1], entry["data"][2])

# the absolute path of the connector
working_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep


# LOAD CONFIGURATION

# load configuration object with configuration file smtp.conf.json
config = ciaotools.load_config(working_dir)

# load parameters
smtp_sender = config["params"]["sender"]
smtp_user = config["params"]["user"]
smtp_pwd = config["params"]["password"]
smtp_host = config["params"]["host"]
smtp_port = config["params"]["port"]
smtp_ssl = config["params"]["ssl"]
smtp_tls = config["params"]["tls"]
smtp_auth = config["params"]["auth"]

# name of the connector
name = config["name"]

# CREATE LOGGER

log_config = config["log"] if "log" in config else None
logger = ciaotools.get_logger(name, logconf=log_config, logdir=working_dir)


# CALL BASE CONNECTOR

#Call a base connector object to help connection to ciao core
ciao_connector = ciaotools.BaseConnector(name, logger, config["ciao"])

#register an handler to manage data from core/mcu
ciao_connector.receive(handler)

# start the connector thread
ciao_connector.start()
