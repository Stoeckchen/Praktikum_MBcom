
birthday = input("Geburtstag(TT.MM.JJJJ): ")
birthday_list = birthday.split(".")
print(birthday_list[2])

birthday_day = int( birthday_list [0])
birthday_month = int(birthday_list [1])
birthday_year = int(birthday_list[2])


today = input ("Datum(TT.MM.JJJJ): ")
today_list = today.split(".")
print(today_list[2])

today_day = int(today_list[0])
today_month = int(today_list[1])
today_year = int(today_list[2])


if(today_month < birthday_month):
    age_year = (today_year - birthday_year-1)
    print((today_year - birthday_year - 1))

elif(today_month > birthday_month):
    age_year = (today_year - birthday_year)
    print(today_month - birthday_month)
    
else:
    if(today_day < birthday_day):
        age_year = (today_year - birthday_year -1)
        print(today_year - birthday_year -1)
    else:
        age_year = (today_year - birthday_year)
        print(today_year - birthday_year)

age_days = age_year * 365

def getDays(month):
    if (month == 1 and month == 3  and month == 5 and month == 7 and month == 8  and month == 8  and month == 10  and month == 12):
        month = 31
    elif(month == 4 and month == 6 and month == 9 and month == 11):
        month = 30 
    elif(month == 2 ):
        month = 28

    month_31 = month * 31 
    month_30 = month * 30
    month_28 = month * 28
    #month_29 = month *29

    if(month == 1):
        month_31 * 1 + month_30 * 0 + month_28 * 0 = age_monthTodays
    elif(month == 2):
        month_31 * 1 + month_30 * 0 + month_28 * 1
    elif(month == 3):
        month_31 * 2 + month_30 * 0 + month_28 * 1
    elif(month == 4):
        month_31 * 2 + month_30 * 1 + month_28 * 1
    elif(month == 5):
        month_31 * 3 + month_30 * 1 + month_28 * 1
    elif(month == 6):
        month_31 * 3 + month_30 * 2 + month_28 * 1
    elif(month == 7)
        month_31 * 4 + month_30 * 2 + month_28 * 1
    elif(month == 8)
        month_31 * 5 + month_30 * 2 + month_28 * 1
    elif(month == 9)
    

#int (t) = 1
#int (feb) = 28
#int (Jan, Mär, Mai, Jul, Aug, Okt, DEZ) = 31 
#int (Apr, Jun, Sep, Nov) = 30