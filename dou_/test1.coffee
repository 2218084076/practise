<script type="text/coffeescript">
comments_use=[]
check_content_comment_save_td =(chat_id,comment_id=null)->
    $.ajax
        url:"/api/page/comment/load"
        type:"GET"
        dataType:"json"
        data:
            chat_id:chat_id
            comment_id:comment_id
        success:(data)->
            console.log "success",data
            if data.info == "ok"
                for comment in data.comments
                    remarks_list = null
                    remark_num = comment[5]["remarks"].length
                    try
                        remarks_list = JSON.parse(comment[5]["remarks"][remark_num-1][1])
                        console.log "remarks_list",remarks_list
                    catch e
                        continue
                    remarks_json =
                        "uid":remarks_list[0]
                        "first_pioneer":remarks_list[1]
                        "first_pioneer_user_id":remarks_list[2]
                        "first_contact":remarks_list[3]
                        "first_contact_user_id":remarks_list[4]
                        "date":remarks_list[5]
                        "second_pioneer":remarks_list[6]
                        "second_contact":remarks_list[8]
                    comments_use.push [comment,data.comment_id,remarks_json]
                    console.log "comments_use",comments_use
                    if data.last_comment_id != null
                        show_content_in_load(chat_id,data.last_comment_id) 
        error:(data)->
            console.log "error",data

check_content_comment_save_td "abd538cb8cbf418781d006aa091f9162",null

</script>
<script src="/static/js/coffeescript.js"></script>
