# เขียน function ชื่อ calculate_sphere(radius):

# คำนวณหา ปริมาตร ของทรงกลม

# volume = 4.0 / 3 * pi * radius ** 3

# จากนั้นแสดงผลลัพธ์ที่เหมาะสมออกทางหน้าจอ


def calculate_sphere(radius):
    """Calculates and displays sphere volume"""

    volume = 4.0 / 3 * 3.1416 * radius ** 3

    print(f"Sphere with radius {radius}")
    print(f"Volume = 4.0 / 3 * 3.1416 * ({radius}) ** 3) = {volume}")
    print()

calculate_sphere(5)