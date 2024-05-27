#!/usr/bin/env python3

class MyString:
  def __init__(self, value=" "):
      self.value = value


  @property
  def value(self):
      return self._value
  
  @value.setter
  def value(self, new_value):
      if isinstance(new_value, str):
          self._value = new_value
      else:
          print("The value must be a string.")

  def is_sentence(self):
      return self._value.endswith(".")
  def is_question(self):
      return self._value.endswith("?")
  def is_exclamation(self):
      return self._value.endswith("!")
  def count_sentences(self):
      import re
      sentences = re.split(r"[.?!]+", self._value)
      return len([i for i in sentences if i.strip()])
     
    
