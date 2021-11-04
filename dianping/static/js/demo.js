a=$(".shop-all-list>ul").getElementsByTagName("li")
result = []
for(i=0;i<a.length;i++){
    link = a[i].getElementsByClassName("tit")[0].getElementsByTagName("a")[0].getAttribute("href")
    title = a[i].getElementsByClassName("tit")[0].getElementsByTagName("a")[0].getElementsByTagName("h4")[0].textContent
    result_item = {
        "link":link,
        "title":title,
    }
    result.push(result_item)
}
result_str = JSON.stringify(result)


$.ajax({
    url: "http://127.0.0.1:8888/api/add",
    data: {
        pll: result_str,
    },
    dataType: 'json',
    type: 'GET',
    success: function(data) {
        console.log(data)
    },
    error: function(data) {
        console.log(data)
    }
});
document.getElementsByClassName("next")[0].click()