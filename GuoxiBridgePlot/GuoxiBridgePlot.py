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

    def PlotZDeckElevation(self):
        """
           绘制桥面标高曲线（桥梁前进方向左侧，前进方向为0#台=>3#台）
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

    def PlotYDeckElevation(self):
        """
           绘制桥面标高曲线（桥梁前进方向左侧，前进方向为0#台=>3#台）
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

        legendList = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        markerListLoop = ['o','s','p','x','v','h']    #线条超过6条，则marker重复利用
        #markerList=['o','s','p','x','v','h','o','s','p','x','v','h']
        xticksLabelList = ['LY1','LY2','LY3','LY4','LY5']
        
        xList = []
        markerList = []
        for i in range(0,len(xticksLabelList)):
            xList.append(i + 1)
        for i in range(0,len(legendList)):
            markerList.append(markerListLoop[i % len(markerListLoop)])    #整数+余数

        x = np.array(xList)
        yList = [np.array([8.92,9.692,9.830,9.663,8.850])
            ,np.array([8.92,9.687,9.826,9.660,8.847])
            ,np.array([8.922,9.683,9.822,9.656,8.842])
            ,np.array([8.921,9.68,9.819,9.653,8.843])
            ,np.array([8.922,9.679,9.818,9.652,8.843])
            ,np.array([8.923,9.687,9.827,9.657,8.843])
            ,np.array([8.924,9.69,9.83,9.66,8.844])
            ,np.array([8.927,9.693,9.831,9.663,8.845])
            ,np.array([8.927,9.693,9.832,9.665,8.845])
            ,np.array([8.928,9.694,9.833,9.667,8.847])
            ,np.array([8.925,9.698,9.849,9.675,8.852])
            ,np.array([8.929,9.686,9.826,9.658,8.852])]

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

    def PlotZCableLineShape(self):
        """
           绘制主缆线形（桥梁前进方向左侧，前进方向为0#台=>3#台）
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

        legendList = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        markerListLoop = ['o','s','p','x','v','h']    #线条超过6条，则marker重复利用
        #markerList=['o','s','p','x','v','h','o','s','p','x','v','h']
        xticksLabelList = ['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17','Z18','Z19']
        
        xList = []
        markerList = []
        for i in range(0,len(xticksLabelList)):
            xList.append(i + 1)
        for i in range(0,len(legendList)):
            markerList.append(markerListLoop[i % len(markerListLoop)])    #整数+余数

        x = np.array(xList)
        yList = [np.array([11.24,13.84,16.84,17.9,15.87,14.19,12.91,12.01,11.46,11.33,11.47,11.99,12.9,14.2,15.86,17.9,16.86,13.83,11.25])
            ,np.array([11.25,13.85,16.84,17.9,15.87,14.19,12.91,12.01,11.46,11.33,11.46,12,12.9,14.21,15.86,17.9,16.86,13.84,11.26])
            ,np.array([11.26,13.85,16.85,17.9,15.88,14.19,12.91,12.02,11.47,11.33,11.47,12,12.91,14.21,15.86,17.9,16.87,13.85,11.27])
            ,np.array([11.26,13.85,16.84,17.9,15.87,14.19,12.91,12.02,11.46,11.32,11.47,12,12.9,14.2,15.86,17.9,16.84,13.84,11.27])
            ,np.array([11.26,13.85,16.85,17.91,15.87,14.19,12.92,12.01,11.45,11.32,11.46,12.02,12.9,14.22,15.87,17.91,16.84,13.85,11.27])
            ,np.array([11.25,13.84,16.84,17.9,15.87,14.19,12.92,12.02,11.46,11.33,11.47,12.01,12.91,14.21,15.88,17.92,16.86,13.85,11.27])
            ,np.array([11.25,13.85,16.84,17.9,15.87,14.19,12.91,12.02,11.47,11.33,11.47,12,12.91,14.2,15.88,17.91,16.86,13.85,11.27])
            ,np.array([11.25,13.85,16.84,17.9,15.86,14.19,12.91,12.01,11.47,11.33,11.46,11.99,12.9,14.2,15.88,17.91,16.85,13.84,11.27])
            ,np.array([11.25,13.84,16.84,17.89,15.86,14.19,12.91,12.01,11.46,11.33,11.46,11.99,12.9,14.2,15.88,17.91,16.84,13.84,11.27])
            ,np.array([11.25,13.84,16.83,17.9,15.87,14.18,12.9,12.01,11.45,11.32,11.46,12,12.9,14.2,15.89,17.9,16.85,13.84,11.27])
            ,np.array([11.23,13.92,16.83,17.88,15.86,14.2,12.91,12.02,11.47,11.3,11.48,12.02,12.92,14.21,15.89,17.91,16.85,13.83,11.26])
            ,np.array([11.24,13.9,16.82,17.89,15.86,14.18,12.9,12.01,11.46,11.31,11.46,12,12.9,14.19,15.88,17.91,16.83,13.83,11.25])]

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

    def PlotYCableLineShape(self):
        """
           绘制主缆线形（桥梁前进方向右侧，前进方向为0#台=>3#台）
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

        legendList = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        markerListLoop = ['o','s','p','x','v','h']    #线条超过6条，则marker重复利用
        #markerList=['o','s','p','x','v','h','o','s','p','x','v','h']
        xticksLabelList = ['Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8','Y9','Y10','Y11','Y12','Y13','Y14','Y15','Y16','Y17','Y18','Y19']
        
        xList = []
        markerList = []
        for i in range(0,len(xticksLabelList)):
            xList.append(i + 1)
        for i in range(0,len(legendList)):
            markerList.append(markerListLoop[i % len(markerListLoop)])    #整数+余数

        x = np.array(xList)
        yList = [np.array([11.26,13.86,16.86,17.92,15.93,14.28,12.99,12.07,11.51,11.35,11.51,12.07,13,14.26,15.93,17.92,16.86,13.85,11.27])
            ,np.array([11.26,13.86,16.86,17.92,15.93,14.28,12.99,12.07,11.52,11.34,11.51,12.07,13.01,14.26,15.93,17.92,16.85,13.86,11.28])
            ,np.array([11.25,13.86,16.87,17.93,15.93,14.27,12.99,12.06,11.51,11.33,11.51,12.06,13,14.25,15.92,17.92,16.84,13.85,11.27])
            ,np.array([11.26,13.86,16.86,17.92,15.92,14.28,12.98,12.07,11.51,11.35,11.52,12.06,13.01,14.25,15.93,17.91,16.85,13.86,11.28])
            ,np.array([11.27,13.86,16.86,17.91,15.91,14.26,12.97,12.06,11.52,11.35,11.51,12.05,13.02,14.25,15.93,17.9,16.84,13.86,11.27])
            ,np.array([11.26,13.87,16.87,17.93,15.93,14.28,12.99,12.07,11.51,11.35,11.51,12.07,13.01,14.27,15.92,17.92,16.85,13.85,11.27])
            ,np.array([11.25,13.88,16.87,17.93,15.93,14.28,13,12.07,11.52,11.35,11.5,12.06,13.01,14.27,15.93,17.93,16.84,13.85,11.27])
            ,np.array([11.26,13.88,16.86,17.92,15.93,14.28,13,12.07,11.52,11.34,11.51,12.06,13.01,14.27,15.93,17.93,16.83,13.85,11.27])
            ,np.array([11.26,13.87,16.86,17.93,15.93,14.28,12.99,12.07,11.52,11.34,11.51,12.06,13.01,14.27,15.92,17.93,16.83,13.85,11.26])
            ,np.array([11.26,13.86,16.86,17.94,15.94,14.28,13,12.07,11.51,11.35,11.51,12.07,13,14.28,15.92,17.94,16.84,13.85,11.26])
            ,np.array([11.26,13.87,16.87,17.93,15.94,14.29,13.01,12.08,11.53,11.36,11.52,12.08,13.01,14.28,15.93,17.94,16.85,13.85,11.26])
            ,np.array([11.26,13.87,16.86,17.93,15.94,14.28,12.99,12.07,11.51,11.34,11.51,12.07,13,14.26,15.92,17.93,16.83,13.85,11.26])]

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