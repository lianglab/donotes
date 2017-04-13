### form

### 前言
记录form使用笔录


#### form属性

<table width="100%">
	<thead>
		<tr>
			<th width="100">属性名</th>
	        <th width="300">属性值</th>
	        <th>描述</th>
	    </tr>
	</thead>
	<tbody>
		<tr>
			<td>action</td>
        	<td> 一个url地址</td>
        	<td> 指定表单提交到的地址 </td>
    	</tr>
		<tr>
			<td>method</td>
        	<td><code>GET</code> , <code>POST</code></td>
        	<td>表单将以此种方法提交到服务器</td>
    	</tr>
		<tr>
			<td>target</td>
        	<td>
		         * <code>_self</code> 当前页面 </br>
		         
		         * <code>_blank</code> 每次在新窗口打开 </br>
		         
		         *  <code>blank</code>  每次在同一个新窗口打开 </br>
		         
		         *  <code>_parent</code> 父级frame </br>
		         
		         * <code>_top</code> 顶级frame </br>
		         
		         * iframename 指定的iframe
       
        	</td>
        	<td>表单提交后，收到回复的页面</td>
    	</tr>
		<tr>
			<td>name</td>
        	<td>-</td>
        	<td>一个html文档中，每个form的name应该是唯一的</td>
    	</tr>
		<tr>
			<td>enctype</td>
        	<td>
        		* <code>application/x-www-form-urlencoded</code> 默认值 </br>
        
        		* <code>multipart/form-data</code> 上传file用 </br>
        
        		* <code>text/plain</code> html5默认
        	</td>
        	<td>
				以 <code>POST</code> 方式提交form时的MIME类型。文件上传必须使用 <code>multipart/form-data</code>
			</td>
    	</tr>
		<tr>
			<td>autocomplete</td>
        	<td><code>on</code> , <code>off</code></td>
        	<td>是否自动完成表单字段</td>
    	</tr>
		<tr>
			<td>autocapitalize</td>
	        <td>
	        * <code>none</code> 完全禁用自动首字母大写 </br>
	        
	        * <code>sentences</code> 自动对每句话首字母大写 </br>
	        
	        * <code>words</code> 自动对每个单词首字母大写 </br>
	        
	        * <code>characters</code> 自动大写所有的字母
	        </td>
	        <td>
	             iOS 专用属性，表单中文本域英文大小写
	        </td>
    	</tr>
		<tr>
			<td>accept-charset</td>
        	<td>字符编码格式( <code>utf-8</code> , <code>gb-2312</code> 等)</td>
        	<td>
            	将会以此种编码格式提交表单到服务器，默认值是UNKONWN，即html文档所采用的编码格式。
        	</td>
    	</tr>
		<tr>
			<td>novalidate</td>
        	<td>
				<code>true</code> , <code>false</code>
			</td>
        	<td>
            	是否启用表单校验
        	</td>
    	</tr>
		<tr>
			<td colspan="3"></td>
    	</tr>
	</tbody>
</table>

>举例说明

	<form action="/login" method="post" target="blank" >
    	<input type="text" name='username'>
    	<button>提交</button>
	</form>

表单以post方式提交给 /login 接口，并会打开一个新页面显示返回结果，由于 target="blank" ，所以就算提交多次该表单，都只会继续刷新之前打开的窗口。

>问题记录

	使用jquery-mobile，渲染触摸事件，参考代码为
	$(document).on("pagecreate","#pageone",function(){
        $("#paneltitle").on("swiperight",function(){
        $("#revealherf").click();
        });
    });
	
	默认重载页面为当前页面，会产生两个body,导致渲染事件失败。