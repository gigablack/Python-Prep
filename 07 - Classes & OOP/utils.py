class Utils:
    def __init__(self):
        self.lista = [1,2,3,4,5,6,7,8,9]
    def verificar_primo(self,num):
        if num < 2:
            return False
        prime = True
        for i in range(2,num):
            if((num % i) == 0):
                prime = False
                break
        return prime
    def valor_modal(self,lis,first=True):
        num = {}
        for i in set(lis):
            num[lis.count(i)] = i
        if first:
            return num[max(num)]
        else:
            num.pop(max(num))
            return num[max(num)]
    def conversor_grados(self,value,origin,destiny):
        def c_2_f(c):
            return (c * (9/5)) + 32
        def c_2_k(c):
            return c + 273.15
        def k_2_c(k):
            return k - 273.15
        def f_2_c(f):
            return (f - 32)*5/9
        if origin == 'celsius':
            if destiny == 'farenheit':
                return c_2_f(value)
            else:
                return c_2_k(value)
        elif origin == 'farenheit':
            if destiny == 'celsius':
                return f_2_c(value)
            else:
                return c_2_k(f_2_c(value))
        else:
            if destiny == 'celsius':
                return k_2_c(value)
            else:
                return c_2_f(k_2_c(value))
    def factorial(self,num):
        if type(num) != int or num < 0:
            print('introduzca un numero entero positivo')
        else:
            fac = 1
            while(num > 0):
                fac = fac * num
                num -= 1
            return fac
