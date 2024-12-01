import json
import os

class JsonDialogues:
    def __init__(self):
        self.root = {}
        self.running = True
    
    def create_options(self, option_amount: int):
        options = {}
        for i in range(option_amount):
            option_id = input("Type an option id, please: ")
            option_text = input("Write an option text, please: \n")
            options[option_id] = option_text
        
        return options
    
    def create_dialogue(self, name: str):
        dialogue = {}
        id = int(input("Type an id for dialogue, please: "))
        text = input("Write a dialogue here: \n")
        opt_amount = int(input("Type an amount of your options, please: "))
        options = self.create_options(opt_amount)
        dest_id = int(input("Type a destination id for your dialogue here: "))

        dialogue[name] = {"id": id, "text": text, "options": options, "dest_id": dest_id}
        return dialogue[name]
    
    def create_dialogue_structure(self):
        name = input("Please, name your dialogue: \n")
        if name in self.root:
            print(f"{name} has already created, please try with another name.")
            return
        dialogue = self.create_dialogue(name)
        self.root[name] = dialogue
        
    def setup(self):
        while self.running:
            print("***Welcome to JSONDialogues!***\n")
            file_name = input("Name or load your JSON file, please: \n")
            for file in os.listdir(os.getcwd()):
                if file.startswith(file_name):
                    with open(file_name, "r") as j:
                        data = json.load(j)
                        self.root = dict(data)
                        print(f"JSON Content: {self.root}")
                    self.create_dialogue_structure()
                else:
                    self.create_dialogue_structure()
                    with open(file_name, "w") as jsonfile:
                        json.dump(self.root, jsonfile, indent=4)
                    wannaExit = bool(input("\nDo you wanna exit this software?: "))
                    if wannaExit:
                        print("Thank you for using this software!")
                        break
                    else:
                        continue

if __name__ == "__main__":
    jsonDialogues = JsonDialogues()
    jsonDialogues.setup()