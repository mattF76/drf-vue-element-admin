import logging

# 创建一个日志记录器
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# 创建一个文件处理器，用于将日志写入文件
file_handler = logging.FileHandler("run.log")
file_handler.setLevel(logging.DEBUG)

# 创建一个控制台处理器，用于将日志输出到终端
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建一个格式化器，定义日志输出格式
file_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s"
)

console_formatter = logging.Formatter(
    "%(asctime)s - %(message)s"
)

# 将格式化器添加到处理器
file_handler.setFormatter(file_formatter)
console_handler.setFormatter(console_formatter)

# 将处理器添加到日志记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 示例日志输出
# logger.debug("This is a debug message.")
# logger.info("This is an info message.")
# logger.warning("This is a warning message.")
# logger.error("This is an error message.")