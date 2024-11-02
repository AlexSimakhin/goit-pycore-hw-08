from collections import UserDict
from datetime import datetime, timedelta
from constants import DATE_FORMAT

class AddressBook(UserDict):
  
  def add_record(self, record):
    # Додає запис за ім'ям.
    self.data[record.name.value] = record

  def find(self, name):
    # Знаходить запис за ім'ям.
    record = self.data.get(name, None)
    return record

  def delete(self, name):
    # Видаляє запис за ім'ям.
    del self.data[name]
    
  def get_upcoming_birthdays(self):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for name, record in self.data.items():
      birthday = record.birthday
      
      if birthday:
        # Отримуємо день народження в поточному році
        birthday_this_year = birthday.value.replace(year=today.year).date()
        
        # Якщо день народження вже минув цього року, перевіряємо наступний рік
        if birthday_this_year < today:
          birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Перевіряємо, чи знаходиться день народження в межах наступного тижня
        days_until_birthday = (birthday_this_year - today).days
        
        if 0 <= days_until_birthday <= 7:
          congratulation_date = birthday_this_year
          
          # Переносимо на наступний понеділок, якщо день народження - вихідний
          if congratulation_date.weekday() == 5:  # Субота
            congratulation_date += timedelta(days=2)
          elif congratulation_date.weekday() == 6:  # Неділя
            congratulation_date += timedelta(days=1)

          # Додаємо до списку
          upcoming_birthdays.append({
            "name": name,
            "congratulation_date": congratulation_date.strftime(DATE_FORMAT)
          })
    
    return upcoming_birthdays
  
  def __str__(self):
    lines = [str(record) for record in self.data.values()]
    return "\n".join(lines)
  