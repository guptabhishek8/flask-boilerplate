import logging

logger = logging.getLogger("flask_app")

class DatabaseClass:
    def __init__(self, db_conn):
        self.conn = db_conn
        self.cursor = self.conn.cursor()

    def execute(self, query, args=None):
        if args:
            self.cursor.execute(query, args)
        else:
            self.cursor.execute(query)
        self.conn.commit()
        return self.cursor

    def fetch_all(self, query, args=None):
        if args:
            self.cursor.execute(query, args)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query, args=None):
        if args:
            self.cursor.execute(query, args)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone()

    def fetch_from_table(self, tableName, columns, whereClause=None, groupClause=None, orderByClause=None):
        query = 'SELECT {} FROM {} '.format(columns, tableName)
        if whereClause:
            query = query + whereClause
        if groupClause:
            query = query + groupClause
        if orderByClause:
            query = query + orderByClause
        print("QUERY: ", query)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_from_table(self, tableName, whereClause=None):
        query = 'DELETE FROM {} '.format(tableName)
        if whereClause:
            query = query + whereClause
        self.execute(query)
        return True

    def update_table(self, tableName, setClause, whereClause=None):
        query = 'UPDATE {} SET {} '.format(tableName, setClause)
        if whereClause:
            query = query + whereClause
        logger.info("UPDATE QUERY %s", query)
        self.execute(query)
        return True

    def insert_into_table(self, tableName, columns, values, updateKey=None):
        query = 'INSERT INTO {} {} VALUES {}'.format(
            tableName, columns, values)
        if updateKey:
            query = query + ' ON DUPLICATE KEY UPDATE {}'.format(updateKey)
        else:
            query = query + ' ON DUPLICATE KEY UPDATE updatedAt=NOW()'
        logger.info("INSERT QUERY %s", query)
        self.execute(query)
        return True
    
    def insert_into_table_with_cursor_return(self, tableName, columns, values, updateKey=None):
        query = 'INSERT INTO {} {} VALUES {}'.format(
            tableName, columns, values)
        if updateKey:
            query = query + ' ON DUPLICATE KEY UPDATE {}'.format(updateKey)
        else:
            query = query + ' ON DUPLICATE KEY UPDATE updatedAt=NOW()'
        logger.info("INSERT QUERY %s", query)
        self.execute(query)
        return self.cursor

    def __del__(self):
        self.cursor.close()
