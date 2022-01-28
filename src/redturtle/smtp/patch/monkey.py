# coding=utf-8
from os import environ
from smtplib import SMTP_SSL
from smtplib import SMTP

if environ.get("DISABLE_MAIL_SSL", ""):
    smtp = SMTP
else:
    smtp = SMTP_SSL
