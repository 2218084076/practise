import json
import random
import time

from playwright.sync_api import sync_playwright

"""
每页20个商品 共6页
"""
page_num = [20]

ip_pool = ['13.250.37.103:4799', '13.250.46.50:4345', '54.169.37.186:16547', '13.250.37.103:4778', '13.213.67.125:4123',
           '13.213.67.125:4125', '13.213.67.125:4139', '3.72.86.226:13847', '13.213.67.125:4177', '13.250.37.103:4786',
           '13.250.37.103:4792', '3.93.195.111:14528', '13.250.37.103:4808', '13.213.67.125:4124', '3.93.195.111:14502',
           '3.72.86.226:13879', '3.93.195.111:14542', '13.213.67.125:4167', '3.93.195.111:14483', '3.72.86.226:13831',
           '175.41.175.240:14714', '3.93.195.111:14516', '3.93.195.111:14538', '13.250.37.103:4774',
           '13.250.46.50:4355', '13.250.37.103:4793', '13.250.37.103:4785', '13.213.67.125:4160', '13.250.37.103:4801',
           '54.169.37.186:16564', '13.250.37.103:4780', '13.250.37.103:4815', '13.250.37.103:4810', '3.72.86.226:13832',
           '13.250.37.103:4806', '3.93.195.111:14533', '175.41.175.240:14724', '13.250.46.50:4368',
           '3.93.195.111:14540', '175.41.175.240:14703', '13.213.67.125:4150', '13.250.46.50:4333',
           '13.250.37.103:4791', '3.93.195.111:14505', '13.250.46.50:4366', '3.72.86.226:13871', '13.250.37.103:4813',
           '3.93.195.111:14499', '3.72.86.226:13796', '3.72.86.226:13866', '54.169.37.186:16565',
           '175.41.175.240:14704', '13.250.46.50:4344', '13.250.46.50:4367', '3.93.195.111:14520', '13.213.67.125:4166',
           '54.169.37.186:16560', '13.250.37.103:4817', '3.72.86.226:13807', '13.213.67.125:4161', '13.213.67.125:4180',
           '13.250.37.103:4771', '3.72.86.226:13808', '13.250.46.50:4358', '13.213.67.125:4163', '13.250.46.50:4354',
           '3.72.86.226:13878', '3.72.86.226:13860', '175.41.175.240:14698', '3.93.195.111:14490', '13.250.37.103:4773',
           '13.250.37.103:4818', '13.213.67.125:4179', '13.250.46.50:4389', '3.72.86.226:13815', '3.93.195.111:14530',
           '13.213.67.125:4154', '175.41.175.240:14708', '175.41.175.240:14696', '3.93.195.111:14486',
           '13.250.46.50:4377', '13.250.37.103:4784', '54.169.37.186:16554', '3.93.195.111:14513', '3.72.86.226:13864',
           '54.169.37.186:16567', '3.72.86.226:13814', '13.250.37.103:4775', '13.250.37.103:4772', '3.72.86.226:13874',
           '13.250.46.50:4369', '175.41.175.240:14709', '3.72.86.226:13846', '13.213.67.125:4130', '3.72.86.226:13876',
           '13.250.37.103:4762', '175.41.175.240:14710', '54.169.37.186:16561', '13.250.37.103:4816',
           '13.250.46.50:4340', '3.72.86.226:13843', '13.213.67.125:4159', '3.72.86.226:13854', '3.93.195.111:14493',
           '13.250.46.50:4341', '3.72.86.226:13799', '175.41.175.240:14701', '175.41.175.240:14706',
           '3.72.86.226:13868', '3.72.86.226:13856', '13.250.37.103:4804', '3.72.86.226:13822', '3.93.195.111:14501',
           '13.213.67.125:4134', '3.72.86.226:13820', '13.250.37.103:4796', '3.72.86.226:13858', '13.250.46.50:4372',
           '3.93.195.111:14519', '3.93.195.111:14491', '3.93.195.111:14522', '13.213.67.125:4156', '13.250.46.50:4357',
           '3.93.195.111:14492', '3.93.195.111:14488', '3.93.195.111:14517', '13.250.46.50:4359', '3.72.86.226:13817',
           '13.250.37.103:4802', '13.250.46.50:4334', '13.213.67.125:4145', '3.72.86.226:13872', '54.169.37.186:16548',
           '3.72.86.226:13867', '13.250.46.50:4378', '3.72.86.226:13797', '3.72.86.226:13869', '13.213.67.125:4140',
           '3.72.86.226:13810', '13.250.37.103:4803', '13.213.67.125:4137', '13.250.37.103:4811', '13.250.46.50:4356',
           '13.250.37.103:4800', '3.72.86.226:13836', '13.213.67.125:4135', '175.41.175.240:14716',
           '175.41.175.240:14711', '3.93.195.111:14531', '3.72.86.226:13803', '13.213.67.125:4171',
           '13.213.67.125:4153', '3.93.195.111:14512', '13.213.67.125:4181', '54.169.37.186:16556',
           '3.93.195.111:14500', '54.169.37.186:16570', '3.93.195.111:14534', '13.213.67.125:4152',
           '54.169.37.186:16545', '13.213.67.125:4158', '13.213.67.125:4148', '13.250.46.50:4364', '13.250.46.50:4337',
           '13.213.67.125:4126', '13.250.46.50:4376', '13.250.46.50:4363', '54.169.37.186:16557', '13.250.37.103:4776',
           '13.250.46.50:4375', '13.213.67.125:4151', '13.250.37.103:4794', '13.250.46.50:4381', '13.250.37.103:4765',
           '13.213.67.125:4133', '54.169.37.186:16551', '3.72.86.226:13805', '3.93.195.111:14518', '3.72.86.226:13834',
           '3.72.86.226:13828', '13.250.46.50:4360', '13.250.37.103:4820', '13.250.46.50:4338', '3.93.195.111:14498',
           '13.250.46.50:4351', '13.213.67.125:4128', '3.72.86.226:13855', '3.72.86.226:13883', '13.213.67.125:4144',
           '3.93.195.111:14535', '13.213.67.125:4136', '3.72.86.226:13882', '3.93.195.111:14484', '3.93.195.111:14509',
           '3.93.195.111:14510', '13.250.46.50:4383', '13.250.46.50:4380', '13.250.37.103:4763', '175.41.175.240:14707',
           '13.250.46.50:4339', '13.250.37.103:4819', '3.93.195.111:14494', '3.72.86.226:13840', '3.72.86.226:13824',
           '13.250.37.103:4783', '3.72.86.226:13826', '13.213.67.125:4129', '13.250.46.50:4373', '54.169.37.186:16569',
           '54.169.37.186:16552', '3.72.86.226:13809', '13.250.46.50:4353', '3.72.86.226:13861', '13.250.37.103:4777',
           '3.93.195.111:14521', '54.169.37.186:16558', '13.250.37.103:4781', '13.250.46.50:4348',
           '175.41.175.240:14725', '3.72.86.226:13857', '3.72.86.226:13881', '3.72.86.226:13806', '13.213.67.125:4132',
           '3.72.86.226:13825', '3.72.86.226:13823', '54.169.37.186:16566', '13.250.37.103:4789',
           '175.41.175.240:14697', '175.41.175.240:14702', '13.213.67.125:4157', '13.250.37.103:4798',
           '3.72.86.226:13870', '13.213.67.125:4165', '3.72.86.226:13852', '13.250.46.50:4370', '175.41.175.240:14717',
           '13.250.46.50:4361', '3.93.195.111:14523', '175.41.175.240:14720', '13.250.46.50:4335', '3.93.195.111:14514',
           '3.72.86.226:13812', '3.72.86.226:13821', '3.72.86.226:13818', '3.93.195.111:14495', '13.213.67.125:4176',
           '3.72.86.226:13838', '13.213.67.125:4142', '13.213.67.125:4122', '3.93.195.111:14539', '54.169.37.186:16571',
           '13.250.46.50:4388', '3.72.86.226:13842', '13.213.67.125:4170', '54.169.37.186:16555', '3.72.86.226:13839',
           '13.250.37.103:4764', '3.72.86.226:13849', '13.250.46.50:4342', '13.250.37.103:4805', '54.169.37.186:16550',
           '13.250.46.50:4392', '175.41.175.240:14699', '13.213.67.125:4138', '13.250.37.103:4807', '3.72.86.226:13877',
           '3.72.86.226:13859', '175.41.175.240:14722', '54.169.37.186:16568', '13.250.46.50:4374', '13.250.46.50:4382',
           '13.250.37.103:4761', '3.72.86.226:13829', '3.72.86.226:13800', '175.41.175.240:14712', '3.72.86.226:13850',
           '3.93.195.111:14526', '54.169.37.186:16574', '13.250.46.50:4385', '3.93.195.111:14525', '13.250.37.103:4770',
           '13.250.37.103:4795', '13.213.67.125:4162', '13.250.37.103:4797', '3.72.86.226:13844', '3.72.86.226:13837',
           '13.213.67.125:4172', '175.41.175.240:14719', '13.250.46.50:4347', '3.93.195.111:14524',
           '3.93.195.111:14529', '13.250.37.103:4788', '13.250.37.103:4767', '13.250.46.50:4365', '13.213.67.125:4147',
           '13.250.37.103:4809', '3.72.86.226:13798', '3.72.86.226:13880', '13.213.67.125:4164', '13.250.46.50:4391',
           '3.72.86.226:13802', '3.93.195.111:14541', '13.250.37.103:4812', '13.250.46.50:4336', '54.169.37.186:16573',
           '54.169.37.186:16553', '13.250.46.50:4350', '13.213.67.125:4155', '3.72.86.226:13835',
           '175.41.175.240:14721', '54.169.37.186:16562', '13.213.67.125:4149', '3.93.195.111:14485',
           '3.72.86.226:13811', '13.213.67.125:4173', '3.72.86.226:13853', '3.72.86.226:13827', '13.250.37.103:4814',
           '3.93.195.111:14506', '13.213.67.125:4174', '3.72.86.226:13845', '3.93.195.111:14515', '13.213.67.125:4143',
           '13.213.67.125:4127', '54.169.37.186:16563', '13.250.46.50:4346', '54.169.37.186:16546', '3.72.86.226:13819',
           '13.213.67.125:4146', '3.93.195.111:14503', '13.250.46.50:4390', '3.72.86.226:13795', '54.169.37.186:16559',
           '175.41.175.240:14700', '3.93.195.111:14532', '175.41.175.240:14715', '13.250.46.50:4343',
           '13.213.67.125:4168', '3.72.86.226:13841', '13.213.67.125:4169', '13.213.67.125:4178', '3.72.86.226:13816',
           '13.250.46.50:4384', '3.93.195.111:14537', '13.213.67.125:4131', '175.41.175.240:14713', '13.250.46.50:4371',
           '13.250.37.103:4787', '3.72.86.226:13862', '13.250.46.50:4379', '3.93.195.111:14536', '13.250.37.103:4768',
           '3.72.86.226:13873', '175.41.175.240:14705', '3.72.86.226:13813', '3.72.86.226:13863', '3.93.195.111:14504',
           '13.250.37.103:4790', '13.250.46.50:4387', '13.213.67.125:4175', '13.250.46.50:4352', '3.93.195.111:14497',
           '54.169.37.186:16572', '3.72.86.226:13801', '3.93.195.111:14496', '13.250.37.103:4779', '13.250.46.50:4349',
           '175.41.175.240:14723', '3.93.195.111:14508', '13.250.37.103:4782', '3.72.86.226:13833', '13.250.46.50:4362',
           '13.250.37.103:4769', '3.72.86.226:13865', '3.72.86.226:13848', '3.93.195.111:14511', '175.41.175.240:14718',
           '3.93.195.111:14489', '3.72.86.226:13884', '3.93.195.111:14487', '13.213.67.125:4141', '13.250.37.103:4766',
           '3.72.86.226:13804', '3.93.195.111:14507', '13.250.46.50:4386', '3.72.86.226:13875', '3.93.195.111:14527',
           '54.169.37.186:16549', '3.72.86.226:13851', '3.72.86.226:13830']
infos = []


def run(page_one, num) -> None:
    print('page', page_one)
    page_one.wait_for_timeout(random.randint(3, 5))
    page_one.locator('//*[@id="root"]/div/div[2]/div/div[4]/div/div[1]/div[%s]' % num).click()
    with page_one.expect_popup() as popup_info:
        page1 = popup_info.value
    page1.wait_for_timeout(random.randint(5, 8))
    try:
        detail_box_title = page1.locator(
            '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div').inner_text()
    except Exception as e:
        print('error %s' % e)
        detail_box_title = page1.locator(
            '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/ul/li[3]/span[2]').inner_text()
    property_item = page1.evaluate('''
    a = function() {
    ths=document.getElementsByClassName("property-item-title")
    tds=document.getElementsByClassName("property-item-value")
    kv={}
    for (i=0;i<ths.length;i++){
        kv[ths[i].innerText]=tds[i].innerText
    }
    return kv
    }
            ''')
    try:
        product_name = page1.evaluate('document.getElementsByClassName("product-name")[0].innerText')
    except:
        product_name = page1.evaluate('document.getElementsByClassName("product-info-title")[0].innerText')
    try:
        code_value = page1.locator(
            '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/span[2]').inner_text()
    except:
        code_value = page1.evaluate('document.getElementsByClassName("product-code-value")[0].innerText')
    try:
        price_now = page1.evaluate('document.getElementsByClassName("price-now")[0].innerText')
    except:
        price_now = page1.locator(
            '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div').inner_text()
    try:
        promotion_item = page1.evaluate(
            'document.getElementsByClassName("promotion-item-wrap")[0].innerText').replace('\n', ' ')
    except:
        promotion_item = page1.locator(
            '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]').inner_text().replace('\n',
                                                                                                             ' ')
    result_info = {
        "detail-box-title": detail_box_title,
        "product-name": product_name,
        "product-code-value": code_value,
        "price-now": price_now,
        "promotion-item": promotion_item,
        "property-item": property_item
    }
    time.sleep(random.randint(5, 10))
    page1.wait_for_timeout(random.randint(500, 1500))
    page1.close()
    infos.append(result_info)

    print(len(infos), infos[len(infos) - 1].get('product-name'))
    with open("D:/Desktop/cdf-%s.json" % (time.strftime('%Y%m%d%H', time.localtime())), "w",
              encoding='utf-8') as obj:
        json.dump(infos, obj)


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.cdfgsanya.com/product-list.html?sw=%E8%B5%84%E7%94%9F%E5%A0%82")
    for p in page_num:
        for n in range(p):
            run(page, n)
        page.locator("text=下一页").click()
