﻿# concurency

แอปคำนวณหาค่า fibonucci ด้วย process pool

โปรแกรมนี้ใช้ multiprocessing.Pool เพื่อคำนวณเลข Fibonacci สำหรับหลาย ๆ ตัวเลขพร้อมกัน โดย กระจายงานไปหลาย CPU Core ช่วยให้โปรแกรมรันได้เร็วขึ้นเมื่อทำงานที่ใช้ CPU หนัก

- ฟังก์ชัน fibonacci(n)
เป็นฟังก์ชันคำนวณลำดับ Fibonacci แบบ recursive จะทำงานหนักขึ้นหากค่า n ยิ่งเยอะ

- ฟังก์ชัน calculate_fibonacci_numbers(numbers)
1. ใช้ multiprocessing.Pool เพื่อรันฟังก์ชัน fibonacci() บน หลาย CPU Core
2. multiprocessing.cpu_count() → ใช้จำนวน CPU Core สูงสุด ที่เครื่องรองรับ
3. pool.map(fibonacci, numbers)
    กระจาย numbers ไปคำนวณ Fibonacci พร้อมกัน
    แต่ละค่าของ numbers จะถูกส่งไปให้ Process แยกกัน
