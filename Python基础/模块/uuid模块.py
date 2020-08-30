#uuid用来生成一个全局唯一的id
import uuid

print(uuid.uuid1()) #32个长度，每一个字符有16个选择 16**32

print(uuid.uuid3(uuid.NAMESPACE_DNS,'zhangsan')) #生成的固定uuid
print(uuid.uuid5(uuid.NAMESPACE_DNS,'zhangsan')) #生成的固定uuid

print(uuid.uuid4()) #使用的最多