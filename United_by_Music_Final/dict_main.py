def main():

    # This file is just to create my list of questions and I will start with one question
    #and then it will be dynamically updated by the user

    import json
    dict = {1: {"What are the musical Institutes in Yerevan ": "Yerevan State Conservatory after Komitas,Sayat-Nova Music School"}}

    with open('my_dict.json', 'w') as f:
        json.dump(dict, f)


main()