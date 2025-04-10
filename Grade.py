math = int(input("Enter Math Marks: "))
english = int(input("Enter English Marks: "))
c = int(input("Enter C Marks: "))
python = int(input("Enter Python Marks: "))
java = int(input("Enter Java Marks: "))
mark=(math+english+c+python+java)/5
print("Average Mark: ",mark)
if mark>=90 and mark<=100:
    print("Grade 'O'")
elif mark>=80 and mark<=89:
    print("Grade A")
elif mark>=70 and mark<=79:
    print("Grade B")
elif mark>=60 and mark<=69:
    print("Grade C")
elif mark>=50 and mark<=59:
    print("Grade D")
else:
    print("Grade E")