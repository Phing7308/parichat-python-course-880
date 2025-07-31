# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Parichat", 20, "chonburi", "thai")  # name, age, city, country
    hobbies = []
    
    # Your code here
    while true:

          print("1 Display into,2 Add hobby,3 Remove hobby, 4 Edit age, 5 Exit")
          choice = input("What do you want to do?:")
    
    if choice == "1":
        print("Name:",person[0])
        print("Age:",person[1])
        print("City:",person[2])
        print("Country:",person[3])
        print("Hobbies:,person")
    
    elif choice == "2"
        hobby = input("Insert new hobby: ")
        hobbies.append(hobby)
    
    elif choice == "3"
         dle  hobbies[0]

    elif choice == "4"
        age = int(input("Insert new age: "))
        person_list = list(person)# ["Parichat",20,"Chonburi","Thai"]
        person_list[1]= age
        person = tuple(person_list)


 

if __name__ == "__main__":
    personal_info_manager()