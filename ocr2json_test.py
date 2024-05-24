import os

import pytesseract
from PIL import Image
import json
'''
1 读取文件夹 √
2 打开文件夹中的图片文件 √
3 对图片文件内容进行识别 √
4 键值对映射
'''
#1 读取文件夹
folder_path = 'E:/project_result/python_result/Example'  # 请替换为你的文件夹路径
file_list = []
file_path_list = []
json_list = []
json_total = {}
# 获取文件夹中的内容
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path):
        file_list.append(folder_path + '/' + str(item))

for i in range(len(file_list)):
    if i == 0 :
    #打开图片文件
        image = Image.open(file_list[i])
        # 使用Tesseract-OCR识别图片中的文字
        text = pytesseract.image_to_string(image, lang='chi_sim')
        trimmed_string = text.replace("\n", "")
        json_data = {'title' :trimmed_string }
    elif i == 1:
        image = Image.open(file_list[i])
        # 使用Tesseract-OCR识别图片中的文字
        text = pytesseract.image_to_string(image, lang='chi_sim')
        trimmed_string = text.replace("\n", "")
        json_data = {'unit' : trimmed_string }
    elif i == 2:
        image = Image.open(file_list[i])
        # 使用Tesseract-OCR识别图片中的文字
        text = pytesseract.image_to_string(image, lang='chi_sim')
        trimmed_string = text.replace("\n", "")
        json_data = {'header' : trimmed_string }
    elif i == 3:
        image = Image.open(file_list[i])
        # 使用Tesseract-OCR识别图片中的文字
        text = pytesseract.image_to_string(image, lang='chi_sim')
        trimmed_string = text.replace("\n", "")
        json_data = {'key_index' : trimmed_string}
    else:
        image = Image.open(file_list[i])
        # 使用Tesseract-OCR识别图片中的文字
        text = pytesseract.image_to_string(image, lang='chi_sim')
        trimmed_string = text.replace("\n", "")
        json_data = {'values' : trimmed_string}
    json_total.update(json_data)

print(json_total)


