<div>
    <textarea id="wlb_20220114_json_check_content"></textarea>
    <button id="wlb_20220114_json_check_btn">check</button>
</div>
<script type="text/coffeescript">

check_content_action = (base_json,key,value,chat_id,comment_id=null)->
    $ajax
        url:"/api/page/comment/load"
        type:"GET"
        dataType:"json"
        data:
            chat_id:chat_id
            comment_id:comment_id
        succes:(data)->
            console.log data
            if data.info == "ok"
                for comment in data.comments
                    comment_json = null
                    try
                        comment_json = JSON.parse(comment[4])
                    catch e
                        continue
                    if comment_json[key] == value
                        console.log "action",comment_json
                        return
                    else
                        $.ajax
                            url:"api/page/comment/submit"
                            type:"POST"
                            dataType:"json"
                            data:
                                name:base_json["name"]
                                number:base_json["number"]
                            success:(data)->
                                console.log data
                                if data.info == "ok"
                                    send_json = 
                                        "name":name
                                        "number":number
                                    $(".comments_area[data-block=#{chat_id}]>div>textarea.comment_content").val JSON.stringify(send_json)
                                    $(".comments_area[data-block=#{chat_id}]>div>button.comment_submit").click()
                            error:(data)->
                                console.log data

        error:(data)->
            console.log data

$("body").on "click","#{wlb_20220114_json_check_btn}",(e)->
    check_content = $("#wlb_20220114_json_check_content").val()
    check_content_json = null
    try
        check_content_json = JSON.parse(check_content)
    catch e
        alert "content is not json"
        return
    number = check_content_json["number"]
    console.log number
    check_content_in_action check_content_json,"number",number,"ae6d663c789f4b69bd9341cdb3428b37",null 
</script>
<script src="/static/js/coffeescript.js"></script>



(r"/api/page/add_comment",findmaster_comment.AddCommentAPIHandler),
(r"/api/page/get_comment",findmaster_comment.GetCommentAPIHandler),
(r"/api/page/comment/submit",findmaster_comment.CommentSubmitAPIHandler),
(r"/api/page/comment/load",findmaster_comment.CommentLoadAPIHandler),
(r"/api/page/comment/load_one",findmaster_comment.CommentLoadOneAPIHandler),

(r"/api/page/comment/remark",       findmaster_comment.RemarkAPIHandler),
(r"/api/page/comment/remark_del",   findmaster_comment.RemarkDelAPIHandler),
(r"/api/page/comment/like",         findmaster_comment.LikeAPIHandler),
(r"/api/page/comment/ref",          findmaster_comment.RefAPIHandler),
(r"/api/page/comment/ref_add",      findmaster_comment.RefAddAPIHandler),
(r"/api/page/comment/del",          findmaster_comment.DelAPIHandler),