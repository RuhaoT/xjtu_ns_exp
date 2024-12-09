"""Encode string for telnet/ssh login."""
import base64

def base64_encode(data):
    """Encodes the given data to base64."""
    return base64.b64encode(data.encode()).decode()

if __name__ == "__main__":
    # wait for user input
    data = input("Enter the data to encode: ")
    print(base64_encode(data))
    # data
    # subject: 关于第一次实验
    # from:王树国<2203113234@oaurewouerw.com>
    # to:郑庆华<tianruhao@163.com>
    # Hello, 天冷了多吃点饺子注意保暖, thank you!
    # .