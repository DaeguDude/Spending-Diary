import gspread
from oauth2client.service_account import ServiceAccountCredentials

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
sheet = client.open('Spending Diary')

# Select the worksheet by its title
worksheet = sheet.worksheet('Week 1')

# Number of Days
num_days = 7
# We are going to sum up how much we spent here at the variable
overallMoneySpent = 0


# it starts from 2 because column that has monday is 2nd column
for day in range(2, num_days + 2):
    dailyMoneySpent = worksheet.col_values(day)

    print(dailyMoneySpent)
# Sort out Days, so we can just read the things we spent on
    count = 0
    for good in dailyMoneySpent:
        if(count == 0):
            count += 1
            continue
        # Now let's extract number from string and add to the variable
        # 'overallMoneySpent' to see how much we spent in the week
        for money in good.split():
            try:
                overallMoneySpent += float(money)
                print(money, "euro added")
            except ValueError:
                pass

print("\nYou have spent", overallMoneySpent, "Euro this week.")
