# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pos_title = scrapy.Field()  # 岗位名称
    pos_address = scrapy.Field()  # 工作地址（城市）
    pos_des = scrapy.Field()  # 职位介绍
    item_condition = scrapy.Field()  # 人数
    pos_salary = scrapy.Field()  # 薪资
    base_info = scrapy.Field()  # 公司名称
    industry = scrapy.Field()  # 补充说明（所在行业分类）
    area = scrapy.Field()  # 详细地址


pass
