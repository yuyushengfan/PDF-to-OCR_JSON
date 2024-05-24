import json
from paddleocr import PaddleOCR
'''
ocr = PaddleOCR(lang="ch")  # 使用中文识别
result = ocr.ocr("F:\job_exam\ocr_streamlit")

for line in result:
   print(line)  # 输出识别结果
'''
# 初始化OCR模型
ocr = PaddleOCR(lang="ch")

# 定义图片路径列表
image_paths = [
    "F:\job_exam\ocr_streamlit\pdf2jpg\page_6.jpg"
]

cleaned_ocr_results = []

# 对每张图片进行OCR处理
for image_path in image_paths:
    result = ocr.ocr(image_path)
    print(result)