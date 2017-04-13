## JS note

### 前言
记录一些jsx相关的笔记


### js压缩

	uglifyjs FileSaver.js --comments /@source/ > FileSaver.min.js


### 传输内容，实现文件下载

>在触发器上，添加下载函数

	downloadfunction = 'downloadFile("' + name + '")'
    $("#downloadconf").attr("onclick",downloadfunction);

>下载函数

	function downloadFile(name){
	    fileName = name + '.conf'  //文件名
	    content = $("#file_content").html();  //捕获内容

	    var aLink = document.createElement('a');
	    var blob = new Blob([content]);
	    var evt = document.createEvent("HTMLEvents");
	    evt.initEvent("click", false, false);//initEvent 不加后两个参数在FF下会报错
	    aLink.download = fileName;
	    aLink.href = URL.createObjectURL(blob);
	    aLink.dispatchEvent(evt);
	}
	
