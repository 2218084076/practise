import pyautogui
import time
import pyperclip
pyperclip.copy(rf'''
result=[]
result.push(document.getElementsByClassName("card--1fmeJ")[3].getElementsByClassName("name--3OXp2")[0].innerText)
result.push(document.getElementsByClassName("card--1fmeJ")[3].getElementsByClassName("time--1J-Ei")[0].innerText)
result.push(document.getElementsByClassName("card--1fmeJ")[3].getElementsByClassName("valueWrapper--3jbBR")[0].innerText)
result.push(document.getElementsByClassName("card--1fmeJ")[3].getElementsByClassName("valueWrapper--3jbBR")[1].innerText)
result.push(document.getElementsByClassName("card--1fmeJ")[3].getElementsByClassName("valueWrapper--3jbBR")[2].innerText)
result_info={
    "date":"2月1日"
    "name":result[0],
    "time":result[1],
    "clinch":result[2],
    "number":result[3],
    "thousands":result[4],
}
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"
''')