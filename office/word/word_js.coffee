for i in color
    _html = """"""
    for j in i["font_color"]
        _html ="""#{_html }<span style="font-size:#{j["size"]/10000}px;color:rgb(#{j["color"][0]},#{j["color"][1]},#{j["color"][2]});">#{j["text"]}</span>"""
    $("#docx").append """<p>#{_html}</p>"""