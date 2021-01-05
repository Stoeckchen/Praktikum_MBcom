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
    print(today_year - birthday_year - 1)

elif(today_month > birthday_month):
    print(today_month - birthday_month)
    
else:
    if(today_day < birthday_day):
        print(today_year - birthday_year -1)
    else:
        print(today_year - birthday_year)
