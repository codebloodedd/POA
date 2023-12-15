spaces = input("Enter the spaces with a space gap: ").split(" ")
spaces = [int(i) for i in spaces]
spaces.sort(reverse=True)

inserts = input("Enter the inserts with a space gap: ").split(" ")
inserts = [int(i) for i in inserts]
inserts.sort()

for i in inserts:
    if i > spaces[0]:
        print(f"{i} can not be inserted")
    else:
        print(f"{i} inserted at {spaces[0]}")
        spaces[0] = spaces[0] - i
        spaces.sort(reverse=True)