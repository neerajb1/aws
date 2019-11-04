from .apimodel import ApiModel

class Apicontroler:

    def get_test_apidata(self):
        try:
            return ApiModel().get_test_apidata()
        except Exception as ex :
           
            return []