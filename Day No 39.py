# ---------------------- Day 39 -------------------
#                  Ramadan 12

# Kon banaga Karoru Pati

question1 = [
    "Who is invented python",
    "Guido van Rossum",
    "shahbaz",
    "Newton",
    "Mask Zaker bag",
    "None",
    1,
]
question1 = [
    "Who is invented python",
    "Guido van Rossum",
    "shahbaz",
    "Newton",
    "Mask Zaker bag",
    "None",
    1,
]
question1 = [
    "Who is invented python",
    "Guido van Rossum",
    "shahbaz",
    "Newton",
    "Mask Zaker bag",
    "None",
    1,
]
question1 = [
    "Who is invented python",
    "Guido van Rossum",
    "shahbaz",
    "Newton",
    "Mask Zaker bag",
    "None",
    1,
]
question1 = [
    "Who is invented python",
    "Guido van Rossum",
    "shahbaz",
    "Newton",
    "Mask Zaker bag",
    "None",
    1,
]
question1 = [
    "Who is invented python",
    "Guido van Rossum",
    "shahbaz",
    "Newton",
    "Mask Zaker bag",
    "None",
    1,
]
question1 = [
    "Who is invented python",
    "Guido van Rossum",
    "shahbaz",
    "Newton",
    "Mask Zaker bag",
    "None",
    1,
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 16000, 20000, 32000]
money = 0

for i in range(0, len(question1)):
    question = question1[i]
    print(f"Question for rupees ", levels[i])
    print(f"a.{question1[1]} b.{question1[2]}  ")
    print(f"c.{question1[3]} d.{question1[4]}  ")
    print(f"e.{question1[5]}")
    reply = int(input("Enter Your Answer(1-5):"))
    if reply == question[1]:
        print(f"Correct Answer,You have win Rs.{levels[i]}")
        if i == 4:
            money == 5000
        elif i == 7:
            money == 32000

    else:
     print("Wrong No")
     break
