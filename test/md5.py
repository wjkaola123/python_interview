import hashlib

def calculate_md5(string):
    # 创建一个md5对象
    md5_hash = hashlib.md5()

    # 更新哈希对象以包含待计算哈希的字符串
    md5_hash.update(string.encode('utf-8'))

    # 计算哈希值并返回
    return md5_hash.hexdigest()

# 示例用法
string = "E3FB8*9Pg&rF@Vwa"
md5_value = calculate_md5(string)
print("MD5哈希值:", md5_value)