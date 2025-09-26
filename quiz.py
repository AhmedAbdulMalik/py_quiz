import textwrap
game_score = 0

startup_text = "Welcome to THE quiz, where correct answer gets you +4 and wrong answers get you -1 \n totally not trying to revive the PTSD of JEE :)\nHAVE FUN\n"

wrapped_startuptext = textwrap.wrap(startup_text, width=30)
for line in wrapped_startuptext:
	print(line)
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
	user_answer = input("Answer:").strip().lower()
	
	if user_answer == plays["answer"]:
		print("Correct!")
		game_score += 4 
	else:
		print(f"LOL you are Wrong!\n {plays["answer"]} was the correct answer")
		game_score -= 1
print(f"The final score is {game_score}") 		
