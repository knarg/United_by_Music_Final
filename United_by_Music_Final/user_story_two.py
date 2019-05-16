import json
#As files are according to field and level by naming them accordingly and calling them using a function.
def showCourse(field , level):
    print("Please wait untill the material is shown")
    from PIL import Image
    image = ("{}_{}.png".format(field, level))
    imagee = Image.open(image)
    imagee.show()
    return;

def main():
    while True:
        print("Your key to music world is ready!!! Start learning...")

        with open("music_data.json") as data_file:
              data = json.load(data_file)
        # openning the data file that contains our variables for this project
        user_data = {"user_data":{}}

        print("Avaliable fields to learn about are : " + " and ".join(list(data["specifications"]["type"].keys())))
        #showing the options
        for key in data:
            user_data["user_data"][key] = input("Please specify what you want to learn about instrument or vocal\n")
        if user_data["user_data"][key] == "instrument":
        #showing options and asking for specififcations to user
            while True:
                print("An instrument can belong to these families: " + " , " .join(list(data["specifications"]["type"]["instrument"]["family"])))
                family_user = input("what is the family of your instrument\n")
                if family_user == "brass" or family_user == "percussion" or family_user == "strings" or family_user == "woodwinds":

                    print("Level options are: " + " , " .join(list(data["specifications"]["type"]["instrument"]["level"])))
                    level_ins = input("What is your level?\n")
                    #storing the user information
                    if level_ins == "beginner" or level_ins == "intermediate" or level_ins == "advanced":
                        data_usr = {}
                        data_usr["data_i_u"] = []
                        data_usr["data_i_u"].append({
                        "type":"instrument",
                        "family":family_user,
                        "level":level_ins})

                        with open('user_specifications.json',"w") as outfile:
                            json.dump(data_usr, outfile)
                        #showing different materials according to different families and levels
                        showCourse(field = family_user, level = level_ins)
                        break
                    else:
                        print("Please type as required")
                else:
                    print("Please type as required")

        elif user_data["user_data"][key] == "vocal":
         # showing options and asking for specififcations to user
            while True:
                print("A voice can belong to the types of: " + " , " .join(list(data["specifications"]["type"]["vocal"]["voice_types"])))
                vtype_user = input("what is the type of your voice?\n")

                if vtype_user  == "alto" or vtype_user == "soprano" or vtype_user == "tenor" or vtype_user  == "bass":

                    print("Level options are: " + " , " .join(list(data["specifications"]["type"]["vocal"]["level_vocal"])))
                    level_v = input("What is your level?\n")
                    if level_v == "beginner" or level_v == "intermediate" or level_v == "advanced":

                        #storing user information
                        data_voice = {}
                        data_usr_v = {}
                        data_usr_v["data_v_u"] = []
                        data_usr_v["data_v_u"].append({
                            "type": "vocal",
                            "voice_type":vtype_user,
                            "level": level_v})

                        with open('user_specifications.json', "w") as outfile:
                            json.dump(data_usr_v, outfile)

                        showCourse(field=vtype_user, level=level_v)
                        break
                    else:
                        print("Please type as required")
                else:
                    print("Please type as required")
        else:
            print("Please print as required")

main()