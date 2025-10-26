#5. Write a program to accept an integer amount from user and tell minimum
#number of notes needed for representing that amount. (Use looping to optimize the problem)

amount = int(input("Enter the amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10]

note_count = {}

for note in notes:
    count = amount // note
    if(count > 0):
        note_count[note] = count
        amount -= note * count

print("\nMinimum number of notes needed:")
for note, count in note_count.items():
    print(f"₹{note} x {count}")
