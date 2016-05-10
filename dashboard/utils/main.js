
domain="http://127.0.0.1";

function tip(type,message){
	var html="";
	switch(type){
		case "success":
			html+='<div class="alert alert-success" role="alert">'+message+'</div>';
			break;
		case "info":
			html+='<div class="alert alert-info" role="alert">'+message+'</div>';
			break;
		case "warning":
			html+='<div class="alert alert-warning" role="alert">'+message+'</div>';
			break;
		case "danger":
			html+='<div class="alert alert-danger" role="alert">'+message+'</div>';
			break;
	}
	$("#func-tip").html(html);
}

$(document).ready(function(){
	// 页面状态初始化
	var activeRequire=window.location["search"];
	$('ul.dropdown-menu a[href="'+activeRequire+'"]').parent().addClass('active');

	var html='';
	switch(activeRequire){
		case "?path=file-upload":
			html+='<div class="uploadFile">';
			html+='<form method="POST" id="uploadFile" enctype="multipart/form-data" action="/zero_admin/mfs/upload">';
			html+='<div class="input-group"><span class="input-group-addon" id="basic-addon1">文件路径</span><input type="text" name="path" class="form-control" placeholder="/upload/2016/05/10/upload.png，为空系统随机" /></div>';
			html+='<div class="input-group"><span class="input-group-addon" id="basic-addon1">本地文件</span><input type="file" name="uploadFile" class="form-control" /></div>';
			html+='<div><input type="submit" class="form-control" value="上传" /><div>';
			html+='</form></div>';
			break;
		case "?path=file-clean-cache":
			html+='清缓存';
			break;
		case "?path=last-login-ip":
			html+='最后登录IP';
			break;
		case "?path=api-encrypt":
			html+='协议加解密';
			break;
	}
	$("#func-view").html(html);

	// 其它
	$("#func-view #uploadFile").submit(function(){
		// console.log($(this).children('input[name="path"]').val());
		// return false;

		// if(""==$(this).children('input[name="uploadFile"]').val()){
		// 	tip("warning","没有选择本地文件");
		// 	return false;
		// }
		$.ajax({
		    url: "/zero_admin/mfs/upload",
		    type: "POST",
		    cache: false,
		    data: new FormData($(this)[0]),
		    processData: false,
		    contentType: false,
		    // dataType: "josn",
		    success: function(res){
				if(0==res.ret){
					var message=res.info;
					message+="，CDN访问的地址列表：<br/><ul>";
					$.each(res.addr,function(i,item){
						message+='<li>'+item+'<a target="_blank" href="'+item+'">&nbsp;点击</a></li>';
					});
					message+="</ul>"
					tip("success",message);
				}else{
					tip("warning",res.info);
				}
			},
			error: function(){}
		});

		return false;
	});

});

console.log("Completed");

