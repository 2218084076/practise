<script src="https://sdk.amazonaws.com/js/aws-sdk-2.235.1.min.js"></script>
<div class="wlb_upload">选择图片</div>
<input type="file" class="file_input">
<button class="file_add">upload</button>
<img class="demo" src="">
<script type="text/coffeescript">

root = exports ? this
root.Hs or= {}
Hs = root.Hs

bucket = new AWS.S3({
    accessKeyId: "jxgdp44t3iyvlwiqdqu5ivfddq5q",
    secretAccessKey: "j3itwcmq5fwywenoj6ad75w5qxpgtk4xexravxdbwbz3mbdovrae2",
    endpoint: new AWS.Endpoint("https://bifrostcloud.com"),
    params: {
        Bucket: "us1-dcs-s3"
    }
})

$("body").on "click",".file_add",(evt)->
    $(".wlb_upload").text "上传中"
    file = $(".file_input")[0].files[0]
    console.log file
    params =
        Key: "wlb/#{file.name}"
        ContentType: file.type
        Body: file
        ACL: 'public-read'
    bucket.upload params,(err,data)->
        $(".comments_area[data-block=be280473039548fcaf67911feb5473db]").find(".comment_content").val(JSON.stringify(data))
        $(".comments_area[data-block=be280473039548fcaf67911feb5473db]").find(".comment_submit").click()

encode_from_s3 = (data)->
    str = data.reduce (a,b)->
            return a+String.fromCharCode(b)
        ,''
    return btoa(str).replace(/.{76}(?=.)/g,'$&\n')
$("body").on "click",".load_file",(evt)->
    dom = $(this)
    dom_preview_str = dom.parents(".load_preview_area").first().find(".load_preview_str")
    dom_preview_str.text "加载中..."
    dom_preview = dom.parents(".load_preview_area").first().find(".load_preview")
    dom_preview.empty()
    dom_load_key = dom.parents(".load_preview_area").first().find(".load_key").text()
    bucket.getObject {Key: dom_load_key},(err,file)->
        console.log err
        console.log file
        file_type = file.ContentType
        file_src = "data:#{file_type};base64," + encode_from_s3(file.Body)
        if file_type.split("/")[0] in ["image"]
            dom_preview.append """
                <img src="#{file_src}" style="width:100%;">
            """
        else
            dom_preview.append """
                <a target="_blank" href="#{file_src}" style="width:100%;">文件下载</a>
            """
$(window).on "load",()->
    root.comment_add_one_base = (content_json)->
        user_name = content_json["nickname"]
        content = content_json["content"]
        date_html = formatDateAllEn(content_json["time"]*1000)
        user_headimgurl = content_json["headimgurl"]
        comment_id = content_json["comment_id"]
        sequence = content_json["sequence"]
        control_tools=""
        if IS_EDITOR or USER_ID == content_json["user_id"]
            control_tools = """
            <div class="comment_line">
                <button class="comment_control_tool_btn comment_del">DEL</button>
            </div>
            """
        content_json = null
        try
            content_json = JSON.parse(content)
        catch
            content = content
        if content_json != null
            console.log content_json
            key = content_json["Location"].split("https://us1-dcs-s3.bifrostcloud.com/")[1]
            key = decodeURIComponent(key)
            content = """
                <div class="load_preview_area">
                    <div class="load_key">#{key}</div>
                    <div class="load_preview_str">点击加载</div>
                    <div class="load_preview"></div>
                    <button class="load_file">加载文件</button>
                </div>
            """
        html = """
            <div class="comment" data-comment-id="#{comment_id}_#{sequence}">
                <div class="comment_img"><img src="#{user_headimgurl}"></div>
                <div class="comment_line"><span class="name">#{user_name}</span><span class="date">#{date_html}</span></div>
                <div class="comment_line"><p class="content">#{content}</p></div>
                #{control_tools}
            </div>
        """
        return html
    root.comment_load_one_base = (comment_list,comment_id)->
        if comment_list[6]==1
            return ""
        user_name = members[comment_list[1]]["name"]
        content = comment_list[4]
        if comment_list[3] in ["COMMENT"]
            content_json = null
            try
                content_json = JSON.parse(content)
            catch
                content = content
            if content_json != null
                key = content_json["Location"].split("https://us1-dcs-s3.bifrostcloud.com/")[1]
                key = decodeURIComponent(key)
                content = """
                    <div class="load_preview_area">
                        <div class="load_key">#{key}</div>
                        <div class="load_preview_str">点击加载</div>
                        <div class="load_preview"></div>
                        <button class="load_file">加载文件</button>
                    </div>
                """
        else if comment_list[3] in ["WEIXINPAYCALLBACKSUCCESS","ALIPAYPAYCALLBACKSUCCESS"]
            content = ("""<div class="content_table"><div>#{k}</div><div>#{v}</div></div>""" for k,v of content).join("\n\r")

        date_html = formatDateAllEn(comment_list[2]*1000)
        user_headimgurl = members[comment_list[1]]["headimgurl"]
        control_tools=""
        if comment_list[3] not in ["WEIXINPAYCALLBACKSUCCESS","ALIPAYPAYCALLBACKSUCCESS"]
            if IS_EDITOR or USER_ID == comment_list[1]
                control_tools = """
                <div class="comment_line">
                    <button class="comment_control_tool_btn comment_del" style="margin-top:15px;">DEL</button>
                </div>
                """
        html = """
            <div class="comment" data-comment-id="#{comment_id}_#{comment_list[0]}">
                <div class="comment_img"><img src="#{user_headimgurl}"></div>
                <div class="comment_line"><span class="name">#{user_name}</span><span class="date">#{date_html}</span></div>
                <div class="comment_line"><p class="content">#{content}</p></div>
                #{control_tools}
            </div>
        """
        return html
</script>
<script src="/static/js/coffeescript.js"></script>