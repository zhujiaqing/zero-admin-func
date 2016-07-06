
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

	$("#func-view").children("div").hide();
	$("#func-"+activeRequire.split("=")[1]).show();

	// 文件上传
	$("#func-file-upload form").submit(function(){

		// console.log($(this))
		// console.log($(this)[0])
		// console.log(new FormData($(this)[0]))


		var formData=new FormData();
		formData.append("myfile",$('#func-file-upload input[name="myfile"]'))
		console.log(fromData)
		return false

		$.ajax({
		    url: "/zero_admin/mfs/upload",
		    type: "POST",
		    cache: false,
		    data: formData,
		    processData: false,
		    contentType: false,
		    dataType: "json",
		    success: function(res){
				if(0==res.ret){
					var message=res.info;
					message+="，CDN访问的地址列表：<br/><ul>";
					$.each(res.addrs,function(i,addr){
						message+='<li>'+addr+'<a target="_blank" href="'+addr+'">&nbsp;点击</a></li>';
					});
					message+="</ul>"

					tip("success",message);
					$('#func-file-upload input[type="text"]').val("");
					$('#func-file-upload input[type="file"]').val("");
				}else{
					tip("warning",res.info);
				}
			},
			error: function(){}
		});
		return false;
	});

	// 清缓存
	$("#func-file-clean-cache form").submit(function(){
		console.log("Ok")
		console.log($("#func-file-clean-cache form"))		

		return false;
		$.ajax({
		    url: "/zero_admin/mfs/clean_cache",
		    type: "POST",
		    data: {
		    	"keys":$("#func-file-clean-cache textarea").val(),
		    },
		    dataType: "json",
		    success: function(res){
				if(0==res.ret){
					var message="清除成功，已经清除的地址列表：<br/><ul>";
					$.each(res.keys,function(i,key){
						message+='<li>'+key+'</li>';
					});
					message+="</ul>"

					tip("success",message);
					$("#func-file-clean-cache textarea").val("");
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

