import base64
import os

from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from werkzeug.datastructures import FileStorage
import loguru

# UPLOAD_FOLDER = config.get_required("UPLOAD_FOLDER")
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
logger = loguru.logger
# 确保日志文件保存在项目根目录下的log文件夹中，日志文件名以日期命名
logger.add("log/file_{time:YYYY-MM-DD}.log", rotation="1 day")

def encode_image(image_path):
    """将图片编码为Base64"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


class ImageAnalysis:
    def __init__(self,  model_name: str = "qvq-max", api_key="",
                 base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"):
        self.llm = ChatOpenAI(
            model=model_name,
            base_url=base_url,
            api_key=api_key,
            streaming=True,  # 图片识别一定要使用流失输入，否则会报错
        )
        self.parser = StrOutputParser()
        self.chain = self.llm | self.parser

    def analysis(self, images: list[FileStorage], upload_folder: str) -> str | None:
        logger.debug(f"images[0]: {images[0].filename}")

        # 检查并创建上传文件夹（新增逻辑）
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)  # 递归创建所有不存在的目录[1,8](@ref)
            logger.debug(f"Created upload folder: {upload_folder}")

        count_image = 0
        image_ai_msg = "以下是用户上传的的图片识别结果,结合图片和用户问题回答：\n"

        try:
            for image in images:
                count_image += 1
                image_path = os.path.join(upload_folder, image.filename)
                logger.debug(f"image_path: {image_path}")

                # 保存图片（确保文件夹存在后操作）
                image.save(image_path)

                # 调用模型识别图片（原逻辑保持不变）
                response = self.chain.invoke([HumanMessage(
                    content=[
                        {"type": "text", "text": "识别图片上的东西是什么,使用中文来回答"},
                        {
                            "type": "image",
                            "source_type": "base64",
                            "data": encode_image(image_path),
                            "mime_type": image.content_type,
                        },
                    ]
                )])
                image_ai_msg += f"图片{count_image}识别结果:{response}\n"

                # 删除临时图片
                os.remove(image_path)

            logger.debug(f"image_ai_msg: {image_ai_msg}")
            return image_ai_msg

        except Exception as e:
            logger.error(f"Image analysis failed: {str(e)}")
            return None
