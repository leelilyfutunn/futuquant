**富途牛牛Win PLS API 开发文档**

[1. 名词定义 5](#_Toc486409106)

[2. 概述 5](#_Toc486409107)

[2.1. PLS说明 5](#_Toc486409108)

[2.1.1. 接口背景 5](#_Toc486409109)

[2.1.2. 源代码 5](#_Toc486409110)

[2.1.2.1. 安装及使用 5](#_Toc486409111)

[2.1.2.2. 当前api最低版本要求 5](#_Toc486409112)

[2.2. 错误码说明 5](#_Toc486409113)

[2.3. 协议号 6](#_Toc486409114)

[2.4. 市场说明 6](#_Toc486409115)

[2.5. 订阅类型说明 6](#_Toc486409116)

[2.6. 时间说明 7](#_Toc486409117)

[3. API接口 7](#_Toc486409118)

[3.1. 接口简介 7](#_Toc486409119)

[3.2. Socket 连接 7](#_Toc486409120)

[3.3. Json基础字段 7](#_Toc486409121)

[3.4. 获取基础报价(Protocol: 1001) 8](#_Toc486409122)

[3.5. 获取摆盘数据(Protocol: 1002) 8](#_Toc486409123)

[3.6. 订阅股票协议 (Protocol: 1005) 9](#_Toc486409124)

[3.7. 反订阅股票协议 (Protocol: 1006) 9](#_Toc486409125)

[3.8. 查询订阅股票协议 (Protocol: 1007) 9](#_Toc486409126)

[3.9. 设置要接收推送协议的股票信息 (Protocol: 1008) 9](#_Toc486409127)

[3.10. 拉取分时数据(Protocol: 1010) 10](#_Toc486409128)

[3.11. 拉取最近1000根K线数据(Protocol:1011) 11](#_Toc486409129)

[3.12. 逐笔协议(Protocol:1012) 11](#_Toc486409130)

[3.13. 交易日列表协议(Protocol:1013) 12](#_Toc486409131)

[3.14. 股票信息协议(Protocol:1014) 13](#_Toc486409132)

[3.15. 市场快照协议(Protocol:1015) 13](#_Toc486409133)

[3.16. 批量报价协议(Protocol:1023) 15](#_Toc486409134)

[3.17. 历史K线(Protocol:1024) 16](#_Toc486409135)

[3.18. 复权因子(Protocol:1025) 16](#_Toc486409136)

[3.19. 获取板块集合下的子板块列表(Protocol: 1026) 17](#_Toc486409137)

[3.20. 获取板块下的股票列表(Protocol: 1027) 18](#_Toc486409138)

[3.21. 获取经纪队列(Protocol: 1028) 18](#_Toc486409139)

[3.22. 获取牛牛程序全局状态(Protocol: 1029) 19](#_Toc486409140)

[市场状态字段说明: 19](#_Toc486409141)

[3.23. 港股下单交易(Protocol: 6003) 20](#_Toc486409142)

[3.24. 港股设置订单状态(Protocol: 6004) 20](#_Toc486409143)

[3.25. 港股修改订单(Protocol: 6005) 21](#_Toc486409144)

[3.26. 解锁交易(Protocol: 6006) 22](#_Toc486409145)

[3.27. 港股查询帐户信息(Protocol: 6007) 22](#_Toc486409146)

[3.28. 港股查询订单列表(Protocol: 6008) 23](#_Toc486409147)

[3.29. 港股查询持仓列表(Protocol: 6009) 24](#_Toc486409148)

[3.30. 港股查询成交记录(Protocol:6010) 25](#_Toc486409149)

[3.31. 美股下单交易(Protocol: 7003) 26](#_Toc486409150)

[3.32. 美股设置订单状态(Protocol: 7004) 26](#_Toc486409151)

[3.33. 美股修改订单(Protocol: 7005) 27](#_Toc486409152)

[3.34. 美股查询帐户信息(Protocol: 7007) 27](#_Toc486409153)

[3.35. 美股查询订单列表(Protocol: 7008) 28](#_Toc486409154)

[3.36. 美股查询持仓列表(Protocol: 7009) 29](#_Toc486409155)

[3.37. 美股查询成交记录(Protocol: 7010) 30](#_Toc486409156)

**修改历史**

| 修改日期       | 修改内容                                     | 修改人        | 备注                         |
| ---------- | ---------------------------------------- | ---------- | -------------------------- |
| 2015. 9.15 | 初稿                                       |            |                            |
| 2015.11.5  | 1. 增加行情现价接口   2. 增加仿真交易参数  3. 新增条件交易demo | Ysq/Hugh   | 牛牛版本需要最低307版本才可以正常运行       |
| 2015.12.18 | 1.报价增加时间字段 2.股票个数上限由100上调至300            | Ysq        |                            |
| 2015.1.21  | 1. 更新港股交易接口文档，修改部分参数**'OrderTypeHK’**改为**'OrderType'** “**SetOrderStatusHK**”改为”**SetOrderStatus**” 2. 增加美股交易接口(下单，撤单，改单) 3. 增加解锁接口 | YSQ        | **!! 新接口需要3.14及以上客户端版本支持** |
| 2015.2.22  | 6007协议文档错误纠正                             | Ysq        |                            |
| 2016.11.23 | 1001协议增加每手数量字段                           | zeno       |                            |
| 2016.12.12 | 1010协议 拉取当天分时数据 6010 协议 港股成交记录 7010 协议 美股成交记录 | zeno       |                            |
| 2016.12.26 | 1011协议 拉取最近1000根K线                       | zeno       |                            |
| 2017.1.10  | API一期                                    | Zeno;Tajod |                            |
| 2017.4.\~  | 1. 快照1015增加总市值及流通市值/窝轮信息/字符串返回的更新时间  2. 1014取股票列表增加owner股票信息及子类型(窝轮用到）  3. 增加1026获取板块集合的子板块列表  4. 港、美股查订单列表增加过滤选项 | Ysq        |                            |



1. **名词定义**

FTNN : 特指富途牛牛For Windows

PLS : Plugin Local Server 的简称, 该模块是FTNN的一个标准插件

1.  **概述**

2.1  **PLS说明**

本节主要介绍如何使用富途牛牛windows客户端插件PLS进行socket二次开发.

2.1.1  **接口背景**

富途牛牛3.3 版本之后，开始支持插件开发, 接口规范详见
<https://github.com/szmile2008/FTPlugin.git> 但考虑到实现插件需要较厚深的win
vc编程基础，
使用多有不便，故官方提供socket插件中间层，方便用户使用第三方工具如Python，以脚本的方式调用行情交易接口

2.1.2.  **源代码**

基于富途牛牛插件框架开发的本地Server , 代码完全开源, 见上述开源项目 “
PluginServer”目录 , 该工程在vc2005下编译通过

2.1.2.1  **安装及使用**

<https://github.com/szmile2008/FTPlugin/blob/master/Plugins/PluginLocalServer/bin/readme.txt>

2.1.2.2  **当前api最低版本要求**

**牛牛版本号: 3.32**

2.2  **错误码说明**

| 错误码  | 错误说明       |
| ---- | ---------- |
| 0    | 无错误        |
| 400  | 未知错误       |
| 401  | 版本不支持      |
| 402  | 股票未找到      |
| 403  | 协议号不支持     |
| 404  | 参数错误       |
| 405  | 频率错误（请求过快） |
| 406  | 订阅达到上限     |
| 407  | 未订阅        |
| 408  | 未满足反订阅时间限制 |
| 501  | 服务器忙       |
| 502  | 超时         |
| 503  | 网络错误       |

2.3  **协议号**

| 行情相关 |          |      |          |
| ---- | -------- | ---- | -------- |
| 1001 | 报价       | 1002 | 摆盘       |
| 1005 | 订阅       | 1006 | 反订阅      |
| 1007 | 查询订阅     | 1008 | 推送协议     |
| 1010 | 分时       | 1011 | 最近K线     |
| 1012 | 逐笔       | 1013 | 交易日      |
| 1014 | 股票信息     | 1015 | 市场快照     |
| 1023 | 批量报价     | 1024 | 历史K线     |
| 1025 | 复权因子     |      |          |
| 交易相关 |          |      |          |
| 6003 | 港股下单     | 7003 | 美股下单     |
| 6004 | 港股订单状态更改 | 7004 | 美股订单状态修改 |
| 6005 | 港股改单     | 7005 | 美股改单     |
| 6006 | 解锁交易     |      |          |
| 6007 | 港股查询账户信息 | 7007 | 美股查询账户信息 |
| 6008 | 港股查询订单列表 | 7008 | 美股查询订单列表 |
| 6009 | 港股查询持仓   | 7009 | 美股查询持仓   |
| 6010 | 港股查询成交记录 | 7010 | 美股查询成交记录 |

2.4  **市场说明**

| Market值 | 对应市场 |
| ------- | ---- |
| 1       | 港股   |
| 2       | 美股   |
| 3       | 沪股   |
| 4       | 深股   |
| 5       | 旧期货  |
| 6       | 新期货  |

2.5  **订阅类型说明**

| StockSubType值 | 对应订阅类型   | 对应协议      |
| ------------- | -------- | --------- |
| 1             | 报价       | 1001、1023 |
| 2             | 摆盘       | 1002      |
| 4             | 逐笔       | 1012      |
| 5             | 分时       | 1010      |
| 6             | 日分K      | 1011      |
| 7             | 5分K      | 1011      |
| 8             | 15分K     | 1011      |
| 9             | 30分K     | 1011      |
| 10            | 60分K     | 1011      |
| 11            | 1分K      | 1011      |
| 12            | 周K       | 1011      |
| 13            | 月K       | 1011      |
| **14**        | **经纪队列** | **1028**  |
|               |          |           |

2.6  **时间说明**

时间的标准格式为“2017-01-01 08:18:28”，部分时间例如end_date精准到日即可。

1. **API接口**

3.1 **接口简介**

-   协议采用纯文本，方便脚本语言处理。

-   协议内容是一个完整的json字符。

-   Json 请求或返回以\\r\\n 作为分隔。

-   所有金额相关的字段都是\*1000， 也就是开盘价1000表示1.000\$

-   所有成交量都是股数， 非在UI上看到的”xx手”

-   **所有行情相关协议获取数据都需要先通过（1005）协议订阅成功后才能查询**

-   **订阅的上限为500个订阅单位。一只股票的一个K线类型占2个订阅单位、分时占2个订阅单位、报价占1个订阅单位、摆盘占5个订阅单位（牛熊为1）、逐笔占5个订阅单位（牛熊为1）、经纪队列占5个订阅单位（牛熊为1）。**

-   **反订阅（1006）的时间限制为１分钟，即订阅某支股票某个订阅位１分钟之后才能反订阅**

-   **30秒内不能超过20次交易请求。**

-   **建议所有行情拉取接口在同一条长连接上。推送数据在第二条长连接上。交易接口在第三条长连接上。**

3.2 **Socket 连接**

-   IP: 127.0.0.1 (为安全起见， 默认只作本地监听）

-   Port: 11111

3.3 **Json基础字段**

| 字段名       | 字段值            | 备注            |
| --------- | -------------- | ------------- |
| Protocol  |                | 请求协议号         |
| Version   | ‘1’            | 协议版本号         |
| Market    | Int32          | 市场类型 详见市场类型说明 |
| ErrCode   | Int64 : 0 表示成功 | 返回错误码 详见错误码说明 |
| ErrDesc   | UTF-8          | 返回错误描述        |
| StockCode | eg ’00700’     | 股票代码          |
| ReqParam  | 随协号定义          | 请求参数          |
| RetData   | 随协号定义          | 返回数据          |
|           |                |               |

3.4  **获取基础报价(**Protocol: **1001)**

**C-\>S eg:**

{'Protocol':'1001', 'ReqParam':{'Market':'1','StockCode':'00700'},'Version':'1'}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1001","RetData":{"Close":"135400","CurPrice":"135400","High":"137600","LastClose":"139800","LotSize":"0","Low":"133800","Market":"1","Open":"136900","StockCode":"00700","Time":"57600","Turnover":"3588168326322","Volume":"26441962"},"Version":"1"}

字段说明:

| 字段名          | 字段值       | 备注                    |
| ------------ | --------- | --------------------- |
| Close        | Int32     | 收盘价                   |
| High         | Int32     | 最高价                   |
| LastClose    | Int32     | 昨收                    |
| Low          | Int32     | 最低价                   |
| Open         | Int32     | 开盘价                   |
| Turnover     | Int64     | 成交额                   |
| Volume       | Int64     | 成交量                   |
| LotSize      | Int32     | 每手数量（沪深为0，美股为1, 期货为0） |
| **CurPrice** | **Int32** | **现价**                |
| **Time**     | **Int32** | **报价最后更新时间**          |

3.5  **获取摆盘数据(**Protocol: **1002)**

**C-\>S eg:**

{"Protocol":"1002","ReqParam":{"Num":"3","Market":"1","StockCode":"00700"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1002","RetData":{"GearArr":[{"BuyOrder":"1","BuyPrice":"135300","BuyVol":"3400","SellOrder":"2","SellPrice":"135400","SellVol":"27000"},{"BuyOrder":"5","BuyPrice":"135200","BuyVol":"64000","SellOrder":"5","SellPrice":"135500","SellVol":"70200"},{"BuyOrder":"20","BuyPrice":"135100","BuyVol":"108300","SellOrder":"9","SellPrice":"135600","SellVol":"142300"}],"Market":"1","StockCode":"00700"},"Version":"1"}

字段说明:

| 字段名       | 字段值          | 备注       |
| --------- | ------------ | -------- |
| GearArr   |              | 摆盘数据结点   |
| BuyOrder  | Int32        | 买盘经纪个数   |
| BuyPrice  | Int32        | 买价       |
| BuyVol    | Int64        | 买量       |
| SellOrder | Int32        | 卖盘经纪个数   |
| SellPrice | Int32        | 卖价       |
| SellVol   | Int64        | 卖量       |
| Num       | In32(1\~ 10) | 待请求的摆盘个数 |

**注:1.Num为原先的(GetGearNum)**

**2.当实际摆盘数小于Num的数值时，只返回实际的摆盘情况**

**3.调用前须先1005订阅摆盘**

3.6  **订阅股票协议 (**Protocol: 1005**)**

**C-\>S eg:**

{"Protocol":"1005","ReqParam":{ "StockSubType": "1", "Market": "1", "StockCode":
"00700"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1005","RetData":{"Market":"1","StockCode":"00700","StockSubType":"1"}"Version":"1"}

3.7  **反订阅股票协议 (**Protocol: 1006**)**

**C-\>S eg:**

{"Protocol":"1006","ReqParam":{ "StockSubType": "1", "Market": "1", "StockCode":
"00700"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1006","RetData":{"Market":"1","StockCode":"00700","StockSubType":"1"}"Version":"1"}

注：反订阅带有1分钟的时间限制，如果不满足时间要求则会反订阅失败。

3.8  **查询订阅股票协议 (**Protocol: 1007**)**

**C-\>S eg:**

{"Protocol":"1007","ReqParam":{"QueryAllSocket":"0"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1007","RetData":{"SubInfoArr":[{"Market":"1","StockCode":"00038","StockSubType":"1"},{"Market":"1","StockCode":"00700","StockSubType":"1"},{"Market":"1","StockCode":"00700","StockSubType":"4"}]},Version":"1"}

字段说明:

| 字段名            | 字段值   | 备注                                 |
| -------------- | ----- | ---------------------------------- |
| QueryAllSocket | Int32 | 非0表示查询所有socket的订阅状态,否则表示当前查询socket |
| StockPushType  | Int32 | 同StockSubType                      |

3.9  **设置要接收推送协议的股票信息 (**Protocol: 1008**)**

**C-\>S eg:**

{"Protocol":"1008","ReqParam":{ "StockPushType": "1", "Market": "1",
"StockCode": "00700"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1008","RetData":{ "StockPushType": "1",
"Market": "1", "StockCode": "00700"},Version":"1"}

字段说明:

| 字段名           | 字段值   | 备注            |
| ------------- | ----- | ------------- |
| StockPushType | Int32 | 同StockSubType |

推送数据协议号

| 推送数据类型 | 推送协议号 | 拉取协议号 |
| ------ | ----- | ----- |
| 报价     | 1030  | 1023  |
| 摆盘     | 1031  | 1002  |
| K线     | 1032  | 1011  |
| 逐笔     | 1033  | 1012  |
| 分时     | 1034  | 1010  |
| 经纪队列   | 1035  | 1028  |

**注:调用该接口会在该条连接上推送数据。建议所有推送数据请求在同一条新建连接上，并做好异步处理。推送的数据协议号如上表所示，结构与拉取数据相同。例如：拉取摆盘时协议号为1002、推送摆盘为1031。其他协议字段不变。**

3.10  **拉取分时数据(**Protocol: 1010**)**

**C-\>S eg:**

{"Protocol":"1010", "ReqParam":{"Market":"1","StockCode":"00700"},"Version":
"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1010","RetData":{"Num":"305","Market":"1","RTDataArr":[{"Volume":"0","Turnover":"0","OpenedMins":"570","AvgPrice":"0","CurPrice":"4350","DataStatu":"1","LastClose":"4350","Time":"2016-11-129:30"},{"Volume":"0","Turnover":"0","OpenedMins":"571","AvgPrice":"0","CurPrice":"4350","DataStatus":"1","LastClose":"4350","Time":"2016-11-12
9:31:0"},{"Volume":"0","Turnover":"0",

"OpenedMins":"572","AvgPrice":"0","CurPrice":"4330","DataStatus":"1","LastClose":"4350",

"strTime":"2016-11-12
9:32"},{"Volume":"0","Turnover":"0","OpenedMins":"573","AvgPrice":"0","CurPrice":

"4340","DataStatus":"1","LastClose":"4350","Time":"2016-11-12
9:33:0"}],"StockCode":"00700"},"Version":"1"}

字段说明:

| 字段名        | 字段值    | 备注                      |
| ---------- | ------ | ----------------------- |
| RTDataArr  |        | 分时数据                    |
| DataStatus | Int32  | 数据状态（1为正确，2、3暂不支持，4为伪造） |
| Time       | String | 时间                      |
| OpenedMins | Int32  | 开盘多少分钟                  |
| CurPrice   | Int32  | 目前价                     |
| LastClose  | Int32  | 昨收价                     |
| AvgPrice   | Int32  | 平均价                     |
| Volume     | Int64  | 成交量                     |
| Turnover   | Int64  | 成交额                     |
| Num        | Int32  | 数据个数                    |

3.11  **拉取最近1000根K线数据(**Protocol:1011**)**

**C-\>S eg:**

{"Protocol":"1011","ReqParam":{ "Num":
"2","Market":"1","StockCode":"00700","KLType":"1","RehabType":

"1"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1011","RetData":{"Market":"1","StockCode":"00700","KLType":"1","RehabType":"1""KLDataArr":[{"Close":"181400","DataStatus":"1","High":"181400","Low":"181300","Open":"181300","PERatio":"0","Turnover":"6982740000","Volume":"38500","Time":"2016-11-19
15:54:0","Turnover":"0"},{"Close":"181300","DataStatus":"1","High":"181400","Low":"181200","Open":"181300","PERatio":"0","Turnover":"9374000000","Volume":"51700","Time":"2016-11-19
15:55:0","Turnover":"0"}],"Version":"1"}

字段说明:

| 字段名          | 字段值            | 备注                                       |
| ------------ | -------------- | ---------------------------------------- |
| KLDataArr    |                | K线数据                                     |
| DataStatus   | Int32          | 数据状态（1为正确，2、3暂不支持，4为伪造）                  |
| KLType       | Int32          | K线类型 1 = 1分K; 2 = 日K; 3 = 周K; 4 = 月K; 6 = 5分K; 7 = 15分K; 8 = 30分K; 9 = 60分K; |
| RehabType    | Int32          | 复权类型 0 = 不复权； 1 = 前复权； 2 = 后复权；          |
| Time         | String         | 时间                                       |
| Close        | Int32          | 收盘价                                      |
| High         | Int32          | 最高价                                      |
| Low          | Int32          | 最低价                                      |
| Open         | Int32          | 开盘价                                      |
| Volume       | Int64          | 成交量                                      |
| Turnover     | Int64          | 成交额                                      |
| PERatio      | Int32          | 市盈率                                      |
| TurnoverRate | Int32          | 换手率                                      |
| Num          | Int32（1\~1000） | 拉取个数                                     |

**注:Num为新增参数，为拉取个数。但实际返回个数不一定有Num个。Num取值为1至1000。**

3.12  **逐笔协议**(Protocol:1012)

**C-\>S eg:**

{"Protocol":"1012","ReqParam":{"Market":"1","StockCode":"00700","Num":"3","Sequence":"-1"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1012","RetData":{"Market":"1","NextSequence":"-1","StockCode":"00700","TickerArr":[{"Direction":"2","Price":"199000","Sequence":"6376603941391569400","Time":"2017-01-18
14:22:16","Turnover":"119400000","Volume":"600"},{"Direction":"2","Price":"199000","Sequence":"6376603941391569401","Time":"2017-01-18
14:22:16","Turnover":"19900000","Volume":"100"},{"Direction":"2","Price"

:"199000","Sequence":"6376603941391569402","Time":"2017-01-18
14:22:18","Turnover":"59700000",

"Volume":"300"}]},"Version":"1"}

字段说明:

| 字段名          | 字段值    | 备注                     |
| ------------ | ------ | ---------------------- |
| Num          | Int32  | 返回的最多逐笔个数              |
| TickerArr    | Array  | 返回的逐笔记录数组              |
| Sequence     | Int64  | 暂不起作用（输入时填入-1即可）       |
| NextSequence | Int64  | 暂不起作用                  |
| Direction    | Int32  | 买卖方向 1 = 买 2 = 卖 3 = 平 |
| Price        | Int64  | 价格                     |
| Time         | String | 时间（精确到秒）               |
| Volume       | Int64  | 成交量（股）                 |
| Turnover     | Int64  | 成交金额                   |

**注：1.最多逐笔个数为请求返回的最多逐笔个数，但实际返回数量不一定会返回这么多。**

**2.只返回订阅逐笔以后的逐笔成交记录，订阅以前的逐笔成交记录不返回**

**3.Sequence、NextSequence暂时没用到，将在以后版本用于扩展。本版本使用者只需注意在发送请求时将Sequence值设为-1即可。**

3.13  **交易日列表协议**(Protocol:1013)

**C-\>S eg:**

{"Protocol":"1013", "ReqParam":{"start_date":"2017-01-10","end_date":
"2017-01-17", "Market": "1"}, "Version": "1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1013","RetData":{"Market":"1","TradeDateArr":["2017-01-16","2017-01-13","2017-01-12","2017-01-11","2017-01-10"],"end_date":"2017-01-17","start_date":"2017-01-10"},"Version":"1"}

字段说明:

| 字段名          | 字段值    | 备注      |
| ------------ | ------ | ------- |
| TradeDateArr | Array  | 返回交易日数组 |
| end_date     | string | 结束日期    |
| start_date   | string | 开始日期    |

3.14  **股票信息协议**(Protocol:1014)

**C-\>S eg:**

{"Protocol":"1014", "ReqParam": {"StockType": "3", "Market": "1"}, "Version":
"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1013","RetData":{"Market":"1",
"BasicInfoArr":[{"LotSize":"500",

" StockName
":"长和","StockCode":"00001","StockID":"4440996184065","StockType":"3","StockChildType"

:"0", "OwnerStockCode":"","OwnerMarketType":"0"},{"LotSize":"6000","StockName
":"九号运通","StockCode"

:"00009","StockID":"49718541418505","StockType":"3","StockChildType":"0",
"OwnerStockCode":"",

"OwnerMarketType":"0"},{"LotSize":"1000"," StockName
":"鹰君","StockCode":"00041","StockID":"41"

,"StockType":"3","StockChildType":"0",
"OwnerStockCode":"","OwnerMarketType":"0"}]},"Version":"1"}

字段说明:

| 字段名             | 字段值    | 备注                                       |
| --------------- | ------ | ---------------------------------------- |
| BasicInfoArr    | Array  | 股票信息数组                                   |
| ListTime        | String | 上市时间                                     |
| LotSize         | Int32  | 每手数量                                     |
| StockName       | String | 股票名                                      |
| StockCode       | String | 股票代码                                     |
| StockType       | Int32  | 股票类型 1 = BOND--债券 3 = STOCK--正股 4 = ETF--ETF基金 5 = WARRANT--窝轮牛熊 6 = IDX--指数 |
| StockID         | Int64  | 股票哈希代码                                   |
| StockChildType  | Int32  | 子类型: 1=认购证 2=认沽证 3=牛证4=熊证 (目前仅支持窝轮)      |
| OwnerStockCode  | String | 所属正股的code(目前仅支持窝轮）                       |
| OwnerMarketType | Int32  | 所属正股的market(目前仅支持窝轮）                     |

**注：start_date需小于end_date，否则TradeDateArr为空**

3.15  **市场快照协议**(Protocol:1015)

**C-\>S eg:**

{"Protocol": "1015", "Version":"1","ReqParam":{"StockArr": [{"Market": "1",
"StockCode": "00700"}, {"Market": "1", "StockCode": "00038"}]}}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1015","RetData":{"SnapshotArr":[{"HighestPrice":"226400","StockType":"3","LastClose":"225200","ListingDate":"1087315200","ListingStatus":"0","LotSize":"100","LowestPrice":"222600","MarketType":"1","NominalPrice":"222800","OpenPrice":"225400","RetErrCode":"0","Volume":"16116998","StockCode":"00700","StockID":"54047868453564","SuspendFlag":"0",,"Turnover":"3614003913900","TurnoverRate":"170","UpdateTime":"1490947724","CircularMarketVal":"0","TotalMarketVal":"0","UpdateTimeStr":"2017-03-31
16:08:44","Wrt_ConversionRatio":"0","Wrt_Delta":"0","Wrt_EndTradeDateStr":"",

"Wrt_ImpliedVolatility":"0","Wrt_IssueVol":"0","Wrt_MaturityDateStr":"","Wrt_OwnerMarketType":"0","Wrt_OwnerStockCode":"","Wrt_Premium":"0","Wrt_RecoveryPrice":"0","Wrt_StreetRatio":"0","Wrt_StreetVol":"0","Wrt_StrikePrice":"0","Wrt_Type":"0","Wrt_Valid":"0"},{"CircularMarketVal":"0","HighestPrice":"4540","StockType":"3","LastClose":"4480","ListingDate":"866995200","ListingStatus":"0","LotSize":"2000","LowestPrice":"4460","MarketType":"1","NominalPrice":"4540","OpenPrice":"4500","RetErrCode":"0","Volume":"1164000","StockCode":"00038","StockID":"43095701848102","SuspendFlag":"0","TotalMarketVal":"0","Turnover":"5240900000","TurnoverRate":"290","UpdateTime":"1490947726","UpdateTimeStr":"2017-03-31
16:08:46",

"Wrt_ConversionRatio":"0","Wrt_Delta":"0","Wrt_EndTradeDateStr":"","Wrt_ImpliedVolatility":"0","Wrt_IssueVol":"0","Wrt_MaturityDateStr":"","Wrt_OwnerMarketType":"0","Wrt_OwnerStockCode":"","Wrt_Premium":"0","Wrt_RecoveryPrice":"0","Wrt_StreetRatio":"0","Wrt_StreetVol":"0","Wrt_StrikePrice":"0","Wrt_Type":"0","Wrt_Valid":"0"}]},"Version":"1"}

字段说明:

| 字段名                   | 字段值    | 备注                               |
| --------------------- | ------ | -------------------------------- |
| StockArr              | Array  | 快照信息数组                           |
| StockType             | Int32  | 股票类型 1=债券 3=正股 4=EFT 5=窝轮牛熊 6=指数 |
| ListingDate           | Int64  | 上市日期                             |
| ListingStatus         | Int64  | 上市状态                             |
| NominalPrice          | Int64  | 按盘价                              |
| StockID               | Int64  | 股票哈希代码                           |
| SuspendFlag           | Int64  | 停牌状态（1表示停牌，0表示非停牌）               |
| TurnoverRate          | Int32  | 换手率                              |
| UpdateTime            | Int64  | 更新时间                             |
| UpdateTimeStr         | String | 格式化的更新时间                         |
| Volume                | Int64  | 成交量                              |
| Turnover              | Int64  | 成交额                              |
| CircularMarketVal     | Int64  | 流通市值 (3位精度) ( 只对A股有效)            |
| TotalMarketVal        | Int64  | 总市值(3位精度)                        |
| Wrt_Valid             | Int32  | 是否是窝轮                            |
| Wrt_ConversionRatio   | Int32  | 换股比率                             |
| Wrt_Type              | Int32  | 窝轮类型: 1=认购证 2=认沽证 3=牛证4=熊证       |
| Wrt_StrikePrice       | Int32  | 行使价格(3位精度)                       |
| Wrt_MaturityDateStr   | String | 格式化窝轮到期时间                        |
| Wrt_EndTradeDateStr   | String | 格式化窝轮最后交易时间                      |
| Wrt_OwnerStockCode    | String | 窝轮对应的正股code                      |
| Wrt_OwnerMarketType   | Int32  | 窝轮对应的正股market                    |
| Wrt_RecoveryPrice     | Int64  | 窝轮回收价(3位精度)                      |
| Wrt_StreetVol         | Int64  | 窝轮街货量                            |
| Wrt_IssueVol          | Int64  | 窝轮发行量                            |
| Wrt_StreetRatio       | Int32  | 窝轮街货占比(除100000得到浮点数)             |
| Wrt_Delta             | Int32  | 窝轮对冲值（3位精度）                      |
| Wrt_ImpliedVolatility | Int32  | 窝轮引伸波幅(3位精度)                     |
| Wrt_Premium           | Int32  | 窝轮溢价(3位精度)                       |
|                       |        |                                  |

3.16  **批量报价协议**(Protocol:1023)

**C-\>S eg:**

{"Protocol":"1023","ReqParam":{"ReqArr":[{"Market":"1","StockCode": "00700"},
{"Market": "1", "StockCode": "00038"}]},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1023","RetData":{
"SubSnapshotArr":[{"Amplitude":"910","CurPrice":"199500","Date":"2017-01-18","High":"199800","LastClose":"197700","ListTime":"2004-06-16","Low":"198000","Market":"1","Open":"197700","StockCode":"00700","Suspension":"2","Turnover":"1609391321800","Volume":"8082594","Time":"15:02:13","TurnoverRate":"85"
,{"Amplitude":"3571","CurPrice":"4610","Date":"2017-01-18","High":"4640","LastClose":"4480","ListTime":"1997-06-23","Low":"4480","Market":"1","Open":"4480","StockCode":"00038","Suspension":"2","Turnover":"14022680000","Volume":"3068000","Time":"15:02:13","TurnoverRate":"763"}]},"Version":"1"}

字段说明:

| 字段名            | 字段值    | 备注                                       |
| -------------- | ------ | ---------------------------------------- |
| ReqArr         | Array  | 查询数组                                     |
| SubSnapshotArr | Array  | 回复批量报价数组                                 |
| ListTime       | String | 上市时间                                     |
| Amplitude      | Int64  | 振幅                                       |
| Suspension     | Int32  | 股票状态 1 =停牌 2 = 正常 3 = 熔断（可恢复） 4 = 熔断（不可恢复） |
| Volume         | Int64  | 成交量·                                     |
| Turnover       | Int64  | 成交额                                      |
| TurnoverRate   | Int32  | 换手率                                      |
| Time           | String | 报价时间                                     |

**注：1.使用该协议查询的股票必须先订阅基础报价（StockSubType = 1）**

**2.每次查询的股票个数上限为50支（与订阅基础报价的上限个数相同）**

3.17  **历史K线**(Protocol:1024)

**C-\>S eg:**

{"Protocol":"1024","ReqParam":{"KLType":"2","Market":"2","RehabType":"1","StockCode":"CFO","end_date":"2017-03-01","start_date":"2017-01-01"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1024","RetData":{"HistoryKLArr":[{"Close":"42710000000","High":"42745000000","Low":"42360000000","Open":"42360000000","PERatio":"0","Turnover":"1872941000","Volume":"43904","Time":"2017-02-21
00:00:00","TurnoverRate":"0"},{"Close":"42704000000","High":"42718000000",

"Low":"42580000000","Open":"42700000000","PERatio":"0","Turnover":"1059874000","Volume":"24830","Time":"2017-02-2200:00:00","TurnoverRate":"0"},{"Close":"42620000000","High":"42900000000","Low":"42535000000","Open":"42900000000","PERatio":"0","Turnover":"1211681000","Volume":"28394","Time":"2017-02-23
00:00:00","TurnoverRate":"0"}],"KLType":"2","Market":"2","RehabType":"1","StockCode":"CFO","end_date":"2017-03-01","start_date":"2017-01-01"},"Version":"1"}

放大系数：Close/High/Low/Open为10的9次方。成交额为10的3次方。

| 字段名          | 字段值    | 备注                                       |
| ------------ | ------ | ---------------------------------------- |
| HistoryKLArr |        | K线数据                                     |
| DataStatus   | Int32  | 数据状态（1为正确，4为伪造）                          |
| KLType       | Int32  | K线类型 1 = 1分K; 2 = 日K; 3 = 周K; 4 = 月K; 6 = 5分K; 7 = 15分K; 8 = 30分K; 9 = 60分K; |
| RehabType    | Int32  | 复权类型 0 = 不复权； 1 = 前复权； 2 = 后复权；          |
| Time         | String | 时间                                       |
| Close        | Int64  | 收盘价                                      |
| High         | Int64  | 最高价                                      |
| Low          | Int64  | 最低价                                      |
| Open         | Int64  | 开盘价                                      |
| Volume       | Int64  | 成交量                                      |
| Turnover     | Int64  | 成交额                                      |
| PERatio      | Int32  | 市盈率                                      |
| TurnoverRate | Int32  | 换手率                                      |
| end_date     | String | 结束日期                                     |
| start_date   | String | 开始日期                                     |

3.18  **复权因子**(Protocol:1025)

**C-\>S eg:**

{"Protocol":"1025","ReqParam":{"StockArr":[{"Market":"2","StockCode":"CFO"}]},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1025","RetData":{"ExRightInfoArr":[{"AllotmentPrice":"0","AllotmentRatio":"0","BackwarAdjFactorB":"2020","BackwardAdjFactorA":"100000","ExDivDate":"2017-01-17","ForwardAdjFactorA":"100000","ForwardAdjFactorB":"-2020","Market":"2","PerCashDiv":"2000","PerShareDivRatio":"0","PerShareTransRatio":"0","SplitRatio":"0","StkSpoPrice":"0","StkSpoRatio":"0","StockCode":"CFO"},{"AllotmentPrice":"0","AllotmentRatio":"0","BackwarAdjFactorB":"2600","BackwardAdjFactorA":"100000","ExDivDate":"2017-02-14","ForwardAdjFactorA":"100000","ForwardAdjFactorB":"-2600","Market":"2","PerCashDiv":"2600","PerShareDivRatio":"0","PerShareTransRatio":"0","SplitRatio":"0","StkSpoPrice":"0","StkSpoRatio":"0","StockCode":"CFO"}]},"Version":"1"}

放大系数全部为10的5次方。

| 字段名                | 字段值    | 备注     |
| ------------------ | ------ | ------ |
| ExRightInfoArr     |        | K线数据   |
| ExDivDate          | Int32  | 除权除息日期 |
| AllotmentRatio     | Int32  | 配股比例   |
| AllotmentPrice     | Int32  | 配股价    |
| PerCashDiv         | string | 现金派现   |
| PerShareDivRatio   | Int32  | 送股比例   |
| PerShareTransRatio | Int32  | 转增股比例  |
| SplitRatio         | Int32  | 拆合股比例  |
| StkSpoPrice        | Int32  | 增发价格   |
| StkSpoRatio        | Int64  | 增发比例   |
| ForwardAdjFactorA  | Int64  | 前复权因子A |
| ForwardAdjFactorB  | Int64  | 前复权因子B |
| ForwardAdjFactorA  | Int64  | 后复权因子A |
| ForwardAdjFactorB  | Int64  | 后复权因子B |

3.19  **获取板块集合下的子板块列表(**Protocol: 1026**)**

**C-\>S eg:**

{"Protocol":"1026","ReqParam":{"Market":"1","PlateClass":"1"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1026","RetData":

{"Market":"1","PlateClass":"1","PlatesetIDsArr":[{"Market":"1","StockCode":"BK1001","StockID":"10001001","StockName":"乳制品"},{"Market":"1","StockCode":"BK1002","StockID":"10001002","StockName":"供应链管理"}]},"Version":"1"}

字段说明:

| 字段名          | 字段值                                 | 备注                                       |
| ------------ | ----------------------------------- | ---------------------------------------- |
| ‘PlateClass’ | Int32 0:所有板块 1: 行业分类 2:地域分类 3: 概念分类 | 板块分类 说明： 港美股市场的地域分类数据暂为空（富途牛牛客户端也没有对应展现） |
| ‘Market’     | Int32                               | 市场id                                     |
| ‘StockCode’  | Utf8 string                         | 板块代码                                     |
| ‘StockName’  | Utf8 string                         | 板块名称                                     |
| ‘StockID’    | Int64                               | 板块ID                                     |

3.20  **获取板块下的股票列表(**Protocol: 1027**)**

**C-\>S eg:**

{"Protocol":"1027","ReqParam":{"Market":"1","StockCode":"BK1001"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1027","RetData":{"Market":"1","PlateSubIDsArr":[{"LotSize"

:"4000","Market":"1","StockName":"天然乳品","OwnerMarketType":"0","OwnerStockCode":"","StockCode"

:"00462","StockChildType":"0","StockType":"3"},{"LotSize":"1000","Market":"1","StockName":"大庆乳业","OwnerMarketType":"0","OwnerStockCode":"","StockCode":"01007","StockChildType":"0","StockType":"3"}

],"StockCode":"BK1001"},"Version":"1"}

字段说明:

| 字段名               | 字段值         | 备注                                       |
| ----------------- | ----------- | ---------------------------------------- |
| ‘StockCode’       | Utf8 string | 板块代码                                     |
| ‘Market’          | Int32       | 市场id                                     |
| ‘LotSize’         | Int32       | 股票每手                                     |
| ‘StockName’       | Utf8 string | 股票名称                                     |
| ‘OwnerMarketType’ | Int32       | 所属股票的市场id(目前仅支持窝轮)                       |
| ‘OwnerStockCode’  | Utf8 string | 所属股票的code(目前仅支持窝轮)                       |
| ‘StockChildType’  | Int32       | 子类型: 1=认购证 2=认沽证 3=牛证4=熊证 (目前仅支持窝轮)      |
| ‘StockType’       | Int32       | 股票类型 1 = BOND--债券 3 = STOCK--正股 4 = ETF--ETF基金 5 = WARRANT--窝轮牛熊 6 = IDX--指数 |

3.21  **获取经纪队列(**Protocol: **1028)**

**C-\>S eg:**

{"Protocol":"1028","ReqParam":{"Market":"1","StockCode":"00700"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1028","RetData":{"BrokerAskArr":

[{"BrokerID":"4057","BrokerName":"法巴","BrokerPos":"0"},

{"BrokerID":"4057","BrokerName":"法巴","BrokerPos":"1"}],

"BrokerBidArr":

[{"BrokerID":"3440","BrokerName":"高盛","BrokerPos":"0"},

{"BrokerID":"5347","BrokerName":"J.P.摩根","BrokerPos":"0"}],

"Market":"1","StockCode":"00700"},"Version":"1"}

字段说明:

| 字段名            | 字段值         | 备注               |
| -------------- | ----------- | ---------------- |
| ‘StockCode’    | Utf8 string | 股票代码             |
| ‘Market’       | Int32       | 市场id             |
| ‘BrokerAskArr’ | 数组          | 经纪Ask(卖)盘        |
| ‘BrokerID’     | Int32       | 经纪ID             |
| ‘BrokerName’   | Utf8 string | 经纪名称             |
| ‘BrokerBidArr’ | 数组          | 经纪Bid(买)盘        |
| ‘BrokerPos’    | Int32       | 经纪档位(0, 1, 2...) |

**注： 同1001拉取报价接口一样，调用拉取时，需先主动定阅**

3.22  **获取牛牛程序全局状态(**Protocol: **1029)**

**C-\>S eg:**

{"Protocol":"1029","ReqParam":{"StateType":"0"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"1029","RetData":{"Market_HK":"5","Market_HKFuture":"15","Market_SH":"6","Market_SZ":"6","Market_US":"11","Quote_Logined":"1","Trade_Logined":"1"},"Version":"1"}

字段说明:

| 字段名               | 字段值           | 备注                     |
| ----------------- | ------------- | ---------------------- |
| StateType         | Int32         | 暂时无用， 保留字段             |
| Market_HK         | Int32         | 港股主板市场状态， 字段定义详见下表     |
| Market_US         | Int32         | 美股Nasdaq市场状态， 字段定义详见下表 |
| Market_SH         | Int32         | 沪市状态， 字段定义详见下表         |
| Market_SZ         | Int32         | *深市*状态， 字段定义详见下表       |
| Market_HKFuture   | Int32         | 港股期市场状态， 字段定义详见下表      |
| Quote_Logined     | Int32(0 \| 1) | 是否登陆行情服务器              |
| **Trade_Logined** | Int32(0 \| 1) | 是否登陆交易服务器              |
|                   |               |                        |

**市场状态字段说明:**

| 市场状态   | 说明                     |
| ------ | ---------------------- |
| **0**  | 未开盘                    |
| **1**  | 竞价交易(港股)               |
| **2**  | 早盘前等待开盘(港股)            |
| **3**  | 早盘(A\|港股)              |
| **4**  | 午休(A\|港股)              |
| **5**  | 午盘(A\|港股) / 盘中(美股)     |
| **6**  | 交易日结束(A\|港股) / 已收盘(美股) |
| **8**  | 盘前开始(美股)               |
| **9**  | 盘前结束(美股)               |
| **10** | 盘后开始(美股)               |
| **11** | 盘后结束(美股)               |
| **12** | 内部状态，用于交易日切换           |
| **13** | 夜市交易中(港期货)             |
| **14** | 夜市收盘(港期货)              |
| **15** | 日市交易中(港期货)             |
| **16** | 日市午休(港期货)              |
| **17** | 日市收盘(港期货)              |
| **18** | 日市等待开盘(港期货)            |
| **19** | 港股盘后竞价                 |

3.23  **港股下单交易(**Protocol: 6003**)**

**C-\>S eg:**

{"Protocol":"6003","ReqParam":{"Cookie":"123456","EnvType":"0","OrderSide":"0","OrderType":"0","Price":"253600","Qty":"100","StockCode":"00700"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"6003","RetData":{"Cookie":"123456","EnvType":"0","LocalID":"2233082358006646","OrderID":"10486570","SvrResult":"0"},"Version":"1"}

字段说明:

| 字段名           | 字段值                                      | 备注         |
| ------------- | ---------------------------------------- | ---------- |
| Cookie        | Uint32                                   | 操作标识       |
| OrderSide     | 0: 买入 1: 卖出                              | 交易方向       |
| **OrderType** | **0： 增强限价单(普通交易) 1： 竞价单(竞价交易) 2：限价单 （暂不支持)**  **3： 竞价限价单(竞价限价)** | **交易类型**   |
| Price         | Int32                                    | 交易价格       |
| Qty           | Int64                                    | 交易数量       |
| LocalID       | Int64                                    | 订单的本地标识    |
| OrderID       | Int64                                    | 订单ID       |
| SvrResult     | int32                                    | Svr的返回结果   |
| **EnvType**   | **0=真实交易**  **1=仿真交易**                   | **交易环境参数** |

3.24  **港股设置订单状态(**Protocol: 6004**)**

**C-\>S eg:**

{"Protocol":"6004","ReqParam":{"Cookie":"33333","EnvType":"0","LocalID":"0","OrderID":"11283","SetOrderStatus":"0"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"6004","RetData":{"Cookie":"33333","EnvType":"0","LocalID":"0","OrderID":"11283","SvrResult":"0"},"Version":"1"}

字段说明:

| 字段名                | 字段值                         | 备注          |
| ------------------ | --------------------------- | ----------- |
| Cookie             |                             | 操作标识        |
| **SetOrderStatus** | **0: 撤单 1: 失效 2: 生效 3: 删除** | **更改状态的类型** |
| OrderID            | Int64                       | 定单id        |
| LocalID            | Int64                       | 订单的本地标识     |
| SvrResult          | Int32                       | Svr的返回结果    |
| **EnvType**        | **0=真实交易**  **1=仿真交易**      | **交易环境参数**  |
|                    |                             |             |

**注：OrderID、LocalID只用设一个非0有效值(因PlaceOrder只能返回LocalID),OrderID参数优先处理**

3.25  **港股修改订单(**Protocol: 6005**)**

**C-\>S eg:**

{"Protocol":"6005","ReqParam":{"Cookie":"654231","EnvType":"0","LocalID":"0","OrderID":"11283","Price":"365","Qty":"4000"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"6005","RetData":{"Cookie":"654231","EnvType":"0","LocalID":"0","OrderID":"11283","SvrResult":"0"},"Version":"1"}

字段说明:

| 字段名         | 字段值                    | 备注                            |
| ----------- | ---------------------- | ----------------------------- |
| Cookie      | Uint32                 | 请求操作标识，输入参数,为了区分一个连接中有多个同样的请求 |
| Price       | Int32                  | 修改的新价格                        |
| Qty         | Int64                  | 修改的新数量                        |
| OrderID     | Int64                  | 定单id                          |
| LocalID     | Int64                  | 订单的本地标识                       |
| SvrResult   | int32                  | Svr的返回结果                      |
| **EnvType** | **0=真实交易**  **1=仿真交易** | **交易环境参数**                    |
|             |                        |                               |

**注：OrderID、LocalID只用设一个非0有效值(因PlaceOrder只能返回LocalID),OrderID参数优先处理**

3.26  **解锁交易(**Protocol: 6006**)**

**C-\>S eg:**

{"Protocol":"6006","ReqParam":{"Cookie":"123456","Password":"123456"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"6006","RetData":{"Cookie":"123456","SvrResult":"0"},"Version":"1"}

字段说明:

| 字段名       | 字段值    | 备注                            |
| --------- | ------ | ----------------------------- |
| Cookie    | Uint32 | 请求操作标识，输入参数,为了区分一个连接中有多个同样的请求 |
| SvrResult | int32  | Svr的返回结果                      |
|           |        | 该接口会同时对美股和港股交易解锁              |

3.27  **港股查询帐户信息(**Protocol: 6007**)**

**C-\>S eg:**

{"Protocol":"6007","ReqParam":{"Cookie":"123456","EnvType":"0"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"6007","RetData":{"Cookie":"123456","DJZJ":"0","EnvType":"0","GPBZJ":"0","KQXJ":"0","Power":"0","XJJY":"0","YYJDE":"0","ZCJZ":"0","ZGJDE":"0","ZQSZ":"0","ZSJE":"0"},"Version":"1"}

字段说明:

| 字段名         | 字段值                    | 备注                                       |
| ----------- | ---------------------- | ---------------------------------------- |
| Cookie      | Uint32                 | 请求操作标识，输入参数,为了区分一个连接中有多个同样的请求            |
| **Power**   | **Int64**              | **现金账号的购买力，不适用于融资账号（因每支股票的融资额不同，融资账号的购买力由购买的股票决定）** |
| **ZCJZ**    | **Int64**              | **资产净值**                                 |
| **ZQSZ**    | **Int64**              | **证券市值**                                 |
| **XJJY**    | **Int64**              | **现金结余**                                 |
| **KQXJ**    | **Int64**              | **可取现金**                                 |
|             |                        |                                          |
| **DJZJ**    | **Int64**              | **冻结资金**                                 |
| **ZSJE**    | **Int64**              | **追收金额**                                 |
| **ZGJDE**   | **Int64**              | **最高借贷额**                                |
| **YYJDE**   | **Int64**              | **已用信贷额**                                |
| **GPBZJ**   | **Int64**              | **股票保证金**                                |
|             |                        |                                          |
| **EnvType** | **0=真实交易**  **1=仿真交易** | **交易环境参数**                               |
|             |                        |                                          |

3.28  **港股查询订单列表(**Protocol: 6008**)**

**C-\>S eg:**

{"Protocol":"6008","ReqParam":{"Cookie":"123123","EnvType":"0",
"StatusFilterStr": "0,1,2" },"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"6008","RetData":{"Cookie":"123123","EnvType":"0","HKOrderArr":[

{"DealtAvgPrice":"0","DealtQty":"0","ErrCode":"0","LocalID":"2827880381052386","OrderID":"18680","Price":"150000","Qty":"100","OrderSide":"1","Status":"1","StockCode":"00700","StockName":"腾讯控股",

"SubmitedTime":"1454485407","OrderType":"0","UpdatedTime":"1454485407"},{"DealtAvgPrice":"0",

"DealtQty":"0","ErrCode":"0","LocalID":"2827934046337573","OrderID":"18687","Price":"151000","Qty":"100","OrderSide":"1","Status":"1","StockCode":"00700","StockName":"腾讯控股","SubmitedTime":"1454485424"

,"OrderType":"0","UpdatedTime":"1454485424"}]},"Version":"1"}

字段说明:

| 字段名                 | 字段值                                      | 备注                                     |
| ------------------- | ---------------------------------------- | -------------------------------------- |
| **StatusFilterStr** | **String**                               | **状态过滤字符串, ",”号分隔需要返回的状态, 空字符串返回全部订单** |
| Cookie              | Uint32                                   | 请求操作标识，输入参数,为了区分一个连接中有多个同样的请求          |
| **DealtAvgPrice**   | **Int32**                                | **成交均价**                               |
| **DealtQty**        | **Int64**                                | **成交数量**                               |
| OrderID             | Int64                                    | 定单id                                   |
| LocalID             | Int64                                    | 订单的本地标识                                |
| Price               | Int32                                    | 订单价格                                   |
| Qty                 | Int64                                    | 订单数量                                   |
| OrderSide           | 0: 买入 1: 卖出                              | 交易方向                                   |
| **Status**          | **0 = 服务器处理中... 1 = 等待成交 2 = 部分成交 3 = 全部成交 4 = 已失效 5 = 下单失败**  **6 = 已撤单 7 = 已删除 8 = 等待开盘 21 = 本地已发送 22 = 本地已发送，服务器返回下单失败，没产生订单 23 = 本地已发送，等待服务器返回超时** | **订单状态**                               |
| StockCode           | string                                   | 股票代码                                   |
| StockName           | string                                   | 股票名称                                   |
| **SubmitedTime**    | **Int64**                                | **服务器收到的订单提交时间(GMT)**                  |
| **UpdatedTime**     | **Int64**                                | **订单最后更新的时间(GMT)**                     |
| **'OrderType'**     | **0： 增强限价单(普通交易) 1： 竞价单(竞价交易) 2：限价单 （暂不支持)**  **3： 竞价限价单(竞价限价)** | **交易类型**                               |
| **EnvType**         | **0=真实交易**  **1=仿真交易**                   | **交易环境参数**                             |
|                     |                                          |                                        |

3.29  **港股查询持仓列表(**Protocol: 6009**)**

**C-\>S eg:**

{"Protocol":"6009","ReqParam":{"Cookie":"123123","EnvType":"0"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"6009","RetData":{"Cookie":"123123","EnvType":"0","HKPositionArr"[

{"CanSellQty":"100","CostPrice":"140000","CostPriceValid":"1","MarketVal":"15000000","NominalPrice":"141000","PLRatio":"0","PLRatioValid":"1","PLVal":"0","PLValValid":"1","Qty":"100","StockCode":"00700","StockName":"腾讯控股","Today_BuyQty":"0","Today_BuyVal":"0","Today_PLVal":"0","Today_SellQty":"0",

"Today_SellVal":"0"},{"CanSellQty":"12000","CostPrice":"1953","CostPriceValid":"1","MarketVal":"9480000","NominalPrice":"790","PLRatio":"-54320","PLRatioValid":"1","PLVal":"-13960000","PLValValid":"1","Qty":"12000","StockCode":"00587","StockName":"华瀚健康","Today_BuyQty":"0","Today_BuyVal":"0","Today_PLVal"

:"0","Today_SellQty":"0","Today_SellVal":"0"},]},"Version":"1"}

字段说明:

| 字段名                | 字段值                    | 备注                                |
| ------------------ | ---------------------- | --------------------------------- |
| **Cookie**         | **Uint32**             | **请求操作标识，输入参数,为了区分一个连接中有多个同样的请求** |
| **Qty**            | **Int64**              | **持有数量**                          |
| **CanSellQty**     | **Int64**              | **可卖数量**                          |
| **NominalPrice**   | **Int32**              | **市价**                            |
| **MarketVal**      | **Int64**              | **市值**                            |
| **CostPrice**      | **Int32**              | **成本价**                           |
| **CostPriceValid** | **Int32 非0表求有效**       | **成本价是否有效**                       |
| **PLVal**          | **Int64**              | **盈亏金额**                          |
| **PLRatioValid**   | **Int32 非0表求有效**       | **盈亏金额是否有效**                      |
| **PLRatio**        | **Int32**              | **盈亏比例 (\*100000) eg: 1% = 1000** |
| **PLRatioValid**   | **Int32 非0表求有效**       | **盈亏比例是否有效**                      |
| **Today_PLVal**    | **Int64**              | **今日盈亏金额**                        |
| **Today_BuyQty**   | **Int64**              | **今日买入成交量**                       |
| **Today_BuyVal**   | **Int64**              | **今日买入成交额**                       |
| **Today_SellQty**  | **Int64**              | **今日卖出成交量**                       |
| **Today_SellVal**  | **Int64**              | **今日卖出成交额**                       |
| StockCode          | string                 | 股票代码                              |
| StockName          | string                 | 股票名称                              |
| **EnvType**        | **0=真实交易**  **1=仿真交易** | **交易环境参数**                        |
|                    |                        |                                   |

3.30  **港股查询成交记录(**Protocol:6010**)**

**C-\>S eg:**

{"Protocol":"6010","ReqParam":{"Cookie":"123123","EnvType":"0"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"6010","RetData":{"Cookie":"123123","EnvType":"0","HKDealArr":

[{"DealID":"2827880381052386","OrderID":"18680","Price":"150000","Qty":"100","Orderside":"1","StockCode":"00700","StockName":"腾讯控股","Time":"1454485407",}]},"Version":"1"}

字段说明:

| 字段名         | 字段值                                      | 备注                            |
| ----------- | ---------------------------------------- | ----------------------------- |
| Cookie      | Uint32                                   | 请求操作标识，输入参数,为了区分一个连接中有多个同样的请求 |
| OrderID     | Int64                                    | 定单id                          |
| DealID      | Int64                                    | 成交id                          |
| Price       | Int32                                    | 订单价格                          |
| Qty         | Int64                                    | 订单数量                          |
| OrderSide   | 0: 买入 1: 卖出                              | 交易方向                          |
| **Status**  | **0 = 服务器处理中... 1 = 等待成交 2 = 部分成交 3 = 全部成交 4 = 已失效 5 = 下单失败**  **6 = 已撤单 7 = 已删除 8 = 等待开盘 21 = 本地已发送 22 = 本地已发送，服务器返回下单失败，没产生订单 23 = 本地已发送，等待服务器返回超时** | **订单状态**                      |
| StockCode   | string                                   | 股票代码                          |
| StockName   | string                                   | 股票名称                          |
| **Time**    | **Int64**                                | **成交时间**                      |
| **EnvType** | **0=真实交易**  **1=仿真交易**                   | **交易环境参数**                    |

3.31  **美股下单交易(**Protocol: 7003**)**

**C-\>S eg:**

{"Protocol":"7003","ReqParam":{"Cookie":"123456","EnvType":"0","OrderSide":"0","OrderType":"2","Price":"153000","Qty":"1","StockCode":"AAPL"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"7003","RetData":{"Cookie":"123456","EnvType":"0","LocalID":"2237423408207425","OrderID":"2237423408207425","SvrResult":"0"},"Version":"1"}

字段说明:

| 字段名           | 字段值                                      | 备注         |
| ------------- | ---------------------------------------- | ---------- |
| Cookie        | Uint32                                   | 操作标识       |
| OrderSide     | 0: 买入 1: 卖出                              | 交易方向       |
| **OrderType** | **1: 市价单 2: 限价 51: 盘前交易，限价 52: 盘后交易，限价** | **交易类型**   |
| Price         | Int32                                    | 交易价格       |
| Qty           | Int64                                    | 交易数量       |
| LocalID       | Int64                                    | 订单的本地标识    |
| OrderID       | Int64                                    | 订单ID       |
| SvrResult     | int32                                    | Svr的返回结果   |
| **EnvType**   | **0=真实交易**  **美股暂不支持仿真交易！！**             | **交易环境参数** |
|               |                                          |            |

3.32  **美股设置订单状态(**Protocol: 7004**)**

**C-\>S eg:**

{"Protocol":"7004","ReqParam":{"Cookie":"33333","EnvType":"0","LocalID":"127958246102014","OrderID":"0","SetOrderStatus":"0"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"7004","RetData":{"Cookie":"33333","EnvType":"0","LocalID":"127958246102014","OrderID":"8105524018778112041","SvrResult":"0"},"Version":"1"}

字段说明:

| 字段名                | 字段值                          | 备注          |
| ------------------ | ---------------------------- | ----------- |
| Cookie             | Uint32                       | 操作标识        |
| **SetOrderStatus** | **0: 撤单 美股目前只支持撤单!!**        | **更改状态的类型** |
| OrderID            | Int64                        | 定单id        |
| LocalID            | Int64                        | 订单的本地标识     |
| SvrResult          | int32                        | Svr的返回结果    |
| **EnvType**        | **0=真实交易**  **美股暂不支持仿真交易！！** | **交易环境参数**  |
|                    |                              |             |

**注：OrderID、LocalID只用设一个非0有效值(因PlaceOrder只能返回LocalID),OrderID参数优先处理**

3.33  **美股修改订单(**Protocol: 7005**)**

**C-\>S eg:**

{"Protocol":"7005","ReqParam":{"Cookie":"654231","EnvType":"0","LocalID":"131717320241577","OrderID":"0","Price":"51500","Qty":"2000"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"7005","RetData":{"Cookie":"654231","EnvType":"0","LocalID":"131717320241577","OrderID":"7190271782920348012","SvrResult":"0"},"Version":"1"}

字段说明:

| 字段名         | 字段值                          | 备注                            |
| ----------- | ---------------------------- | ----------------------------- |
| Cookie      | Uint32                       | 请求操作标识，输入参数,为了区分一个连接中有多个同样的请求 |
| Price       | Int32                        | 修改的新价格                        |
| Qty         | Int64                        | 修改的新数量                        |
| OrderID     | Int64                        | 定单id                          |
| LocalID     | Int64                        | 订单的本地标识                       |
| SvrResult   | int32                        | Svr的返回结果                      |
| **EnvType** | **0=真实交易**  **美股暂不支持仿真交易！！** | **交易环境参数**                    |
|             |                              |                               |

**注：OrderID、LocalID只用设一个非0有效值(因PlaceOrder只能返回LocalID),OrderID参数优先处理**

3.34  **美股查询帐户信息(**Protocol: 7007**)**

**C-\>S eg:**

{"Protocol":"7007","ReqParam":{"Cookie":"123456","EnvType":"0"},"Version":"1"}

**S-\>C eg:**

{"EnvType":"0","Cookie":"123456","Power":"1000","ZCJZ":"1000","ZQSZ":"1000","XJJY":"1000","KQXJ":"1000","DJZJ":"0",
"ZSJE":"0", "ZGJDE":"0" ,"YYJDE":"0", "GPBZJ":"0"},"Version":"1"}

字段说明:

| 字段名         | 字段值                    | 备注                            |
| ----------- | ---------------------- | ----------------------------- |
| Cookie      | Uint32                 | 请求操作标识，输入参数,为了区分一个连接中有多个同样的请求 |
| **Power**   | **Int64**              | **购买力**                       |
| **ZCJZ**    | **Int64**              | **资产净值**                      |
| **ZQSZ**    | **Int64**              | **证券市值**                      |
| **XJJY**    | **Int64**              | **现金结余**                      |
| **KQXJ**    | **Int64**              | **可取现金**                      |
|             |                        |                               |
| **DJZJ**    | **Int64**              | **冻结资金**                      |
| **ZSJE**    | **Int64**              | **追收金额**                      |
| **ZGJDE**   | **Int64**              | **最高借贷额**                     |
| **YYJDE**   | **Int64**              | **已用信贷额**                     |
| **GPBZJ**   | **Int64**              | **股票保证金**                     |
|             |                        |                               |
| **EnvType** | **0=真实交易**  **1=仿真交易** | **交易环境参数**                    |
|             |                        | **目前的字段名称与港股完全一样！！**          |

3.35  **美股查询订单列表(**Protocol: 7008**)**

**C-\>S eg:**

{"Protocol":"7008","ReqParam":{"Cookie":"123123","EnvType":"0",
"StatusFilterStr": "0,1,2"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"7008","RetData":{"Cookie":"123123","EnvType":"0","USOrderArr":[

{"DealtAvgPrice":"65090","DealtQty":"100","ErrCode":"0","LocalID":"2850058438979314","OrderID":"5001812055423488114","OrderSide":"0","OrderType":"2","Price":"65090","Qty":"100","Status":"3","StockCode":"BABA","StockName":"阿里巴巴","SubmitedTime":"1454492354","UpdatedTime":"1454492354"},{"DealtAvgPrice"

:"94480","DealtQty":"200","ErrCode":"0","LocalID":"2850119943956001","OrderID":"948333054225995228","OrderSide":"0","OrderType":"2","Price":"94480","Qty":"200","Status":"3","StockCode":"AAPL","StockName":"苹果","SubmitedTime":"1454492373","UpdatedTime":"1454492373"}]},"Version":"1"}}

字段说明:

| 字段名                 | 字段值                                      | 备注                                     |
| ------------------- | ---------------------------------------- | -------------------------------------- |
| **StatusFilterStr** | **String**                               | **状态过滤字符串, ",”号分隔需要返回的状态, 空字符串返回全部订单** |
| Cookie              | Uint32                                   | 请求操作标识，输入参数,为了区分一个连接中有多个同样的请求          |
| **DealtAvgPrice**   | **Int32**                                | **成交均价**                               |
| **DealtQty**        | **Int64**                                | **成交数量**                               |
| OrderID             | Int64                                    | 定单id                                   |
| LocalID             | Int64                                    | 订单的本地标识                                |
| Price               | Int32                                    | 订单价格                                   |
| Qty                 | Int64                                    | 订单数量                                   |
| OrderSide           | 0: 买入 1: 卖出                              | 交易方向                                   |
| **Status**          | **0 = 服务器处理中... 1 = 等待成交 2 = 部分成交 3 = 全部成交 4 = 已失效 5 = 下单失败**  **6 = 已撤单 7 = 已删除 8 = 等待开盘 21 = 本地已发送 22 = 本地已发送，服务器返回下单失败，没产生订单 23 = 本地已发送，等待服务器返回超时** | **订单状态**                               |
| StockCode           | string                                   | 股票代码                                   |
| StockName           | string                                   | 股票名称                                   |
| **SubmitedTime**    | **Int64**                                | **服务器收到的订单提交时间(GMT)**                  |
| **UpdatedTime**     | **Int64**                                | **订单最后更新的时间(GMT)**                     |
| **OrderType**       | **1: 市价单 2: 限价 51: 盘前交易，限价 52: 盘后交易，限价** | **交易类型**                               |
| **EnvType**         | **0=真实交易**  **美股暂不支持仿真交易！！**             | **交易环境参数**                             |
|                     |                                          |                                        |

3.36  **美股查询持仓列表(**Protocol: 7009**)**

**C-\>S eg:**

{"Protocol":"7009","ReqParam":{"Cookie":"123123","EnvType":"0"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"7009","RetData":{"Cookie":"123123","EnvType":"0","USPositionArr"[

{"CanSellQty":"100","CostPrice":"65090","CostPriceValid":"1","MarketVal":"6509000","NominalPrice":"65090","PLRatio":"0","PLRatioValid":"1","PLVal":"0","PLValValid":"1","Qty":"100","StockCode":"BABA","StockName":"阿里巴巴","Today_BuyQty":"100","Today_BuyVal":"6509000","Today_PLVal":"0","Today_SellQty":"0",

"Today_SellVal":"0"},{"CanSellQty":"200","CostPrice":"94480","CostPriceValid":"1","MarketVal":"18896000"

,"NominalPrice":"94480","PLRatio":"0","PLRatioValid":"1","PLVal":"0","PLValValid":"1","Qty":"200","StockCode":"AAPL","StockName":"苹果","Today_BuyQty":"200","Today_BuyVal":"18896000","Today_PLVal":"0",

"Today_SellQty":"0","Today_SellVal":"0"}]},"Version":"1"}

字段说明:

| 字段名                | 字段值                          | 备注                                |
| ------------------ | ---------------------------- | --------------------------------- |
| **Cookie**         | **Uint32**                   | **请求操作标识，输入参数,为了区分一个连接中有多个同样的请求** |
| **Qty**            | **Int64**                    | **持有数量**                          |
| **CanSellQty**     | **Int64**                    | **可卖数量**                          |
| **NominalPrice**   | **Int32**                    | **市价**                            |
| **MarketVal**      | **Int64**                    | **市值**                            |
| **CostPrice**      | **Int32**                    | **成本价**                           |
| **CostPriceValid** | **Int32 非0表求有效**             | **成本价是否有效**                       |
| **PLVal**          | **Int64**                    | **盈亏金额**                          |
| **PLRatioValid**   | **Int32 非0表求有效**             | **盈亏金额是否有效**                      |
| **PLRatio**        | **Int32**                    | **盈亏比例 (\*100000) eg: 1% = 1000** |
| **PLRatioValid**   | **Int32 非0表求有效**             | **盈亏比例是否有效**                      |
| **Today_PLVal**    | **Int64**                    | **今日盈亏金额**                        |
| **Today_BuyQty**   | **Int64**                    | **今日买入成交量**                       |
| **Today_BuyVal**   | **Int64**                    | **今日买入成交额**                       |
| **Today_SellQty**  | **Int64**                    | **今日卖出成交量**                       |
| **Today_SellVal**  | **Int64**                    | **今日卖出成交额**                       |
| StockCode          | string                       | 股票代码                              |
| StockName          | string                       | 股票名称                              |
| **EnvType**        | **0=真实交易**  **美股暂不支持仿真交易！！** | **交易环境参数**                        |
|                    |                              |                                   |

3.37  **美股查询成交记录(**Protocol: 7010**)**

**C-\>S eg:**

{"Protocol":"7010","ReqParam":{"Cookie":"123123","EnvType":"0"},"Version":"1"}

**S-\>C eg:**

{"ErrCode":"0","ErrDesc":"","Protocol":"7010","RetData":{"Cookie":"123123","EnvType":"0","USDealArr":

[{"DealID":"2827880381052386","OrderID":"18680","Price":"150000","Qty":"100","Orderside":"1","StockCode":"BABA","StockName":"阿里巴巴","nTime":"1454485407",}]},"Version":"1"}

字段说明:

| 字段名         | 字段值                                      | 备注                            |
| ----------- | ---------------------------------------- | ----------------------------- |
| Cookie      | Uint32                                   | 请求操作标识，输入参数,为了区分一个连接中有多个同样的请求 |
| OrderID     | Int64                                    | 定单id                          |
| DealID      | Int64                                    | 成交id                          |
| Price       | Int32                                    | 订单价格                          |
| Qty         | Int64                                    | 订单数量                          |
| OrderSide   | 0: 买入 1: 卖出                              | 交易方向                          |
| **Status**  | **0 = 服务器处理中... 1 = 等待成交 2 = 部分成交 3 = 全部成交 4 = 已失效 5 = 下单失败**  **6 = 已撤单 7 = 已删除 8 = 等待开盘 21 = 本地已发送 22 = 本地已发送，服务器返回下单失败，没产生订单 23 = 本地已发送，等待服务器返回超时** | **订单状态**                      |
| StockCode   | string                                   | 股票代码                          |
| StockName   | string                                   | 股票名称                          |
| **Time**    | **Int64**                                | **成交时间**                      |
| **EnvType** | **0=真实交易**  **1=仿真交易**                   | **交易环境参数**                    |
