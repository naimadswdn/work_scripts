import pypyodbc
import pandas as pd


class RunQueryMssql(object):
    def __init__(self, user, password, server, database):
        self.user = user
        self.password = password
        self.server = server
        self.database = database
        self.connection_string='Driver={SQL Server};'+ f'Server={self.server};Database={self.database};Uid={self.user};Pwd={self.password};'
        self.connection = pypyodbc.connect(self.connection_string)

    def __str__(self):
        return """
        Class that allow to run SQL query on MSSQL database. Parameters needed are: user, password, server, database - all are strings.
Functions:
    - select - execute select statement against database. It return a list of tuples with results (each tuple is one row).
    - insert_update - execute insert/update/detete statement against database. Commit is included as well.
    - table_columns - it returns column names for table defined from sql from parameter. It is a list of strings.??
        """

    def test_mssql_connection(self):
        """
        Function to test connection to Oracle database.
        :return: OK/Error depending of connection status.
        """
        try:
            cur = self.connection.cursor()
            print('Connection ok')
        except:
            print('Error!')

    def select(self, sql):
        """
        Function to run select statement against database and return result.
        Column names are displayed as well by default.
        :param sql: SQL query that is going to be executed.
        :return: Result is a tuple of lists with results.
        """
        result = []
        cur = self.connection.cursor()
        cur.execute(sql)
        column_names = [row[0] for row in cur.description]
        for i in cur:
            result.append(i)
        try:
            column_names = tuple(column_names)
            result.insert(0,column_names)
        except TypeError:
            type_result = type(result)
            type_column_names = type(column_names)
            return 'Issue with types! Result type: {} is differ then column_names type: {}.Please check'.format(type_result, type_column_names)
        return result

    def insert_update(self, sql):
        """
        Function to run insert/update statement against database. Autocommit is on.
        :param sql: SQL query that is going to be executed.
        :return: Done/Error depending on query run result.
        """
        cur = self.connection.cursor()
        cur.execute(sql)
        self.connection.commit()
        return 'Done!'

    def table_columns(self, sql):
        """
                Returns table columns. Basically it need to run a query on a table to get columns description.
        :param sql: Random sql executed against table that we want to know columns names.
        :return: Return is a tuple with column names 
        """
        col_names = []
        cur = self.connection.cursor()
        cur.execute(sql)
        col_names_list = [row[0] for row in cur.description]
        for i in col_names_list:
            col_names.append(i)
        return col_names

    def pandas_query(self,sql):
        pd.set_option('display.max_columns', 30)
        df = pd.read_sql_query(sql, self.connection)
        return df

 
