# coding: utf-8 
__author__ = '財'
__time__ = '2018/11/1 0:39'

import os


class ToRef():
    def __init__(self):
        self.file = None
        self.iter = None
        self.namespaces = None
        pass

    def get_file(self):
        """

        Returns:

        """
        # 获取文件路径

    def check_params(self, filepath):
        """

        Args:
            filepath:

        Returns:

        """
        # 判断是否是文件
        if not os.path.isfile(filepath):
            pass
            return
        else:
            # 把文件路径赋予变量
            self.file = filepath
        # 判断空间名是否为空
        # 如果为空
        # 警告用户，不能为空，不能用默认空间名
        # 返回函数
        # 如果不
        # 获取空间名信息
        # 获取次数，默认为1

    # 返回连接按钮函数

    def connect_to_ref(self):
        return self.ref()

    def ref(self):
        while self.iter:
            mc.file(self.file, r=True, ignoreVersion=True, gl=True, mergeNamespacesOnClash=False,
                    namespace=self.namespaces, options="mo=1")
            self.iter -= 1
