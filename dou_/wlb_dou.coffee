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
    height: 40px;
    box-shadow: 0 5px 10px 0 rgba(0,0,0,0.2), 0 6px 15px 0 rgba(0,0,0,0.19);
}

</style>
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
<button id="wlb_add_line">新增一行</button>
<script type="text/coffeescript">
root = exports ? this
# !!!! Hotpoor root object
root.Hs or= {}
Hs = root.Hs


comments_use=[]
comments_use_action=()->
    i=1
    for [comment,comment_id,comment_use] in comments_use
        has_mark = false
        remarks_list = null
        remark_num = comment[5]["remarks"].length
        try
            remarks_list = JSON.parse(comment[5]["remarks"][remark_num-1][1])
            console.log "remarks_list",remarks_list
            has_mark = true
        catch e
            has_mark = false
        if has_mark
            remarks_json =
                "uid":remarks_list[0]
                "first_pioneer":remarks_list[1]
                "first_pioneer_user_id":remarks_list[2]
                "first_contact":remarks_list[3]
                "first_contact_user_id":remarks_list[4]
                "date":remarks_list[5]
                "second_pioneer":remarks_list[6]
                "second_contact":remarks_list[8]
            _html = """
                <td><button class="del" data-theme="c" data-icon="flat-man" data-role="button">删除</button><button class="edit">修改</button><button class="update">更新</button></td>
                <td style="text-align:center;font-size:15px;">#{i}</td>
                <td style="text-align:center">#{remarks_json["uid"]}</td>
                <td>#{remarks_json["first_pioneer"]}</td>
                <td style="text-align:center">#{remarks_json["first_pioneer_user_id"]}</td>
                <td>#{remarks_json["first_contact"]}</td>
                <td>#{remarks_json["first_contact_user_id"]}</td>
                <td>#{remarks_json["date"]}</td>
                <td>#{remarks_json["first_contact"]}</td>
                <td>#{remarks_json["second_pioneer"]}</td>
                <td>#{remarks_json["second_contact"]}</td>
                <td></td>
            """
        else
            _html = """
                <td><button class="del">删除</button><button class="edit">修改</button><button class="update">更新</button></td>
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
            """
        $(".wlb_dyzbjl").append """
            <tr class="wlb_td" data-comment-id="#{comment_id}_#{comment[0]}">
                #{_html}
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
            console.log "success",data
            if data.info=="ok"
                for comment in data.comments
                    console.log comment
                    try
                        content_json = JSON.parse(comment[4])
                    catch
                        continue
                    comments_use.push [comment,data.comment_id,content_json]
                comments_use_action()
                if data.last_comment_id !=null
                    show_content_in_load(chat_id,data.last_comment_id)
        error:(data)->
            console.log "error",data

check_content_comment_edit = (chat_id,comment_id)->
    $(".wlb_td[data-comment-id='#{comment_id}']").attr("contenteditable",true)

check_content_comment_update = (chat_id,data_comment_id)->
    tds = $(".wlb_td[data-comment-id=#{data_comment_id}]>td")
    console.log tds
    remark_content_list = []
    td_num=0
    for td in tds
        console.log td
        if td_num in [0,1]
            td_num=td_num+1
            continue
        remark_content_list.push $(td).text()
        console.log $(td).text()
        td_num=td_num+1
    console.log remark_content_list
    $.ajax
        url:"/api/page/comment/remark"
        type:"POST"
        dataType:"json"
        data:
            block_id: BLOCK_ID
            chat_id: chat_id
            content: "remark comment #{data_comment_id}"
            uuid: uuid2(6,null)
            comment_id: data_comment_id.split("_")[0]
            comment_sequence: data_comment_id.split("_")[1]
            remark_content: JSON.stringify(remark_content_list)
        success:(data)->
            console.log data
        error:(data)->
            console.log data

check_content_comment_del = (chat_id,comment_id)->
    console.log comment_id
    $.ajax
        url:"/api/page/comment/del"
        type:"POST"
        dataType:"json"
        data:
            block_id: BLOCK_ID
            chat_id: chat_id
            content: "del comment #{comment_id}"
            comment_id: comment_id.split("_")[0]
            comment_sequence: comment_id.split("_")[1]
            like_content: "del"
            uuid:uuid2(6,null)        
        success:(data)->
            if data.info =="ok"
                $(".wlb_td[data-comment-id='#{comment_id}']").remove()
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

check_content_action_in_load = (uid,content_list,user_id,chat_id,comment_id=null)->
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
                        "uid":content_list[0]
                        "first_pioneer":content_list[1]
                        "first_pioneer_user_id":content_list[2]
                        "first_contact":content_list[3]
                        "first_contact_user_id":content_list[4]
                        "date":content_list[5]
                        "second_pioneer":content_list[6]
                        "second_contact":content_list[8]
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
                        "uid":content_list[0]
                        "first_pioneer":content_list[1]
                        "first_pioneer_user_id":content_list[2]
                        "first_contact":content_list[3]
                        "first_contact_user_id":content_list[4]
                        "date":content_list[5]
                        "second_pioneer":content_list[6]
                        "second_contact":content_list[8]
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

show_content_in_load("abd538cb8cbf418781d006aa091f9162")

$("body").on "click",".update",()->
    data_comment_id = $($(this).parents(".wlb_td")[0]).attr("data-comment-id")
    check_content_comment_update "abd538cb8cbf418781d006aa091f9162",data_comment_id

$("body").on "click",".edit",()->
    data_comment_id = $($(this).parents(".wlb_td")[0]).attr("data-comment-id")
    check_content_comment_edit "abd538cb8cbf418781d006aa091f9162",data_comment_id

$("body").on "click",".del",()->
    data_comment_id = $($(this).parents(".wlb_td")[0]).attr("data-comment-id")
    check_content_comment_del "abd538cb8cbf418781d006aa091f9162",data_comment_id

$("body").on "click","#wlb_add_line",(evt)->
    $(".wlb_dyzbjl").append """
<tr id="#{USER_ID}">
<td><button class="wlb_save_line">save</button> <button class="wlb_remove_line">remove</button></td>
<td>待确认</td>
<td contenteditable="true">输入博主uid ...</td>
<td contenteditable="true">输入开拓（首月）...</td> 
<td>#{USER_ID}</td>
<td contenteditable="true">输入运维（首月）...</td>
<td contenteditable="true">输入运维（首月）USER_ID...</td>
<td contenteditable="true">输入开拓日期...</td>
<td contenteditable="true">输入开拓（次月起）...</td>
<td>#{USER_ID}</td>
<td contenteditable="true">输入运维（次月起）...</td>
<td contenteditable="true">输入运维（次月起）USER_ID...</td>
</tr>
    """

$("body").on "click",".wlb_remove_line",()->
    user_id=$("##{USER_ID}>td")[4].innerText
    check_content_remove user_id,"abd538cb8cbf418781d006aa091f9162",null

$("body").on "click",".wlb_save_line",(e)->
    tds = $("##{USER_ID}>td")
    console.log tds
    content_list = []
    td_num=0
    for td in tds
        console.log td
        if td_num in [0,1]
            td_num=td_num+1
            continue
        content_list.push $(td).text()
    console.log content_list
    uid = content_list[0]
    check_content_action_in_load uid,content_list,USER_ID,"abd538cb8cbf418781d006aa091f9162",null
</script>
<script src="/static/js/coffeescript.js"></script>