## XScanner
Full Network Scanner Project (Worker)

# 全网web扫描系统

该项目主要为全网扫描web服务建立。收集网络信息。

# 环境

python2.7

redis

elasticsearch


# 安装

pip install -r requirements.txt

下载并启动ielasticsearch

下载并启动redis


# 运行任务

首先启动redis、elasticsearch

windows系统

startWork.bat  			多任务

startWork_single.bat   单任务

linux系统

startWork.sh  			多任务

startWork_single.sh   单任务

# 导入任务

单目标导入 python run.py target(不加http)

通过文件中导入 编辑将目标存入list.txt中，然后运行 python run_file.py

# TODO:

  子域名爆破

  端口扫描

  导出目标或者提供api接口，输出列表给扫描器，让扫描器去扫描
  
  cms识别和IP地理位置的识别

Author : BaCde[Glacier@insight-labs.org]

