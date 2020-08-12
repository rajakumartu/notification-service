#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import os
import email_service

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def message():
    name = request.json['name']
    return jsonify({'message': 'Hello %s ' % name})


@app.route('/health', methods=['GET'])
def health():
    return 'OK HEALTHY State 2.0!!!'


@app.route('/notify', methods=['POST'])
def notify():
    # os.environ['AWS_MAIL_SERVER_HOST'] = 'email-smtp.us-east-1.amazonaws.com'
    # os.environ['AWS_MAIL_SERVER_USERNAME'] = 'AKIAZQ6ZNDCWGE3Y3QEI'
    # os.environ['AWS_MAIL_SERVER_PASSWORD'] = 'BOGKaub0ThNi6jN4mFTCPv9JOQCLcpH5POdET+N6LRzJ'
    # os.environ['AWS_MAIL_SERVER_FROM_ADDRESS'] = 'kokkikumar2510.2@gmail.com'

    data = request.json

    # Create the body of the message (a plain-text and an HTML version).
    body_text_content = data['body_text_content']
    body_html_content = data['body_html_content']

    to_emails = data['toEmails']
    subject = data['subject']

    # msg = email_service.constuct_mail_message(to_emails, subject, body_text_content, body_html_content)
    # send_mail(receivers, msg)

    # email_service.send_mail(to_emails, msg)
    response = { 
      "to_emails": to_emails, 
      "subject": subject, 
      "header" : body_html_content , 
      "body": body_text_content, 
      "notification": "Success"
      }
    return response

@app.route('/notify_sample', methods=['GET'])
def notify_sample():
    # os.environ['AWS_MAIL_SERVER_HOST'] = 'email-smtp.us-east-1.amazonaws.com'
    # os.environ['AWS_MAIL_SERVER_USERNAME'] = 'AKIAZQ6ZNDCWGE3Y3QEI'
    # os.environ['AWS_MAIL_SERVER_PASSWORD'] = 'BOGKaub0ThNi6jN4mFTCPv9JOQCLcpH5POdET+N6LRzJ'
    # os.environ['AWS_MAIL_SERVER_FROM_ADDRESS'] = 'kokkikumar2510.2@gmail.com'

    # Create the body of the message (a plain-text and an HTML version).
    text_content = "Notification 2.0"
    html_content = " Hi  !!! How are you? This is the Kubernetes Advanced sample "
    # to_emails = ['kokkikumar2510.1@gmail.com']
    # subject = 'Test Mail Subject Working 1234'
    # msg = email_service.constuct_mail_message(to_emails, subject, text_content, html_content)
    # send_mail(receivers, msg)

    # email_service.send_mail(to_emails, msg)
    return {"header" : text_content , "body": html_content}

# Return errors as JSON objects
def app_error(e):
    return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    port = os.environ['APPLICATION_PORT']
    app.register_error_handler(Exception, app_error)
    app.run(host='0.0.0.0', port=port)