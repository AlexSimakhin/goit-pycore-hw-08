from field import Field

class Phone(Field):

  def __init__(self, number):
    # Ініціалізує поле Phone з номером телефону.
    self.value = self.validate_number(number)

  def validate_number(self, number):
    # Перевіряє правильність номера телефону.

    if len(number) != 10:
      raise ValueError("The phone number must contain 10 digits")

    if not number.isdigit():
      raise ValueError("The phone number must contain only numbers")

    return number
