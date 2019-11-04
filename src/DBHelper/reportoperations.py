from DBHelper.dbconnection import DbConnection

class ReportOperations:
    
    def __init__(self):
        self.__dbcontext=DbConnection.get_sql_connection()
        self.__reportdbcontext=DbConnection.get_sql_reportserver__connection()

    def get_sqldata_proc(self, procedure_name, *args):
        if self.__dbcontext:
            cursor=self.__dbcontext.cursor()
            try:
                cursor.callproc(procname=procedure_name,args=args)
                rows=cursor.fetchall()
                self.__dbcontext.close()
                return rows
            except Exception as ex :
                self.__dbcontext.rollback()
                return []
        else:
            return []

    def get_report_server_data(self, query):
        if self.__reportdbcontext:
            cursor=self.__reportdbcontext.cursor()
            try:
                cursor.execute(query)
                rows=cursor.fetchall()
                return rows
            except Exception as ex :
                self.__reportdbcontext.rollback()
                return []


class BA_ReportOperations:

    def __init__(self):
        self.__reportope_obj=ReportOperations()
        
    def get_sqldata_proc(self, procedure_name, *args):
        try:
            return self.__reportope_obj.get_sqldata_proc(procedure_name, *args)
        except :
            return []

    def get_report_server_data(self, query):
        try:
            return self.__reportope_obj.get_report_server_data(query)    
        except Exception as ex :
            return []