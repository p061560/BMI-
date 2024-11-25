import csv
import os
import time
import openai  # 引入 openai 套件
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 設定 Matplotlib 的中文字體，避免亂碼
rcParams['font.sans-serif'] = ['Microsoft JhengHei']
rcParams['axes.unicode_minus'] = False

# 設定 OpenAI API 金鑰
openai.api_key = 'YOUR_API_KEY'  # 請將 'YOUR_API_KEY' 替換為你的實際 API 金鑰

# CSV 文件路徑
FILE_PATH = "bmi_records.csv"

# 初始化 CSV 文件（如果不存在）
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["日期時間", "身高 (cm)", "體重 (kg)", "BMI", "分類"])

def save_record(height, weight, bmi, category):
    """將 BMI 計算結果儲存到 CSV 文件"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([now, height, weight, bmi, category])
    print("結果已成功儲存至本地檔案！")

def plot_records():
    """讀取 CSV 文件並繪製圖表"""
    if not os.path.exists(FILE_PATH):
        print("沒有可用的資料來繪製圖表！")
        return

    dates, heights, weights, bmis = [], [], [], []

    with open(FILE_PATH, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dates.append(row["日期時間"])
            heights.append(float(row["身高 (cm)"]))
            weights.append(float(row["體重 (kg)"]))
            bmis.append(float(row["BMI"]))

    # 繪製圖表
    plt.figure(figsize=(10, 6))
    
    plt.plot(dates, heights, label="身高 (cm)", marker="o")
    plt.plot(dates, weights, label="體重 (kg)", marker="o")
    plt.plot(dates, bmis, label="BMI", marker="o")
    
    plt.xlabel("日期時間")
    plt.ylabel("數值")
    plt.title("身高、體重與 BMI 變化圖")
    plt.xticks(rotation=45, fontsize=8)
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def clear_records():
    """清除歷史記錄"""
    confirm = input("確定要清除所有歷史記錄嗎？(Y/N): ").upper().strip()
    if confirm == "Y":
        with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["日期時間", "身高 (cm)", "體重 (kg)", "BMI", "分類"])
        print("歷史記錄已清除！")
    else:
        print("取消清除操作。")

def get_advice(bmi, category):
    """向 ChatGPT 請求建議"""
    prompt = f"我的 BMI 是 {bmi:.2f}，屬於「{category}」。請給我一些健康建議。"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "你是一個健康顧問，給出關於體重管理的建議，限100字以內。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            n=1,
            temperature=0.7,
        )
        advice = response['choices'][0]['message']['content']
        print("\n=== ChatGPT 的建議 ===")
        print(advice)
    except Exception as e:
        print(f"無法獲取建議：{e}")

# BMI 計算邏輯
while True:
    print("\n=== BMI 計算系統 ===")
    print("1. 計算 BMI 並儲存記錄")
    print("2. 查看 BMI 圖表")
    print("3. 清除所有歷史記錄")
    print("4. 離開系統")
    choice = input("請選擇功能 (1/2/3/4): ").strip()

    if choice == "1":
        try:
            height = float(input("身高 (cm): "))
            weight = float(input("體重 (kg): "))
        except ValueError:
            print("輸入無效，請輸入有效的數字！")
            continue

        if height > 0 and weight > 0:
            if height <= 2:  # 身高以公尺為單位，轉換為公分
                height *= 100
            bmi = float(weight / ((height / 100) ** 2))
            print(f"BMI 為 {bmi:.2f}")

            # BMI 分類
            if bmi < 18.5:
                category = "體重過輕"
            elif 18.5 <= bmi < 24:
                category = "體重正常"
            elif 24 <= bmi < 27:
                category = "體重過重"
            elif 27 <= bmi < 30:
                category = "輕度肥胖"
            elif 30 <= bmi < 35:
                category = "中度肥胖"
            else:
                category = "重度肥胖"
            print(f"BMI 分類: {category}")

            # 儲存記錄
            save_record(height, weight, bmi, category)

            # 詢問是否需要建議
            need_advice = input("是否需要 ChatGPT 給予健康建議？(Y/N): ").upper().strip()
            if need_advice == "Y":
                get_advice(bmi, category)

            # 等待 3 秒後繼續
            print("等待 3 秒...")
            time.sleep(3)
        else:
            print("輸入的身高或體重無效，請重新輸入！")

    elif choice == "2":
        plot_records()

    elif choice == "3":
        clear_records()

    elif choice == "4":
        print("感謝使用，系統中止")
        break

    else:
        print("無效的選擇，請重新輸入！")
