##qrcode

###前言
python生产二维码记录

###依赖
	
	pip install Image
	pip install qrcode


###实例

>简单

	import qrcode
	img = qrcode.make('Some data here')
	img.save("xxx.png")

>高级用法

	import qrcode
	qr = qrcode.QRCode(
	    version=1,
	    error_correction=qrcode.constants.ERROR_CORRECT_L,
	    box_size=10,
	    border=4,
	)
	qr.add_data('Some data')
	qr.make(fit=True)

	img = qr.make_image()	
	img.save("xxx.png")

参数解析：

	version：值为1~40的整数，控制二维码的大小（最小值是1，是个12x12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。
	
	error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
	
		ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
		ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
		ERROR_CORRECT_Q：大约25%或更少的错误能被纠正。
		ERROR_CORRECT_H：大约30%或更少的错误能被纠正。
		box_size：控制二维码中每个小格子包含的像素数。
	
	border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）


>带图标

	#!/usr/bin/env python
	# encoding: utf-8
	import qrcode  
	from PIL import Image  
	import os  

	def gen_qrcode(string, path, logo=""):  
	    """
	    生成中间带logo的二维码
	    需要安装qrcode, PIL库
	    @参数 string: 二维码字符串
	    @参数 path: 生成的二维码保存路径
	    @参数 logo: logo文件路径
	    @return: None
	    """
	
	    qr = qrcode.QRCode(  
	        version=2,  
	        error_correction=qrcode.constants.ERROR_CORRECT_H,  
	        box_size=10,  
	        border=4  
	        )  
	    qr.add_data(string)  
	    qr.make(fit=True)  
	
	    img = qr.make_image()  
	    img = img.convert("RGBA")  
	
	    if logo and os.path.exists(logo):
	        try:
	            icon = Image.open(logo)  
	            img_w, img_h = img.size  
	        except Exception, e:
	            print e
	
	        factor = 4  
	        size_w = int(img_w/factor) 
	
	
	        size_h = int(img_h / factor)  
	
	        icon_w, icon_h = icon.size  
	        if icon_w > size_w:  
	            icon_w = size_w  
	        if icon_h > size_h:  
	            icon_h = size_h
	
	        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)  
	
	        w = int((img_w - icon_w) / 2)  
	        h = int((img_h - icon_h) / 2)  
	        icon = icon.convert("RGBA")  
	        img.paste(icon, (w, h), icon)  
	
	    img.save(path)  
	
	if __name__ == "__main__":  
	    gen_qrcode("http://www.baidu.com","qr.png", "favicon.ico")