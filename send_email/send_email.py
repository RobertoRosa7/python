# -*- coding: utf-8 -*-

import smtplib
import imapclient
import pyzmail


"""
Send E-mail
pip install imapclient pyzmail

SMTP Servers

Gmail: smtp.gmail.com
Outlook: smtp-mail.outlook.com
Yahoo: smtp.mail.yahoo.com
AT&T: smtp.mail.att.net
Comcast: smtp.comcast.net
Version: smtp.version.net


IMAP: Internet Message Access Protocol

Gmail: imap.gmail.com
Outlook: imap-mail.outlook.com
Yahoo: imap.mail.yahoo.com
AT&T: imap.mail.att.net
Comcast: imap.comcast.net
Version: incoming.version.net
"""


def send_email():
  conn = smtplib.SMTP('smtp.gmail.com', 587)
  conn.ehlo()
  """
    Values of the 'bytes' data type look like strings but begin with a 'b' when typed as code
  """
  conn.starttls()
  conn.login('email', 'password')

  """
    from_addr: string
    to_addr: string
    msg: string
    mail_options: array
    rcpt:options: array
  """
  text = 'Subject: E-mail enviado por python\n\nOlá Roberto!\nEste e-mail foi enviado por python module.'
  conn.sendmail('from', 'to', text)
  conn.quit()


def receive_email():
  conn = imapclient.IMAPClient('smtp.gmail.com', ssl=True)
  conn.login('email', 'password')
  conn.select_folder('INBOX', readonly=True)
  # UIDs = conn.search(['SINCE 20-Aug-2020'])
  rawMessages = conn.fetch([47474], ['BODY[]', 'FLAGS'])

  message = pyzmail.PyzMessage.factory(rawMessages[47474][b'BODY[]'])
  # message.get_subject()
  # message.get_addresses('from')
  # message.get_addresses('to')
  # message.get_addresses('bcc')
  message.text_part.get_payload().decode('UTF-8')

  conn.logout()
