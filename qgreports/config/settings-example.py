__author__ = 'dmwoods38'

debug = False

# scan_template - template id for a scan report template that has similar
#                 settings to the Quick Actions report.
QualysAPI = {
    'username': '',
    'password': '',
    'scan_template': ''
}

# elasticsearch settings
#       aws_auth - True or False if authenticating to AWS ES using a key.
ELASTICSEARCH = {
    'host': '',
    'port': None,
    'aws_auth': False
}

AWS = {
    'access_key': '',
    'secret_key': '',
    'region': ''
}
# where reports are temporarily stored before being emailed.
report_folder = ''

# report archive folder after reports are emailed.
archive_folder = ''

# log file for any unprocessed reports. sorry it looks terrible atm.
unprocessed_log = ''
# sender
email_from = ''

# email server used to send the reports.
smtp_server = ''

# Destination setting, should probably find a better way of doing this eventually.
# local - saving to report_folder only, no emailing
# email - use report_folder as temp storage, then send to recipients
# elasticsearch - saves to report_folder and then parses results into JSON
#                 and ships them off to elasticsearch
destination = 'local'
