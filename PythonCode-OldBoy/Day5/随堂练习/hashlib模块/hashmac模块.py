# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 必须encoding成utf-8格式
# 散列消息鉴别码，简称HMAC，是一种基于消息鉴别码MAC（Message Authentication Code）的鉴别机制。
# 使用HMAC时,消息通讯的双方，通过验证消息中加入的鉴别密钥K来鉴别消息的真伪；一般用于网络通信中消息加密，
# 前提是双方先要约定好key,就像接头暗号一样，然后消息发送把用key把消息加密，
# 接收方用key ＋ 消息明文再加密，拿加密后的值 跟 发送者的相对比是否相等，这样就能验证消息的真实性，及发送者的合法性了
import hmac
h = hmac.new(b'12345', '宝塔镇河妖'.encode(encoding="utf-8"))
print(h.hexdigest())