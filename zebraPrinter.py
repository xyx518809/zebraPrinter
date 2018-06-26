import win32print
from PIL import Image
import hzk16

class Zebra():
    def __init__(self,darkness = 25,width = 100):
        """
        :param darkness:灰度
        :param width: 宽度
        :param length: 长度
        """
        self.darkness = '~SD' + str(darkness)
        self.width = '^PW' + str(width)
        self.begin = '^XA' + self.darkness+self.width + '\n'
        self.end = '^XZ'
        self.printerList = self.getPrinterList()#获取本地打印机列表
        self.content = ''
        if len(self.printerList) == 0:
            print("打印机不存在")

    @staticmethod
    def pictureToHex(fileName, threshold):
        """
        获取图片点阵
        :param fileName: 文件名称
        :param threshold: 二值化阈值
        :return: 宽度，长度，二值化字符串
        """
        img = Image.open(fileName).convert('L')

        w = int(img.size[0] / 8) * 8  # 图片宽度
        h = img.size[1]  # 图片高度
        print(w, h)

        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        bImg = img.point(table, '1')  # 二值化
        bImg_array = bImg.load()  # 数据化
        temp = ''
        for i in range(h):
            for j in range(w):
                temp = temp + str(1 - bImg_array[j, i])

        pictureLenth = int(len(temp) / 4)
        picture = hex(int(temp, 2))[2:]
        return (w, h, picture.zfill(pictureLenth))

    def otherCommand(self,begin,commands,end):
        self.begin = begin
        self.content = commands
        self.end = end

    def setBarcode11(self,text, x, y, o='N', e='N', h=100, f='Y', g='N'):
        """
        code 11条码
        :param o:字体方向,N=正常，R=顺时针90度，I=顺时针180度，B=顺时针270度
        :param e:校验位，N=2位，Y=1位
        :param h:条码高度，1-9999
        :param f:打印注释行，N=不打印在条码上方；Y=打印在条码上方
        :param g:将注释行打印在条码上方，N=不打印在条码上方；Y=打印在条码上方
        :return:None
        """
        self.content = self.content + "^FO{},{}^B1{},{},{},{},{}^FD{}^FS\n".format(str(x),str(y),str(o),str(e),str(h),str(f),str(g),str(text))

    def setBarcodeITF(self, text, x, y, w=2, r=3.0, o='N', e='N', h=100, f='Y', g='N'):
        """
        Interleaved Two of Five
        :param text:内容
        :param x: 横坐标
        :param y: 纵坐标
        :param w: 模块窄条宽度，1-10
        :param r: 宽条与窄条比例，2.0-3.0
        :param o:字体方向,N=正常，R=顺时针90度，I=顺时针180度，B=顺时针270度
        :param e:校验位，N=2位，Y=1位
        :param h:条码高度，1-9999
        :param f:打印注释行，N=不打印在条码上方；Y=打印在条码上方
        :param g:将注释行打印在条码上方，N=不打印在条码上方；Y=打印在条码上方
        :return:None
        """
        self.content = self.content + "^FO{},{}^BY{},{},{}^B1{},{},{},{},{}^FD{}^FS\n".format(str(x), str(y), str(w),
                                                                                              str(r), str(h), str(o),
                                                                                              str(h), str(f), str(g),
                                                                                              str(e), str(text))

    def setBarcode39(self,text, x, y, w=2, r=3.0, o='N', e='N', h=100, f='Y', g='N'):
        """
        code 39
        :param text:内容
        :param x: 横坐标
        :param y: 纵坐标
        :param w: 模块窄条宽度，1-10
        :param r: 宽条与窄条比例，2.0-3.0
        :param o:字体方向,N=正常，R=顺时针90度，I=顺时针180度，B=顺时针270度
        :param e:校验位，N=2位，Y=1位
        :param h:条码高度，1-9999
        :param f:打印注释行，N=不打印在条码上方；Y=打印在条码上方
        :param g:将注释行打印在条码上方，N=不打印在条码上方；Y=打印在条码上方
        :return:None
        """
        self.content = self.content + "^FO{},{}^BY{},{},{}^B1{},{},{},{},{}^FD{}^FS\n".format(str(x), str(y), str(w),
                                                                                              str(r), str(h), str(o),
                                                                                              str(e), str(h), str(f),
                                                                                              str(g), str(text))

    def setBarcode128(self,text, x, y, w=2, r=3.0, o='N', e='N', h=100, f='Y', g='N', m='N'):
        """
        code 128
        :param text:内容
        :param x: 横坐标
        :param y: 纵坐标
        :param w: 模块窄条宽度，1-10
        :param r: 宽条与窄条比例，2.0-3.0
        :param o:字体方向,N=正常，R=顺时针90度，I=顺时针180度，B=顺时针270度
        :param e:校验位，N=2位，Y=1位
        :param h:条码高度，1-9999
        :param f:打印注释行，N=不打印在条码上方；Y=打印在条码上方
        :param g:将注释行打印在条码上方，N=不打印在条码上方；Y=打印在条码上方
        :param m:模式，N=不选择模式；U=UCC匹配模式，A=自动模式
        :return:None
        """
        self.content = self.content + "^FO{},{}^BY{},{},{}^BC{},{},{},{},{},{}^FD{}^FS\n".format(str(x), str(y), str(w),
                                                                                              str(r), str(h), str(o),
                                                                                              str(h), str(f), str(g),
                                                                                              str(e), str(m), str(text))

    def setChineseText(self, text, x=0, y=0, w=3):
        """
        打印中文字符
        :param text:中文字符
        :param x: 横坐标
        :param y: 纵坐标
        :param w: 比例
        :return: None
        """
        xOffset = 0
        for word in text:
            gbWord = word.encode('gb2312')
            self.content = self.content + '^FO{0},{1}~DGR:{2}.GRF,32,2,{3}^XG{2}.GRF,{4},{4}^FS\n'.format(x + xOffset, y, gbWord.hex(), hzk16.hzk16[word] , w)
            xOffset = xOffset + w*16

    def setEnglishText(self,text,x,y, o='N', h=15, w=12):
        """
        打印ASCII字符
        :param text:ASCII
        :param x: 横坐标
        :param y: 纵坐标
        :param o: 旋转角度
        :param h: 字符高度
        :param w: 字符宽度
        :return: None
        """
        self.content = self.content + '^FO{},{}^A0,{},{},{}^FD{}^FS\n'.format(x,y,o,h,w,text)

    def setImage(self, image, threshold, x, y, w=1):
        """
        设置打印图片
        :param image: 图片地址
        :param threshold: 二值化阈值
        :param x: 横坐标
        :param y: 纵坐标
        :param w: 放大比例
        :return: None
        """
        picture = Zebra.pictureToHex(image,threshold)
        self.content = self.content + '^FO{0},{1}~DGR:photo.GRF,{2},{3},{4}^XGphoto.GRF,{5},{5}^FS\n'.format(x,y,picture[0]*picture[1]/8,picture[0]/8, picture[2], w)

    def setBox(self, x, y, w, h, r=True, m=1, c='B'):
        """
        画方框和线条
        :param x:横坐标
        :param y: 纵坐标
        :param w: 宽度
        :param h: 长度
        :param r: 旋转
        :param m: 线粗细
        :param c: 打印颜色
        :return:
        """
        if r:
            self.content = self.content + '^FO{},{}^GB{},{},{},{}^FS\n'.format(x, y, w, h, m, c)
        else:
            self.content = self.content + '^FO{},{}^GB{},{},{},{}^FS\n'.format(x, y, h, w, m, c)

    def _getCommend(self):
        """
        获取命令
        :return:返回命令
        """
        return (self.begin+self.content+self.end).encode('utf-8')

    def getPrinterList(self):
        """
        获取本地打印机列表
        :return:本地打印机列表
        """
        printerList = []
        for (a,b,name,d) in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL):
            printerList.append(name)
        return printerList

    def printTab(self,printer):
        """
        打印标签
        :param printer: 打印机名称
        :return: None
        """
        hPrinter = win32print.OpenPrinter(printer)
        command = self._getCommend()
        try:
            hJob = win32print.StartDocPrinter(hPrinter, 1, ('Label', None, 'raw'))
            try:
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, command)
                win32print.EndPagePrinter(hPrinter)
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, '^EG'.encode('utf-8'))
                win32print.EndPagePrinter(hPrinter)
            finally:
                win32print.EndDocPrinter(hPrinter)
        finally:
            win32print.ClosePrinter(hPrinter)

    def resetPrinter(self):
        """
        重设
        :return:None
        """
        self.begin = '^XA' + self.darkness+self.width + '\n'
        self.end = '^XZ'
        self.content = ''


if __name__ == '__main__':
    test = Zebra(width=800)
    test.setBarcode11('1234',10,50,e = "Y")
    test.setBarcode128("1231531",10,100)
    test.setImage('atbslogo.png',200,10,150)
    test.setBox(10,200,100,50,m=10)
    test.printTab('ZDesigner ZT410-300dpi ZPL')
    #print(test.getPrinterList())