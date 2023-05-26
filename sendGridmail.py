from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import ( Mail, Attachment, FileContent,FileName, FileType, Disposition, ContentId ) 
import base64
import email_config

def sendMail():
    # contents of email
    message = Mail(
        from_email = email_config.getSenderMail(),
        to_emails = email_config.getRecieverMail(),
        subject = 'Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>' )

    # get pdf path
    reportPath = email_config.getReportPath()

    # reading file contents as bytes
    with open(reportPath, 'rb') as f:
        PDFdata = f.read()
        f.close()
    encodedPDF = base64.b64encode(PDFdata).decode()
    attachmentPDF = Attachment()
    attachmentPDF.file_content = FileContent(encodedPDF)
    attachmentPDF.file_type = FileType('application/pdf')
    attachmentPDF.file_name = FileName("SaiaIntegrationReport.pdf")
    attachmentPDF.disposition = Disposition('attachment')
    attachmentPDF.content_id = ContentId('ReportContentID1')
    # adding pdf attachment
    message.add_attachment(attachmentPDF)

    # get csv path
    csvPath = email_config.getCSVPath()

    with open(csvPath, 'rb') as f:
        CSVdata = f.read()
        f.close()
    encodedCSV = base64.b64encode(CSVdata).decode()
    attachmentCSV = Attachment()
    attachmentCSV.file_content = FileContent(encodedCSV)
    attachmentCSV.file_type = FileType('application/csv')
    attachmentCSV.file_name = FileName("report.csv")
    attachmentCSV.disposition = Disposition('attachment')
    attachmentCSV.content_id = ContentId('ReportContentID2')
    # adding pdf attachment
    message.add_attachment(attachmentCSV)

    # get API Key
    api_key = email_config.getAPIKey()
    sg = SendGridAPIClient(api_key=api_key)
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
sendMail()
