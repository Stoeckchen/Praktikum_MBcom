
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
    print(today_year - birthday_year - 1)

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

if (birthday_month == 1 and birthday_month == 3  and birthday_month == 5 and birthday_month == 7 and birthday_month == 8  and birthday_month == 8  and birthday_month == 10  and birthday_month == 12):
    birthday_month = 31
elif( birthday_month == 4 and birthday_month == 6 and birthday_month == 9 and birthday_month == 11):
    birthday_month = 30 
elif(birthday_month == 2 ):
    birthday_month = 28



#int (t) = 1
#int (feb) = 28
#int (Jan, Mär, Mai, Jul, Aug, Okt, DEZ) = 31 
#int (Apr, Jun, Sep, Nov) = 30