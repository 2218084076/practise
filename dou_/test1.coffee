
<div contenteditable="false">
<table class="wlb_dyzbjl" border="1" bordercolor="black" cellpadding="10" cellspacing="0">
<tbody>

<tr>
<th>操作</th>
<th>编号</th>
<th>抖音博主UID</th>
<th>开拓（首月）</th>
<th>开拓（首月）USER_ID</th>
<th>运维（首页）</th>
<th>运维（首页）USER_ID</th>
<th>开拓日期</th>
<th>开拓（次月起）</th>
<th>开拓（次月起）USER_ID</th>
<th>运维（次月起）</th>
<th>运维（次月起）USER_ID</th>
</tr>
</tbody></table>
</div>

<script type="text/coffeescript">
comments_use=[]

comments_use_action=()->
    i=1
    for [comment,comment_id,comment_use] in comments_use
        $(".wlb_dyzbjl").append """
<tr class="wlb_td" data-comment-id="#{comment_id}_#{comment[0]}">
    <td><button class="del">删除</button><button class="edit">修改</button><button class="update">更新</button><button class="save_td">save</button></td>
    <td style="text-align:center;font-size:15px;">#{i}</td>
    <td style="text-align:center">#{comment_use["uid"]}</td>
    <td>#{comment_use["first_pioneer"]}</td>
    <td style="text-align:center">#{comment_use["first_pioneer_user_id"]}</td>
    <td>#{comment_use["first_contact"]}</td>
    <td>#{comment_use["first_contact_user_id"]}</td>
    <td>#{comment_use["date"]}</td>
    <td>#{comment_use["first_contact"]}</td>
    <td>#{comment_use["second_pioneer"]}</td>
    <td>#{comment_use["second_contact"]}</td>
    <td></td>
</tr>
"""
        i++

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
                    comments_use.push [remarks_json]
                    console.log "comments_use",comments_use
                    comments_use_action
                    if data.last_comment_id != null
                        check_content_comment_save_td(chat_id,data.last_comment_id) 
        error:(data)->
            console.log "error",data

check_content_comment_save_td "abd538cb8cbf418781d006aa091f9162",null

</script>
<script src="/static/js/coffeescript.js"></script>
