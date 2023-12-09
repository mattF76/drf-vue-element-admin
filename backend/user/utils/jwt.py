import jwt
import datetime

from utils.log import logger
from django.conf import settings

# 定义秘钥，用于签名和验证JWT
SECRET_KEY = 'your-secret-key'
EXPIRE_MINUTES = settings.JWT['EXPIRE_MINUTES']

class UserInfo:
    # 初始化方法（构造函数）
    def __init__(self, id, username):
        # 实例变量
        self.id = id
        self.username = username

    def __str__(self):
        return f"用户：{self.id}, {self.username}"

def generate_token(user: UserInfo) -> str:
    """生成用户对应token
    @param user: 输入一个用户对象
    @return: 返回字符串格式token
    """
    # 定义JWT的payload（负载）
    payload = {
        'id': user.id,
        'username': user.username,
        'exp': datetime.datetime.now() + datetime.timedelta(minutes=EXPIRE_MINUTES)  # 设置过期时间
    }

    # 生成JWT
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    logger.debug(f'Generated JWT: {token}')

    return token

def is_token_valid(token: str) -> bool:
    """
    验证JWT token是否有效
    @param token: JWT token
    @return: 如果token有效，则返回True；否则返回False
    """
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

def is_token_expired(token: str) -> bool:
    """
    检测JWT token是否过期
    @param token: JWT token
    @return: 如果token已过期，则返回True；否则返回False
    """
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return False
    except jwt.ExpiredSignatureError:
        return True

def parse_token(token: str) -> UserInfo:
    """
    解析token，验证是否有效，返回用户对象
    @param token:
    """
    # 验证token是否有效
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        # print("Token is valid.")
        return UserInfo(decoded_token["id"], decoded_token["username"])
    except jwt.ExpiredSignatureError:
        logger.debug("Token is expired.")
    except jwt.InvalidTokenError:
        logger.debug("Token is invalid.")

    return UserInfo(id=None, username=None)


def update_token_expiration(token: str) -> str:
    """
    更新JWT token的过期时间
    @param token: JWT token
    @return: 更新后的JWT token
    """
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    # 更新过期时间
    decoded_token["exp"] = datetime.datetime.now() + datetime.timedelta(minutes=EXPIRE_MINUTES)  # 设置过期时间

    # 重新生成token
    updated_token = jwt.encode(decoded_token, SECRET_KEY, algorithm="HS256")

    return updated_token



