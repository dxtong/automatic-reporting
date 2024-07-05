from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
from smtplib import SMTPAuthenticationError
import sys
import datetime
from autogenReportModel import *


class sendEmail():
    def __init__(self, email_id, email_pw):
        self.email_id = email_id
        self.email_pw = email_pw
        self.server = SMTP('smtp.office365.com',587)
        self.server.starttls()
        self.server.login(self.email_id, self.email_pw)

    def get_send(self):
        self.recipients = pd.read_csv('email_info/recipients.txt')
        self.emaillist = [elem.strip().split(',') for elem in self.recipients]
        self.tolist = pd.read_csv('email_info/tolist.txt')
        self.cclist = pd.read_csv('email_info/cclist.txt')
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = '香港 (太古+NBA項目) 工作简报' + ' ' + datetime.datetime.now().strftime('%Y %b %d')
        self.msg['From'] = self.email_id
        self.msg['To'] = ', '.join(self.tolist)
        self.msg['Cc'] = ', '.join(self.cclist)

        self.df_html = autogenReport().autogen().to_html()

        self.head = \
            '''
            <head>
                <meta charset="utf-8">
                <STYLE TYPE="text/css" MEDIA=screen>
                    table.dataframe {
                        border-collapse: collapse;
                        width: 700px
                    }

                    table.dataframe thead {
                        border: 1px solid lightgray;
                        padding: 10px 10px 10px 10px;
                        background: #FFFF99;
                    }

                    table.dataframe tbody {
                        border: 1px solid lightgray;
                        background: white;
                    }

                    table.dataframe tr {
                    }

                    table.dataframe th {
                        padding: 10px 10px 10px 10px;
                        color: black;
                        font-family: arial;
                        text-align: center;
                    }

                    table.dataframe td {
                        text-align: center;
                        padding: 10px 10px 10px 10px;
                    }

                </STYLE>
            </head>
            '''


        self.body = \
            '''
            <body>
            <p>Dear All,</p>
            <p>香港 (太古+NBA項目) 工作简报 '''+datetime.datetime.now().strftime('%Y %b %d')+'''. Thanks.</p>
            {df_html}
            <br>
            <hr>
            <p>香港倉 | {email_id}</p>  
            </body>
            '''.format(df_html=self.df_html, email_id=self.email_id)

        self.html_msg= '<html>' + self.head + self.body + '</html>'

        self.content_html = MIMEText(self.html_msg, 'html', 'utf-8')
        self.msg.attach(self.content_html)

        return self.server.sendmail(self.msg['From'], self.emaillist , self.msg.as_string())