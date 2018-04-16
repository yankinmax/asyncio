class Value:     
    def __init__(self):
        self.value = None
    
    @staticmethod
    def _prepare_value(value):
        return value - int(value * new_account.commission)

    def __get__(self, obj, obj_type):
        return self.value
    
    def __set__(self, obj, value):
        self.value = self._prepare_value(value)

class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount)

#________________________________________________________________#
class Value:
    def __init__(self):
        self.amount = 0

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        self.amount = value - int(value * obj.commission)


class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount)