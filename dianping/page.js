a=document.getElementsByClassName("shop-name")
shop_name=a[0].getElementsByTagName("h1")[0].innerText
b=document.getElementsByClassName("midsml-rank-stars")
shop_star=b[0].className.replaceAll("midsml-rank-stars mid-str","")
c=document.getElementsByClassName("rank")[0].getElementsByClassName("item")[0].innerText
shop_comments_num = ""+parseInt(c)
d=document.getElementsByClassName("inner")[0].innerText.split("  ")
shop_area_list = d
e=window.location.href
shop_link=e
f=document.getElementsByClassName("brief-info")[0].getElementsByClassName("address")[0].innerText.replaceAll("地址： ","")
shop_address=f
shop_info_list_check = document.getElementsByClassName("mod shop-info")
if (shop_info_list_check.length>0){
    shop_info_list = document.getElementsByClassName("mod shop-info")[0].getElementsByClassName("con")[0].getElementsByTagName("li")
}else{
    shop_info_list=[]
}

shop_info={}
for (i=0;i<shop_info_list.length;i++){
    console.log(shop_info_list[i])
    key = shop_info_list[i].getElementsByClassName("title")[0].innerText
    value = shop_info_list[i].innerText.replaceAll(key+"\n","")
    shop_info[key]=value
}

shop_createtime ="尚未营业，没有数据"
shop_opentime ="尚未营业，没有数据"
if (shop_info["营业时间"]!=undefined){
    shop_opentime=shop_info["营业时间"]
}
if (shop_info["创立时间"]!=undefined){
    shop_createtime=shop_info["创立时间"]
}

shop_cards = []

cards_check = document.getElementsByClassName("promotion")
if (cards_check.length>0){
    document.getElementsByClassName("view-more")[0].click()
    cards = document.getElementsByClassName("promotion")[0].getElementsByClassName("group")[0].getElementsByClassName("item")
    for(j=0;j<cards.length;j++){
        console.log(cards[j])
        c_title = cards[j].getElementsByClassName("title")[0].innerText
        c_price = cards[j].getElementsByClassName("price")[0].innerText
        c_sold_count = cards[j].getElementsByClassName("sold-count")[0].innerText
        c_info = {
            "title":c_title,
            "price":c_price,
            "sold_count":c_sold_count,
        }
        shop_cards.push(c_info)
    }
}else{
    cards = []
    shop_cards = []
}


result = {
    "shop_name":shop_name,
    "shop_star":shop_star,
    "shop_comments_num":shop_comments_num,
    "shop_area_list":shop_area_list,
    "shop_link":shop_link,
    "shop_address":shop_address,
    "shop_info":shop_info,
    "shop_createtime":shop_createtime,
    "shop_opentime":shop_opentime,
    "shop_cards":shop_cards,
}
console.log(JSON.stringify(result))
add = document.createElement("textarea")
add.value = JSON.stringify(result)
add.style="position:fixed;right:0;top:0;"
document.body.append(add)