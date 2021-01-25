## Auto Connect
这是一个神奇的python脚本，可以维持你的设备与SZU网络的连接(仅限办公区域)

## 用法

### 配置 conf.conf 文件
* `user`: "你的账号" (保留引号)
* `pwd`:  "你的密码" (保留引号)
* `retry: connected`: 连接成功后下次尝试间隔，单位：分钟，默认: 10
* `retry: disconnected`: 连接失败后下次尝试间隔，单位：分钟，默认: 5

### 运行
* python >= 2.7
* SZU内网环境
* 正确的账号密码(填入conf.conf)和未欠费的套餐

执行命令
```
python main.py
```

### 测试
* 手动断开网络连接
* 运行脚本
* 查看对应log，预期出现以下类似信息
```
2021-01-25 20:51:21,988 - WARNING - Disconnected
2021-01-25 20:51:25,502 - WARNING - Connection repaired
```
* 如果有任何问题，请留下你的issue

### 保持脚本常驻
* 设置BIOS来电自启动
* Windows 设置计划任务
* Linux & Mac 设置脚本自启动


## 申明
* 禁止用此脚本干扰他人正常上网
* 本脚本使用构造POST表单完成上网请求，完全安全可信
* 本脚本导致上网账号被封禁概不负责
* conf.conf 明文密码可能导致您的账号密码泄露