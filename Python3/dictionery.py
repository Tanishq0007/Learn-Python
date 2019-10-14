def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f"There are {num} {belt} belts")

# def ninja_intro(dictionary):
#     for key,val in dictionary.items():
#         print(f"Iam {key} and iam {val} belt")
ninja_belts = {}

while True:
    ninja_name = input("Enetr a ninja name:")
    ninja_belt = input("Enter the belt:")
    ninja_belts[ninja_name] = ninja_belt

    another = input("Want to add more?(y/n):")
    if another == 'y':
        continue
    else:
        break

#ninja_intro(ninja_belts)
belt_count(ninja_belts)
