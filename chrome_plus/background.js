console.log("this is background.js")
check_urls =[]
chrome.webRequest.onCompleted.addListener(
  function (details) {
    console.log(details)
    if (details.statusCode == 200) {
      

      // chrome.tabs.sendMessage("fillingPass", details.tabId, (e) => {
        
      //   console.log(e)
      //   console.log('==== 巨量星图 数据监听结束 ====');
      // })
        is_get = false
        is_get_num = 0
        check_urls_has = [
            "&platform_source=1&platform_channel=1&type=1&service_name=data.AdStarDataService&service_method=GetAuthorWatchedDistribution&sign_strict=1&sign=",
            "&platform_source=1&author_type=1&service_name=data.AdStarDataService&service_method=GetAuthorFansDistributionV2&sign_strict=1&sign=",
            "http://www.cdfgsanya.com/api/overseas/products/search?"
        ]
        for (i=0;i<check_urls_has.length;i++){
            if (details.url.indexOf(check_urls_has[i])>-1){
                is_get=true
                is_get_num = i
                continue
            }
        }

        if (is_get){
            if (check_urls.indexOf(details.url)>-1){
                return
            }
            check_urls.push(details.url)
            console.log(details.url)
            console.log("==== 数据监听 is_get ====");
            chrome.tabs.sendMessage(details.tabId,{ 
                "url":details.url, 
                "data":"get_data_back" ,
                "is_get_num":is_get_num
            },(res)=>{
                console.log("send")
            })

            // $.ajax({
            //     url:details.url,
            //     type:"GET",
            //     dataType:"json",
            //     data:null,
            //     success:function(data){
            //         console.log(data)
            //         chrome.tabs.sendMessage(details.tabId,{ 
            //             "url":details.url, 
            //             "data":data ,
            //             "is_get_num":is_get_num
            //         },(res)=>{
            //             console.log("send")
            //         })
            //     },
            //     error:function(data){}
            // })
        }
    }
  },

  { urls: [
    "https://pgy.xiaohongshu.com/api/solar/cooperator/user/blogger/*",
    "http://www.cdfgsanya.com/api/overseas/products/*",
    "https://www.xingtu.cn/h/api/gateway/handler_get/*"
   ] }  //监听页面请求,你也可以通过*来匹配。
);



chrome.runtime.onMessage.addListener((req, sender, sendResponse) => {
  const res = req.info
  console.log(res)
  if (res=="fensihuoyuedu"){
      check_urls = []
  }
})
// function FindData(strURL) {
//     var req = new XMLHttpRequest();
//     req.open("GET", strURL, true);
//     req.onreadystatechange=function() {
//         if (req.readyState==4) {
//             if (req.status==200)
//             {
//                 console.info("Sucess!");
//                 console.info("Data: " + req.responseText);
//             }
//         else if (req.status==404) console.info("URL doesn't exist!")
//         else console.info("Error: Status is " + req.status)
//         }
//     }
//     req.send();
// }