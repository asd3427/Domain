#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: teatt.py
@time: 2020/5/11 下午 07:59
@desc:
'''

datas = {
    "c_1_1": {
        "image_url": "\/teamwork\/img\/tea_menu\/Refreshing_can_Sijichun.jpg",
        "title": "不知春",
        "text": "冬茶與春茶間的四季春，飄散濃郁的梔子花香。",
        "price": "880 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Refreshing_can_Sijichun.jpg",
        "about": {
            "name": "品名：不知春",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：不知春 200g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_1_2": {
        "image_url": "\/teamwork\/img\/tea_menu\/Refreshing_can_Alishan_jing.jpg",
        "title": "阿里山金萱",
        "text": "金萱樹種特有的奶糖香，觸動味蕾的驚喜口感。",
        "price": "980 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Refreshing_Alishan_jing.jpg",
        "about": {
            "name": "品名：阿里山金萱",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：阿里山金萱 200g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_1_3": {
        "image_url": "\/teamwork\/img\/tea_menu\/Refreshing_can_Alishan_oo.jpg",
        "title": "清香阿里山烏龍",
        "text": "淡雅的花香和柔順的甘甜，品味高山茶迴盪口中的芬芳。",
        "price": "1380 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Refreshing_Alishan_oo.jpg",
        "about": {
            "name": "品名：清香阿里山烏龍",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：清香阿里山烏龍 200g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_1_4": {
        "image_url": "\/teamwork\/img\/tea_menu\/Refreshing_can_Shanlinsi.jpg",
        "title": "清香杉林溪烏龍",
        "text": "原始杉木林造就獨特的山頭氣，蘭花香中帶有木質基調的醇厚。",
        "price": "1980 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Refreshing_Shanlinsi.jpg",
        "about": {
            "name": "品名：清香杉林溪烏龍",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：清香杉林溪烏龍 200g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_2_1": {
        "image_url": "\/teamwork\/img\/tea_menu\/Roasted_can_LR_DongDing_oo.jpg",
        "title": "輕焙凍頂烏龍",
        "text": "交織茶香和蜜香古早味，是記憶中的經典好味道。",
        "price": "980 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Roasted_LR_DongDing_oo.jpg",
        "about": {
            "name": "品名：輕焙凍頂烏龍",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：輕焙凍頂烏龍 200g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_2_2": {
        "image_url": "\/teamwork\/img\/tea_menu\/Roasted_can_LR_Alishan_oo.jpg",
        "title": "輕焙阿里山烏龍",
        "text": "經文火烘焙的阿里山烏龍，轉化出高山茶內斂的花果甜香。",
        "price": "1380 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Roasted_LR_Alishan_oo.jpg",
        "about": {
            "name": "品名：輕焙阿里山烏龍",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：輕焙阿里山烏龍 200g+_0.3g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_2_3": {
        "image_url": "\/teamwork\/img\/tea_menu\/Roasted_can_LR_Shanlinsi.jpg",
        "title": "輕焙杉林溪烏龍",
        "text": "獨家烘焙法引出無瑕的細緻蜜味，是京盛宇輕烘焙茶種的自信之作。",
        "price": "1980 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Roasted_LR_Shanlinsi.jpg",
        "about": {
            "name": "品名：輕焙杉林溪烏龍",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：輕焙杉林溪烏龍 200g+_0.3g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_2_4": {
        "image_url": "\/teamwork\/img\/tea_menu\/Roasted_can_Shanlinsi.jpg",
        "title": "深焙杉林溪烏龍",
        "text": "琥珀色的茶湯飄逸濃郁焦香，濃烈的口感保有成熟的甘味。",
        "price": "1980 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Roasted_Shanlinsi.jpg",
        "about": {
            "name": "品名：深焙杉林溪烏龍",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：深焙杉林溪烏龍 200g+_0.3g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_3_1": {
        "image_url": "\/teamwork\/img\/tea_menu\/Special_can_Jasmine.jpg",
        "title": "白毫茉莉",
        "text": "稀有珍貴的品種「白毛猴」，與茉莉花「窨製」夢幻般的香甜口感。",
        "price": "880 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Special_Jasmine.jpg",
        "about": {
            "name": "品名：白毫茉莉",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：白毫茉莉 200g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_3_2": {
        "image_url": "\/teamwork\/img\/tea_menu\/Special_can_WunShan.jpg",
        "title": "桂香包種",
        "text": "細膩精湛的揉捻製茶工藝，飄逸的桂花香融合山林的自然氣息。",
        "price": "680 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Special_WunShan.jpg",
        "about": {
            "name": "品名：桂香包種",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：桂香包種 100g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_3_3": {
        "image_url": "\/teamwork\/img\/tea_menu\/Special_can_LR_WunShan.jpg",
        "title": "穀香包種",
        "text": "包種茶經烘焙轉化的穀香，品味樸實怡人的大地氣息。",
        "price": "680 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Special_LR_WunShan.jpg",
        "about": {
            "name": "品名：穀香包種",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：不知春200g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_3_4": {
        "image_url": "\/teamwork\/img\/tea_menu\/Special_can_Taiwanese_black.jpg",
        "title": "高山小葉種紅茶",
        "text": "迷人的柑橘香和絲綢般的口感，是京盛宇人氣首選的茶品。",
        "price": "980 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Special_Taiwanese_black.jpg",
        "about": {
            "name": "品名：高山小葉種紅茶",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：高山小茶種紅茶 100g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_4_1": {
        "image_url": "\/teamwork\/img\/tea_menu\/Aged_can_Taiwanese_oo.jpg",
        "title": "二十年老烏龍",
        "text": "豐富和諧的味覺層次，品味往昔的自然與人文。",
        "price": "1780 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Aged_Taiwanese_oo.jpg",
        "about": {
            "name": "品名：二十年老烏龍",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：二十年老烏龍 150g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_4_2": {
        "image_url": "\/teamwork\/img\/tea_menu\/Aged_can_TieGuanYin.jpg",
        "title": "窖藏鐵觀音",
        "text": "珍貴稀少的鐵觀音老茶，酸韻豐沛紮實。",
        "price": "1980 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Aged_TieGuanYin.jpg",
        "about": {
            "name": "品名：窖藏鐵觀音",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：窖藏鐵觀音 150g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    },
    "c_4_3": {
        "image_url": "\/teamwork\/img\/tea_menu\/Aged_can_DongDing_oo.jpg",
        "title": "窖藏老凍頂",
        "text": "未經覆焙的凍頂老茶，亮黃的茶湯閃耀台灣茶的昨日光輝。",
        "price": "2480 NTD",
        "image_url2": "\/teamwork\/img\/tea_menu\/Aged_DongDing_oo.jpg",
        "about": {
            "name": "品名：窖藏老凍頂",
            "loc": "茶葉產地：台灣",
            "spe": "規格：鋁箔真空包裝",
            "weight": "淨重：窖藏老凍頂 150g",
            "date": "有效日期：如包裝所示（年/月/日）",
            "date2": "保存期限：2年",
            "other1": "保存條件：置於乾燥陰涼處，開封後請儘快沖泡飲用。",
            "other2": "安心宣言：本產品已投保三千萬產品責任險，並通過SGS檢驗合格。"
        }
    }

}

for i in range(1,5):
    ids = 'c_1_{}'.format(i)
    print(datas[ids])

    $.ajax({
               url: "product_json.json", // json檔案位置
    type: "GET", // 請求方式為get
    dataType: "json", // 返回資料格式為json
    success: function(datas)
    { // 請求成功完成後要執行的方法
    var
    product = $(".products").children()
    for (let i = 0; i < 4; i++) {
        let ids = product[i].id
    $('#' + product[i].id).click(function () {
    $('#about_product_list').hide()
    $('.detail').html(`
    < div


    class ="row justify-content-left  about_padding product_list" >
\t\t\t\t\t < div


class ="product_list_1" > 清香系列 < / div >

\t\t\t\t\t < div


class ="product_list_2" > 熟香系列 < / div >

\t\t\t\t\t < div


class ="product_list_3" > 特殊風味 < / div >

\t\t\t\t\t < div


class ="product_list_4" > 窖藏系列 < / div >

\t\t\t\t < / div >
\t\t\t\t < div


class ="product_top row justify-content-left   product_list" >

\t\t\t\t\t < div


class ="detail_product row justify-content-center product_list"

\t\t\t\t\t
style = "background-image: url(${datas[ids].image_url}) " >
\t\t\t\t\t < / div >
\t\t\t\t\t < div


class ="detail_about justify-content-right " >

\t\t\t\t\t < ul >
\t\t\t\t\t\t < li >${datas[ids].title} < / li >
\t\t\t\t\t\t < li >${datas[ids].text} < / li >
\t\t\t\t\t\t < li >${datas[ids].price} < / li >
\t\t\t\t\t < / ul >
\t\t\t\t\t < / div >
\t\t\t\t < / div >
\t\t\t\t
\t\t\t\t < div


class ="detail_pd_img"

\t\t\t\t
style = "background-image: url(${datas[ids].image_url2})" > < / div >
\t\t\t\t < div


class ="detail_pd_text" >

\t\t\t\t\t < ul >
\t\t\t\t\t\t < li >${datas[ids].about.name} < / li >
\t\t\t\t\t\t < li >${datas[ids].about.loc} < / li >
\t\t\t\t\t\t < li >${datas[ids].about.spe} < / li >
\t\t\t\t\t\t < li >${datas[ids].about.weight} < / li >
\t\t\t\t\t\t < li >${datas[ids].about.date} < / li >
\t\t\t\t\t\t < li >${datas[ids].about.date2} < / li >
\t\t\t\t\t\t < li >${datas[ids].about.other1} < / li >
\t\t\t\t\t\t < li >${datas[ids].about.other2} < / li >
\t\t\t\t\t
\t\t\t\t\t < / ul >
\t\t\t\t < / div >

`)
$('.detail').show()

})
}

}
})
