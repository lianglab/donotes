##flask-web##

###前言###
记录使用flask框架，前端的一些用法

####静态文件调用

>js

	<!-- <script src="http://cdn.bootcss.com/html5shiv/3.7.0/html5shiv.js"></script> -->
	<script src="{{url_for('static',filename='ie-emulation-modes-warning.js')}}"></script>

>css

	<!-- <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet"> -->
	<link href="{{url_for('static',filename='bootstrap.min.css')}}" rel="stylesheet">


####get请求前端

	<head>
	<meta charset="utf-8">  
	<script type="text/javascript">
		$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
	</script>
	<script type=text/javascript>
	  
	// ajax异步传递请求结果
	$(function() {
	    $('#redis_run').bind('click', function() {
	      $.getJSON($SCRIPT_ROOT + '/redis_run', {
	        host: $('input[name="host"]').val(),
	        port: $('input[name="port"]').val(),
	        shell: $('input[name="shell"]').val()
	      }, function(data) {
	        // $("#result").text(data.result);
	        var strData = [];
    		for (list in data.result) {
    				strData.push("<tr>");
                	strData.push("<td>"+list+"</td>");
                	if(typeof data.result[list]==="object")
                	{
                		strData.push("<td>");
                		for (value in data.result[list]){
                			strData.push("<li>");
                			strData.push(value);
                			strData.push("&nbsp;&nbsp;&nbsp;")
                			strData.push(data.result[list][value]);
                			strData.push("</li>");
                		}
                		strData.push("</td>");
                	}
                	else
                	{
                	strData.push("<td>"+data.result[list]+"</td>");
                	}	
            		strData.push("</tr>");
            		   	}
              	$("#result").html(strData.join(""));

	      });
	      return false;
	    });
	  });


	// 捕获回车键，指向开始执行事件
	document.onkeydown = function(event_e){    
        if(window.event)    
         event_e = window.event;    
         var int_keycode = event_e.charCode||event_e.keyCode;    
         if(int_keycode ==13){   
          $('#redis_run').click();  
        }  
    }  

	</script>
	
	</head>
	<body>
	
	<div>
		<h2>redis console</h2>
		主机:&nbsp;<input type="text" size=20 name='host' value="192.168.1.217">&nbsp;&nbsp;&nbsp;
		端口:&nbsp;<input type="number" size=20 name='port' value="6382">&nbsp;&nbsp;&nbsp;
		模糊查询:&nbsp;<input type="text" size=30 name='shell' value='null->help;Blank->redis info' onclick="if(value==defaultValue){value='';this.style.color='#000'}" onBlur="if(!value){value=defaultValue;this.style.color='#999'}" style="color:#999"/>&nbsp;&nbsp;
		<button id="redis_run">开始执行</button>&nbsp;&nbsp;&nbsp;
	
		</br />
	
	
		<div class="table-responsive">
	 	<h2>result</h2>
	        <table class="table table-striped">
	          <thead>
	            <tr>
	              <th>keys</th>
	              <th>value</th>
	            </tr>
	          </thead>
	          <tbody id='result'>
	           
	          </tbody>
	        </table>
	      </div>
	
	
	</div>
	
	</body>




####post

	<!DOCTYPE html>
	<html>
	<head>
	  <meta charset="utf-8">  
	  <script src="{{url_for('static',filename='jquery.min.js')}}"></script>
	  <script type="text/javascript">
	    $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
	  </script>
	  <script type="text/javascript">
	  $("input[name=hostname]").focus();
	
	  function ajaxForm(){
	    $.ajax({
	      type: 'post',
	      url:$SCRIPT_ROOT + '/createcontainer',
	      dataType: 'json',
	      data:{
	      'plat':$('select[name=plat]').val(),
	      'servicetype':$('select[name=servicetype]').val(),
	      'hostname':$('input[name=hostname]').val(),
	      'Imagename': $('input[name=Imagename]').val(),
	      'tag': $('input[name=ImageTag]').val(),
	      'containername': $('input[name=containername]').val(),
	      'command':$('input[name=command').val()
	    },
	
	    error: function(xhr, err){
	      alert('请求失败，原因可能是：' + err + '！')
	    },
	
	    success: function(data, textStatus){
	      // $('#Tip').text(data.result);
	      alert(data.result);
	      }
	
	  });
	  return false
	
	}
	
	
	$(function() {
	        $.getJSON($SCRIPT_ROOT + '/db_fetchall_servicenamelist',{
	          plat: $('select[name="plat"]').val()
	        }, function(data) {
	          // alert(data.result);
	          var strData = [];
	          servicenamelist = data.result;
	          for (key in servicenamelist) {
	              strData.push("<option value="+servicenamelist[key]+">"+servicenamelist[key]+"</option>");
	        }
	        $("#servicetypelist").html(strData.join(""));
	
	        });
	    });
	
	
	$(document).ready(function(){
	  $("#selectplat").change(function(){
	    $.getJSON($SCRIPT_ROOT + '/db_fetchall_servicenamelist',{
	          plat: $('select[name="plat"]').val()
	        }, function(data) {
	          // alert(data.result);
	          var strData = [];
	          servicenamelist = data.result;
	          for (key in servicenamelist) {
	              strData.push("<option value="+servicenamelist[key]+">"+servicenamelist[key]+"</option>");
	        }
	        $("#servicetypelist").html(strData.join(""));
	
	        });
	  });
	});
	
	  </script>
	
	  <style type="text/css">
	  .btn{width:80px;height:30px;line-height:14px;font-size:14px;color:#4CA669;}
	
	  </style>
	</head>
	  <h1>Create Container</h1>
	
	  <!-- <form action="/createcontainer" method=post> -->
	  <form method=post action="" onSubmit="return ajaxForm()">
	    <dl>
	      <dt>plat:</dt>
	      <!-- <dd><input type=text name=servicetype></dd> -->
	      <select name="plat" id="selectplat">
	      <option value="tbc">tbc</option>
	      <option value="lbox">lbox</option>
	      <option value="Mware">Mware</option>
	      </select>
	      <dt>service:</dt>
	      <!-- <dd><input type=text name=servicetype></dd> -->
	      <select name="servicetype" id="servicetypelist">
	   
	      </select>
	      <dt>hostname:</dt>
	      <dd><input type=text name=hostname value='192.168.1.120'></dd>
	      <dt>Image:</dt>
	      <dd><input type=text name=Imagename></dd>
	      <dt>Tag:</dt>
	      <dd><input type=text name=ImageTag></dd>
	      <dt>containername:</dt>
	      <dd><input type=text name=containername></dd>
	      <dt>command:</dt>
	      <dd><input type=text name=command></dd>
	
	    </dl>
	    <!-- <p><input type=submit value=create class="btn" onmouseover="this.style.backgroundPosition='left -36px'" onmouseout="this.style.backgroundPosition='left top'"> -->
	    <p><input type=submit value=create class="btn">
	  </form>
	
	</html>

****
###TROUBLE

>AttributeError: ‘module’ object has no attribute ‘autoescape’

	yum install python-pip -y
	pip install --upgrade jinja2