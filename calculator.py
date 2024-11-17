class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        is_negative = False
        if b < 0:
            is_negative = True
            b = -b  # 

        result = 0

        for i in range(b):
            result = self.add(result, a)
        if is_negative:
            result = -result
            
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        # Handle signs
        is_negative = (a < 0) != (b < 0)  # True if only one number is negative
        a, b = abs(a), abs(b)
        
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result = self.add(result, 1)
            
        return -result if is_negative else result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")
            
        while a >= b:
            a = self.subtract(a, b)
            
        return a