from module1 import Question  

#this the array of questions that will be showed to the 
question_prompt = ["what color are apple?\n(a)red\n(b)burble\n(c)orange",
                   "what color are bananas?\n(a)teal\n(b)magenta\n(c)yeallow",
                   "what color are strewberries?\n(a)yellow\n(b)red\n(c)green"]


#array of the instanciated objects 
questions=[Question(question_prompt[0],"a"),
           Question(question_prompt[1],"c"),
           Question(question_prompt[2],"b")
           ]

          
#def that save the input of the user, check the input , create the score 
def run_test(element):
    score = 0
    for element in questions :
        #take user input 

        userInput = input(element.prompt)

        if (element.answer == userInput):
            score +=1 

    return print(f"you got {score} out of {str(len(questions))}")

    #call of a function
run_test(questions)


 



