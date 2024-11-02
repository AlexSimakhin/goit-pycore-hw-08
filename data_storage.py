import pickle
from address_book import AddressBook
from constants import FILE_DATA_PKL

def save_data(book, filename=FILE_DATA_PKL):
  with open(filename, "wb") as file:
    pickle.dump(book, file)

def load_data(filename=FILE_DATA_PKL):
  try:
    with open(filename, "rb") as file:
      return pickle.load(file)
  except FileNotFoundError:
    return AddressBook()