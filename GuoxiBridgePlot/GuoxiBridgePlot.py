# -*- coding: utf-8 -*-
"""
莆田市过溪桥用于作图的各个模块
"""
import matplotlib.pyplot as plt  # 使用import导入模块matplotlib.pyplot，并简写成plt
import numpy as np  # 使用import导入模块numpy，并简写成np
class GuoxiBridge(object):
    """
       莆田市绶溪公园过溪桥用于作图的各个模块
    """
    def __init__(self):
        self.MarkerList = ['o','s','p','x','v','h']    #默认的MarkerList

    def _PlotChart(self,plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList):
        """
           绘制图形功能代码
        """

        plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
        plt.figure()  # 使用plt.figure定义一个图像窗口.

        for i in range(0,len(yList)):
            plt.plot(x, yList[i],marker=self.MarkerList[i])

        plt.legend(legendList)
        plt.xticks(x, xticksLabelList)    #自定义标签
        plt.xlabel(xlabelText)
        plt.ylabel(ylabelText)
        #plt.title(title) # 设置标题
        plt.show()

    def PlotDeckElevationTimeHistory(self):
        """
           绘制桥面标高时程曲线
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

        legendList = ['LZ1','LZ2','LZ3','LZ4','LZ5','LY1','LY2','LY3','LY4','LY5']
        markerListLoop = ['o','s','p','x','v','h']    #线条超过6条，则marker重复利用
        #markerList=['o','s','p','x','v','h','o','s','p','x','v','h']
        xticksLabelList = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        
        xList = []
        markerList = []
        for i in range(0,len(xticksLabelList)):
            xList.append(i + 1)
        for i in range(0,len(legendList)):
            markerList.append(markerListLoop[i % len(markerListLoop)])    #整数+余数

        x = np.array(xList)
        yList = [np.array([8.92,8.921,8.92,8.925,8.928,8.93,8.931,8.929,8.929,8.928,8.929,8.938])
            ,np.array([9.703,9.7,9.703,9.691,9.678,9.678,9.687,9.673,9.678,9.691,9.698,9.697])
            ,np.array([9.822,9.821,9.822,9.813,9.807,9.805,9.81,9.798,9.807,9.823,9.834,9.83])
            ,np.array([9.653,9.652,9.653,9.643,9.643,9.643,9.653,9.644,9.65,9.658,9.661,9.67])
            ,np.array([8.911,8.913,8.911,8.917,8.92,8.921,8.923,8.922,8.923,8.922,8.923,8.931])
            ,np.array([8.907,8.912,8.923,8.921,8.921,8.922,8.923,8.922,8.922,8.921,8.921,8.931])
            ,np.array([9.7,9.698,9.695,9.688,9.689,9.691,9.698,9.684,9.69,9.703,9.709,9.709])
            ,np.array([9.85,9.844,9.817,9.836,9.825,9.823,9.839,9.822,9.832,9.847,9.857,9.853])
            ,np.array([9.67,9.666,9.647,9.665,9.656,9.655,9.653,9.657,9.662,9.67,9.676,9.681])
            ,np.array([8.923,8.926,8.915,8.935,8.936,8.937,8.94,8.942,8.941,8.939,8.94,8.95])]

        plt.figure()  # 使用plt.figure定义一个图像窗口.

        for i in range(0,len(yList)):
            plt.plot(x, yList[i],marker=markerList[i])
            #plt.plot(x, yList[i])

        plt.legend(legendList)
        plt.xticks(x, xticksLabelList)    #自定义标签
        plt.xlabel('时间')
        plt.ylabel('高程（m）')
        #plt.title('E匝道第一阶段桥墩沉降数据时程曲线图') # 设置标题
        plt.show()

    def PlotDeckElevation(self):
        """
           绘制桥面标高曲线
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

        legendList = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        markerListLoop = ['o','s','p','x','v','h']    #线条超过6条，则marker重复利用
        #markerList=['o','s','p','x','v','h','o','s','p','x','v','h']
        xticksLabelList = ['LZ1','LZ2','LZ3','LZ4','LZ5']
        
        xList = []
        markerList = []
        for i in range(0,len(xticksLabelList)):
            xList.append(i + 1)
        for i in range(0,len(legendList)):
            markerList.append(markerListLoop[i % len(markerListLoop)])    #整数+余数

        x = np.array(xList)
        yList = [np.array([8.92,9.703,9.822,9.653,8.911])
            ,np.array([8.921,9.7,9.821,9.652,8.913])
            ,np.array([8.92,9.703,9.822,9.653,8.911])
            ,np.array([8.925,9.691,9.813,9.643,8.917])
            ,np.array([8.928,9.678,9.807,9.643,8.92])
            ,np.array([8.93,9.678,9.805,9.643,8.921])
            ,np.array([8.931,9.687,9.81,9.653,8.923])
            ,np.array([8.929,9.673,9.798,9.644,8.922])
            ,np.array([8.929,9.678,9.807,9.65,8.923])
            ,np.array([8.928,9.691,9.823,9.658,8.922])
            ,np.array([8.929,9.698,9.834,9.661,8.923])
            ,np.array([8.938,9.697,9.83,9.67,8.931])]

        plt.figure()  # 使用plt.figure定义一个图像窗口.

        for i in range(0,len(yList)):
            plt.plot(x, yList[i],marker=markerList[i])
            #plt.plot(x, yList[i])

        plt.legend(legendList)
        plt.xticks(x, xticksLabelList)    #自定义标签
        plt.xlabel('测点')
        plt.ylabel('高程（m）')
        #plt.title('E匝道第一阶段桥墩沉降数据时程曲线图') # 设置标题
        plt.grid()
        plt.show()

    def PlotTowerDispTimeHistory(self):
        """
           绘制塔顶位移时程曲线
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

        legendList = ['1#','2#','3#','4#']
        markerListLoop = ['o','s','p','x','v','h']    #线条超过6条，则marker重复利用
        #markerList=['o','s','p','x','v','h','o','s','p','x','v','h']
        xticksLabelList = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        
        xList = []
        markerList = []
        for i in range(0,len(xticksLabelList)):
            xList.append(i + 1)
        for i in range(0,len(legendList)):
            markerList.append(markerListLoop[i % len(markerListLoop)])    #整数+余数

        x = np.array(xList)
        yList = [np.array([0,0.2,0.5,0,1,1,-0.3,1.9,1.8,1.8,1.7,2.7])
            ,np.array([0.1,0.3,0.3,0,1,1,-0.95,1.25,1.3,1.4,1.3,2.3])
            ,np.array([0,-0.2,-0.5,0,-1,-1.1,0.2,-2,-1.9,-2,-1.9,-3])
            ,np.array([0,-0.1,-0.7,0,-1,-0.9,1.05,-1.15,-1,-1.2,-1.3,-2.5])]

        plt.figure()  # 使用plt.figure定义一个图像窗口.

        for i in range(0,len(yList)):
            plt.plot(x, yList[i],marker=markerList[i])
            #plt.plot(x, yList[i])

        plt.legend(legendList)
        plt.xticks(x, xticksLabelList)    #自定义标签
        plt.xlabel('时间')
        plt.ylabel('位移（m）')
        plt.show()

    def PlotCableLineShape(self):
        """
           绘制主缆线形
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

        legendList = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        markerListLoop = ['o','s','p','x','v','h']    #线条超过6条，则marker重复利用
        #markerList=['o','s','p','x','v','h','o','s','p','x','v','h']
        xticksLabelList = ['LZ1','LZ2','LZ3','LZ4','LZ5']
        
        xList = []
        markerList = []
        for i in range(0,len(xticksLabelList)):
            xList.append(i + 1)
        for i in range(0,len(legendList)):
            markerList.append(markerListLoop[i % len(markerListLoop)])    #整数+余数

        x = np.array(xList)
        yList = [np.array([8.92,9.703,9.822,9.653,8.911])
            ,np.array([8.921,9.7,9.821,9.652,8.913])
            ,np.array([8.92,9.703,9.822,9.653,8.911])
            ,np.array([8.925,9.691,9.813,9.643,8.917])
            ,np.array([8.928,9.678,9.807,9.643,8.92])
            ,np.array([8.93,9.678,9.805,9.643,8.921])
            ,np.array([8.931,9.687,9.81,9.653,8.923])
            ,np.array([8.929,9.673,9.798,9.644,8.922])
            ,np.array([8.929,9.678,9.807,9.65,8.923])
            ,np.array([8.928,9.691,9.823,9.658,8.922])
            ,np.array([8.929,9.698,9.834,9.661,8.923])
            ,np.array([8.938,9.697,9.83,9.67,8.931])]

        plt.figure()  # 使用plt.figure定义一个图像窗口.

        for i in range(0,len(yList)):
            plt.plot(x, yList[i],marker=markerList[i])
            #plt.plot(x, yList[i])

        plt.legend(legendList)
        plt.xticks(x, xticksLabelList)    #自定义标签
        plt.xlabel('测点')
        plt.ylabel('高程（m）')
        #plt.title('E匝道第一阶段桥墩沉降数据时程曲线图') # 设置标题
        plt.grid()
        plt.show()