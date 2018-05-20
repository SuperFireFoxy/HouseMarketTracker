# HouseMarketTracker
A simple implement of Scrapy spider to track house market

# Testing Data

+ DataBase: MongoDB
+ DB-Name: house_info_db_2018-05-20
+ IP: 65.49.202.235
+ Port: 27017
+ UserName: dba1
+ Password: test

# Single Item Demo

```json
{
    "_id" : "黄龙溪谷:https://cd.fang.lianjia.com/loupan/p_hlxgaataf/",
    "house_name" : "黄龙溪谷",
    "home_page" : "https://cd.fang.lianjia.com/loupan/p_hlxgaataf/",
    "house_detail" : {
        "basic_info" : {
            "物业类型：" : "别墅",
            "参考价格：" : "均价 1300万/套",
            "项目特色：" : "低密度 复式",
            "区域位置：" : "成都-天府新区南区",
            "楼盘地址：" : "剑南大道南延线黄龙大道四段(黄龙古镇旁)",
            "售楼处地址：" : "剑南大道南延线黄龙大道四段(黄龙古镇旁)（接待时间 9:00 - 18:00）",
            "开发商：" : "四川万融房地产开发有限公司"
        },
        "opening_info" : [ 
            {
                "开盘时间" : "2016年09月30日",
                "售卖楼栋" : "三期279栋,三期340栋,三期81栋,三期89栋,三期62栋,三期415栋,三期379栋,三期338栋,三期293栋,三期412栋,三期335栋,三期22栋,三期7栋,三期27栋,三期10栋,三期21栋,三期138栋6号,三期129栋,三期167栋,三期172栋,三期179栋,三期257栋,二期422栋,三期69栋,三期189栋,三期197栋,三期249栋,三期181栋,三期191栋,三期238栋,三期203栋,三期183栋,三期346栋,三期175栋,三期40栋,三期169号,三期170栋,三期-185栋,三期-379栋,三期-231栋,三期-170栋,三期146栋,三期329栋,一期45栋,三期239栋,三期235栋,三期347栋,三期241栋,三期259栋,三期331栋,三期206栋,三期361栋,三期385栋,三期222栋,三期226栋",
                "交房时间" : "2018年10月31日",
                "分期信息" : "第1期：三期279栋,三期340栋,三期81栋,三期89栋,三期62栋,三期415栋,三期379栋,三期338栋,三期293栋,三期412栋,三期335栋,三期22栋,三期7栋,三期27栋,三期10栋,三期21栋,三期138栋6号,三期129栋,三期167栋,三期172栋,三期179栋,三期257栋,二期422栋,三期69栋,三期189栋,三期197栋,三期249栋,三期181栋,三期191栋,三期238栋,三期203栋,三期183栋,三期346栋,三期175栋,三期40栋,三期169号,三期170栋,三期-185栋,三期-379栋,三期-231栋,三期-170栋,三期146栋,三期329栋,一期45栋,三期239栋,三期235栋,三期347栋,三期241栋,三期259栋,三期331栋,三期206栋,三期361栋,三期385栋,三期222栋,三期226栋"
            }
        ],
        "plan_info" : {
            "建筑类型：" : "塔板结合",
            "绿化率：" : "50.00",
            "占地面积：" : "8,000,000㎡",
            "容积率：" : "0.42",
            "建筑面积：" : "2,000,000㎡",
            "物业类型：" : "别墅",
            "规划户数：" : "100",
            "产权年限：" : "70年",
            "楼盘户型：" : {
                "全部(4)" : "/loupan/p_hlxgaataf/huxingtu",
                "五居室(3)" : "/loupan/p_hlxgaataf/huxingtu/5ju/",
                "四居室(1)" : "/loupan/p_hlxgaataf/huxingtu/4ju/"
            }
        },
        "pre_sales_info" : [ 
            {
                "预售许可证" : "2016)房预售证第010号",
                "发证时间" : "2016-07-07",
                "绑定楼栋" : "三期279栋,三期340栋,三期81栋,三期89栋,三期62栋,三期415栋,三期379栋,三期338栋,三期293栋,三期412栋,一期279栋,三期335栋,三期22栋,三期7栋,三期27栋,三期10栋,三期21栋,三期138栋6号,三期129栋,三期167栋,三期172栋,三期179栋,三期257栋,三期69栋,三期189栋,三期197栋,三期249栋,三期181栋,三期191栋,三期238栋,三期203栋,三期183栋,三期346栋,三期175栋,三期40栋,三期169号,三期331栋,三期206栋,三期361栋,三期-365栋,三期222栋,三期226栋"
            }, 
            {
                "预售许可证" : "2014)房预售证第035号",
                "发证时间" : "2014-12-11",
                "绑定楼栋" : "二期140栋,二期422栋"
            }, 
            {
                "预售许可证" : "2014)房预售证第020号",
                "发证时间" : "2014-07-30",
                "绑定楼栋" : "一期68-1栋,一期81栋,一期87栋,一期86栋,一期88栋,一期89栋,一期57栋,一期68-2栋"
            }, 
            {
                "预售许可证" : "2015)房预售证第023号",
                "发证时间" : "2015-11-07",
                "绑定楼栋" : "二期377栋,二期282栋"
            }, 
            {
                "预售许可证" : "2016)房预售证第005号",
                "发证时间" : "2016-05-07",
                "绑定楼栋" : "二期411栋,二期417栋"
            }, 
            {
                "预售许可证" : "2014)房预售证第020号",
                "发证时间" : "2014-08-03",
                "绑定楼栋" : "一期100栋,三期170栋,三期-185栋,三期-379栋,三期-231栋,三期-170栋,三期146栋,三期329栋,一期45栋,三期239栋,三期235栋,三期347栋,三期241栋,三期259栋,一期99－2栋,三期385栋,三期220栋,三期360栋"
            }
        ],
        "facility_info" : {
            "物业公司：" : "成都卓望嘉物业服务有限公司",
            "车位配比：" : "1:1",
            "物业费：" : "5.9元/m²/月",
            "供暖方式：" : "自采暖",
            "供水方式：" : "民水",
            "供电方式：" : "民电",
            "车位：" : "地下车位数1200",
            "周边规划：" : {
                "地铁：" : {},
                "教育设施：" : {
                    "四川省旅游学校" : "成都市双流区黄龙大道四段2681号",
                    "四川省旅游学校(黄龙溪校区)-美食学院" : "四川省成都市双流区黄龙大道四段2681",
                    "黄龙溪学校" : "四川省成都市双流区黄龙溪镇黄龙社区1组201号",
                    "嘉禾小学" : "公黄路附近",
                    "成都艺术职业学院(黄龙溪校区)" : "相君街2号",
                    "双流区黄龙溪幼儿园" : "黄龙溪镇黄龙大道4段2880号",
                    "成都中信职业技术学校" : "成都市双流区川龙街43号",
                    "双流县黄龙溪镇老年大学" : "四川省成都市双流区7组205",
                    "双流区黄龙溪镇红太阳幼儿园" : "四川省成都市双流区黄龙大道四段2841",
                    "黄龙溪文化艺术研究院" : "成都市双流区黄龙溪镇正街27号"
                },
                "医院：" : {
                    "双流县黄龙溪镇公立卫生院" : "成都市双流区黄龙大道四段2840号"
                },
                "购物：" : {
                    "红旗超市(黄龙溪分场)" : "双流区镇龙街86号",
                    "果味王草莓自摘园" : "双黄路",
                    "红旗超市(双流黄龙溪二分场)" : "黄龙溪景溪路黄龙溪古镇市场1层10-12号",
                    "大狗的小院" : "黄龙溪镇新街48号",
                    "黄龙溪杨大姐山腊肉专卖" : "黄龙溪古镇仿清街17号",
                    "锦色蜀绣" : "成都市双流区镇龙街51号附3号",
                    "小卖部" : "成都市双流区",
                    "龙泉宝剑" : "四川省成都市双流区复兴街25",
                    "顺路渔具" : "四川省成都市双流区中山路20",
                    "葫芦丝" : "镇龙街74号"
                },
                "公园：" : {},
                "其他：" : {}
            }
        }
    },
    "house_layout" : [ 
        {
            "img_src" : "https://image1.ljcdn.com/hdic-frame/5bc15256-7e3b-4f5e-88e0-73b7dda29c12.jpg.1000x.jpg",
            "layout_type_name" : "C2户型",
            "layout_type" : "5室3厅4卫 ",
            "construction_area" : "建面 240m²",
            "sales_status" : "售罄",
            "layout_price" : "均价 1300 万/套",
            "last_update_time" : "最近更新时间：05月09日",
            "户型解读：" : "三层设计，家中成员休息互不影响；客厅的双层挑空提升了采光率和空间感",
            "tags" : [ 
                "阳台", 
                "主卧带卫", 
                "多卫", 
                "明厨"
            ]
        }, 
        {
            "img_src" : "https://image1.ljcdn.com/hdic-frame/90e3854b-1179-4bd9-9b97-6894d0f4b5b8.jpg.1000x.jpg",
            "layout_type_name" : "F2",
            "layout_type" : "5室2厅4卫 ",
            "construction_area" : "建面 292m²",
            "sales_status" : "在售",
            "layout_price" : "均价 1300 万/套",
            "last_update_time" : "最近更新时间：4天前",
            "户型解读：" : "三层设计，家中成员休息互不影响；客厅的双层挑空提升了采光率和空间感。",
            "tags" : [ 
                "全明格局", 
                "花园", 
                "干湿分离", 
                "主卧带卫"
            ]
        }, 
        {
            "img_src" : "https://image1.ljcdn.com/hdic-frame/a6542c86-1a11-4caf-889c-cc0ce475e985.jpg.1000x.jpg",
            "layout_type_name" : "D1",
            "layout_type" : "5室2厅5卫 ",
            "construction_area" : "建面 195m²",
            "sales_status" : "售罄",
            "layout_price" : "均价 620 万/套",
            "last_update_time" : "最近更新时间：05月10日",
            "户型解读：" : "三层设计，家中成员休息互不影响；客厅的双层挑空提升了采光率和空间感",
            "tags" : [ 
                "全明格局", 
                "露台", 
                "花园", 
                "多阳台"
            ]
        }, 
        {
            "img_src" : "https://image1.ljcdn.com/hdic-frame/d7937995-e4f6-4c7c-813f-ba3e18579353.jpg.1000x.jpg",
            "layout_type_name" : "E1",
            "layout_type" : "4室2厅4卫 ",
            "construction_area" : "建面 246m²",
            "sales_status" : "在售",
            "layout_price" : "均价 1300 万/套",
            "last_update_time" : "最近更新时间：4天前",
            "户型解读：" : "空间方正通透，居住舒适度较高，动静区分，休息不易受打扰。",
            "tags" : [ 
                "全明格局", 
                "花园", 
                "干湿分离", 
                "主卧带卫"
            ]
        }, 
        {
            "img_src" : "https://image1.ljcdn.com/hdic-frame/5bc15256-7e3b-4f5e-88e0-73b7dda29c12.jpg.1000x.jpg",
            "layout_type_name" : "C2户型",
            "layout_type" : "5室3厅4卫 ",
            "construction_area" : "建面 240m²",
            "sales_status" : "售罄",
            "layout_price" : "均价 1300 万/套",
            "last_update_time" : "最近更新时间：05月09日",
            "户型解读：" : "三层设计，家中成员休息互不影响；客厅的双层挑空提升了采光率和空间感",
            "tags" : [ 
                "阳台", 
                "主卧带卫", 
                "多卫", 
                "明厨"
            ]
        }, 
        {
            "img_src" : "https://image1.ljcdn.com/hdic-frame/d7937995-e4f6-4c7c-813f-ba3e18579353.jpg.1000x.jpg",
            "layout_type_name" : "E1",
            "layout_type" : "4室2厅4卫 ",
            "construction_area" : "建面 246m²",
            "sales_status" : "在售",
            "layout_price" : "均价 1300 万/套",
            "last_update_time" : "最近更新时间：4天前",
            "户型解读：" : "空间方正通透，居住舒适度较高，动静区分，休息不易受打扰。",
            "tags" : [ 
                "全明格局", 
                "花园", 
                "干湿分离", 
                "主卧带卫"
            ]
        }, 
        {
            "img_src" : "https://image1.ljcdn.com/hdic-frame/90e3854b-1179-4bd9-9b97-6894d0f4b5b8.jpg.1000x.jpg",
            "layout_type_name" : "F2",
            "layout_type" : "5室2厅4卫 ",
            "construction_area" : "建面 292m²",
            "sales_status" : "在售",
            "layout_price" : "均价 1300 万/套",
            "last_update_time" : "最近更新时间：4天前",
            "户型解读：" : "三层设计，家中成员休息互不影响；客厅的双层挑空提升了采光率和空间感。",
            "tags" : [ 
                "全明格局", 
                "花园", 
                "干湿分离", 
                "主卧带卫"
            ]
        }, 
        {
            "img_src" : "https://image1.ljcdn.com/hdic-frame/a6542c86-1a11-4caf-889c-cc0ce475e985.jpg.1000x.jpg",
            "layout_type_name" : "D1",
            "layout_type" : "5室2厅5卫 ",
            "construction_area" : "建面 195m²",
            "sales_status" : "售罄",
            "layout_price" : "均价 620 万/套",
            "last_update_time" : null,
            "户型解读：" : "三层设计，家中成员休息互不影响；客厅的双层挑空提升了采光率和空间感",
            "tags" : [ 
                "全明格局", 
                "露台", 
                "花园", 
                "多阳台"
            ]
        }
    ],
    "house_images" : {
        "样板间" : [ 
            "https://image1.ljcdn.com/hdic-resblock/087d56b3-4fe8-4ee4-96d0-6ec007ec8371.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/dcca1507-702f-4250-a910-b31167e6d09d.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/caa5a217-3fd2-45c7-9f7c-4b6a7fbecafa.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/0ce7dd58-2d28-4770-8890-e3e4318476b4.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/72e46450-5c67-46d5-9840-17a177659dd7.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/8b172fb6-e2ec-4be9-9333-8409ff6883c7.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/2b7050fb-bba9-44ae-a0ba-59c8aecd0cb6.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/b0ab57ee-46ee-41ac-802f-ddfc3bb92e07.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/69e0e29a-1909-41d5-a894-0947432d6787.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/78af5d26-eb2a-427d-804f-04631569e703.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/45f7ea52-98ad-4208-bf01-d3ffcb715317.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/de5d7bdd-5cbc-4c7a-bf9a-0cb0f0258739.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/0f636e76-4b5f-4dbe-b136-3c2d1ddb5e6c.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/75bfda17-609e-4f92-9ff2-20ee154f9b26.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/a4d46561-9dd5-48f3-895d-62a99cd98cce.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/9769eb81-6bbe-4ce5-883e-e3ff546922cf.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/19bf847a-a09b-412a-97f3-08b3ca56a927.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/a3604107-ab6a-4907-a606-93b3a62f1903.jpg.1000x.jpg"
        ],
        "效果图" : [ 
            "https://image1.ljcdn.com/hdic-resblock/fe00ea98-a29f-41e6-895d-bd47b1104217.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/d0397d64-bc06-4e0b-ba58-a1eef8bcebbe.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/1e90835c-514d-4bc2-9e82-272a2fe2e88b.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/dd522616-6999-480c-81de-a238f4d9be4f.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/0efb0673-abb3-4587-ab5e-c505273f5a97.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/fe1f2387-1932-48e9-be9c-f987a15ddbdf.jpg.1000x.jpg"
        ],
        "实景图" : [ 
            "https://image1.ljcdn.com/hdic-resblock/01f01cdd-7f77-4e68-96cb-55e7eb6a30c4.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/ae5583ba-480f-471b-b794-ba77cf56a7e0.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/ab21c673-def7-42c5-8cbe-a9713a27f311.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/6d29ac65-fd32-431d-92f4-b725086cdc1c.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/22b076ea-3432-423b-b664-a38450250954.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/8f8ff6c3-05e4-4259-b06b-4153244d12e5.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/841d0111-a219-40f1-9a90-ed4fac27649e.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/8ad159a0-e862-4d72-add2-8a3194174f3f.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/a842890c-1ade-41c9-94b0-4367a5cac87f.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/d43bff8e-c67e-4b6a-ab66-4f5f92811460.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/735a6dc6-1faa-4eba-a215-2d62f3886cc0.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/08fa5a07-2df4-4cbd-91b8-81848e3c16f8.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/2cee5bab-a0a2-4c1d-90f3-0a8741a7b775.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/15babeec-7f6e-4fad-880d-e754abef846f.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/190c263a-9969-4c62-b9e1-72993a2e7cfa.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/3cc51509-ba52-4d24-8fb5-bc6b1aeeb4b4.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/98949ad8-e978-46af-9353-62d7ea46b13c.jpg.1000x.jpg"
        ],
        "小区配套" : [ 
            "https://image1.ljcdn.com/hdic-resblock/cdb09b70-74a7-4982-8954-bc187902fca6.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/938df86d-e6ed-4cbc-b4c7-dbcaf8967d49.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/7692b6aa-4c5b-4515-8aab-6792b26b71ef.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/f0e653a4-a533-4bf6-9464-42f4ac25765c.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/bc4f8132-e931-4be6-96e0-1dd522d41bca.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/44396e00-9a9d-4bc1-962a-a92440faa318.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/04857a49-21b7-4b37-b7f1-ad7644e917b2.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/89cffe2c-551c-48c9-afed-b5af8608c974.jpg.1000x.jpg"
        ],
        "项目现场" : [ 
            "https://image1.ljcdn.com/hdic-resblock/072ee033-c3e5-41d4-bf54-b8aded3fdaaa.jpg.1000x.jpg", 
            "https://image1.ljcdn.com/hdic-resblock/3a3a6558-2d9e-4104-847d-206cc3770742.jpg.1000x.jpg"
        ]
    },
    "house_comment" : {
        "用户点评" : {
            "综合评分" : "4.1分",
            "评分比例" : "高于91.5%同类新盘",
            "周边配套" : "3.7分",
            "交通方便" : "4分",
            "绿化环境" : "4.8分"
        },
        "comments" : [ 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家543天",
                "tag" : null,
                "star" : 4.0,
                "配套" : "4",
                "交通" : "3",
                "环境" : "5",
                "words" : "黄龙溪谷从名字上来说就晓得这个楼盘距离黄龙溪景区很近，从百度地图上来看，相距1公里左右，平时陪家人逛一下景区还是很惬意的，小区内部环境也很好，设计有游泳池、喷泉、人工湖、健康绿道等，非常适合休闲；但是有一个缺点就是距离成都市区有点远，到三环路天府立交约36公里，驾车需要1个小时。",
                "time" : "2017-12-13 18:09:04",
                "like" : "1"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家186天",
                "tag" : null,
                "star" : 4.0,
                "配套" : "3",
                "交通" : "4",
                "环境" : "5",
                "words" : "吊打麓山国际的牛盘，未来估计只有麓湖能与之匹敌，不过后者绝对是天价。还好之前入手小户别墅，用相对小的代价能跟这帮土豪共享私宅，也算搭上了末班车。",
                "time" : "2017-12-04 14:02:31",
                "like" : "2"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家423天",
                "tag" : null,
                "star" : 5.0,
                "配套" : "5",
                "交通" : "5",
                "环境" : "5",
                "words" : "上个月去了一趟黄龙溪玩，刚好看到了宣传广告，就直接开车过去了。房子很不错，配得上在黄龙溪的山清水秀，给人一种古朴而又新奇的感受。",
                "time" : "2017-07-28 15:03:50",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家1001天",
                "tag" : null,
                "star" : 4.0,
                "配套" : "4",
                "交通" : "4",
                "环境" : "4",
                "words" : "感觉黄龙溪谷风景区周围的旅游别墅，肯定不会差。有这么好的景区在周围，还怕没地方耍？还是可以考虑。",
                "time" : "2016-08-24 18:56:27",
                "like" : "1"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家1025天",
                "tag" : null,
                "star" : 4.0,
                "配套" : "4",
                "交通" : "4",
                "环境" : "4",
                "words" : "黄龙溪谷位置在黄龙溪古镇旁边，旅游别墅啊！剑南大道南延线也通到这里，还是可以的。考虑中。",
                "time" : "2016-08-24 15:52:50",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家5天",
                "tag" : "实看点评",
                "star" : 4.5,
                "配套" : "5",
                "交通" : "4",
                "环境" : "5",
                "words" : "楼盘很大，绿化环境也非常漂亮！比较喜欢！",
                "time" : "2018-05-15 18:53:32",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "13*******63",
                "user_life" : "使用链家498天",
                "tag" : "实看点评",
                "star" : 4.5,
                "配套" : "4",
                "交通" : "5",
                "环境" : "5",
                "words" : "产品非常好，很前唯，环境很喜欢，就是价格有点小贵",
                "time" : "2018-05-10 18:26:27",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "13*******99",
                "user_life" : "使用链家19天",
                "tag" : "实看点评",
                "star" : 5.0,
                "配套" : "5",
                "交通" : "5",
                "环境" : "5",
                "words" : "环境非常好，适合居住。",
                "time" : "2018-05-02 17:56:23",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "明净如溪",
                "user_life" : "使用链家532天",
                "tag" : "实看点评",
                "star" : 3.0,
                "配套" : "1",
                "交通" : "3",
                "环境" : "5",
                "words" : "环境超级好",
                "time" : "2018-05-01 19:40:31",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "18*******77",
                "user_life" : "使用链家144天",
                "tag" : "实看点评",
                "star" : 5.0,
                "配套" : "5",
                "交通" : "5",
                "环境" : "5",
                "words" : "环境不错，户型好！",
                "time" : "2018-04-28 15:32:44",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "15*******74",
                "user_life" : "使用链家50天",
                "tag" : "实看点评",
                "star" : 4.0,
                "配套" : "4",
                "交通" : "4",
                "环境" : "4",
                "words" : "太远啊 不咋满意",
                "time" : "2018-04-24 17:24:00",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "18*******89",
                "user_life" : "使用链家53天",
                "tag" : "实看点评",
                "star" : 5.0,
                "配套" : "5",
                "交通" : "5",
                "环境" : "5",
                "words" : "「优品道控股」与复地集团两大实力企业，划时代合力打造的世界级低密国际休闲别墅区。黄龙溪谷项目位处中国成都，国家4A级旅游景区、1700余年历史的中国十大古镇黄龙溪内。独具稀世资源，更是历代皇家庇佑之风水宝地。同时项目位属国际城南的天府新区生态宜居核心区，距城南核心及双流国际机场仅半小时车程。纯正血统，与生俱来，两大豪门萃取成都休闲文化精华，联袂VITA、RYAN YOUNG、BISCAYNE、ARTHUR HILLS四大“全美系”鼎级设计团队，凝神苛创，倾力打造中国高端国际休闲别墅住区。[1]",
                "time" : "2018-04-20 20:31:42",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "18*******55",
                "user_life" : "使用链家697天",
                "tag" : "实看点评",
                "star" : 5.0,
                "配套" : "5",
                "交通" : "5",
                "环境" : "5",
                "words" : "小区非常舒适，只是不喜欢间距",
                "time" : "2018-01-31 12:35:36",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "18*******98",
                "user_life" : "使用链家188天",
                "tag" : "实看点评",
                "star" : 5.0,
                "配套" : "5",
                "交通" : "5",
                "环境" : "5",
                "words" : "环境很好，我很喜欢，但太贵了",
                "time" : "2017-12-17 09:43:55",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家176天",
                "tag" : "实看点评",
                "star" : 5.0,
                "配套" : "5",
                "交通" : "5",
                "环境" : "5",
                "words" : "改善环境，这边真的是对的起别墅的设计！期待后面小面积的！",
                "time" : "2017-12-05 17:00:59",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家456天",
                "tag" : null,
                "star" : 3.0,
                "配套" : "2",
                "交通" : "3",
                "环境" : "5",
                "words" : "此楼盘是属于眉山彭山区！眉山彭山区！眉山彭山区！",
                "time" : "2017-11-18 01:39:54",
                "like" : "1"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家714天",
                "tag" : null,
                "star" : 2.0,
                "配套" : "1",
                "交通" : "1",
                "环境" : "4",
                "words" : "紧挨着公墓，还买那么贵。这边睡活人那边睡死人",
                "time" : "2017-10-12 05:58:01",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家543天",
                "tag" : null,
                "star" : 4.5,
                "配套" : "4",
                "交通" : "5",
                "环境" : "5",
                "words" : "前两天和闺蜜说我们家买了黄龙溪谷的房子，他们都很羡慕。现在价格不高，觉得我买对了，还跟我咨询具体情况，等着以后房子拿到装修好了再邀请朋友来玩，旁边就是黄龙溪古镇，好耍",
                "time" : "2017-07-27 14:30:49",
                "like" : "3"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家596天",
                "tag" : "实拍图",
                "star" : 4.5,
                "配套" : "4",
                "交通" : "5",
                "环境" : "5",
                "words" : "从现在住的地方开车过去大概有42公里，看房子真是一趟漫长旅程，还好黄龙溪谷值得看，不然对不起花出去的油费",
                "time" : "2017-07-26 15:47:17",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家301天",
                "tag" : null,
                "star" : 4.0,
                "配套" : "3",
                "交通" : "5",
                "环境" : "5",
                "words" : "真不知道网上那些人怎么想的，又想房子、配套、环境哪里都好，又想房子便宜，馅饼掉下来让你捡嘛？？肯定是有取有舍，黄龙溪谷这环境、价格，也算是对得起观众了",
                "time" : "2017-07-24 18:09:06",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家973天",
                "tag" : null,
                "star" : 4.5,
                "配套" : "4",
                "交通" : "5",
                "环境" : "5",
                "words" : "周边配套目前的确还不够齐全，只是现在这个价格，也不能要求太多，要是等配套都起来了，估计这个价格也买不到了，买来先晾晾",
                "time" : "2017-07-21 17:00:00",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家973天",
                "tag" : null,
                "star" : 4.0,
                "配套" : "3",
                "交通" : "4",
                "环境" : "5",
                "words" : "配套目前还不够齐全，不过现在入手价格也合适，要是再过几年，谁知道会涨到多少钱。",
                "time" : "2017-07-21 14:43:35",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家973天",
                "tag" : null,
                "star" : 3.0,
                "配套" : "3",
                "交通" : "3",
                "环境" : "4",
                "words" : "旁边就是国家4A景区黄龙溪古镇，楼盘环境确实好，绿化也做的非常好，但位置有点偏远，现在生活不方便，不知道配套什么时候才会起来",
                "time" : "2017-07-18 11:26:25",
                "like" : "1"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "18*******70",
                "user_life" : "使用链家347天",
                "tag" : "实看点评",
                "star" : 4.0,
                "配套" : "5",
                "交通" : "3",
                "环境" : "5",
                "words" : "美美哒",
                "time" : "2017-07-08 11:21:31",
                "like" : "1"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "18*******84",
                "user_life" : "使用链家960天",
                "tag" : null,
                "star" : 3.5,
                "配套" : "3",
                "交通" : "3",
                "环境" : "5",
                "words" : "位置位于黄龙溪古镇附近，里面的环境非常好，宜居！",
                "time" : "2017-05-12 10:55:12",
                "like" : "1"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "胡丹",
                "user_life" : "使用链家601天",
                "tag" : null,
                "star" : 2.0,
                "配套" : "1",
                "交通" : "1",
                "环境" : "5",
                "words" : "居然去看了这个盘 我想我是疯了。记得提前一天预约 否则不让进。虽然偏僻而且紧挨莲花公墓，但是仍然从环境服务各方面保持了别墅的水准。很美很美。值得一看。在成都到黄龙溪的路边上。",
                "time" : "2017-04-11 04:17:31",
                "like" : "0"
            }, 
            {
                "user_image" : "//s1.ljcdn.com/phoenix/static/dist/pages/pinglun/img/userpic.png?_v=20180508160207",
                "user_name" : "链家房友",
                "user_life" : "使用链家456天",
                "tag" : "实拍图",
                "star" : 4.0,
                "配套" : "3",
                "交通" : "5",
                "环境" : "5",
                "words" : "楼盘位置在未来1到2年可以说是很好的位置，发展前景巨大，是成都乃至全国别墅里面环境的第一，太美了，可以传世的大宅！",
                "time" : "2017-02-21 23:44:03",
                "like" : "1"
            }
        ]
    },
    "house_news" : [ 
        {
            "tag" : "楼盘资讯",
            "title" : "黄龙溪谷预计交房时间为2018年10月31日",
            "time" : "2018年05月18日",
            "content" : "黄龙溪谷在售三期别墅，总价1300万-3700万，优惠6个点左右，预计交房时间为2018年10月31日。",
            "link" : "/loupan/p_/dongtai/508837.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷别墅在售",
            "time" : "2018年05月17日",
            "content" : "黄龙溪谷在售三期别墅，在售E户型，建面240平，实得440平，总价1300万起；在售F户型，建面293平，实得666平，总价1300万起。",
            "link" : "/loupan/p_/dongtai/507906.html"
        }, 
        {
            "tag" : "优惠信息",
            "title" : "黄龙溪谷在售三期别墅，购房优惠6%左右",
            "time" : "2018年05月16日",
            "content" : "黄龙溪谷在售三期别墅，总价1300万-3700万，购房优惠6%左右。",
            "link" : "/loupan/p_/dongtai/506710.html"
        }, 
        {
            "tag" : "施工进度",
            "title" : "黄龙溪谷预计2018年10月31日交房",
            "time" : "2018年05月15日",
            "content" : "黄龙溪谷黄龙溪谷在售三期别墅，总价1300万~3700万，购买优惠6%左右，预计2018年10月31日交房。",
            "link" : "/loupan/p_/dongtai/503662.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷在售三期别墅",
            "time" : "2018年05月14日",
            "content" : "黄龙溪谷黄龙溪谷在售三期别墅，总价1300万-3700万/套。在售E户型：建面240平，实得440平，总价1300万起；在售F户型：建面293平，实得666平，总价1300万起。",
            "link" : "/loupan/p_/dongtai/501316.html"
        }, 
        {
            "tag" : "优惠信息",
            "title" : "黄龙溪谷购房优惠6%左右",
            "time" : "2018年05月11日",
            "content" : "黄龙溪谷在售三期别墅，总价1300万-3700万，购房优惠6%左右。",
            "link" : "/loupan/p_/dongtai/500529.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷在售三期别墅，总价1300万-3700万",
            "time" : "2018年05月10日",
            "content" : "黄龙溪谷在售三期别墅，总价1300万-3700万。\n（1）E户型，建面240平，实得440平，总价1300万起；\n（2）F户型，建面293平，实得666平，总价1300万起。",
            "link" : "/loupan/p_/dongtai/498546.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷在售三期别墅",
            "time" : "2018年05月09日",
            "content" : "黄龙溪谷黄龙溪谷在售三期别墅，总价1300万-3700万，剩余房源46套。",
            "link" : "/loupan/p_/dongtai/462407.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷在售240㎡、293㎡户型",
            "time" : "2018年05月08日",
            "content" : "黄龙溪谷在售E户型，建面240平，实得440平，总价1300万起。在售F户型，建面293平，实得666平，总价1300万起。",
            "link" : "/loupan/p_/dongtai/460296.html"
        }, 
        {
            "tag" : "优惠信息",
            "title" : "黄龙溪谷购房优惠6%左右",
            "time" : "2018年05月07日",
            "content" : "黄龙溪谷在售三期别墅，总价1300万-3700万，购房优惠6%左右。",
            "link" : "/loupan/p_/dongtai/457664.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷别墅总价1300万-3700万",
            "time" : "2018年05月04日",
            "content" : "黄龙溪谷在售E户型，建面240平，实得440平，总价1300万起，余4套；在售F户型，建面293平，实得666平，总价1300万起，余44套。",
            "link" : "/loupan/p_/dongtai/455508.html"
        }, 
        {
            "tag" : "优惠信息",
            "title" : "黄龙溪谷在售三期别墅，购买优惠补贴6%",
            "time" : "2018年05月03日",
            "content" : "黄龙溪谷在售三期别墅，建面240平，实得440平，总价1300万起；建面293平，实得666平，总价1300万起；购房优惠补贴6%。",
            "link" : "/loupan/p_/dongtai/454031.html"
        }, 
        {
            "tag" : "施工进度",
            "title" : "黄龙溪谷预计2018年10月31日交房",
            "time" : "2018年05月02日",
            "content" : "黄龙溪谷在售三期别墅，总价1300万~3700万，购买优惠6%，预计2018年10月31日交房。",
            "link" : "/loupan/p_/dongtai/452009.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷在售三期别墅，总价1300万-3700万",
            "time" : "2018年04月27日",
            "content" : "黄龙溪谷在售三期E户型，建面240平，实得440平，总价1300万起，余4套；在售F户型，建面293平，实得666平，总价1300万起，余44套。",
            "link" : "/loupan/p_/dongtai/401832.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷五一活动：野餐音乐会",
            "time" : "2018年04月26日",
            "content" : "黄龙溪谷将于4月29日-5月1日推出五一活动，针对1000万以上级别客户，举办野餐音乐聚会，链家名额有限，可免费体验。",
            "link" : "/loupan/p_/dongtai/347765.html"
        }, 
        {
            "tag" : "优惠信息",
            "title" : "黄龙溪谷购房就享6%优惠",
            "time" : "2018年04月25日",
            "content" : "黄龙溪谷在售三期别墅，总价1300万-3700万，现\n购房就享6%优惠。",
            "link" : "/loupan/p_/dongtai/346136.html"
        }, 
        {
            "tag" : "楼盘资讯",
            "title" : "黄龙溪谷在售三期别墅，总价1300万-3700万",
            "time" : "2018年04月24日",
            "content" : "黄龙溪谷在售三期别墅，总价1300万-3700万，现剩余房源48套。",
            "link" : "/loupan/p_/dongtai/340073.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷在售三期E、F户型，总价1300万起",
            "time" : "2018年04月23日",
            "content" : "黄龙溪谷在售三期E户型，建面240㎡，实得440㎡，总价1300万起，现剩余4套。在售三期F户型，建面293㎡，实得666㎡，总价1300万起，现剩余44套。",
            "link" : "/loupan/p_/dongtai/332147.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷项目三期别墅在售",
            "time" : "2018年04月20日",
            "content" : "黄龙溪谷项目三期别墅在售",
            "link" : "/loupan/p_/dongtai/330508.html"
        }, 
        {
            "tag" : "楼盘资讯",
            "title" : "黄龙溪谷后期将推出独栋别墅",
            "time" : "2018年04月04日",
            "content" : "黄龙溪谷项目后期将推出独栋别墅，价格待定。",
            "link" : "/loupan/p_/dongtai/305149.html"
        }, 
        {
            "tag" : "楼盘资讯",
            "title" : "黄龙溪谷项目后期将推出300㎡~800㎡独栋别墅",
            "time" : "2018年03月29日",
            "content" : "黄龙溪谷项目后期将推出300㎡~800㎡独栋别墅，价格待定。",
            "link" : "/loupan/p_/dongtai/285872.html"
        }, 
        {
            "tag" : "楼盘资讯",
            "title" : "黄龙溪谷毗邻黄龙溪古镇，山清水秀",
            "time" : "2018年03月22日",
            "content" : "黄龙溪谷毗邻黄龙溪古镇，山清水秀，远离大城市的喧嚣与嘈杂。项目在售三期别墅，总价1000-3000万/套。",
            "link" : "/loupan/p_/dongtai/277394.html"
        }, 
        {
            "tag" : "楼盘资讯",
            "title" : "黄龙溪谷是由优品道控股与复地集团两大企业打造",
            "time" : "2018年03月20日",
            "content" : "黄龙溪谷是由优品道控股与复地集团两大实力企业，合力打造的低密国际休闲别墅区。",
            "link" : "/loupan/p_/dongtai/273774.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷在售三期大户型别墅",
            "time" : "2018年03月15日",
            "content" : "黄龙溪谷在售三期大户型别墅，在售户型240实得530平，293实得666平，总价1000万/套起。",
            "link" : "/loupan/p_/dongtai/265489.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷项目在售385栋",
            "time" : "2018年03月08日",
            "content" : "黄龙溪谷项目在售385栋，总价1200-3000万/套。",
            "link" : "/loupan/p_/dongtai/254605.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷预计2018年中旬会推出四期别墅",
            "time" : "2018年02月24日",
            "content" : "黄龙溪谷项目总价1200-3000万/套，在售三期别墅，在售户型240实得530平，293实得666平。预计2018年中旬会推出四期别墅。",
            "link" : "/loupan/p_/dongtai/241874.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷项目总价1000-2000万/套",
            "time" : "2018年02月05日",
            "content" : "黄龙溪谷项目总价1000-2000万/套，在售三期别墅，在售户型240实得530平，293实得666平。",
            "link" : "/loupan/p_/dongtai/235289.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷当前在售建面240平米别墅",
            "time" : "2018年01月29日",
            "content" : "黄龙溪谷当前在售建面240平米，实得530平米的大户型别墅，总价1500-2000万/套。",
            "link" : "/loupan/p_/dongtai/230428.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷项目小户型别墅已售完",
            "time" : "2018年01月22日",
            "content" : "黄龙溪谷项目小户型别墅已售完，当前在售建面240平米，实得530平米的大户型别墅，总价1500-2000万/套。",
            "link" : "/loupan/p_/dongtai/212263.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷项目别墅600万/套起",
            "time" : "2018年01月15日",
            "content" : "黄龙溪谷毗邻黄龙溪古镇，山清水秀，远离大城市的喧嚣与嘈杂。项目别墅600万/套起，在售三期别墅，户型为170-190平米类独栋。",
            "link" : "/loupan/p_/dongtai/207410.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷在售三期别墅",
            "time" : "2018年01月08日",
            "content" : "黄龙溪谷项目总价：550万/套起，在售三期别墅，在售户型170实得330平，293实得666平。",
            "link" : "/loupan/p_/dongtai/202955.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷项目总价：550万-2000万/套",
            "time" : "2018年01月01日",
            "content" : "黄龙溪谷项目总价：550万-2000万/套；在售户型170实得330平，195实得373平，293实得666平。",
            "link" : "/loupan/p_/dongtai/197675.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷项目物业费5.9元/月/平米",
            "time" : "2017年12月22日",
            "content" : "黄龙溪谷总价：550万-2000万/套；户型：C：170实得330平，赠花园50-150平，550万/套起，D：195实得373平，赠花园100-180平，620万/套起，D：293实得666平，赠花园400—600平，2000万/套起。项目物业费5.9元/月/平米 。",
            "link" : "/loupan/p_/dongtai/192789.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷C户型见面170平实得330平",
            "time" : "2017年12月15日",
            "content" : "黄龙溪谷总价：550万-2000万/套；户型：C：170实得330平，赠花园50-150平，550万/套起，D：195实得373平，赠花园100-180平，620万/套起，D：293实得666平，赠花园400—600平，2000万/套起。在售三期385栋。",
            "link" : "/loupan/p_/dongtai/188379.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷在售三期385栋",
            "time" : "2017年12月08日",
            "content" : "黄龙溪谷总价：550万-2000万/套；户型：C：170实得330平，赠花园50-150平，550万/套起，D：195实得373平，赠花园100-180平，620万/套起，D：293实得666平，赠花园400—600平，2000万/套起。在售三期385栋。",
            "link" : "/loupan/p_/dongtai/184662.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷总价：550万-2000万/套",
            "time" : "2017年12月01日",
            "content" : "黄龙溪谷总价：550万-2000万/套；户型：C：170实得330平，赠花园50-150平，550万/套起，D：195实得373平，赠花园100-180平，620万/套起，D：293实得666平，赠花园400—600平，2000万/套起。在售三期347栋，三期259栋。",
            "link" : "/loupan/p_/dongtai/180183.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷170平实得330平，550万/套起",
            "time" : "2017年11月27日",
            "content" : "黄龙溪谷总价：550万-2000万/套；户型：C：170实得330平，赠花园50-150平，550万/套起，D：195实得373平，赠花园100-180平，620万/套起，D：293实得666平，赠花园400—600平，2000万/套起。在售三期347栋，三期259栋。",
            "link" : "/loupan/p_/dongtai/177907.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷项目于2016年9月30日开盘",
            "time" : "2017年11月20日",
            "content" : "黄龙溪谷总价：550万-2000万/套；户型：C：170实得330平，赠花园50-150平，550万/套起，D：195实得373平，赠花园100-180平，620万/套起，D：293实得666平，赠花园400—600平，2000万/套起。在售三期347栋，三期259栋。",
            "link" : "/loupan/p_/dongtai/173959.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷预计2018年10月交房",
            "time" : "2017年11月14日",
            "content" : "黄龙溪谷总价：550万-2000万/套；户型：C：170实得330平，赠花园50-150平，550万/套起，D：195实得373平，赠花园100-180平，620万/套起，D：293实得666平，赠花园400—600平，2000万/套起。在售三期347栋，三期259栋。",
            "link" : "/loupan/p_/dongtai/170520.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷在售三期347栋，三期259栋",
            "time" : "2017年11月13日",
            "content" : "黄龙溪谷总价：550万-2000万/套；户型：C：170实得330平，赠花园50-150平，550万/套起，D：195实得373平，赠花园100-180平，620万/套起，D：293实得666平，赠花园400—600平，2000万/套起。在售三期347栋，三期259栋。",
            "link" : "/loupan/p_/dongtai/169843.html"
        }, 
        {
            "tag" : "最新活动",
            "title" : "黄龙溪谷总价550万——2000万/套",
            "time" : "2017年11月04日",
            "content" : "黄龙溪谷总价：550万-2000万/套；户型：C：170实得330平，赠花园50-150平，550万/套起，D：195实得373平，赠花园100-180平，620万/套起，D：293实得666平，赠花园400—600平，2000万/套起。",
            "link" : "/loupan/p_/dongtai/163696.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷房源在售",
            "time" : "2017年10月30日",
            "content" : "黄龙溪谷总价：550万——2000万；户型：C：170实得330平，赠花园50—150平，550万起，D：195实得373平，赠花园100—180平，620万起，E：240实得440平，赠花园400—600平，1500万起，D：293实得666平，赠花园400—600平，2000万起。",
            "link" : "/loupan/p_/dongtai/161025.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷别墅在售",
            "time" : "2017年10月23日",
            "content" : "黄龙溪谷总价：550万——2000万；楼栋：三期347栋，三期259栋；户型：C：170平临溪，550万起；D：195平，620万起；E：240平临湖，1500万起；D：293平临湖，2000万起。",
            "link" : "/loupan/p_/dongtai/155004.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷别墅在售",
            "time" : "2017年10月16日",
            "content" : "黄龙溪谷在售价格：总价：550万——2000万；2、在售楼栋：三期347栋，三期259栋；3、在售户型：C：建面170实得330平，550万起；D：建面195实得373平，620万起；E：建面240实得440平，1500万起；D：建面293实得666平，2000万起。",
            "link" : "/loupan/p_/dongtai/151228.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷别墅在售",
            "time" : "2017年10月11日",
            "content" : "黄龙溪谷建面：170实得220，价格530万起。建面：195实得373，价格620万起。建面:240实得440，价格1500万起（临湖）。建面：293实得666，价格2000万起（临湖）。花园面积：50-600平",
            "link" : "/loupan/p_/dongtai/149283.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷别墅在售",
            "time" : "2017年10月10日",
            "content" : "黄龙溪谷建面：170实得220，价格530万起。建面：195实得373，价格620万起。建面:240实得440，价格1500万起（临湖）。建面：293实得666，价格2000万起（临湖）。花园面积：50-600平",
            "link" : "/loupan/p_/dongtai/148283.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷独栋别墅在售",
            "time" : "2017年09月30日",
            "content" : "黄龙溪谷项目目前最小的85平已卖完，目前在售户型总价460万起。",
            "link" : "/loupan/p_/dongtai/143856.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷独栋别墅在售",
            "time" : "2017年09月26日",
            "content" : "黄龙溪谷项目在售总价420万-1500万。",
            "link" : "/loupan/p_/dongtai/140974.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷独栋别墅在售",
            "time" : "2017年09月25日",
            "content" : "黄龙溪谷项目在售总价420万-1500万。",
            "link" : "/loupan/p_/dongtai/140208.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷新房源持续加推",
            "time" : "2017年09月04日",
            "content" : "黄龙溪谷项目房源持续加推，独栋别墅在售，具体加推楼栋详询售楼部",
            "link" : "/loupan/p_/dongtai/126975.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷临水别墅540万起",
            "time" : "2017年08月28日",
            "content" : "黄龙溪谷项目三期十八里海在售85-290平别墅，销售总价330万起，临水别墅540万起",
            "link" : "/loupan/p_/dongtai/124051.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷地铁11号线规划站点",
            "time" : "2017年08月22日",
            "content" : "黄龙溪谷地铁11号线规划站点，有花园、带私家车位",
            "link" : "/loupan/p_/dongtai/120039.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷项目当期总数3期",
            "time" : "2017年08月21日",
            "content" : "黄龙溪谷项目当期总数3期，别墅2-3层，每户均带有停车位",
            "link" : "/loupan/p_/dongtai/119984.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷物业费5.9元/平米·月",
            "time" : "2017年08月07日",
            "content" : "黄龙溪谷项目物业费5.9元/平米·月，项目当期总数3期，别墅2-3层，每户均带有停车位。",
            "link" : "/loupan/p_/dongtai/111592.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷85-290平别墅总价330万起",
            "time" : "2017年07月31日",
            "content" : "黄龙溪谷项目三期十八里海在售85-290平别墅，销售总价330万起，临水别墅540万起",
            "link" : "/loupan/p_/dongtai/108363.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷两公里内有6处银行/ATM",
            "time" : "2017年07月24日",
            "content" : "黄龙溪谷项目两公里内有6处银行，类型为成都市农村商业银行和中国民生银行",
            "link" : "/loupan/p_/dongtai/103361.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷项目居住舒适度好",
            "time" : "2017年07月17日",
            "content" : "黄龙溪谷项目户型设计有花园、带私家车位，环境较好，居住舒适度高",
            "link" : "/loupan/p_/dongtai/99837.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷一期、三期均在售",
            "time" : "2017年07月10日",
            "content" : "黄龙溪谷一期别墅在售总价600万起，三期别墅在售总价330万起",
            "link" : "/loupan/p_/dongtai/95602.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷现房期房都在售",
            "time" : "2017年07月03日",
            "content" : "黄龙溪谷纯独栋产品，现房、期房都在售，微独栋产品，高层的价格买别墅。地铁11号线规划站点，有花园、带私家车位",
            "link" : "/loupan/p_/dongtai/92037.html"
        }, 
        {
            "tag" : "销控信息",
            "title" : "黄龙溪谷独栋别墅在售",
            "time" : "2017年06月28日",
            "content" : "黄龙溪谷由复地集团、优品道控股，共同打造成都城南复合生态住区，在售85、168、200、290平米独栋别墅。总价320-3000万/套。【快速线路一】自城南桐梓林出发：经剑南大道，双向10车道不设红绿灯;",
            "link" : "/loupan/p_/dongtai/78046.html"
        }
    ]
}
```