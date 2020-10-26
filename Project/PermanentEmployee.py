class Per_Emp:
      __salary = 5000

      def calculatesalary(self,exp):
            #2 Implement “calculatesalary” method
            if exp >= 15:
                  return self.__salary + (self.__salary * 20) / 100
            elif 10 <= exp < 15:
                  return self.__salary + (self.__salary * 10) / 100
            elif 5 <= exp < 10:
                  return self.__salary + (self.__salary * 5) / 100
            else:
                  return self.__salary         