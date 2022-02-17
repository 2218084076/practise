<style>
.wlb_dyzbjl>tbody>tr>th{
width:120px;
}
.wlb_dyzbjl>tbody>tr>td {
    word-break: break-all;
    font-size:12px
}
.wlb_dyzbjl>tbody>tr>td>button{
    margin-right:25px;
    font-size: 16px;
    width: 100%;
}

</style>
<div contenteditable="false">
<button id="check">查看</button><table class="wlb_dyzbjl" border="1" bordercolor="black" cellpadding="10" cellspacing="0">
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
<button id="wlb_add_line">新增一行</button>
<script type="text/coffeescript">


comments_use=[]
comments_use_action=()->
    i=1
    for comment_ues in comments_use
        $(".wlb_dyzbjl").append """
<tr class="wlb_td">
    <td></td>
    <td style="text-align:center;font-size:15px;">#{i}</td>
    <td style="text-align:center">#{comment_ues["uid"]}</td>
    <td>#{comment_ues["pioneer"]}</td>
    <td style="text-align:center">#{comment_ues["user_id"]}</td>
    <td>#{comment_ues["contact"]}</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
"""
        i++
show_content_in_load =(chat_id,comment_id=null)->
    $.ajax
        url:"/api/page/comment/load"
        type:"GET"
        dataType:"json"
        data:
            chat_id:chat_id
            comment_id:comment_id
        success:(data)->
            console.log data
            if data.info=="ok"
                for comment in data.comments
                    console.log comment
                    try
                        content_json = JSON.parse(comment[4])
                    catch
                        continue
                    comments_use.push content_json
                comments_use_action()
                if data.last_comment_id !=null
                    www(chat_id,data.last_comment_id)
                    
        error:(data)->
            console.log data


check_content_remove = (user_id,chat_id,comment_id=null)->
    $.ajax
        url:"/api/page/comment/load"
        type:"GET"
        dataType:"json"
        data:
            chat_id:chat_id
            comment_id:comment_id
        success:(data)->
            console.log data
            if data.info == "ok"
                for comment in data.comments
                    comment_json = null
                    try
                        comment_json = JSON.parse(comment[4])
                    catch e
                        continue
                    if user_id == USER_ID
                        $("##{USER_ID}").remove()
                    else
                        alert "无法删除"

check_content_action_in_load = (uid,pioneer,user_id,chat_id,comment_id=null)->
    uid=$(".wlb_dyzbjl>tbody>tr>td")[2].innerText
    pioneer=$(".wlb_dyzbjl>tbody>tr>td")[3].innerText
    contact=$(".wlb_dyzbjl>tbody>tr>td")[5].innerText
    $.ajax
        url:"/api/page/comment/load"
        type:"GET"
        dataType:"json"
        data:
            chat_id:chat_id
            comment_id:comment_id
        success:(data)->
            console.log data
            if data.info == "ok"
                for comment in data.comments
                    comment_json = null
                    try
                        comment_json = JSON.parse(comment[4])
                    catch e
                        continue
                    if uid == comment_json["uid"]
                        alert "博主uid存在"
                        return
                last_comment_id = data.last_comment_id
                if last_comment_id == null
                    send_json = 
                        "uid":uid
                        "pioneer":pioneer
                        "user_id":USER_ID
                        "contact":contact
                    $.ajax
                        url:"/api/page/comment/submit"
                        type:"POST"
                        dataType:"json"
                        data:
                            block_id: BLOCK_ID
                            chat_id: chat_id
                            content: JSON.stringify(send_json)
                            uuid: uuid2(6,null)
                        success:(data)->
                            console.log data
                        error:(data)->
                            console.log data
                else
                    check_content_action_in_load uid,pioneer,USER_ID,chat_id,last_comment_id
            else if data.info == "error"
                console.log data
                if data.about == "no chat's comment"
                    send_json = 
                        "uid":uid
                        "pioneer":pioneer
                        "user_id":USER_ID
                        "contact":contact
                    $.ajax
                        url:"/api/page/comment/submit"
                        type:"POST"
                        dataType:"json"
                        data:
                            block_id: BLOCK_ID
                            chat_id: chat_id
                            content: JSON.stringify(send_json)
                            uuid: uuid2(6,null)
                        success:(data)->
                            console.log data
                        error:(data)->
                            console.log data
        error:(data)->
            console.log data

# $("body").on "click","#check",()->
show_content_in_load("abd538cb8cbf418781d006aa091f9162")

$("body").on "click","#wlb_add_line",(evt)->
    $(".wlb_dyzbjl").append """
<tr id="#{USER_ID}">
<td><button id="wlb_save_line">save</button> <button id="wlb_remove_line">remove</button></td>
<td>待确认</td>
<td contenteditable="true">输入博主uid ...</td>
<td contenteditable="true">输入开拓（首月）...</td> 
<td>#{USER_ID}</td>
<td contenteditable="true">输入运维（首页）...</td>
<td contenteditable="true">输入运维（首页）USER_ID...</td>
<td contenteditable="true">输入开拓日期...</td>
<td contenteditable="true">输入开拓（次月起）...</td>
<td>#{USER_ID}</td>
<td contenteditable="true">输入运维（次月起）...</td>
<td contenteditable="true">输入运维（次月起）USER_ID...</td>
</tr>
    """

$("body").on "click","#wlb_remove_line",()->
    user_id=$("##{USER_ID}>td")[4].innerText
    check_content_remove user_id,"abd538cb8cbf418781d006aa091f9162",null

$("body").on "click","#wlb_save_line",(e)->
    uid=$("##{USER_ID}>td")[2].innerText
    pioneer=$("##{USER_ID}>td")[3].innerText
    contact=$("##{USER_ID}>td")[5].innerText
    check_content_action_in_load uid,pioneer,USER_ID,"abd538cb8cbf418781d006aa091f9162",null

</script>
<script src="/static/js/coffeescript.js"></script>