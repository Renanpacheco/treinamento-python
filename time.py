#working with date and time

from datetime import date,time, datetime

def working_with_date():
    current_date=date.today()
    current_date_str=current_date.strftime('%d/%m/%Y-%a-%A-%b-%B')
    print(current_date_str)

def working_with_time():
    tim=time(hour=1,minute=15,second=30)
    print(tim)

def working_with_datetime():
    current_date=datetime.now()
    print(current_date)
    print(current_date.strftime('%c'))
    print(current_date.day)


if __name__ == "__main__":
    #working_with_date()
    #working_with_time()
    working_with_datetime()