<div>
    <table id="www" class="content"></table>
</div>
<script type="text/coffeescript">

check=(a,b)->
    return parseInt(a["fan"])-parseInt(b["fan"])
comments_use=[]
comments_use_action=()->
    comments_use.sort(check)
    $(".wlb_td").remove()
    i=1
    for comment_ues in comments_use
        $("#www").append """
<div class="sort_list">
    <div class="num_logo">
        <img src="1.png" alt="">
    </div>
    <div style=margin:10px;border-radius:auto;vertical-align: middle;>#{comment_ues["name"]}</div>
    <div style="font-size: x-small;color: #999;">#{comment_ues["number"]}</div>
</div>
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
www("ae6d663c789f4b69bd9341cdb3428b37")
</script>
<script src="/static/js/coffeescript.js"></script>
