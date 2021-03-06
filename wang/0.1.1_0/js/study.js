// Generated by CoffeeScript 2.3.1
(function() {
  console.log("this is translate_demo_ver 2.js");

  $(function() {
    var getWord, hotpoor_translate, hotpoor_translate_save, mouse_move_x, mouse_move_y, mouse_x, mouse_y, translate_content_card_move, translate_content_card_move_x, translate_content_card_move_y;
    hotpoor_translate_save = null;
    hotpoor_translate = function(content, fromLan, toLan) {
      clearTimeout(hotpoor_translate_save);
      return hotpoor_translate_save = setTimeout(function() {
        var content_result;
        content_result = "";
        $("#translate_content_card_content_aim").empty();
        $("#translate_content_card_move_title").text("翻译中·Translating...");
        return $.ajax({
          url: "https://www.hotpoor.com/api/baiduai/translate",
          data: {
            content: content,
            lan: fromLan,
            to: toLan
          },
          dataType: 'json',
          type: 'POST',
          success: function(data) {
            var content_results, i, j, len, len1, ref, result, result_i;
            console.log(data);
            if (data.result != null) {
              ref = data.result;
              for (i = 0, len = ref.length; i < len; i++) {
                result_i = ref[i];
                content_results = result_i["trans_result"];
                for (j = 0, len1 = content_results.length; j < len1; j++) {
                  result = content_results[j];
                  content_result = `${content_result}${result["dst"]}\n`;
                }
                $("#translate_content_card_content_aim").val(content_result);
              }
            }
            return $("#translate_content_card_move_title").text("翻译 · Translate");
          },
          error: function(data) {
            console.log(data);
            return $("#translate_content_card_move_title").text("翻译 · Translate");
          }
        });
      }, 300);
    };
    $("body").append("<div id=\"translate_content_card\">\n    <div id=\"translate_content_card_move\">\n        <img src=\"https://www.hotpoor.com/static/img/translate.png\">\n    </div>\n    <div id=\"translate_content_card_tools\" style=\"display:none\"></div>\n    <div id=\"translate_content_card_content\">\n        <textarea id=\"translate_content_card_content_aim\"></textarea>\n    </div>          \n</div>");
    translate_content_card_move = false;
    translate_content_card_move_x = 0;
    translate_content_card_move_y = 0;
    mouse_x = null;
    mouse_y = null;
    mouse_move_x = null;
    mouse_move_y = null;
    $("body").on("mousedown", "#translate_content_card_move", function(e) {
      e.stopPropagation();
      e.preventDefault();
      translate_content_card_move = true;
      translate_content_card_move_x = parseInt($("#translate_content_card").css("left"));
      translate_content_card_move_y = parseInt($("#translate_content_card").css("top"));
      mouse_x = e.clientX;
      return mouse_y = e.clientY;
    });
    $(window).on("mousemove", function(e) {
      var move_value_x, move_value_y;
      if (translate_content_card_move) {
        if (e.which) {
          e.preventDefault();
          e.stopPropagation();
          mouse_move_x = e.clientX;
          mouse_move_y = e.clientY;
          move_value_x = mouse_move_x - mouse_x;
          move_value_y = mouse_move_y - mouse_y;
          return $("#translate_content_card").css({
            "left": (translate_content_card_move_x + move_value_x) + "px",
            "top": (translate_content_card_move_y + move_value_y) + "px"
          });
        } else {
          return translate_content_card_move = false;
        }
      }
    });
    getWord = function() {
      var word;
      word = window.getSelection ? window.getSelection() : document.selection.createRange().text;
      return word;
    };
    return $(window).on("mouseup", function(e) {
      var translate_content;
      translate_content_card_move = false;
      translate_content = getWord().toString();
      if (translate_content.length > 0) {
        return hotpoor_translate(translate_content, "en", "zh");
      }
    });
  });

}).call(this);
