s=input('請輸入字符串')
# str > bytes
s1=s.encode()
print ('對應的字節串是：',s1)
# # 請輸入字符串你好
# 對應的字節串是： b'\xe4\xbd\xa0\xe5\xa5\xbd'
# 所有的字符串都可以转换成字节串，并不是所有字节串都能转换成字符串

print('对应的字符串:',s1.decode())