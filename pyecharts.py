#导出模块
from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.globals import SymbolType
#定义函数
c = (
        Liquid()
        .add("lq", [0.6, 0.7, 0.8], is_outline_show=False)
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-无边框"))
    )
c.render('1')#定格，括号内为文件名，注意单引号说明文件名省html后缀，双引号文件名，生成后缀，也可以加入路径，默认为代码.py所在的路径或文件夹。
