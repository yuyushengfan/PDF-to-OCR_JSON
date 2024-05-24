import os

import pytesseract
from PIL import Image
import json
'''
1 读取文件夹 √
2 打开文件夹中的图片文件 √
3 对图片文件内容进行识别 √
4 键值对映射 √
'''
'''
new:
1 读取一级文件夹 -> 获得二级文件夹
2 读取二级文件夹 -> 获得图片
'''
#1 读取文件夹
#folder_path_first = 'E:\project_data\ocR-data\snipe'  # 请替换为你的文件夹路径
folder_list = []
file_list = []
file_path_list = []
json_list = []
json_total = {}
# 指定一级文件夹路径
base_path = r"F:\job_exam\ocr_streamlit\all_table"

# 遍历一级文件夹中的所有文件和文件夹
for entry in os.scandir(base_path):
    if entry.is_dir():  # 检查是否为文件夹
        secondary_folder_path = entry.path
        # print(f"二级文件夹: {secondary_folder_path}")
        i = -1
        # 遍历二级文件夹中的文件
        for file_name in os.listdir(secondary_folder_path):
            file_path = os.path.join(secondary_folder_path, file_name)
            i+=1
            if i == 0:
                image = Image.open(file_path)
                # 使用Tesseract-OCR识别图片中的文字
                text = pytesseract.image_to_string(image, lang='eng+chi_sim')
                trimmed_string = text.replace("\n", "")  #去除换行符
                json_data = {'title': trimmed_string}
            elif i == 1:
                image = Image.open(file_path)
                # 使用Tesseract-OCR识别图片中的文字
                text = pytesseract.image_to_string(image, lang='eng+chi_sim')
                trimmed_string = text.replace("\n", "")
                json_data = {'unit': trimmed_string}
            elif i == 2:
                image = Image.open(file_path)
                # 使用Tesseract-OCR识别图片中的文字
                text = pytesseract.image_to_string(image, lang='eng+chi_sim')
                trimmed_string = text.replace("\n", "")
                json_data = {'header': trimmed_string}
            elif i == 3:
                image = Image.open(file_path)
                # 使用Tesseract-OCR识别图片中的文字
                text = pytesseract.image_to_string(image, lang='eng+chi_sim')
                trimmed_string = text.replace("\n", "")
                json_data = {'key_index': trimmed_string}
            else:
                image = Image.open(file_path)
                # 使用Tesseract-OCR识别图片中的文字
                text = pytesseract.image_to_string(image, lang='chi_sim')
                trimmed_string = text.replace("\n", "")
                json_data = {'values': trimmed_string}
            json_total.update(json_data)
        print(json_total)

