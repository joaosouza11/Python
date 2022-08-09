from multiprocessing.connection import answer_challenge


def grades(*n, sit=False):
  """
  -> Function to analyze students grades and his situation
  :param n: student grades(multiple accepted)
  :param sit: optional value, can show the studente situation
  :return: dictionary with information about the performance of the class
  """
  r = dict()
  r["total"] = len(n)
  r["biggest"] = max(n)
  r["lower"] = min(n)
  r["average"] = sum(n) / len(n)
  if sit:
    if r["average"] >= 7:
      r["sittuation"] = "GOOD"
    elif r["average"] >= 5:
      r["sittuation"] = "OK"
    else:
      r["sittuation"] = "BAD"
  return r

#Main Program
answer = grades(5.5, 2.5, 1.5, sit=True)
print(answer)
help(grades)