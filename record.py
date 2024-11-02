from phone import Phone
from name import Name
from birthday import Birthday

class Record:

  def __init__(self, name):
    # Ініціалізує запис з ім'ям, порожнім списком телефонів та полем для дати народження.
    self.name = Name(name)
    self.phones = []
    self.birthday = None

  def __str__(self):
    # Повертає рядкове представлення запису.
    contact_info = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    # Якщо є дата народження, то її теж.
    if self.birthday:
      contact_info += f", birthday: {self.birthday}"
      
    return contact_info

  def add_phone(self, number: str):
    # Додає номер телефону до запису.
    self.phones.append(Phone(number))

  def remove_phone(self, number: str):
    # Видаляє номер телефону із запису.
    self.phones = list(filter(lambda phone: phone == number, self.phones))

  def edit_phone(self, old_number, new_number):
    # Редагує номер телефону у записі.
    self.phones = list(
      map(lambda phone: Phone(new_number) if phone.value == old_number else phone, self.phones)
    )

  def find_phone(self, number):
    # Знаходить номер телефону у записі.
    for phone in self.phones:
      if phone.value == number:
        return phone
      
  def add_birthday(self, date):
    # Додає дату народження до запису.
    self.birthday = Birthday(date)
