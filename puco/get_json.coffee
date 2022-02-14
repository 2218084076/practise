<div>
    <table id="www" class="content"></table>
</div>
<script type="text/coffeescript">
$("#www").append """
<tr class="wlb_th" style="
    text-align: center;
    width: max-content;
" >
    <th>博主</th>
    <th>粉丝数</th>
    <th>合作店铺数</th>
    <th>微信号</th>
    <th>手机号</th>
    <th>简介</th>
    <th>抖音号</th>
</tr>
                    """

check=(a,b)->
    return parseInt(a["fan"])-parseInt(b["fan"])
comments_use=[]
comments_use_action=()->
    comments_use.sort(check)
    $(".wlb_td").remove()
    for comment_ues in comments_use
        $("#www").append """
<tr class="wlb_td">
    <td>#{comment_ues["name"]}</td>
    <td>#{comment_ues["fan"]}</td>
    <td>#{comment_ues["shop"]}</td>
    <td>#{comment_ues["wechat"]}</td>
    <td>#{comment_ues["phone"]}</td>
    <td>#{comment_ues["introduce"]}</td>
    <td>#{comment_ues["dou_id"]}</td>
</tr>
                    """
www =(chat_id,comment_id=null)->
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
www("502c0d441b2a42b6a145a367bc6d1125")
</script>
<script src="/static/js/coffeescript.js"></script>
