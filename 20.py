import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', passwd='Aa123456',
                       db='tips', autocommit=True)

def save_user():
    global conn
    id = input("please enter id: ")
    fname = input("please enter first name: ")
    lname = input("please enter last name: ")
    tip = input("please enter tip percentage: ")
    cursor = conn.cursor()
    cursor.execute(f"insert into tips_table values ('{id}','{fname}','{lname}',{tip})")
    cursor.close()

def print_users():
    global conn
    cursor = conn.cursor()
    cursor.execute('select * from tips_table')
    for row in cursor:
        print(row)
        if row[3] > 7:
            print(f"{row[1]} you are very generous!")

    cursor.close()


save_user()
print_users()
conn.close()
