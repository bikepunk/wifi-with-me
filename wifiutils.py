#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email import utils
import ConfigParser
import smtplib


def read_config(key):
    """Read the default settings file, settings.ini.

    - key: the key of the config to read

    return: a dict
    """
    CONFIG_FILE_NAME = "settings.ini"
    config = ConfigParser.ConfigParser()
    config.read(CONFIG_FILE_NAME)
    items = config.items(key)
    dic = {it[0]: it[1] for it in items}
    return dic


MAIL = """
Nouvelle demande de la part de %(name)s.

- son mail : %(email)s
- son tel : %(phone)s
- habite au %(floor)sème étage sur %(floor_total)s
- commentaire : %(comment)s

Pour gérer cette demande, tu peux visiter : %(admin_url)s
"""


def send_mail(data):
    """Send an email. Read the default config file.

    - data: data coming from the form (dict)

    return: nothing
    """
    try:
        config = read_config('email')
        default_subject = "[wifi-with-me] nouvelle demande de {}".format(data.get('name'))
        SUBJECT = default_subject
        FROM = config.get("from")
        TO = config.get("to")
        HOST = config.get('smtp_host')

        data['admin_url'] = config.get('admin_url')
        msg = MIMEText(MAIL % data, 'plain', 'utf-8')
        msg['Subject'] = SUBJECT
        msg['From'] = FROM
        msg['To'] = TO
        msg['Message-ID'] = utils.make_msgid()
        msg['Date'] = utils.formatdate()

        user = config.get('smtp_user')
        password = config.get('smtp_password')

        server = smtplib.SMTP(HOST)
        server.ehlo()  # may be specific to gmail, but did not bother me so far.
        server.starttls()
        server.login(user, password)
        server.sendmail(FROM, [TO], msg.as_string())
        server.quit()
    except Exception as e:
        print "ERROR while trying to send the email: {}".format(e)
