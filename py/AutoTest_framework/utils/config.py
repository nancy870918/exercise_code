"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import os
from file_reader import YamlReader

#通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改
#之前直接拼接的路径，修改了一下，用现在这种方法，可支持linux和windows等不同的平台，也建议大家多用os.path.split()和os.path.join()，不要直接+‘\\xxx\\ss’这样
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# a = os.path.abspath(__file__)  #返回当前文件绝对路径
# print(a)
# b = os.path.dirname(os.path.abspath(__file__)) #返回文件路径
# print(b)
# c = os.path.split(os.path.dirname(os.path.abspath(__file__))) #把路径分割成dirname和basename，返回一个元组
# print(c)
# d = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  #获取元组里的第一个元素
# print(d)
CONFIG_FILE = os.path.join(BASE_PATH,'config','config.yaml') #把目录和文件名合成一个路径读取config.yaml路径
DATA_PATH = os.path.join(BASE_PATH,'data') #读取data路径
DRIVER_PATH = os.path.join(BASE_PATH,'drivers') #读取drivers路径
LOG_PATH = os.path.join(BASE_PATH,'log') #读取log路径
REPORT_PATH = os.path.join(BASE_PATH,'report') #读取report路径
class Config:
    def __init__(self,config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self,element,index=0):
        """
         yaml是可以通过‘---’分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取
         这样我们其实可以把框架相关的配置放到默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目测试。
        """
        return  self.config[index].get(element)

if __name__ == '__main__':
        c = Config()
        print(c.get('URL'))