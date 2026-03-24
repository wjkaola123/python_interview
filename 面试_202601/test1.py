import time

# 错误示例：继承 BaseException
class CriticalError(BaseException):
    pass

def bad_example():
    try:
        while True:
            print("运行中...")
            time.sleep(10)
            raise CriticalError("严重错误")
    except CriticalError as e:
        print("捕获错误：", e)
        # 这会捕获所有 BaseException，包括 KeyboardInterrupt
        print("捕获错误，继续运行")


bad_example()