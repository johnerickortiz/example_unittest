class string_handler(object):
    """ Perform basic string operations"""
    def __init__(self):
        pass
    def add_str(self,*str_):
        s=''
        for i in str_:
            s +=i
        return s
    def subtract_str(self,from_:str, str_:str):
        s = from_.replace(str_,"")
        return s

# def prueba_string():
#     calc = string_handler()
#     print(calc.add_str("ABC","DE","F"))
#     print(calc.subtract_str("xyzw","yz"))