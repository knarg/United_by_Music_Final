def main():
    import json

    # Opening my dictionary that has one question only ( please refer to the other file to see it )
    with open('my_dict.json') as f:
        dict = json.load(f)

    # prompting the user to input the required details
    while True:
        j = 1
        print("Please choose number from the following:")
        print("1 : Ask new Question")
        print("2 : See the previously asked questions")
        print("3 : Answer existing question")

        user_input= int(input())


        if user_input == 1:

            # taking the user question

            user_ask = input("what is your question?\n")

            #Adding the question at the end of our list of questions

            dict[int(len(dict.keys())+1)]=  {user_ask:""}

            # saving it as json file

            with open('my_dict.json', 'w') as f:
                json.dump(dict, f)
            print("Your question has been saved")
           

        elif user_input == 2:
            # loading the json file to view the latest questions

            with open('my_dict.json') as f:
                dict = json.load(f)

            # This prints out the question and answers
            for i in dict.values():
                print('Question number',j,":", list(i.keys())[0],'The Answer:', list(i.values())[0])
                j = j+1
        elif user_input == 3:

            with open('my_dict.json') as f:
                dict = json.load(f)

            # getting the required detailes
            for i in dict.values():
                print('Question number',j,":", list(i.keys())[0],'The Answer:', list(i.values())[0])
                j = j+1

            question_number = input('What is the number of the question you want to answer ?\n ')

            user_question = ""
            for key in dict[question_number].keys():
                user_question = key
                break
            print("The questıon is", user_question)
            user_answer = input("Please Insert your answer?\n")

            dict[question_number] = {user_question: user_answer}

            # saving the changes to json file to be viewed later

            with open('my_dict.json', 'w') as f:
                json.dump(dict, f)
            print("Your answer has been saved")

        else:
            print("Please type as required")

main()
