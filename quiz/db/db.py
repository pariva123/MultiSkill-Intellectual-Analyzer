import mysql.connector
import sys

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="quiz"
)

cursor = con.cursor()

session = ''
category = ''


def getscores(tup):
    cursor=con.cursor(dictionary=True)
    tup.append(session)
    cursor.execute(""" SELECT * FROM `question_wise` qw JOIN `add_question` aq on qw.`ques_id` = aq.`id` WHERE 
    date(qw.`answertime`)=%s and aq.`category`= %s and qw.`user_id`=%s """,tup)
    print(cursor.statement)
    return(cursor.fetchall())


def fetch_category():
    cursor.execute("SELECT * FROM `add_category` ")
    return (cursor.fetchall())


def addtotalscore(tup):
    tup.insert(0, session)
    cursor.execute("INSERT INTO `users_scores`(`user_id`, `category`, `scores`) VALUES (%s,%s,%s)", tup)
    con.commit()


def set_question_result(args):
    args.insert(2, session)
    cursor.execute("""INSERT INTO `question_wise`(`ques_id`, `result`, `user_id`, `selectedopt`) VALUES 
    (%s,%s,%s,%s)""", args)
    con.commit()


def fetch_questions(self):
    cursor.execute("SELECT * FROM `add_question` where `category` like '{}'".format(category))
    return (cursor.fetchall())


def login_page(tup):
    try:
        cursor.execute("SELECT * FROM login_page WHERE email=%s AND password=%s", tup)
        return (cursor.fetchone())
    except:
        return False


def add_category(tup):
    try:
        cursor.execute("insert into add_category(name,status) values(%s,%s)", tup)
        con.commit()
        return True
    except:
        print(sys.exc_info())
        return False


def delete_category(tup):
    cursor.execute("delete from add_category where id=%s", tup)
    con.commit()
    return True


def delete_question(tup):
    cursor.execute("delete from add_question where id=%s", tup)
    con.commit()
    return True


def update_category(tup):
    cursor.execute("update add_category set name=%s where id=%s", tup)
    con.commit()
    return True


def update_password(tum, tup):
    print(tum)
    try:
        cursor.execute("select * from users_login where email=%s and password=%s", tum)
        if cursor.fetchone():
            cursor.execute("UPDATE users_login SET password=%s where email=%s", tup)
            con.commit()
            return True
        else:
            return False
    except:
        print(sys.exc_info())
        return False


def edit_question(tum, tup):
    print(tum)
    try:
        cursor.execute("select * from add_question where category=%s and question=%s", tum)
        if cursor.fetchone():
            cursor.execute("UPDATE edit_question SET category=%s where question=%s", tup)
            con.commit()
            return True
        else:
            return False
    except:
        print(sys.exc_info())
        return False


def manage_category():
    cursor.execute("select * from add_category")
    return cursor.fetchall()


def add_question(tup):
    try:
        cursor.execute(
            "insert into add_question(category,question,option_1,option_2,option_3,option_4,answer) values(%s,%s,%s,%s,%s,%s,%s)",
            tup)
        con.commit()
        return True
    except:
        print(sys.exc_info())
        return False


def manage_question():
    cursor.execute("select * from add_question")
    return cursor.fetchall()


def manage_users():
    cursor.execute("select * from users_register")
    return cursor.fetchall()


def scores():
    cursor.execute("select * from users_scores")
    return cursor.fetchall()


def users_register(tup):
    try:
        cursor.execute("insert into users_register(name,email,contact,gender,password) values(%s,%s,%s,%s,%s)", tup)
        con.commit()
        return True
    except:
        print(sys.exc_info())
        return False


def users_login(tup):
    try:
        cursor.execute("SELECT * FROM users_login WHERE email=%s AND password=%s", tup)
        return (cursor.fetchone())
    except:
        return False


def users_scores():
    data=(
        session,
    )
    cursor.execute("select * from users_scores where user_id=%s",data)
    return cursor.fetchall()


def student_login(tup):
    print(tup)
    cursor.execute("SELECT * FROM users_register WHERE email=%s AND password=%s", tup)
    return cursor.fetchone()


def delete_users(tup):
    cursor.execute("delete from users_register where id=%s",tup)
    con.commit()
    return True

def delete_scores(tup):
    cursor.execute("delete from users_scores where id=%s",tup)
    con.commit()
    return True

def update_admin_pass(tum, tup):
    print(tum)
    try:
        cursor.execute("select * from login_page where email=%s and password=%s", tum)
        if cursor.fetchone():
            cursor.execute("UPDATE login_page SET password=%s where email=%s", tup)
            con.commit()
            return True
        else:
            return False
    except:
        print(sys.exc_info())
        return False