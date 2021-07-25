
def int_checker(string):
  digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
  if len(string) == 0:
    return string
  for i in string:
    if i not in digits:
      return ""
  return int(string)
