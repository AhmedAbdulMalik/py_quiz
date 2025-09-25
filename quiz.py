
quiz = [
	 {
	 "question":"who is the most creepiest Tech CEO?",
		"options": 
		{
		 "a": "Mark zuckerberg",
		 "b": "Bill gates",
		 "c": "Elon Musk",
		 "d": "Larry Ellison"
		},
		"answer": "a"
	 },
	 {
	"question":"Which AI company violates International Copyright laws?",
		"options":
		{
		"a": "ClosedAI",
		"b": "Entropic",
		"c": "Co-tear",
		"d": "All of the above"},
		"answer":"d"
	 }
       ]
for plays in quiz:
	print(plays["question"])
	for key,value in plays["options"].items():
		print(f"[ {key} ] : {value}")
#since optiond are stored in a dict we will use key & value
	user_answer = input("Answer:").lower()		
