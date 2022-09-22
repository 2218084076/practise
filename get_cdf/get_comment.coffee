<div>
    <table id="www" class="content"></table>
</div>
<script type="text/coffeescript">
comment_list=[]


crawler =()->
    product_list=document.getElementsByClassName("ckass_lit")
    contents=[]
    for i in product_list
        contents.push {
            'title':i.getElementsByTagName("h4")[0].innerText.replace("\n\n",""),
            'price':i.getElementsByTagName("em")[0].innerText.replace("\n",""),
            'stock':i.getElementsByTagName("li")[0].innerText.split("库存：")[1].split("已售")[0].replace("\n",""),
            'sales':i.getElementsByTagName("li")[0].innerText.split("库存：")[1].split("已售")[0].replace("\n",""),
        }
    return contents

www =(chat_id,comment_id=null)->
    $.ajax
        url:"/api/page/comment/load"
        type:"GET"
        dataType:"json"
        data:
            chat_id:chat_id
            comment_id:comment_id
        success:(data)->
            console.log "https://www.qianshanghua.com/api/page/comment/load?chat_id=#{chat_id}&comment_id=#{comment_id}"
            comment_list.push "https://www.qianshanghua.com/api/page/comment/load?chat_id=#{chat_id}&comment_id=#{comment_id}"
            if data.info=="ok"
                for comment in data.comments
                    console.log "comment"
                if data.last_comment_id !=null
                    www(chat_id,data.last_comment_id)
        error:(data)->
            console.log "error"
www("98faef0b1fb142f0b70b9deba77cb90f")
console.log comment_list
</script>
<script src="/static/js/coffeescript.js"></script>