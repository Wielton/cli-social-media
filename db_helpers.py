from dbcreds import *
import mariadb

def connect_db():
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(host=host,port=port,database=database,user=user,password=password)
        cursor=conn.cursor()
        return(conn, cursor)
    except mariadb.OperationalError as e: # This will allow to print the exception as it happens
        print("Got an operational error")
        if ("Access Denied" in e.msg):
            print("Failed to log in")
        disconnect_db(conn, cursor)
        
    # if (e.msg.find("Access denied") != -1)
    
def disconnect_db(conn,cursor):
    if(cursor !=None ):
        cursor.close()
    if (conn != None):
        conn.rollback()
        conn.close()

def run_query(statement, args=None):
    try:
        (conn, cursor) = connect_db()
        if statement.startswith("SELECT"):
            cursor.execute(statement,args)
            results = cursor.fetchall()
            return results
        elif statement.startswith("INSERT"):
            cursor.execute(statement,args)
            conn.commit()
        elif statement.startswith("UPDATE"):
            cursor.execute(statement,args)
            conn.commit()
        else:
            cursor.execute(statement, args)
            if cursor.rowcount == 1:
                conn.commit()
                print("Query successful")
            else:
                print("Query failed")
    
    except mariadb.OperationalError as e: # This will allow to print the exception as it happens
        print("Got an operational error")
        if ("Access Denied" in e.msg):
            print("Failed to log in")
    
    # except mariadb.IntegrityError as e: # I NEED TO SET CONSTRAINTS FIRST
    #         print("Integrity error")
    #         print(e.msg)
    
    except mariadb.ProgrammingError as e:
        if("SQL syntax" in e.msg):
            print("Apparently you cannot run program")
        else:
            print("Got a different programming error")
            print(e.msg)
    
    except IndexError as e:
        print("Username doesn't exist")
        print(e.msg)
    
    except RuntimeError as e:
        print("Caught a runtime error")
        print(e.msg)

    except Exception as e:
        print("Username doesn't exist")
        print(e.with_traceback)
        print(e.msg)
        # Better if solution:
        if ("Access denied" in e.msg):
            print("Failed to login")
            print(e.msg)
    finally:
        disconnect_db(conn, cursor)
        print("Database disconnected")
    