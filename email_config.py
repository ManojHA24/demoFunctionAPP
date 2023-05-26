import os

def getSenderMail():
    SenderMail = 'sagar.heera@optym.com'
    return SenderMail

def getRecieverMail():
    RecieverMail = [ 'manojha.cs19@bmsce.ac.in' ]
    return RecieverMail

def getAPIKey():
    api_key = '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'
    return api_key

def getReportPath():
    reportPath = os.getcwd() + r'\Report\SaiaIntegrationReport.pdf'
    return reportPath

def getCSVPath():
    csvPath = os.getcwd() + r'\Report\report.csv'
    return csvPath