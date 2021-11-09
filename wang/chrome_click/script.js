// alert("抖音评论区点赞");
  // 评论区博主名字
name_list=['小猫咪滚滚','Coco子']
num = 0
function doit(){
	setTimeout(function(){
		list_now = document.getElementsByClassName("aa8946e6a10e3788dca09663eb82fc99-scss")
		for(var i=0;i<list_now.length;i++){
			// console.log(list_now[i].getElementsByTagName("div"))
			console.log(name_list.indexOf(list_now[i].getElementsByTagName("div")[5].textContent))
			if(name_list.indexOf(list_now[i].getElementsByTagName("div")[5].textContent)>-1){
				console.log("<==++==>")
				list_now[i].getElementsByTagName("div")[10].getElementsByTagName("p")[0].click()
				num = 100
				console.log(i)
				list_now[i].scrollIntoViewIfNeeded()
				// window.scrollTo(0,list_now[i].scrollIntoViewIfNeeded())
				break
			}else{
				console.log("----")
			}
		}
		
		num = num +1
		if(num<4){
			window.scrollTo(0,document.getElementById("root").children[0].scrollHeight)
			console.log(num)
			doit()
		}
	},5000)
}
doit()
