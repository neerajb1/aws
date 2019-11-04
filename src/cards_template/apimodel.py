
from DBHelper.reportoperations import BA_ReportOperations
from datetime import datetime, timedelta,date
import pandas as pd
import numpy as np

class ApiModel:

    def __init__(self, **kwargs):
        self.__reportdbcontext = BA_ReportOperations()

    def get_test_apidata(self):
            try:
                ''' To get all the reports fileters data'''    
                query = "Select * from rp_country limit 10"
                list_data = self.__reportdbcontext.get_report_server_data(query)
                
                if list_data:
                    return list_data
                else:
                    return []
            except Exception as ex :
                print(ex.args[0])
                return []
        