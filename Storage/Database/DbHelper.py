import sqlite3

class DbHelper(object):
    def __init__(self, dbPath: str):
        self.conn = sqlite3.connect(dbPath)

    def IsOpen(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT 1")
            return True
        except sqlite3.Error:
            return False
        finally:
            try:
                cursor.close()
            except:
                 pass

    def Close(self):
        if self.IsOpen():
            self.conn.close()
