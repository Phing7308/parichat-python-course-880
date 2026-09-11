"""
สร้างไฟล์ใหม่ใน FOLDER /assignments/
week09/lab-assignment-1109.py

เครื่องคำนวณค่าไฟฟ้าแบบขั้นบันได
เขียนโปรแกรมคำนวณค่าไฟฟ้าจากจำนวนหน่วยไฟฟ้า
ที่ใช้ในเดือนนั้น โดยใช้ฟังก์ชัน
calculate_electricity_cost(units)

ค่าไฟฟ้าขึ้นกับปริมาณการใช้งาน
จำนวนหน่วยที่ใช้       อัตราต่อหน่วย
1-50 หน่วยแรก          2.50 บาท
51-100 หน่วย           3.00 บาท
101-200 หน่วย          3.50 บาท
มากกว่า 200 หน่วย      4.00 บาท

ให้คิดค่าบริการคงที่เพิ่มอีก 25 
บาทต่อเดือน
เงื่อนไข
   • โปรแกรมแสดงเมนูวนซ้ำ
   • ผู้ใช้เลือก 1 เพื่อคำนวณค่าไฟ
   • ผู้ใช้เลือก 2 เพื่อออกจากโปรแกรม
   • หากเลือกเมนูอื่น 
   ให้แจ้งว่าเลือกเมนูไม่ถูกต้อง
   • จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ
   • ให้แสดงรายละเอียดค่าไฟแต่ละช่วง 
   และยอดรวมสุทธิ

ตัวอย่างหน้าจอ
===== โปรแกรมคำนวณค่าไฟฟ้า =====
1. คำนวณค่าไฟ
2. ออกจากโปรแกรม
เลือกเมนู: 1

กรอกจำนวนหน่วยไฟฟ้า: 120

รายละเอียดค่าไฟ:
1-50 หน่วย: 125.00 บาท
51-100 หน่วย: 150.00 บาท
101-120 หน่วย: 70.00 บาท
ค่าบริการ: 25.00 บาท
รวมค่าไฟทั้งสิ้น: 370.00 บาท
"""

def calculate_electricity_cost(units):
   if units > 200:
       cost = (2.50 * 50) + (3.00 * 50) + (3.50 * 100) + (4.00 * (units - 200)) + 25
       print(units, "units =", cost, "THB")
   elif units > 100:
       cost = (2.50 * 50) + (3.00 * 50) + (3.50 * (units - 100)) + 25
       print(units, "units =", cost, "THB")
   elif units > 50:
       cost = (2.50 * 50) + (3.00 * (units - 50)) + 25
       print(units, "units =", cost, "THB")
   elif units > 0:
       cost = (2.50 * units) + 25
       print(units, "units =", cost, "THB")
   else:
       print("Electricity units cannot be negative.")

while True:
   print("\n===== Electricity Cost Calculator =====")
   print("1. Calculate electricity cost")
   print("2. Exit")
   choice = input("Select menu: ")
   if choice == "1":
       units = int(input("Enter electricity units: "))
       calculate_electricity_cost(units)
   elif choice == "2":
       print("Exit program.")
       break
   else:
       print("Invalid menu selection.")