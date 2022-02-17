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
                    else
                        $.ajax
                            url:"/api/page/add_comment"
                            type:"POST"
                            dataType:"json"
                            data:
                                block_id:data.block_id
                                dom_content: uuid2(6,null)
                            success:(data)->
                                console.log data
                                if data.info == "ok"
                                    comment_entity_id = data.comment_entity
                                    send_json = base_json
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