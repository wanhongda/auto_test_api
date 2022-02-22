# This is a sample Python script.

# Press the green button in the gutter to run the script.
import GameTestUtils
from ByteTracker import ByteTracker
import requests


def auth_register_test(tracker: ByteTracker):
    """
    认证接口：不存在账号的情况，该情况下，接口会注册账号，并将账号信息返回给用户
    这里user_id, user_token, account_id, access_token都不需要指定
    """
    # auth_method
    tracker.put_int(1)
    # spreader
    tracker.put_int(0)
    # account_id
    tracker.put_string("")
    # access_token
    tracker.put_string("")
    # device
    tracker.put_string("iphone 12", 32)
    # imei
    tracker.put_string("imei_test", 20)
    # mac
    tracker.put_string("mac_test", 40)
    # oaid
    tracker.put_string("oaid_test", 64)
    # android_id
    tracker.put_string("android_id_test", 64)
    # network_detail
    tracker.put_string("WIFI", 32)
    # loading_duration
    tracker.put_int(3)


# def auth_exists_test(tracker: ByteTracker):
#     """
#     认证接口：存在账号的情况，该情况下，接口会对密码进行校验，校验通过后，将账号信息返回给用户
#     这里user_id, access_token需要指定，access_token传入注册情况下pwd字段
#     """
#     # auth_method
#     tracker.put_int(1)
#     # spreader
#     tracker.put_int(0)
#     # account_id
#     tracker.put_string("")
#     # access_token
#     tracker.put_string("Y[CVtUg&Td")
#     # device
#     tracker.put_string("iphone 12", 32)
#     # imei
#     tracker.put_string("imei_test", 20)
#     # mac
#     tracker.put_string("mac_test", 40)
#     # oaid
#     tracker.put_string("oaid_test", 64)
#     # android_id
#     tracker.put_string("android_id_test", 64)
#     # network_detail
#     tracker.put_string("WIFI", 32)
#     # loading_duration
#     tracker.put_int(3)
#
# def auth_exists_test(tracker: ByteTracker, user_id,user_pwd):
#     """
#     认证接口：存在账号的情况，该情况下，接口会对密码进行校验，校验通过后，将账号信息返回给用户
#     这里user_id, access_token需要指定，access_token传入注册情况下pwd字段
#     """
#     # auth_method
#     tracker.put_int(1)
#     # spreader
#     tracker.put_int(0)
#     # account_id
#     tracker.put_int(user_id)
#     # access_token 传入的是注册之后返回的pwd
#     tracker.put_string(user_pwd)
#     # device
#     tracker.put_string("iphone 12", 32)
#     # imei
#     tracker.put_string("imei_test", 20)
#     # mac
#     tracker.put_string("mac_test", 40)
#     # oaid
#     tracker.put_string("oaid_test", 64)
#     # android_id
#     tracker.put_string("android_id_test", 64)
#     # network_detail
#     tracker.put_string("WIFI", 32)
#     # loading_duration
#     tracker.put_int(3)
def auth_exists_test(tracker: ByteTracker, user_id, user_token, user_pwd):
    """
    认证接口：存在账号的情况，该情况下，接口会对密码进行校验，校验通过后，将账号信息返回给用户
    这里user_id, access_token需要指定，access_token传入注册情况下pwd字段
    """
    """
    这里只指定pwd，因为这里的user_id是facebook的id，不需要指定
    """
    # auth_method
    tracker.put_int(1)
    # spreader
    tracker.put_int(0)
    # account_id 是facebook账号id  不需要传进来 只检验密码就行了
    tracker.put_string("")
    # access_pwd
    tracker.put_string(user_pwd)
    # device
    tracker.put_string("iphone 12", 32)
    # imei
    tracker.put_string("imei_test", 20)
    # mac
    tracker.put_string("mac_test", 40)
    # oaid
    tracker.put_string("oaid_test", 64)
    # android_id
    tracker.put_string("android_id_test", 64)
    # network_detail
    tracker.put_string("WIFI", 32)
    # loading_duration
    tracker.put_int(3)


def auth_response_get(tracker: ByteTracker):
    """
    认证接口响应结果，user_id, user_token用于登录接口使用，user_pwd在注册的情况下会返回密码，认证存在账号的情况access_token需要传入该字段的值，
    建议测试认证注册情况时，保存一批user_id和user_pwd, 方便后续的存在账号的情况测试
    """
    user_id = tracker.get_int()
    user_token = tracker.get_string(32)
    user_pwd = tracker.get_string(32)
    register_flag = tracker.get_int()
    auth_method = tracker.get_int()
    print(f"response=> id:{user_id}, token:{user_token}, pwd:{user_pwd}")


def login_test(tracker: ByteTracker, user_id, user_token):
    """
    登录接口：，user_id, user_token需要指定
    """
    # account_id
    tracker.put_string(user_id)
    # access_token
    tracker.put_string(user_token)
    # network_detail
    tracker.put_string("WIFI", 32)
    # loading_duration
    tracker.put_int(3)
    # device_type
    tracker.put_string("iphone 12", 32)


if __name__ == '__main__':
    # 认证接口注册test
    # print(GameTestUtils.request_generate(0x1001, 0, "", auth_register_test))
    #
    # register_body = GameTestUtils.request_generate(0x1001, 0, "", auth_register_test)
    # body = 'v=' + register_body
    url = "https://itest.tongitsstar.com/data/handleMsg.do"
    # res = requests.get(url=url, params=body, verify=False)
    # GameTestUtils.parse_response(res.text, auth_response_get)

    #
    # 认证接口账号存在test
    # user_id字段和access_token字段需要有值
    # print(GameTestUtils.request_generate(0x1001, 35482, "", auth_exists_test))

    # 登录接口test
    login_body = "YmM1YWVjM2Y0YjMyN2U5MzEyZDY5ZTdjZDYxZDUyZWMEEAAAM1KWYXJhbmRvbV9tYWMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAsK0BADEuMDUAAAAAAAAAAAAAAACVLgIAZDczYjU0ZjVmZDRkYjI1ZAAAAAAAAAAAAAAAAAAAAAAAAAAAV0lGSQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAaXBob25lIDEyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
    # 这段没有打印，GameTestUtils.request_generate仅仅是对请求参数进行初始化操作，并没有响应的数据
    print("注册结果", GameTestUtils.request_generate(0x1004, 19782146, "17c58553c89b5355", login_test))
    body = 'v=' + login_body

    res = requests.get(url=url, params=body, verify=False)
    print("------res.text------:", res.text)
    res_text = "AAAAAEdfMTQyOTk3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAADEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALCtAQDHUZZhYAAAAAAAAAAAAAAAQEIPAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtFKWYQAAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAAAA"
    c = GameTestUtils.parse_response(res_text, auth_response_get)
    print("c", c)
    # response test
    # 认证结果
    # response_text = "AAAAAJqKAAA1YTFjMzE5MTlkYzJkM2IyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAA="
    # GameTestUtils.parse_response(response_text, auth_response_get)
