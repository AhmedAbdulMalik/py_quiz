q1 = "who is the most creepist Tech CEO?"
op1 = "[a]:Mark zuckerberg"
op2 = "[b]:Bill gates"
op3 = "[c]:Elon Musk"
op4 = "[d]:Larry Ellison"
a1 = "a"

answer = input(f"{q1}\n{op1}\n{op2}\n{op3}\n{op4}\n")
answer = answer.lower()

if answer==a1:
	print("Correct")
else:
	print("wrong")

