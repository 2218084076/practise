urls=[]
p=document.getElementsByClassName("default-card")
for(var i=0;i<p.length;i++){
  urls.push(p[i].getElementsByTagName("a")[0].getAttribute("href"))
}
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\" style=width:200px;height:200px;>"+JSON.stringify(urls)+"</textarea>"
document.body.append(dom)
