import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib

EMAIL_ADDRESS = 'PUT_YOUR_EMAIL'
EMAIL_PASSWORD = 'PUT_YOUR_PASSWORD'


# -----------------------------------------------------------------------
# ------'send_email_for_spending' FUNCTION EXPLANATION'------------------
# -----------------------------------------------------------------------

# I will explain these 2 parameters

# 'this_week_spending' is a variable that will hold the value of
# how much we spent in the week

# 'summary' is a variable that will hold the message that will put into
# the email message
def send_email_for_spending(this_week_spending, summary):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # title for your email
        subject = "Here is how much you spent in this week."
        msg = f"""Subject: {subject}\n\n{summary}\n\n
Overall, You have spent {this_week_spending} Euros.
        """

        # .sendmail(SENDER, RECEIVER, MESSAGE)
        smtp.sendmail(EMAIL_ADDRESS, 'PUT_YOUR_EMAIL_RECEIVER', msg)


# Select the scope for APIs you would like to access
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

# here in the 'credntials' variable, you put the json file you have received when you
# created credentials in the google developer console. And lastly, give them the scope
# that they can work within
credentials = ServiceAccountCredentials.from_json_keyfile_name('spendingDiaryCreds.json',
                                                               scope)

# Authorize it with gspread and now let's get started
client = gspread.authorize(credentials)

# Open the spread sheet by its name
sheet = client.open('PUT_YOUR_SPREADSHEET_NAME')

# Select the worksheet by its title
worksheet = sheet.worksheet('PUT_YOUR_WORKSHEET_NAME')

# Number of Days
num_days = 7
# We are going to sum up how much we spent here at the variable
overallMoneySpent = 0

# message holder as empty list, it will hold the spending of a day separated
# by list
spending_by_day = []

# it starts from 2 because column that has monday is 2nd column
for day in range(2, num_days + 2):
    dailyMoneySpent = worksheet.col_values(day)

    # This will erase the date which is located always at the first row
    dailyMoneySpent.pop(0)

    spending_by_day.append(dailyMoneySpent)

    # Calculate how much I spent
    for good in dailyMoneySpent:
        for money in good.split():
            try:
                overallMoneySpent += float(money)
            except ValueError:
                pass


# index 0 of 'spending_by_day' is a list of spending for Monday
# so index 6 will be Sunday
spending_summary = f"""
MON:
    {', '.join(spending_by_day[0])}
TUE:
    {', '.join(spending_by_day[1])}
WED:
    {', '.join(spending_by_day[2])}
THU:
    {', '.join(spending_by_day[3])}
FRI:
    {', '.join(spending_by_day[4])}
SAT:
    {', '.join(spending_by_day[5])}
SUN:
    {', '.join(spending_by_day[6])}
"""

# Finally let's call the function that will send the email which
# summarizes how much we spent in the week.
send_email_for_spending(round(overallMoneySpent, 2), spending_summary)
