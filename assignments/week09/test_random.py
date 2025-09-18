import random
 
# สุ่มเลขระหว่าง 0 - 9
test_random = random.randint(0, 9)
 
print("-- เกมทายตัวเลข มาเดาใจคอมพิวเตอร์กันเถอะ --")
 
# รับค่าการทายเลขจากผู้ใช้
guess_number = int(input("What is your guess num"))
 
# condition ==> if-elif-else
if test_random == guess_number:
    print("ยูเก่งมาก มั่วถูกตั้งแต่ครั้งแรกเลย เทพจริมๆ")
 
elif guess_number < test_random:
    print("ผิดจ้า น้อยไปเนอะ")
 
elif guess_number > test_random:
    print("ผิดจ้า มากไปหน่อย")