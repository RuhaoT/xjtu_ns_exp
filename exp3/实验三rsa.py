# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:32:34 2019

@author: 90415
"""

#%%

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)
 
# master的秘钥对的生成
private_pem = rsa.exportKey()
 
with open('master-private.pem', 'wb') as f:
  f.write(private_pem)
 
public_pem = rsa.publickey().exportKey()
with open('master-public.pem', 'wb') as f:
  f.write(public_pem)


#%%
import base64
message = b"hello, this is a plian text"
with open('master-public.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(message))
    print ('加密后:',cipher_text)



with open('master-private.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(cipher_text), random_generator)
    print ('解密的原文:',text)


#%%
n = b'This is a test message from Ruhao Tian' # 将要签名的内容字符串转换为二进制表示
h = SHA.new() # 建立新的SHA1哈希对象
h.update(n) # 使用SHA1加密算法对要签名的内容字符串生成信息摘要
print('Hash:',h.hexdigest(),'length:',len(h.hexdigest())*4) # 使用hexdigest()方法获取摘要的16进制表示并输出

sign_txt = 'sign.txt' # 签名文件名

with open('master-private.pem') as f: # 打开私钥文件
    key = f.read() # 读取私钥
    private_key = RSA.importKey(key) # 将私钥转换为RSA密钥对象
    hash_obj = SHA.new(n) # 从签名字符串生成信息摘要
    signer = Signature_pkcs1_v1_5.new(private_key) # 使用PKCS1填充算法和私钥创建数字签名对象
    d = base64.b64encode(signer.sign(hash_obj)) # 对信息摘要进行数字签名并导出为base64编码

f = open(sign_txt,'wb') # 保存导出的base64签名到文件
f.write(d) 
f.close()

# 目标：使验签结果为否定
# 随机建立一个新的RSA密钥对
# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)
public_pem = rsa.publickey().exportKey() # 导出公钥

with open('master-public.pem') as f: # 打开公钥文件
    # key = f.read()
    key = public_pem # 用随机公钥替代原有公钥
    public_key = RSA.importKey(key) # 将公钥转换为RSA密钥对象
    sign_file = open(sign_txt,'r') # 读取签名文件
    sign = base64.b64decode(sign_file.read()) # 将读取的base64签名编码转换为二进制位串
    h = SHA.new(n) # 生成内容的SHA1算法信息摘要
    verifier = Signature_pkcs1_v1_5.new(public_key) # 使用公钥创建数字签名对象
    print('result:', verifier.verify(h,sign)) # 验证对内容的签名是否和公钥签名结果一致









# %%
