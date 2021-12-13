#basic grade checker
GradeBoundaries = {'A': 75,'B':60,'C': 52,'D': 41,'E': 20,'F': 10}
#put in the dictionary as a way to show the grade boundaries more easily
def GradeChecker():
  GradeScore = int(input('What is your score?'))
  while GradeScore < 0 or GradeScore > 100:
    GradeScore = int(input('Can you please make it above 0?'))
  return GradeScore 
# the function above inputs the score
class Grades:
  def __init__(self,Boundaries,Grade):
    self.Boundary = {}#initialises the dictionary
    self.Boundary.update(Boundaries) #updates the dictionary from GradeBoundaries into the empty dictionary for usage
    self.Grade = 0 # sets the grade to 0 because I has no idea what else to do to define it as
    self.Grade += Grade # updates the grades from the function above

  def GradeA(self):
    if self.Grade >= self.Boundary['A']: # compares the curent grade to the boundary, if the grade inputted is higher than boundary A, the return True
      return True # returned True for the if statements below

  def GradeB(self):
    if self.Grade < self.Boundary['A'] and self.Grade >= self.Boundary['B']: # creates a range through 'and' statements, in addition to the operators
        return True

  def GradeC(self):
    if self.Grade < self.Boundary['B'] and self.Grade >= self.Boundary['C']:
        return True

  def GradeD(self):
    if self.Grade < self.Boundary['C'] and self.Grade >= self.Boundary['D']:
        return True

  def GradeE(self):
    if self.Grade < self.Boundary['D'] and self.Grade >= self.Boundary['E']:
        return True

  def GradeF(self):
    if self.Grade < self.Boundary['E'] and self.Grade >= self.Boundary['F']:
        return True

  def GradeU(self):
    if self.Grade < self.Boundary['F']:
      return True



Grading = Grades(GradeBoundaries,GradeChecker())
if Grading.GradeA(): # prints the grade
  print('A')
elif Grading.GradeB():
  print('B')
elif Grading.GradeC():
  print('C')
elif Grading.GradeD():
  print('D')
elif Grading.GradeE():
  print('E')
elif Grading.GradeF():
  print('F')
elif Grading.GradeU():
  print('U')
