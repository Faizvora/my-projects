class Students:

	def _init_(self, rollno, marks):
		self.rollno = rollno
		self.marks = marks

	def passing(self):
		if (self.marks >= 40):
			print("passing")
		else:
			print("kt")
a = Students(1,41)
a.passing()
b = Students(2,38)
b.passing()
#name, rollno, marks, branch, year, age
