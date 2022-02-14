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
                if data.last_comment_id !=null
                    www(chat_id,data.last_comment_id)
        error:(data)->
            console.log data
www("93d8f0b9d9b140dfbe15b74a2f2d5276")
