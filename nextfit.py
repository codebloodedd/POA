spaces = input("Enter the spaces with a space gap: ").split(" ")
spaces = [int(i) for i in spaces]

inserts = input("Enter the inserts with a space gap: ").split(" ")
inserts = [int(i) for i in inserts]

temp = 0

for i in inserts:
    inserted = False
    if temp == 0:
        for j in (range(len(spaces))):
            if spaces[j] >= i:
                print(f"{i} inserted at {spaces[j]}")
                spaces[j] -= i
                inserted = True
                temp = j
                break
    else:
        for j in (range(temp , len(spaces))):
            if spaces[j] >= i:
                print(f"{i} inserted at {spaces[j]}")
                spaces[j] -= i
                inserted = True
                temp = j
                break
        for j in (range(temp)):
            if spaces[j] >= i:
                print(f"{i} inserted at {spaces[j]}")
                spaces[j] -= i
                inserted = True
                temp = j
                break

    if inserted == False:
        print(f"cannot insert : {i}")
