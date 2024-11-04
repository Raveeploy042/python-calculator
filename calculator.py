class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        result = 0
        for i in range(b): #change from range(b+1) -> range(b) because for i in range start with 0 
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        if b == 0:
            raise ValueError("Division by zero is not allowed")

        a, b = abs(a), abs(b)
    
        while a >= b: #change from a > b -> a >= b
            a = self.subtract(b, a) #change from self.subtract(a, b) -> self.subtract(b, a) 
            result += 1
        if a < 0 ^ b < 0 :
            return -result
        else :
            return result
    
    def modulo(self, a, b): 
        if b == 0:
            raise ValueError("Modulo by zero is not allowed")
        a, b = abs(a), abs(b)
        while a >= b: #change from a <= b to a >= b
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))