class Currency:

  currencies =  {'CHF': 0.930023, #swiss franc 
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar
      
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def __str__(self):
    
    return self. __repr__()
  
  
  # This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
  def __repr__(self):
  
    return f"Currency(value={self.value:.2f}, units='{self.unit})"
  
   # can also use round
    

  def changeTo(self, new_unit):
    """
      An Currency object is transformed from the unit "self.unit" to "new_unit"
    """
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit

  
  def __add__(self,other):
    # Defines the '+' operator.
    #   If other is a Currency object the currency values 
    #   are added and the result will be the unit of 
    #   self. If other is an int or a float, other will
    #   be treated as a USD value. 
 
    if isinstance(other, Currency):
        # If other is a Currency object
        # Convert 'other' to the same unit as 'self'
        other_converted = Currency(other.value, other.unit)
        other_converted.changeTo(self.unit)
        # Add the values
        new_value = self.value + other_converted.value
        return Currency(new_value, self.unit)
    elif isinstance(other, (int, float)):
        # If other is an int or float (treat as USD)
        # Convert 'other' USD value to the same unit as 'self'
        other_converted = Currency(other, "USD")
        other_converted.changeTo(self.unit)
        # Add the values
        new_value = self.value + other_converted.value
        return Currency(new_value, self.unit)
    
 #  This is similar to _ad_ , but it modifies the the instance itself rather than returning a new instance.

    def __iadd__(self, other):
     result = self + other
     if result is NotImplemented:
        return result
     self.value = result.value
     self.unit = result.unit
    return self
  

  # __sub__ handles subtractions where the right operand is either currency or a numeric value in this case. 
  def __sub__(self, other):
    if isinstance(other, Currency):
        # If other is a Currency object
        # Convert 'other' to the same unit as 'self'
        other_converted = Currency(other.value, other.unit)
        other_converted.changeTo(self.unit)
        # Subtract the values
        new_value = self.value - other_converted.value
        return Currency(new_value, self.unit)
    elif isinstance(other, (int, float)):
        # If other is an int or float (treat as USD)
        # Convert 'other' USD value to the same unit as 'self'
        other_converted = Currency(other, "USD")
        other_converted.changeTo(self.unit)
        # Subtract the values
        new_value = self.value - other_converted.value
        return Currency(new_value, self.unit)
    else:
        return NotImplemented




    #  The __radd__method handles addition when the left operand is not of the class, but the right is. It allows operations like 3 +
    #  currency in this case. by defining how to add numbers to a cuurency object.
  
  def __radd__(self, other):
      if isinstance(other, (int, float)):
        other_converted = Currency(other, "USD")
        return other_converted + self
      return NotImplemented

  #  The __rsub__ handles subtraction where the left operand is not a currency in this case. This method is used when a numeric 
  # value is on the left side of the subtraction operstor and a currency (object) is on the right.

  def __rsub__(self, other):
    if isinstance(other, (int, float)):
        result_value = other - (self.value * Currency.currencies[self.unit])
        return Currency(result_value, "USD")
    return NotImplemented



v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print( 3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 

