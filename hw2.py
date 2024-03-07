# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def calculate_circle(radius):
    import math
    
    circumference = 2 * math.pi * radius
    
    area = math.pi * radius ** 2
    
    return circumference, area

radius_input = float(input("請輸入圓的半徑："))

circumference, area = calculate_circle(radius_input)

print(f"圓周長為：{circumference:.2f}")
print(f"圓面積為：{area:.2f}")


def collect_and_display_user_data():
    user_data = {} 
    
    user_data['姓名'] = input("請輸入您的姓名：")
    user_data['年齡'] = int(input("請輸入您的年齡："))
    user_data['身高'] = float(input("請輸入您的身高（米）："))
    user_data['喜愛的顏色'] = input("請輸入您喜愛的顏色：")
    
    summary = f"{user_data['姓名']}, {user_data['年齡']}歲, 身高{user_data['身高']:.2f}米, 喜愛的顏色是{user_data['喜愛的顏色']}。"
    
    print(summary)

collect_and_display_user_data()


def check_if_even():
    try:
        number = input("請輸入一個整數：")
        if not number.strip():
            raise ValueError("輸入不能為空。")
        number = int(number)
        
        if number % 2 == 0:
            print(f"{number} 是偶數。")
        else:
            print(f"{number} 不是偶數。")
    except ValueError:
        print("錯誤：請輸入一個有效的整數。")

check_if_even()


