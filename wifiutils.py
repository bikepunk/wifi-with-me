#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textwrap import dedent
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

        infos = dedent("""\
        - son mail : {}\n
        - son tel : {}\n
	- habite au {} étage sur {}\n
	- commentaire {}\n
        """.format(data.get('email'), data.get('phone'),data.get('floor'), data.get('floor_total'), data.get('comment')))

        BODY = dedent("""\
From: <{}>
To: <{}>
MIME-Version: 1.0
Content-type: text/html
Subject: {}

Nouvelle demande de la part de {}.\n

{}

        """.format(FROM, TO, SUBJECT, data.get('name'), infos))
        user = config.get('smtp_user')
        password = config.get('smtp_password')

        server = smtplib.SMTP(HOST)
        server.ehlo() # may be specific to gmail, but did not bother me so far.
        server.starttls()
        server.login(user, password)
        server.sendmail(FROM, [TO], BODY)
        server.quit()
    except Exception as e:
            print "ERROR while trying to send the email: {}".format(e)
