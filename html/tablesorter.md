## tablesorter

### 前言
记录一些tablesorter相关的笔记

下载地址：  [http://tablesorter.com/docs/#Download](http://tablesorter.com/docs/#Download)

### 使用（基于flask）

>引用

    <script src="{{url_for('static',filename='js/jquery.tablesorter.min.js')}}"></script>
    <script src="{{url_for('static',filename='js/jquery.min.js')}}"></script>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/themes/blue/style.css') }}">

	or  html

	<script type="text/javascript" src="/path/to/jquery-latest.js"></script> 
	<script type="text/javascript" src="/path/to/jquery.tablesorter.js"></script> 
	<link rel="stylesheet" href="/manage/plugin/tablesorter/blue/style.css type="text/css" />

>table标签

	<table class="tablesorter">
	...
	</table>

>渲染

	//更新缓存	
	$(".tablesorter").trigger("update");

	//渲染排序
	$(".tablesorter").tablesorter();




