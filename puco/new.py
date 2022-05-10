import pyautogui
import time
import json
# 921.6

'''
ids=[]
cards=document.getElementsByClassName("daren-card")
for(i=0;i<cards.length;i++){
ids.push(cards[i].dataset["itemUid"])
}
 
'''

id_list = [
'a54490f3273f9172f412112cdbb35493', '144799b97ccf3f494463a9f298fed65e', '39e2b9d0b28ae81614bf110e23ef36b7', 'e3a3fd3aaaf15cb7563b723acc3b670f', '424f2540dbff65051e4b9c772c10dcc5', '636ae73fa05f5f7dd08cbec44b52686b', '0ef8fb88fd6c33e9e933cc91ae6f84e9', '89f73558e4450eff76a70b2a2b00ed70', 'ed5bbd2711213a357a79b3c2d83b4f46', '7a1e6463464a70640d0b8ffd75ffc82e', '5450f53b909d970c298139229b7eded3', '34eafa722d3caaefc47fac7f6f9cfac3', '2ff1e3b7a27c50490918ac553e55ad5a', 'cfb9102337479109e278223cffa5e177', '086da61d658b2e5db2d9636942e73d6b', '6b5dc7221d4e369451c988623c55b151', 'c008e927c56fdef1413f6b2eff94b6e1', '7c111ea647dd10b2eba196e51881c73f', '5e1a48686cf559e941f349290e87c834', '214249b4492cd5f0d97646f370809f46',
'2a5f8569a17d69b7c5f258903633a995', 'b7b61babf17e065170218d46abdc7ac8', 'e72ef669fec75854b0307e19c2646881', 'fb683aff1ce2c9c6c05a0079e2ca01f6', '9c86c057572a505df34fa5c6cf505603', 'f23aa077d6208c2699c810c7b626dc17', 'c514f91ccbc4e62057d664f7e4c56cb1', '8cab5a735ec1d381a039f0d0dff2c52e', '9c1df559984e3239a57f8ced8b003af8', 'bd3dc8bcd46fabd6ddceecbca58a1e0b', '0cc4fdc949e75c70974ccd8d4948ab08', '0874a46b9b7612494cfe38d0ef77667a', 'e1ca5ccfd718baede435dac8d2ca961a', '0fbe15b925d15ebe84c75c623d60f8b7', 'ad73b0eb0a13ecf53de9c636868fd5b8', '7d2e43a076ffd475d0b8cdade873ed7d', 'fb029c9ee92947789a70e0998f707f6d', '72549be604a326d08d4152e8d29979d7', '91fc7ce0e6df8d2661c209e0d1d6c31e', '7c00752f9723449c86d06494f73bb482',
'fa4a9cd615186e9cbea467aa92a94c8d', '7880164a12bdedbab67078177e3b1611', '50062d74499a5a38bb5f3e91553ae9cc', '76e5e189cc5fa3605b642ba154fb5fe4', 'd7bd6d96cd0ba8ba2cdb7dfaa9e5adda', 'd987181d71650f8fd242c7fc253d3d28', '63aaba7a1500215e85d8fbb3c82c4a87', 'db968a55fe28ce15925f5ff0fd7db44c', '2531df8bd290dbc1667aa1d67b7a5ac4', 'b7da9a60581dea3d705659e094954fa5', '4ccecd47d3d340682ed3f7328ab0064b', 'd07d8d8bc6839850be18d0bb50d0b205', 'f44f112747c00071d81d1d6def8fb459', '8737e63f328902f56a49a5840785102e', '7eca039ebee629540f95433727e88a3e', 'ae0b30aa806f8a25ff2fa073e69d2822', '6c630104d3e2789accdae5246fb3d630', '07f33529a73d4064c0d870f1b0d8e459', 'b4233e066fb5e9d867669aa9034e9897', 'c2f28ca3104a91d895f86a6c764b0735',
'8a770bca0de3383a4edb2c64bad5c3ad', '0c9e0cbb32f57c5b0419062b0c7270b1', '1f3b19dcb2dcd522f0918706ba250622', 'd1858da5baeed8eb3d3ee328a9d237c2', '775423e1f307b34754d503d7f9382198', 'fc8d4c19b58862b01abc11d2e7e70bd9', 'c370c9fd511de34bc4f161600e105959', '793ba34bc8e136c6ce66d0d8023d783c', 'ae98443f549d94deebf88023ead25768', '3774778ef6836d7edd80af6194b3ee21', '104615fd19ead73e49689e5430ee0d05', '75b0e92855046ffa6bee5cb951c06d17', 'a861702db6d234de13c6b7bdb8fb00e6', '476966da4a9a32cf0ea1a6d74a2ca7ec', 'f2cffa153d125f3cf682c9fc1408d598', '66d7efeac0eb328ec3d5df76d8c778a1', '6d1fd508688ed7bce9867659fa2df77f', 'ce2cd8ac691de9242b01f411140250df', '0e2717df09e827b3e9df1dd6f57adc49', '491e69112264c41da305575746856d08',
'5133ca2b8a8957c70d8bebe7173748d6', '11b91ba14171d3acefbe2a1adef9e45e', 'e959c6c7fb6e9b281ae7ad121ee933f5', '2910b1f6ccefab98812cfe58f69cfbb2', '969c71955d195b4387fde6e4b94225a3', 'dedd268106e247d089a17e3d56197a82', '6330fffc058f0c8042a53ba13f3ade3c', 'b7b6e1cf25ac2875ad8aed85b6e1ce4f', '0abfe8f7d92768cf62860485a96539c7', '80c8c6fdcd22fa8a9bbb007ba162df0e', '89b28f4c1c64c02d891b7877ad153dd4', 'f81497600517d22da705a165fb0bb065', '11c6a3c6f08492ff344dd567721917b9', '17c1e0872a9f0da10758fddbaa68aacf', 'f7d64f2c8cb6d9cb699efd8d649ded5f', 'ae01e32f45cb353181048c455e85b2b9', 'd67d8c6c8df0c4e869098e47c925b8d8', 'cc0eb154f9a00f20b11174a5247ced6a', 'f978ffdc52473397e35104ad27dafef7', '173de73a1899319d7a8b40877e3c5369'
]


url_list=[]
news_urls = []

print('url_list',len(id_list))
news_ids = []
for id in id_list:
    if id not in news_ids:
        news_ids.append(id)
print('news_ids:',len(news_ids))

url = 'https://buyin.jinritemai.com/dashboard/servicehall/daren-profile?uid='
for i in news_ids:
    user_url = url + i
    url_list.append(user_url)
num = 1

for n in range(0,100):
    if url_list[n] not in news_urls:
        news_urls.append(url_list[n])
        pyautogui.moveTo(x=617,y=74,duration=0.3)
        pyautogui.click(x=617,y=74,button='left')
        pyautogui.hotkey('ctrl','l')
        pyautogui.typewrite(f'{url_list[n]}')
        pyautogui.keyDown('enter')
        time.sleep(8)
        pyautogui.moveTo(x=1209,y=178,duration=0.3)
        pyautogui.click(x=1209,y=178, button='left')
        time.sleep(0.5)

        pyautogui.moveTo(x=1209,y=178,duration=0.3)
        pyautogui.click(x=1209,y=178,button='left')
        time.sleep(0.5)

        pyautogui.moveTo(x=1324,y=819,duration=0.3)
        pyautogui.click(x=1324,y=819,button='left')
        time.sleep(0.5)

        pyautogui.typewrite('document.getElementsByClassName("contact-btn")[0].click()')
        pyautogui.keyDown('enter')
        time.sleep(2)

        pyautogui.typewrite('document.getElementsByClassName("add-product-operate")[0].getElementsByTagName("button")[0].click()')
        pyautogui.keyDown('enter')
        time.sleep(0.5)

        pyautogui.moveTo(x=350,y=535,duration=0.3)
        pyautogui.click(x=350,y=535,button='left')
        time.sleep(0.5)


        pyautogui.moveTo(x=241,y=490,duration=0.3)
        pyautogui.click(x=241,y=490,button='left')
        time.sleep(0.5)

        # pyautogui.typewrite('document.getElementsByClassName("ant-checkbox")[0].getElementsByTagName("input")[0].click()')
        # pyautogui.keyDown('enter')
        # time.sleep(2)

        pyautogui.moveTo(x=781,y=848,duration=0.3)
        pyautogui.click(x=781,y=848,button='left')
        time.sleep(0.5)

        pyautogui.moveTo(x=962,y=984,duration=0.3)
        pyautogui.click(x=962,y=984,button='left')
        time.sleep(3)

        print(num)
        print(url_list[n])
        num+=1