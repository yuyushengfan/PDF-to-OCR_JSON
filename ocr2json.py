import pytesseract
from PIL import Image
import json
# 打开图片文件
image = Image.open('F:\job_exam\ocr_streamlit\pdf2jpg\page_6.jpg')
# 使用Tesseract-OCR识别图片中的文字
text = pytesseract.image_to_string(image, lang='eng+chi_sim')
trimmed_string = text.replace("\n", "")
# 将文字转化为JSON格式
data = {"text": trimmed_string}
json_data = json.dumps(data, ensure_ascii=False)
print(json_data)


