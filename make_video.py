class MakeVideoArticleAPIHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self):
        imgs = json_decode(self.get_argument("imgs","[]"))
        t = self.get_argument("t",None)
        if not t:
            self.finish({"info":"error"})
            return
        num = 0
        img_remove_list = []
        for img in imgs:
            b64_data = img.split(';base64,')[1]
            data = base64.b64decode(b64_data)
            img_path = os.path.join(os.path.dirname(__file__),'../static/temp/%s_%s.%s'%(t,num,"png"))
            img_path_jpg = os.path.join(os.path.dirname(__file__),'../static/temp/%s_%s.%s'%(t,num,"jpg"))
            f = open(img_path, "ab")
            f.write(data)  # 多媒体存储content
            f.close()
            f_cv = cv2.imread(img_path)
            cv2.imwrite(img_path_jpg,f_cv)
            num +=1
            img_remove_list.append(img_path)
            img_remove_list.append(img_path_jpg)
        imgs_path = os.path.join(os.path.dirname(__file__),'../static/temp')
        video_path = os.path.join(os.path.dirname(__file__),'../static/temp')
        os.system("ffmpeg -y -r 1 -f image2 -i %s/%s_%%d.%s -vcodec libx264 %s/%s.mp4"%(imgs_path,t,"jpg",video_path,t))
        for img_path in img_remove_list:
            os.remove(img_path)
        self.finish({"info":"ok","video":"/static/temp/%s.mp4"%(t)})

$("body").on "click",".make_video",(evt)->
        $(".download_video").remove()
        img_doms = $(".img_made")
        imgs = []
        for img_dom in img_doms
            imgs.push img_dom.src
        $.ajax
            url:"/api/tool/article/make_video"
            type: "POST"
            dataType: "json"
            data:
                t:$("input[data-name=json_file]").val()
                imgs:JSON.stringify(imgs)
            success:(data)->
                console.log data
                $(".make_video").after """
                    <button class="line_btns_btn download_video">Download</button>
                """
            error:(data)->
                console.log data

(r"/api/tool/article/make_video",tool_article.MakeVideoArticleAPIHandler),