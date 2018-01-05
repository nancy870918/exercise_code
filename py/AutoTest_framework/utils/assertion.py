"""
在这里添加各种自定义的断言，断言失败抛出AssertionError就ok
"""

def assertHTTPCode(response,code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError('响应code不再列表中！') #抛出AssertionFrror,unittest会自动判断为用例Failure，而不是Error