from pdf2image import convert_from_path
import os


def pdf_to_jpg(pdf_path, output_folder):
    # 使用pdf2image将PDF转换为图像列表
    images = convert_from_path(pdf_path)

    # 遍历图像列表并保存为JPG格式
    for i, image in enumerate(images):
        output_path = os.path.join(output_folder, f"page_{i}.jpg")
        image.save(output_path, "JPEG")
        print(f"Saved {output_path}")

    # 使用函数
pdf_path = "F:/job_exam/ocr_streamlit/盛剑环境.pdf"  # 请替换为您的PDF文件路径
output_folder = "F:/job_exam/ocr_streamlit/pdf2jpg/"  # 输出文件夹，这里设置为当前文件夹
pdf_to_jpg(pdf_path, output_folder)