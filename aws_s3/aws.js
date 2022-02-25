<script src="https://sdk.amazonaws.com/js/aws-sdk-2.235.1.min.js"></script>
<button id="wlb_upload">upload</button>
<button id="wlb_download">download</button>
<input id="file-chooser" type="file">
<p id="results"></p>
<script>

var bucket = new AWS.S3({
		accessKeyId:"jxgdp44t3iyvlwiqdqu5ivfddq5q",
		secretAccessKey:"j3itwcmq5fwywenoj6ad75w5qxpgtk4xexravxdbwbz3mbdovrae2",
		endpoint: new AWS.Endpoint("https://bifrostcloud.com"),
		params:{
			Bucket:"us1-dcs-s3"
		}
	});
var fileChooser = document.getElementById('file-chooser');
var button = document.getElementById('wlb_upload');
    button.addEventListener('click', function() {
        var file = fileChooser.files[0];
        if (file) {
            results.innerHTML = '';
            var params = { 
            	Key:"wlb/"+file.name, 
            	ContentType: file.type, 
            	Body: file,  
            	ACL: 'public-read' 
            	}; //key可以设置为桶的相抵路径，Body为文件， ACL最好要设置
            console.log(params)
            bucket.upload(params, function(err, data) {
                console.log(err); //打印出错误
                results.innerHTML = err ? 'ERROR!' : 'UPLOADED.';
                console.log(data);
                $(".comments_area[data-block=be280473039548fcaf67911feb5473db]").find(".comment_content").val(JSON.stringify(data))
                $(".comments_area[data-block=be280473039548fcaf67911feb5473db]").find(".comment_submit").click()
            });
        } else {
            results.innerHTML = 'Nothing to upload.';
        }
    }, false);
</script>