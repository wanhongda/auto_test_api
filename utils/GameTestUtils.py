import time

from utils import SignarureUtils
from utils.ByteTracker import ByteTracker


# 初始化请求数据
# generate a request string for testing
# method_to_fill is a method you will keep some params in byte_tracker

# method_to_fill 是 main\login_test方法中的参数处理
def request_generate_register(msg_type: int, user_id=0, user_token="", method_to_fill=None) -> str:
    # first of all, build the utils part of the request
    original_tracker = ByteTracker("little")
    # msgType
    original_tracker.put_int(msg_type)
    # timestamp
    original_tracker.put_int(int(time.time()))
    # mac
    original_tracker.put_string("random_mac", 40)
    # platform
    original_tracker.put_int(1)
    # agent_id
    original_tracker.put_int(110000)
    # version
    original_tracker.put_string("1.05", 16)
    # user_id
    original_tracker.put_int(user_id)
    # user_token
    original_tracker.put_string(user_token, 32)
    # reverse
    original_tracker.put_int(0)

    if not (method_to_fill is None):
        method_to_fill(original_tracker)

    signature = SignarureUtils.signature_generate(original_tracker.message)

    # finally, take the signature
    request_tracker = ByteTracker("little")
    request_tracker.put_string(signature, 32)
    request_tracker.put(original_tracker.message)
    return request_tracker.print()

# generate a request string for testing
# method_to_fill is a method you will keep some params in byte_tracker

def request_generate(msg_type: int, user_id=0, user_token="", user_pwd="", method_to_fill=None) -> str:
    # first of all, build the utils part of the request
    original_tracker = ByteTracker("little")
    # msgType
    original_tracker.put_int(msg_type)
    # timestamp
    original_tracker.put_int(int(time.time()))
    # mac
    original_tracker.put_string("random_mac", 40)
    # platform
    original_tracker.put_int(1)
    # agent_id
    original_tracker.put_int(110000)
    # version
    original_tracker.put_string("1.05", 16)
    # user_id
    original_tracker.put_int(user_id)
    # user_token
    original_tracker.put_string(user_token, 32)
    # reverse
    original_tracker.put_int(0)

    if not (method_to_fill is None):
        method_to_fill(original_tracker, user_id, user_token, user_pwd)

    signature = SignarureUtils.signature_generate(original_tracker.message)

    # finally, take the signature
    request_tracker = ByteTracker("little")
    request_tracker.put_string(signature, 32)
    request_tracker.put(original_tracker.message)
    return request_tracker.print()

def request_generate_exists(msg_type: int, user_id=0, user_token="", user_pwd="", method_to_fill=None) -> str:
    # first of all, build the utils part of the request
    original_tracker = ByteTracker("little")
    # msgType
    original_tracker.put_int(msg_type)
    # timestamp
    original_tracker.put_int(int(time.time()))
    # mac
    original_tracker.put_string("random_mac", 40)
    # platform
    original_tracker.put_int(1)
    # agent_id
    original_tracker.put_int(110000)
    # version
    original_tracker.put_string("1.05", 16)
    # user_id
    original_tracker.put_int(user_id)
    # user_token
    original_tracker.put_string(user_token, 32)
    # reverse
    original_tracker.put_int(0)

    if not (method_to_fill is None):
        method_to_fill(original_tracker, user_id, user_token, user_pwd)

    signature = SignarureUtils.signature_generate(original_tracker.message)

    # finally, take the signature
    request_tracker = ByteTracker("little")
    request_tracker.put_string(signature, 32)
    request_tracker.put(original_tracker.message)
    return request_tracker.print()

# response_text 即res.text  method_to_get 是auth_response_get传入的三个参数 id token pwd
def parse_response(response_text: str, method_to_get=None) -> bool:
    response_tracker = ByteTracker("little")
    response_tracker.load(response_text)
    response_status = response_tracker.get_int()
    print("response_status", response_status)

    if response_status != 0:
        error_detail = response_tracker.get_string(128)
        # raise ValueError("server response error" + error_detail)
        print("error_detail", error_detail)
    if not (method_to_get is None):
        method_to_get(response_tracker)
    return True


# def parse_response(response_text: str, method_to_get=None):
#     response_tracker = ByteTracker("little")
#     response_tracker.load(response_text)
#     response_status = response_tracker.get_int()
#     print("response_status", response_status)
#
#     if response_status != 0:
#         error_detail = response_tracker.get_string(128)
#         raise ValueError("server response error" + error_detail)
#     if not (method_to_get is None):
#         print(method_to_get(response_tracker))
#         method_to_get(response_tracker)
#     return response_tracker


# 重写了一下，只接收数据进行加密解密，然后返回响应状态码
def parse_response_not_judge(response_text: str) -> int:
    response_tracker = ByteTracker("little")
    response_tracker.load(response_text)
    response_status = response_tracker.get_int()
    print("response_status", response_status)
    return response_status
    # if response_statuse:
    #     print("响应状态码为0，本次请求响应成功！")
    #     return response_status
