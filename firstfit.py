spaces = input("Enter the spaces with a space gap: ").split(" ")
spaces = [int(i) for i in spaces]

inserts = input("Enter the inserts with a space gap: ").split(" ")
inserts = [int(i) for i in inserts]

for i in inserts:
    inserted = False
    for j in (range(len(spaces))):
        if spaces[j] >= i:
            print(f"{i} inserted at {spaces[j]}")
            spaces[j] -= i
            inserted = True
            break
    if inserted == False:
        print(f"cannot insert : {i}")
