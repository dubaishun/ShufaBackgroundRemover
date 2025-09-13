from PIL import Image, ImageOps
import os

# 添加边框到单个图片
def add_border(image_path):
    try:
        img = Image.open(image_path)

        # 添加多层边框，分别为不同颜色和宽度
        img = ImageOps.expand(img, border=2, fill="#ecede8")   # 第一层
        img = ImageOps.expand(img, border=1, fill="#0b0c07")   # 第二层
        img = ImageOps.expand(img, border=1, fill="#575757")   # 第三层
        img = ImageOps.expand(img, border=1, fill="#fefefe")   # 第四层
        img = ImageOps.expand(img, border=30, fill="#eaeaea")  # 第五层

        # 输出路径处理
        base_name, ext = os.path.splitext(os.path.basename(image_path))
        output_path = os.path.join(os.path.dirname(image_path), f"{base_name}_已加框{ext}")
        
        img.save(output_path)
        return f"带电子装裱边框图片：{output_path}"
    except Exception as e:
        return f"处理图像时出错 {image_path}: {e}"

# 处理目录中的所有图片文件
def process_images_in_directory():
    pic_directory = "pic"  # 默认目录
    image_formats = (".jpg", ".png", ".webp", ".bmp")
    messages = []

    for filename in os.listdir(pic_directory):
        file_path = os.path.join(pic_directory, filename)

        if file_path.lower().endswith(image_formats):
            result = add_border(file_path)
            messages.append(result)

    return messages
