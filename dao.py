import mysql.connector
import time



def connect():
    cnx = mysql.connector.connect(host="localhost",
    port=3306,
    database="DRIVER_DROWSINESS",
    user="root",
    password="Database_sucks55")
    return cnx


def session_details():
    cnx = connect()
    cursor = cnx.cursor()
    query = "select t.number as TaxiNumber , u.firstname as FirstName, u.lastname as LastName, u.code as Code," \
            "DATE_FORMAT(s.START_TIME, '%M %D, %Y %H:%m:%s') as StartTime, DATE_FORMAT(s.END_TIME, '%M %D, %Y %H:%m:%s') as EndTime, ss.actionedTime as Status " \
            "FROM DRIVER_DROWSINESS.session s LEFT JOIN DRIVER_DROWSINESS.sos ss ON s.id = ss.sessionId , DRIVER_DROWSINESS.taxi t, DRIVER_DROWSINESS.user u " \
            "WHERE s.TAXI_ID = t.ID and s.USER_id = u.ID and u.type = 'Driver'  and u.status='Active'"
    print(query)
    cursor.execute(query)
    res = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
    print(res)
    for row in res:
        if row['Status'] is None:
            row.update({'Status':'Active'})
        else:
            row.update({'Status':'SOS Actioned'})
    print(res)
    # return cursor.fetchall()
    return res


def sos_details(sid=None):
    print(sid)
    if sid is not None:
        action_sos(sid)

    query = "select s.id as ID, u.firstname as FirstName, u.lastname as LastName, t.number as TaxiNumber, u.code as CODE, s.details as SosDetails," \
        " DATE_FORMAT(s.createdTime, '%M %D, %Y %H:%m:%s') as CreatedTime, DATE_FORMAT(s.actionedTime, '%M %D, %Y %H:%m:%s') as ActionedTime" \
        " FROM DRIVER_DROWSINESS.sos s, DRIVER_DROWSINESS.taxi t, DRIVER_DROWSINESS.user u " \
        "WHERE s.taxiid = t.ID and s.taxiid = u.ID and u.type = 'Driver' and u.status='Active'" \
        "AND s.actionedTime IS NULL"


    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(query)

    res = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
    print(res)
    return res


def raise_sos():
    print("Raise SOS ......")
    cnx = connect()
    cursor = cnx.cursor()
    query = """INSERT INTO DRIVER_DROWSINESS.sos(`taxiid`, `driverid`, `details`, `status`, `createdtime`) VALUES
     (1, 2, 'SOS Please check Priority 5', 'NEW', '2023-06-06 011:00:00')"""

    cursor.execute(query)
    cnx.commit()

    cursor.close()
    cnx.close()

def action_sos(sid):
    cnx = connect()
    cursor = cnx.cursor()

    date = time.strftime('%Y-%m-%d %H:%M:%S')
    print(date)
    query = "UPDATE DRIVER_DROWSINESS.sos SET actionedTime = '" + time.strftime('%Y-%m-%d %H:%M:%S') + "' WHERE id =" + sid

    cursor.execute(query)
    cnx.commit()

    cursor.close()
    cnx.close()


class DAO:
    if __name__ == "__main__":
        # raise_sos()
        action_sos2()
