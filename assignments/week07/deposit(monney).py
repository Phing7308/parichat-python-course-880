def deposit(money):
    balance = 1000

    try:
        money = float(money)

        if money <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")

    except ValueError as e:
        print("เกิดข้อผิดพลาด:", e)

    else:
        balance = balance + money
        print("ยอดเงินคงเหลือ:", balance)

    finally:
        print("สิ้นสุดรายการฝากเงิน")


money = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
deposit(money)