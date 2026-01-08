from datetime import datetime as dt

class Calculator:
        
    def simple_calc(self, oprdL, oprdR, oprtr):
        left = float(oprdL)
        right = float(oprdR)
        match oprtr:
            case '+':
                return left + right 
            case '-':
                return left - right 
            case '*':
                return left * right 
            case '/':
                return left / right 
            case '%':
                return left % right 
            
    def percentage_calc(self, part, whole):
        part = float(part)
        whole = float(whole)
        return (part/whole) * 100
    
    # def age_calc(self, d1, d2):
    #     start, end = sorted([d1, d2])
    #     return end - start

    def age_calc(self, d1, d2):
        start, end = sorted([d1.date(), d2.date()])
        
        years = end.year - start.year
        months = end.month - start.month
        days = end.day - start.day

        if days < 0:
            months -= 1
            days += 30  # approx

        if months < 0:
            years -= 1
            months += 12

        return years, months, days


            

# Function Testing

if __name__ == '__main__':

    calc = Calculator()

    print('----------------simple calc--------------------')

    print('1 + 2 =', (calc.simple_calc(1, 2, '+')))
    print('1 - 2 =', calc.simple_calc('1', '2', '-'))
    print('1 * 2 =', calc.simple_calc('1', '2', '*'))
    print('1 / 2 =', calc.simple_calc('1', '2', '/'))

    print('----------------percentage calc--------------------')

    print(calc.percentage_calc(388, 600),'%')

    print('----------------Age calc--------------------')

    rd = (calc.age_calc(dt.strptime('2005-1-05', '%Y-%m-%d'), dt.strptime('2026-01-07', '%Y-%m-%d')))
    
    # rd = calc.age_calc(dt.strptime('2005-1-05', '%Y-%m-%d'), dt.today())
    print(rd)
