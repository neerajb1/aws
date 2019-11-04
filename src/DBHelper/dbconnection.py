import pymysql
import os

class DbConnection :

    @staticmethod
    def get_sql_connection():
        try:
            ##AWS connection
            ##connection="dbname='cadb', user='careaduser',password='TechTree@123', host='ca-prod-reporting.c9c5qvqcyavi.ap-south-1.rds.amazonaws.com'"
            ##SIT Connection
            #dbname='cadb'
            #user='cadbuser'
            #password='cadbuser'
            #host='192.168.2.86'
            #port=3306
            #connection=pymysql.connect(host=host,database=dbname,user=user,password=password,port=port,cursorclass=pymysql.cursors.DictCursor)
            #return connection
            return DbConnection.get_sql_reportserver__connection()
        except Exception as ex :
            return False

    @staticmethod
    def get_sql_reportserver__connection():
        try:
              
            Evn_Key='PROD'
            
            
            
            if(Evn_Key=='PROD'):

              dbname='cadb'
              user='cadbuser'
              password='CAdbUserAt51015'
              host='reciproci-reports.c9c5qvqcyavi.ap-south-1.rds.amazonaws.com'
              port=3306
              connection=pymysql.connect(host=host,database=dbname,user=user,password=password,port=port,cursorclass=pymysql.cursors.DictCursor)
              return connection


            if(Evn_Key=='UAT'):

              dbname='cadb'
              user='pythonuser'
              password='TechTree@123'
              host='13.232.18.208'
              port=3306
              connection=pymysql.connect  (host=host,database=dbname,user=user,password=password,port=port,cursorclass=pymysql.cursors.DictCursor)
              return connection


            
            

            if(Evn_Key=='DemoDb'):

                dbname='cadb'
                user='reciproci'
                password='reciproci@123'
                host='18.209.77.28'
                port=3306
                connection=pymysql.connect  (host=host,database=dbname,user=user,password=password,port=port,cursorclass=pymysql.cursors.DictCursor)
                return connection


        except Exception as ex :
            return False


