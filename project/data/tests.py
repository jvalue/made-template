import os

def system_test():
    # Check if output files exist
    if not os.path.isfile("data.sqlite"):
        print("Output file data.sqlite does not exist.")
        return False

    # Validate the tables in the SQLite database
    import sqlite3

    try:
        conn = sqlite3.connect("data.sqlite")
        cursor = conn.cursor()

        # Check if SpeedEnforcement table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='SpeedEnforcement'")
        if cursor.fetchone() is None:
            print("SpeedEnforcement table does not exist in the database.")
            return False

        # Check if AccidentData table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='AccidentData'")
        if cursor.fetchone() is None:
            print("AccidentData table does not exist in the database.")
            return False

        cursor.close()
        conn.close()
    except sqlite3.Error as e:
        print("Error while accessing the SQLite database:", str(e))
        return False
    
    return True



# Run the system-level test
if system_test():
    print("System test passed.")
else:
    print("System test failed.")