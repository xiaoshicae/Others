# --*-- coding:UTF-8 --*--
import random

common_alphabet = """
一 乙
二 十 丁 厂 七卜 人 入 八 九 几 儿 了 力乃刀又
三 于 干 亏 士 工 土 才 寸 下 大 丈 与 万 上 小 口 巾 山 千
乞 川 亿 个 勺 久 凡 及 夕 丸 么 广 亡 门 义 之 尸 弓 己 已
子 卫 也 女 飞 刃 习 叉 马 乡
丰 王 井 开 夫 天 无 元 专 云 扎 艺 木 五 支 厅 不 太 犬 区
历 尤 友 匹 车 巨 牙 屯 比 互 切 瓦 止 少 日 中 冈 贝 内 水
见 午 牛 手 毛 气 升 长 仁 什 片 仆 化 仇 币 仍 仅 斤 爪 反
介 父 从 今 凶 分 乏 公 仓 月 氏 勿 欠 风 丹 匀 乌 凤 勾 文
六 方 火 为 斗 忆 订 计 户 认 心 尺 引 丑 巴 孔 队 办 以 允
予 劝 双 书 幻
玉 刊 示 末 未 击 打 巧 正 扑 扒 功 扔 去 甘 世 古 节 本 术
汇 头 汉 宁 穴 它 讨 写 让 礼 训 必 议 讯 记 永 司 尼 民 出
汁 丙 左 厉 右 石 布 龙 平 灭 轧 东 卡 北 占 业 旧 帅 归 且
旦 目 叶 甲 申 叮 电 号 田 由 史 只 央 兄 叼 叫 另 叨 叹 四
生 失 禾 丘 付 仗 代 仙 们 仪 白 仔 他 斥 瓜 乎 丛 令 用 甩
印 乐 句 匆 册 犯 外 处 冬 鸟 务 包 饥 主 市 立 闪 兰 半辽
奶 奴 加 召 皮 边 发 孕 圣 对 台 矛 纠 母 幼 丝 可
式 刑 动 扛 寺 吉 扣 考 托 老 执 巩 圾 扩 扫 地 扬 场 耳 共
芒 亚 芝 朽 朴 机 权 过 臣 再 协 西 压 厌 在 有 百 存 而 页
匠 夸 夺 灰 达 列 死 成 夹 轨 邪 划 迈 毕 至 此 贞 师 尘 尖
劣 光 当 早 吐 吓 虫 曲 团 同 吊 吃 因 吸 吗 屿 帆 岁 回 岂
刚 则 肉 网 年 朱 先 丢 舌 竹 迁 乔 伟 传 乒 乓 休 伍 伏 优
伐 延 件 任 伤 价 份 华 仰 仿 伙 伪 自 血 向 似 后 行 舟 全
会 杀 合 兆 企 众 爷 伞 创 肌 朵 杂 危 旬 旨 负 各 名 多 争
色 壮 冲 冰 庄 庆 亦 刘 齐 交 次 衣 产 决 充 妄 闭 问 闯 羊
并 关 米 灯 州 汗 污 江 池 汤 忙 兴 宇 守 宅 字 安 讲 军 许
论 农 讽 设 访 寻 那 迅 尽 导 异 孙 阵 阳 收 阶 阴 防 奸 如
妇 好 她 妈 戏 羽 观 欢 买 红 纤 级 约 纪 驰 巡
寿 弄 麦 形 进 戒 吞 远 违 运 扶 抚 坛 技 坏 扰 拒 找 批 扯
址 走 抄 坝 贡 攻 赤 折 抓 扮 抢 孝 均 抛 投 坟 抗 坑 坊 抖
护 壳 志 扭 块 声 把 报 却 劫 芽 花 芹 芬 苍 芳 严 芦 劳 克
苏 杆 杠 杜 材 村 杏 极 李 杨 求 更 束 豆 两 丽 医 辰 励 否
还 歼 来 连 步 坚 旱 盯 呈 时 吴 助 县 里 呆 园 旷 围 呀 吨
足 邮 男 困 吵 串 员 听 吩 吹 呜 吧 吼 别 岗 帐 财 针 钉 告
我 乱 利 秃 秀 私 每 兵 估 体 何 但 伸 作 伯 伶 佣 低 你 住
位 伴 身 皂 佛 近 彻 役 返 余 希 坐 谷 妥 含 邻 岔 肝 肚 肠
龟 免 狂 犹 角 删 条 卵 岛 迎 饭 饮 系 言 冻 状 亩 况 床 库
疗 应 冷 这 序 辛 弃 冶 忘 闲 间 闷 判 灶 灿 弟 汪 沙 汽 沃
泛 沟 没 沈 沉 怀 忧 快 完 宋 宏 牢 究 穷 灾 良 证 启 评 补
初 社 识 诉 诊 词 译 君 灵 即 层 尿 尾 迟 局 改 张 忌 际 陆
阿 陈 阻 附 妙 妖 妨 努 忍 劲 鸡 驱 纯 纱 纳 纲 驳 纵 纷 纸
纹 纺 驴 纽
奉 玩 环 武 青 责 现 表 规 抹 拢 拔 拣 担 坦 押 抽 拐 拖 拍
者 顶 拆 拥 抵 拘 势 抱 垃 拉 拦 拌 幸 招 坡 披 拨 择 抬 其
取 苦 若 茂 苹 苗 英 范 直 茄 茎 茅 林 枝 杯 柜 析 板 松 枪
构 杰 述 枕 丧 或 画 卧 事 刺 枣 雨 卖 矿 码 厕 奔 奇 奋 态
欧 垄 妻 轰 顷 转 斩 轮 软 到 非 叔 肯 齿 些 虎 虏 肾 贤 尚
旺 具 果 味 昆 国 昌 畅 明 易 昂 典 固 忠 咐 呼 鸣 咏 呢 岸
岩 帖 罗 帜 岭 凯 败 贩 购 图 钓 制 知 垂 牧 物 乖 刮 秆 和
季 委 佳 侍 供 使 例 版 侄 侦 侧 凭 侨 佩 货 依 的 迫 质 欣
征 往 爬 彼 径 所 舍 金 命 斧 爸 采 受 乳 贪 念 贫 肤 肺 肢
肿 胀 朋 股 肥 服 胁 周 昏 鱼 兔 狐 忽 狗 备 饰 饱 饲 变 京
享 店 夜 庙 府 底 剂 郊 废 净 盲 放 刻 育 闸 闹 郑 券 卷 单
炒 炊 炕 炎 炉 沫 浅 法 泄 河 沾 泪 油 泊 沿 泡 注 泻 泳 泥
沸 波 泼 泽 治 怖 性 怕 怜 怪 学 宝 宗 定 宜 审 宙 官 空 帘
实 试 郎 诗 肩 房 诚 衬 衫 视 话 诞 询 该 详 建 肃 录 隶 居
届 刷 屈 弦 承 孟 孤 陕 降 限 妹 姑 姐 姓 始 驾 参 艰 线 练
组 细 驶 织 终 驻 驼 绍 经 贯
奏 春 帮 珍 玻 毒 型 挂 封 持 项 垮 挎 城 挠 政 赴 赵 挡 挺
括 拴 拾 挑 指 垫 挣 挤 拼 挖 按 挥 挪 某 甚 革 荐 巷 带 草
茧 茶 荒 茫 荡 荣 故 胡 南 药 标 枯 柄 栋 相 查 柏 柳 柱 柿
栏 树 要 咸 威 歪 研 砖 厘 厚 砌 砍 面 耐 耍 牵 残 殃 轻 鸦
皆 背 战 点 临 览 竖 省 削 尝 是 盼 眨 哄 显 哑 冒 映 星 昨
畏 趴 胃 贵 界 虹 虾 蚁 思 蚂 虽 品 咽 骂 哗 咱 响 哈 咬 咳
哪 炭 峡 罚 贱 贴 骨 钞 钟 钢 钥 钩 卸 缸 拜 看 矩 怎 牲 选
适 秒 香 种 秋 科 重 复 竿 段 便 俩 贷 顺 修 保 促 侮 俭 俗
俘 信 皇 泉 鬼 侵 追 俊 盾 待 律 很 须 叙 剑 逃 食 盆 胆 胜
胞 胖 脉 勉 狭 狮 独 狡 狱 狠 贸 怨 急 饶 蚀 饺 饼 弯 将 奖
哀 亭 亮 度 迹 庭 疮 疯 疫 疤 姿 亲 音 帝 施 闻 阀 阁 差 养
美 姜 叛 送 类 迷 前 首 逆 总 炼 炸 炮 烂 剃 洁 洪 洒 浇 浊
洞 测 洗 活 派 洽 染 济 洋 洲 浑 浓 津 恒 恢 恰 恼 恨 举 觉
宣 室 宫 宪 突 穿 窃 客 冠 语 扁 袄 祖 神 祝 误 诱 说 诵 垦
退 既 屋 昼 费 陡 眉 孩 除 险 院 娃 姥 姨 姻 娇 怒 架 贺 盈
勇 怠 柔 垒 绑 绒 结 绕 骄 绘 给 络 骆 绝 绞 统
耕 耗 艳 泰 珠 班 素 蚕 顽 盏 匪 捞 栽 捕 振 载 赶 起 盐 捎
捏 埋 捉 捆 捐 损 都 哲 逝 捡 换 挽 热 恐 壶 挨 耻 耽 恭 莲
莫 荷 获 晋 恶 真 框 桂 档 桐 株 桥 桃 格 校 核 样 根 索 哥
速 逗 栗 配 翅 辱 唇 夏 础 破 原 套 逐 烈 殊 顾 轿 较 顿 毙
致 柴 桌 虑 监 紧 党 晒 眠 晓 鸭 晃 晌 晕 蚊 哨 哭 恩 唤 啊
唉 罢 峰 圆 贼 贿 钱 钳 钻 铁 铃 铅 缺 氧 特 牺 造 乘 敌 秤
租 积 秧 秩 称 秘 透 笔 笑 笋 债 借 值 倚 倾 倒 倘 俱 倡 候
俯 倍 倦 健 臭 射 躬 息 徒 徐 舰 舱 般 航 途 拿 爹 爱 颂 翁
脆 脂 胸 胳 脏 胶 脑 狸 狼 逢 留 皱 饿 恋 桨 浆 衰 高 席 准
座 脊 症 病 疾 疼 疲 效 离 唐 资 凉 站 剖 竞 部 旁 旅 畜 阅
羞 瓶 拳 粉 料 益 兼 烤 烘 烦 烧 烛 烟 递 涛 浙 涝 酒 涉 消
浩 海 涂 浴 浮 流 润 浪 浸 涨 烫 涌 悟 悄 悔 悦 害 宽 家 宵
宴 宾 窄 容 宰 案 请 朗 诸 读 扇 袜 袖 袍 被 祥 课 谁 调 冤
谅 谈 谊 剥 恳 展 剧 屑 弱 陵 陶 陷 陪 娱 娘 通 能 难 预 桑
绢 绣 验 继
球 理 捧 堵 描 域 掩 捷 排 掉 堆 推 掀 授 教 掏 掠 培 接 控
探 据 掘 职 基 著 勒 黄 萌 萝 菌 菜 萄 菊 萍 菠 营 械 梦 梢
梅 检 梳 梯 桶 救 副 票 戚 爽 聋 袭 盛 雪 辅 辆 虚 雀 堂 常
匙 晨 睁 眯 眼 悬 野 啦 晚 啄 距 跃 略 蛇 累 唱 患 唯 崖 崭
崇 圈 铜 铲 银 甜 梨 犁 移 笨 笼 笛 符 第 敏 做 袋 悠 偿 偶
偷 您 售 停 偏 假 得 衔 盘 船 斜 盒 鸽 悉 欲 彩 领 脚 脖 脸
脱 象 够 猜 猪 猎 猫 猛 馅 馆 凑 减 毫 麻 痒 痕 廊 康 庸 鹿
盗 章 竟 商 族 旋 望 率 着 盖 粘 粗 粒 断 剪 兽 清 添 淋 淹
渠 渐 混 渔 淘 液 淡 深 婆 梁 渗 情 惜 惭 悼 惧 惕 惊 惨 惯
寇 寄 宿 窑 密 谋 谎 祸 谜 逮 敢 屠 弹 随 蛋 隆 隐 婚 婶 颈
绩 绪 续 骑 绳 维 绵 绸 绿
琴 斑 替 款 堪 搭 塔 越 趁 趋 超 提 堤 博 揭 喜 插 揪 搜 煮
援 裁 搁 搂 搅 握 揉 斯 期 欺 联 散 惹 葬 葛 董 葡 敬 葱 落
朝 辜 葵 棒 棋 植 森 椅 椒 棵 棍 棉 棚 棕 惠 惑 逼 厨 厦 硬
确 雁 殖 裂 雄 暂 雅 辈 悲 紫 辉 敞 赏 掌 晴 暑 最 量 喷 晶
喇 遇 喊 景 践 跌 跑 遗 蛙 蛛 蜓 喝 喂 喘 喉 幅 帽 赌 赔 黑
铸 铺 链 销 锁 锄 锅 锈 锋 锐 短 智 毯 鹅 剩 稍 程 稀 税 筐
等 筑 策 筛 筒 答 筋 筝 傲 傅 牌 堡 集 焦 傍 储 奥 街 惩 御
循 艇 舒 番 释 禽 腊 脾 腔 鲁 猾 猴 然 馋 装 蛮 就 痛 童 阔
善 羡 普 粪 尊 道 曾 焰 港 湖 渣 湿 温 渴 滑 湾 渡 游 滋 溉
愤 慌 惰 愧 愉 慨 割 寒 富 窜 窝 窗 遍 裕 裤 裙 谢 谣 谦 属
屡 强 粥 疏 隔 隙 絮 嫂 登 缎 缓 编 骗 缘
瑞 魂 肆 摄 摸 填 搏 塌 鼓 摆 携 搬 摇 搞 塘 摊 蒜 勤 鹊 蓝
墓 幕 蓬 蓄 蒙 蒸 献 禁 楚 想 槐 榆 楼 概 赖 酬 感 碍 碑 碎
碰 碗 碌 雷 零 雾 雹 输 督 龄 鉴 睛 睡 睬鄙愚暖 盟 歇 暗
照 跨 跳 跪 路 跟 遣 蛾 蜂 嗓 置 罪 罩 错 锡 锣 锤 锦 键 锯
矮 辞 稠 愁 筹 签 简 毁 舅 鼠 催 傻 像 躲 微 愈 遥 腰 腥 腹
腾 腿 触 解 酱 痰 廉 新 韵 意 粮 数 煎 塑 慈 煤 煌 满 漠 源
滤 滥 滔 溪 溜 滚 滨 粱 滩 慎 誉 塞 谨 福 群 殿 辟 障 嫌 嫁
叠 缝 缠
静 碧 璃 墙 撇 嘉 摧 截 誓 境 摘 摔 聚 蔽 慕 暮 蔑 模 榴 榜
榨 歌 遭 酷 酿 酸 磁 愿 需 弊 裳 颗 嗽 蜻 蜡 蝇 蜘 赚 锹 锻
舞 稳 算 箩 管 僚 鼻 魄 貌 膜 膊 膀 鲜 疑 馒 裹 敲 豪 膏 遮
腐 瘦 辣 竭 端 旗 精 歉 熄 熔 漆 漂 漫 滴 演 漏 慢 寨 赛 察
蜜 谱 嫩 翠 熊 凳 骡 缩
慧 撕 撒 趣 趟 撑 播 撞 撤 增 聪 鞋 蕉 蔬 横 槽 樱 橡 飘 醋
醉 震 霉 瞒 题 暴 瞎 影 踢 踏 踩 踪 蝶 蝴 嘱 墨 镇 靠 稻 黎
稿 稼 箱 箭 篇 僵 躺 僻 德 艘 膝 膛 熟 摩 颜 毅 糊 遵 潜 潮
懂 额 慰 劈
操 燕 薯 薪 薄 颠 橘 整 融 醒 餐 嘴 蹄 器 赠 默 镜 赞 篮 邀
衡 膨 雕 磨 凝 辨 辩 糖 糕 燃 澡 激 懒 壁 避 缴
戴 擦 鞠 藏 霜 霞 瞧 蹈 螺 穗 繁 辫 赢 糟 糠 燥 臂 翼 骤
鞭 覆 蹦 镰 翻 鹰
警 攀 蹲 颤 瓣 爆 疆
壤 耀 躁 嚼 嚷 籍 魔 灌
蠢 霸 露
囊
罐
"""

second_common_alphabet = """
匕 刁
丐 歹 戈 夭 仑 讥 冗 邓
艾 夯 凸 卢 叭 叽 皿 凹 囚 矢 乍 尔 冯 玄
邦 迂 邢 芋 芍 吏 夷 吁 吕 吆 屹 廷 迄 臼 仲 伦 伊 肋 旭 匈
凫 妆 亥 汛 讳 讶 讹 讼 诀 弛 阱 驮 驯 纫
玖 玛 韧 抠 扼 汞 扳 抡 坎 坞 抑 拟 抒 芙 芜 苇 芥 芯 芭 杖
杉 巫 杈 甫 匣 轩 卤 肖 吱 吠 呕 呐 吟 呛 吻 吭 邑 囤 吮 岖
牡 佑 佃 伺 囱 肛 肘 甸 狈 鸠 彤 灸 刨 庇 吝 庐 闰 兑 灼 沐
沛 汰 沥 沦 汹 沧 沪 忱 诅 诈 罕 屁 坠 妓 姊 妒 纬
玫 卦 坷 坯 拓 坪 坤 拄 拧 拂 拙 拇 拗 茉 昔 苛 苫 苟 苞 茁
苔 枉 枢 枚 枫 杭 郁 矾 奈 奄 殴 歧 卓 昙 哎 咕 呵 咙 呻 咒
咆 咖 帕 账 贬 贮 氛 秉 岳 侠 侥 侣 侈 卑 刽 刹 肴 觅 忿 瓮
肮 肪 狞 庞 疟 疙 疚 卒 氓 炬 沽 沮 泣 泞 泌 沼 怔 怯 宠 宛
衩 祈 诡 帚 屉 弧 弥 陋 陌 函 姆 虱 叁 绅 驹 绊 绎
契 贰 玷 玲 珊 拭 拷 拱 挟 垢 垛 拯 荆 茸 茬 荚 茵 茴 荞 荠
荤 荧 荔 栈 柑 栅 柠 枷 勃 柬 砂 泵 砚 鸥 轴 韭 虐 昧 盹 咧
昵 昭 盅 勋 哆 咪 哟 幽 钙 钝 钠 钦 钧 钮 毡 氢 秕 俏 俄 俐
侯 徊 衍 胚 胧 胎 狰 饵 峦 奕 咨 飒 闺 闽 籽 娄 烁 炫 洼 柒
涎 洛 恃 恍 恬 恤 宦 诫 诬 祠 诲 屏 屎 逊 陨 姚 娜 蚤 骇
耘 耙 秦 匿 埂 捂 捍 袁 捌 挫 挚 捣 捅 埃 耿 聂 荸 莽 莱 莉
莹 莺 梆 栖 桦 栓 桅 桩 贾 酌 砸 砰 砾 殉 逞 哮 唠 哺 剔 蚌
蚜 畔 蚣 蚪 蚓 哩 圃 鸯 唁 哼 唆 峭 唧 峻 赂 赃 钾 铆 氨 秫
笆 俺 赁 倔 殷 耸 舀 豺 豹 颁 胯 胰 脐 脓 逛 卿 鸵 鸳 馁 凌
凄 衷 郭 斋 疹 紊 瓷 羔 烙 浦 涡 涣 涤 涧 涕 涩 悍 悯 窍 诺
诽 袒 谆 祟 恕 娩 骏
琐 麸 琉 琅 措 捺 捶 赦 埠 捻 掐 掂 掖 掷 掸 掺 勘 聊 娶 菱
菲 萎 菩 萤 乾 萧 萨 菇 彬 梗 梧 梭 曹 酝 酗 厢 硅 硕 奢 盔
匾 颅 彪 眶 晤 曼 晦 冕 啡 畦 趾 啃 蛆 蚯 蛉 蛀 唬 啰 唾 啤
啥 啸 崎 逻 崔 崩 婴 赊 铐 铛 铝 铡 铣 铭 矫 秸 秽 笙 笤 偎
傀 躯 兜 衅 徘 徙 舶 舷 舵 敛 翎 脯 逸 凰 猖 祭 烹 庶 庵 痊
阎 阐 眷 焊 焕 鸿 涯 淑 淌 淮 淆 渊 淫 淳 淤 淀 涮 涵 惦 悴
惋 寂 窒 谍 谐 裆 袱 祷 谒 谓 谚 尉 堕 隅 婉 颇 绰 绷 综 绽
缀 巢
琳 琢 琼 揍 堰 揩 揽 揖 彭 揣 搀 搓 壹 搔 葫 募 蒋 蒂 韩 棱
椰 焚 椎 棺 榔 椭 粟 棘 酣 酥 硝 硫 颊 雳 翘 凿 棠 晰 鼎 喳
遏 晾 畴 跋 跛 蛔 蜒 蛤 鹃 喻 啼 喧 嵌 赋 赎 赐 锉 锌 甥 掰
氮 氯 黍 筏 牍 粤 逾 腌 腋 腕 猩 猬 惫 敦 痘 痢 痪 竣 翔 奠
遂 焙 滞 湘 渤 渺 溃 溅 湃 愕 惶 寓 窖 窘 雇 谤 犀 隘 媒 媚
婿 缅 缆 缔 缕 骚
瑟 鹉 瑰 搪 聘 斟 靴 靶 蓖 蒿 蒲 蓉 楔 椿 楷 榄 楞 楣 酪 碘
硼 碉 辐 辑 频 睹 睦 瞄 嗜 嗦 暇 畸 跷 跺 蜈 蜗 蜕 蛹 嗅 嗡
嗤 署 蜀 幌 锚 锥 锨 锭 锰 稚 颓 筷 魁 衙 腻 腮 腺 鹏 肄 猿
颖 煞 雏 馍 馏 禀 痹 廓 痴 靖 誊 漓 溢 溯 溶 滓 溺 寞 窥 窟
寝 褂 裸 谬 媳 嫉 缚 缤 剿
赘 熬 赫 蔫 摹 蔓 蔗 蔼 熙 蔚 兢 榛 榕 酵 碟 碴 碱 碳 辕 辖
雌 墅 嘁 踊 蝉 嘀 幔 镀 舔 熏 箍 箕 箫 舆 僧 孵 瘩 瘟 彰 粹
漱 漩 漾 慷 寡 寥 谭 褐 褪 隧 嫡 缨
撵 撩 撮 撬 擒 墩 撰 鞍 蕊 蕴 樊 樟 橄 敷 豌 醇 磕 磅 碾 憋
嘶 嘲 嘹 蝠 蝎 蝌 蝗 蝙 嘿 幢 镊 镐 稽 篓 膘 鲤 鲫 褒 瘪 瘤
瘫 凛 澎 潭 潦 澳 潘 澈 澜 澄 憔 懊 憎 翩 褥 谴 鹤 憨 履 嬉
豫 缭
撼 擂 擅 蕾薛薇擎 翰 噩 橱 橙 瓢 磺 霍 霎 辙 冀 踱 蹂 蟆
螃 螟 噪 鹦 黔 穆 篡 篷 篙 篱 儒 膳 鲸 瘾 瘸 糙 燎 濒 憾 懈
窿 缰
壕 藐 檬 檐 檩 檀 礁 磷 瞭 瞬 瞳 瞪 曙 蹋 蟋 蟀 嚎 赡 镣 魏
簇 儡 徽 爵 朦 臊 鳄 糜 癌 懦 豁 臀
藕 藤 瞻 嚣 鳍 癞 瀑 襟 璧 戳
攒 孽 蘑 藻 鳖 蹭 蹬 簸 簿 蟹 靡 癣 羹
鬓 攘 蠕 巍 鳞 糯 譬
霹 躏 髓
蘸 镶 瓤
矗
"""

rarely_used_alphabet = """
厷厸厹厺厼厽厾叀叁参叄叅叆叇亝
収叏叐叒叓叕叚叜叝叞
叧叨叭叱叴叵叺叻叼叽叾卟叿吀吁吂吅吆吇吋吒吔吖吘吙吚吜吡吢吣吤吥吧吩吪吭吮吰吱吲呐吷吺吽呁呃呄呅呇呉呋呋呌呍呎呏呐呒呓呔呕呗呙呚呛呜呝呞呟呠呡呢呣呤呥呦呧周呩呪呫呬呭呮呯呰呱呲呴呶呵呷呸呹呺呻呾呿咀咁咂咃咄咅咇咈咉咊咋咍咎咐咑咓咔咕咖咗咘咙咚咛咜咝咞咟咠咡咢咣咤咥咦咧咨咩咪咫咬咭咮咯咰咲咳咴咵咶啕咹咺咻呙咽咾咿哂哃哅哆哇哈哊哋哌哎哏哐哑哒哓哔哕哖哗哘哙哚哛哜哝哞哟哠咔哣哤哦哧哩哪哫哬哯哰唝哵哶哷哸哹哻哼哽哾哿唀唁唂唃呗唅唆唈唉唊唋唌唍唎唏唑唒唓唔唣唖唗唘唙吣唛唜唝唞唟唠唡唢唣唤唥唦唧唨唩唪唫唬唭唯唰唲唳唴唵唶唷念唹唺唻唼唽唾唿啀啁啃啄啅啇啈啉啋啌啍啎问啐啑啒启啔啕啖啖啘啙啚啛啜啝哑启啠啡唡衔啥啦啧啨啩啪啫啬啭啮啯啰啱啲啳啴啵啶啷啹啺啻啽啾啿喀喁喂喃善喅喆喇喈喉喊喋喌喍喎喏喐喑喒喓喔喕喖喗喙喛喞喟喠喡喢喣喤喥喦喨喩喯喭喯喰喱哟喳喴喵営喷喸喹喺喼喽喾喿嗀嗁嗂嗃嗄嗅呛啬嗈嗉唝嗋嗌嗍吗嗏嗐嗑嗒嗓嗕嗖嗗嗘嗙呜嗛嗜嗝嗞嗟嗠嗡嗢嗧嗨唢嗪嗫嗬嗭嗮嗰嗱嗲嗳嗴嗵哔嗷嗸嗹嗺嗻嗼嗽嗾嗿嘂嘃嘄嘅嘅嘇嘊嘋嘌喽嘎嘏嘐嘑嘒嘓嘕啧嘘嘙嘚嘛唛嘝嘠嘡嘢嘣嘤嘥嘦嘧嘨哗嘪嘫嘬嘭唠啸囍嘴哓嘶嘷呒嘹嘺嘻嘼啴嘾嘿噀噂噃噄咴噆噇噈噉噊噋噌噍噎噏噐噑噒嘘噔噕噖噗噘噙噚噛噜咝噞噟哒噡噢噣噤哝哕噧噩噪噫噬噭噮嗳噰噱哙噳喷噵噶噷吨噺噻噼噽噾噿咛嚁嚂嚃嚄嚅嚆吓嚈嚉嚊嚋哜嚍嚎嚏尝嚑嚒嚓嚔噜嚖嚗嚘啮嚚嚛嚜嚝嚞嚟嚠嚡嚢嚣嚤呖嚧咙嚩咙嚧嚪嚫嚬嚭嚯嚰嚱亸喾嚵嘤嚷嚸嚹嚺嚻嚼嚽嚾嚿啭嗫嚣囃囄冁囆囇呓囊囋囍囎囏囐嘱囒啮囔囕囖
囘囙囜囝囟囡団囤囥囦囧囨囩囱囫囬囮囯困囱囲図囵囶囷囸囹囻囼图囿圀圁圂圂圃圄圅圆囵圈圉圊圌圎圏圎圐圑圔圕图圗圙圚圛圜圝圞凹凸
圠圡圢圤圥圦圧圩圪圫圬圮圯地圱圲圳圴圵圶圷圸圹圻圼埢鴪址坁坂坃坄坅坆坈坉坊坋坌坍坒坓坔坕坖坘坙坜坞坢坣坥坧坨坩坪坫坬坭坮坯垧坱坲坳坴坶坸坹坺坻坼坽坾坿垀垁垃垅垆垇垈垉垊垌垍垎垏垐垑垓垔垕垖垗垘垙垚垛垜垝垞垟垠垡垤垥垧垨垩垪垫垬垭垮垯垰垱垲垲垳垴埯垶垷垸垹垺垺垻垼垽垾垽垿埀埁埂埃埄埅埆埇埈埉埊埋埌埍城埏埐埑埒埓埔埕埖埗埘埙埚埛野埝埞域埠垭埢埣埤埥埦埧埨埩埪埫埬埭埮埯埰埱埲埳埴埵埶执埸培基埻崎埽埾埿堀堁堃堄坚堇堈堉垩堋堌堍堎堏堐堑堒堓堔堕垴堗堘堙堚堛堜埚堞堟堠堢堣堥堦堧堨堩堫堬堭堮尧堰报堲堳场堶堷堸堹堺堻堼堽堾堼堾碱塀塁塂塃塄塅塇塆塈塉块茔塌塍塎垲塐塑埘塓塕塖涂塘塙冢塛塜塝塟塠墘塣墘塥塦塧塨塩塪填塬塭塮塯塰塱塲塳塴尘塶塷塸堑塺塻塼塽塾塿墀墁墂墄墅墆墇墈墉垫墋墌墍墎墏墐墒墒墓墔墕墖墘墖墚墛坠墝增墠墡墢墣墤墥墦墧墨墩墪樽墬墭堕墯墰墱墲坟墴墵垯墷墸墹墺墙墼墽垦墿壀壁壂壃壄壅壆坛壈壉壊垱壌壍埙壏壐壑壒压壔壕壖壗垒圹垆壛壜壝垄壠壡坜壣壤壥壦壧壨坝塆圭
壭壱売壳壴壵壶壷壸壶壻壸壾壿夀夁
夃夅夆夈変夊夌夎夐夑夒夓夔夗夘夛夝夞夡夣夤夥夦
夨夨夬夯夰夲夳夵夶夹夻夼夽夹夿奀奁奃奂奄奃奅奆奊奌奍奏奂奒奓奘奙奚奛奜奝奞奟奡奣奤奦奨奁奫妸奯奰奱奲
奵奺奻奼奾奿妀妁妅妉妊妋妌妍妎妏妐妑妔妕妗妘妚妛妜妟妠妡妢妤妦妧妩妫妭妮妯妰妱妲妴妵妶妷妸妺妼妽妿姀姁姂姃姄姅姆姇姈姉姊姌姗姎姏姒姕姖姘姙姛姝姞姟姠姡姢姣姤姥奸姧姨姩姫姬姭姮姯姰姱姲姳姴姵姶姷姸姹姺姻姼姽姾娀威娂娅娆娈娉娊娋娌娍娎娏娐娑娒娓娔娕娖娗娙娚娱娜娝娞娟娠娡娢娣娤娥娦娧娨娩娪娫娬娭娮娯娰娱娲娳娴娵娷娸娹娺娻娽娾娿婀娄婂婃婄婅婇婈婋婌婍婎婏婐婑婒婓婔婕婖婗婘婙婛婜婝婞婟婠婡婢婣婤婥妇婧婨婩婪婫娅婮婯婰婱婲婳婵婷婸婹婺婻婼婽婾婿媀媁媂媄媃媅媪媈媉媊媋媌媍媎媏媐媑媒媓媔媕媖媗媘媙媚媛媜媝媜媞媟媠媡媢媣媤媥媦媨媩媪媫媬媭妫媰媱媲媳媴媵媶媷媸媹媺媻媪媾嫀嫃嫄嫅嫆嫇嫈嫉嫊袅嫌嫍嫎嫏嫐嫑嫒嫓嫔嫕嫖妪嫘嫙嫚嫛嫜嫝嫞嫟嫠嫡嫢嫣嫤嫥嫦嫧嫨嫧嫩嫪嫫嫬嫭嫮嫯嫰嫱嫲嫳嫴嫳妩嫶嫷嫸嫹嫺娴嫼嫽嫾婳妫嬁嬂嬃嬄嬅嬆嬇娆嬉嬊娇嬍嬎嬏嬐嬑嬒嬓嬔嬕嬖嬗嬘嫱嬚嬛嬜嬞嬟嬠嫒嬢嬣嬥嬦嬧嬨嬩嫔嬫嬬奶嬬嬮嬯婴嬱嬲嬳嬴嬵嬶嬷婶嬹嬺嬻嬼嬽嬾嬿孀孁孂娘孄孅孆孇孆孈孉孊娈孋孊孍孎孏嫫婿媚
孑孒孓孖孚孛孜孞孠孡孢孥孧孨孪孙孬孭孮孯孰孱孲孳孴孵孶孷孹孻孼孽孾
宄宆宊宍宎宐宑宒宓宔宖実宥宧宨宩宬宭宯宱宲宷宸宺宻宼寀寁寃寈寉寊寋寍寎寏寔寕寖寗寘寙寚寜寝寠寡寣寥寪寭寮寯寰寱寲寳寴寷
寽対尀専尃尅尌
尐尒尕尗尛尜尞尟尠
尣尢尥尦尨尩尪尫尬尭尮尯尰尲尳尴尵尶
屃屇屐屒屓屔屖屗屘屙屚屛屉扉屟屡屣履屦屧屦屩屪屫
敳屮屰屲屳屴屵屶屷屸屹屺屻屼屽屾岃岄岅岆岇岈岉岊岋岌岍岎岏岐岑岒岓岔岕岖岘岙岚岜岝岞岟岠岗岢岣岤岥岦岧岨岪岫岬岮岯岰岲岴岵岶岷岹岺岻岼岽岾岿峀峁峂峃峄峅峆峇峈峉峊峋峌峍峎峏峐峑峒峓崓峖峗峘峚峙峛峜峝峞峟峠峢峣峤峥峦峧峨峩峪峬峫峭峮峯峱峲峳岘峵峷峸峹峺峼峾峿崀崁崂崃崄崅崆崇崈崉崊崋崌崃崎崏崐崒崓崔崕崖崘崚崛崜崝崞崟岽崡峥崣崤崥崦崧崨崩崪崫崬崮崯崰崱崲嵛崴崵崶崷崸崹崺崻崼崽崾崿嵀嵁嵂嵃嵄嵅嵆嵇嵈嵉嵊嵋嵌嵍嵎嵏岚嵑岩嵓嵔嵕嵖嵗嵘嵙嵚嵛嵜嵝嵞嵟嵠嵡嵢嵣嵤嵥嵦嵧嵨嵩嵪嵫嵬嵭嵮嵯嵰嵱嵲嵳嵴嵵嵶嵷嵸嵹嵺嵻嵼嵽嵾嵿嶀嵝嶂嶃崭嶅嶆岖嶈嶉嶊嶋嶌嶍嶎嶏嶐嶑嶒嶓嵚嶕嶖嶘嶙嶚嶛嶜嶝嶞嶟峤嶡峣嶣嶤嶥嶦峄峃嶩嶪嶫嶬嶭崄嶯嶰嶱嶲嶳岙嶵嶶嶷嵘嶹岭嶻屿岳帋巀巁巂巃巄巅巆巇巈巉巊岿巌巍巎巏巐巑峦巓巅巕岩巗巘巙巚
巛巜巠巡巢巣巤匘
巪巬巭巯
巵巶巸卺巺巼巽
巿帀帄帇帉帊帋帍帎帏帑帒帓帔帗帙帚帞帟帠帡帢帣帤帨帩帪帬帯帰帱帲帴帵帷帹帺帻帼帽帾帿幁幂帏幄幅幆幇幈幉幊幋幌幍幎幏幐幑幒幓幖幙幚幛幜幝幞帜幠幡幢幤幥幦幧幨幩幪幭幮幯幰幱
幷
幺吆玄兹滋
庀庁仄広庅庇庈庉庋庌庍庎庑庖庘庛庝庠庡庢庣庤庥庨庩庪庬庮庯庰庱庲庳庴庵庹庺庻庼庽庿廀厕廃厩廅廆廇廋廌廍庼廏廐廑廒廔廕廖廗廘廙廛廜廞庑廤廥廦廧廨廭廮廯廰痈廲
廵廸廹廻廼廽
廿弁弅弆弇弉
弋弌弍弎弐弑
弖弙弚弜弝弞弡弢弣弤弨弩弪弫弬弭弮弰弲弪弴弶弸弻弼弽弿彀彁彂彃彄彅彇彉彋弥彍彏
彑彔彖彗彘彚彛彜彝彞彟
彡彣彧彨彭彮彯彲澎
彳彴彵彶彷彸役彺彻彽彾佛徂徃徆徇徉后徍徎徏径徒従徔徕徖徙徚徛徜徝从徟徕御徢徣徤徥徦徧徨复循徫旁徭微徯徰徱徲徳徴徵徶德徸彻徺徻徼徽徾徿忀忁忂
忄惔愔忇忈忉忊忋忎忏忐忑忒忓忔忕忖忚忛応忝忞忟忡忢忣忥忦忨忩忪忬忭忮忯忰忱忲忳忴念忶汹忸忹忺忻忼忾忿怂怃怄怅怆怇怈怉怊怋怌怍怏怐怑怓怔怗怘怙怚怛怞怟怡怢怣怤怦怩怫怬怭怮怯怰怲怳怴怵怶怷怸怹怺怼悙怿恀恁恂恃恄恅恒恇恈恉恊恌恍恎恏恑恒恓恔恖恗恘恙恚恛恜恝恞恠恡恦恧恫恬恮恰恱恲恴恷恹恺恻恽恾恿悀悁悂悃悆悇悈悊悋悌悍悎悏悐悑悒悓悕悖悗悘悙悚悛悜悝悞悟悡悢悤悥悧悩悪悫悭悮悰悱悳悴悷悹悺悻悼悾悿惀惁惂惃惄惆惈惉惊惋惌惍惎惏惐惑惒惓惔惕惖惗惘惙惚惛惜惝惞惠恶惢惣惤惥惦惧惨惩惪惫惬惮恼恽惴惵惶惸惺惼惽惾惿愀愂愃愄愅愆愇愉愊愋愌愍愎愐愑愒愓愕愖愗愘愙愝愞愠愡愢愣愥愦愧愩愪愫愬愭愮愯愰愱愲愳怆愵愶恺愸愹愺愻愼愽忾愿慀慁慂慃栗慅慆慈慉慊态慏慐慑慒慓慔慖慗惨慙惭慛慜慝慞恸慠慡慢慥慦慧慨慩怄怂慬悯慯慰慲悭慴慵慷慸慹慺慻慽慿憀憁忧憃憄憅憆憇憈憉惫憋憌憍憎憏怜憓憔憕憖憗憘憙憛憜憝憞憟憠憡憢憣愤憥憦憧憨憩憪憬憭怃憯憰憱憳憴憵忆憷憸憹憺憻憼憽憾憿懀懁懂懄懅懆恳懈懊懋怿懔懎懏懐懑懓懔懕懖懗懘懙懚懛懜懝怼懠懡懢懑懤懥懦懧恹懩懪懫懬懭懮懯懰懱惩懳懴懵懒怀悬懹忏懻惧懽慑懿恋戁戂戃戄戅戆懯
戉戊戋戌戍戎戓戋戕彧或戗戙戛戜戝戞戟戠戡戢戣戤戥戦戗戨戬截戫戭戮戱戳戴戵戈戚残牋
戸戹戺戻戼戽戾扂扃扄扅扆扈扊
扏扐払扖扗扙扚扜扝扞扟扠扦扢扣扤扥扦扨扪扭扮扰扲扴扵扷扸抵扻扽抁挸抆抇抈抉抋抌抍抎抏抐抔抖抙抝択抟抠抡抣护抦抧抨抩抪抬抮抰抲抳抵抶抷抸抹抺押抻抾抿拀拁拃拄拇拈拊拎拏拑拓拕拗拘拙拚拝拞拠拡拢拣拤拧择拪拫括拭拮拯拰拱拲拳拴拵拶拷拸拹拺拻拼拽拾拿挀挂挃挄挅挆挈挊挋挌挍挎挏挐挒挓挔挕挗挘挙挚挛挜挝挞挟挠挡挢挣挦挧挨挩挪挫挬挭挮挰挱挲挳挴挵挷挸挹挺挻挼挽挿捀捁捂捃捄捅捆捇捈捊捋捌捍捎捏捐捑捒捓捔捕捖捗捘捙捚捛捜捝捞损捠捡换捣捤捥捦捧舍捩捪扪捬捭据捯捰捱捳捴捵捶捷捸捹捺捻捼捽捾捿掀掁掂扫抡掅掆掇授掉掊掋掍掎掐掑排掓掔掕挜掖掘挣掚挂掜掝掞掟掠采探掣掤掦措掫掬掭掮掯掰掱掲掳掴掵掶掸掹掺掻掼掽掾掿拣揁揂揃揅揄揆揇揈揉揊揋揌揍揎揑揓揔揕揖揗揘揙揜揝揞揟揠揢揤揥揦揧揨揫捂揰揱揲揳援揵揶揷揸揻揼揾揿搀搁搂搃搄搅搇搈搉搊搋搌搎搏搐搑搒搓搔搕搘搙搚搛搝擀搠搡搢搣搤捶搦搧搨搩搪搫搬搮搰搱搲搳搴搵搷搸搹搻搼搽榨搿摂摅摈摉摋摌摍摎摏摐掴摒摓摔摕摖摗摙摚摛掼摝摞摠摡摢揸摤摥摦摧摨摪摫摬摭摮挚摰摱摲抠摴摵抟摷摹摺掺摼摽摾摿撀撁撂撃撄撅撉撊撋撌撍撎挦挠撒挠撔撖撗撘撙捻撛撜撝挢撠撡掸掸撧撨撩撪撬撮撯撱揿撴撵撶撷撸撹撺挞撼撽挝擀擃掳擅擆擈擉擌擎擏擐擑擓擕擖擗擘擙擛擜擝擞擟擡擢擤擥擧擨擩擪擫擭擮摈擳擵擶撷擸擹擽擿攁攂攃摅攅撵攇攈攉攊攋攌攍攎拢攐攑攒攓攕撄攗攘搀攚撺攞攟攠攡攒挛攥攦攧攨攩搅攫攭攮
攰攱攲攳攴攵攸攺攼攽敀敁敂敃敄敆敇敉敊敋敍敐敒敓敔敕敖敚敜敟敠敡敤敥敧敨敩敪敫敭敮敯敱敳敶敹敺敻敼敽敾敿斀斁敛斄斅斆敦
斈斉斊斍斎斏斒斓斔斓斖斑
斘斚斛斝斞斟斠斡斢斣
斦斨斪斫斩斮斱斲斳斴斵斶斸
斺斻於斾斿旀旃旄旆旇旈旊旍旎旐旑旒旓旔旕旖旘旙旚旜旝旞旟
旡旣旤兂
旪旫旮旯旰旲旳旴旵旸旹旻旼旽旾旿昀昁昃昄昅昈昉昊昋昍昐昑昒昕昖昗昘昙昚昛昜昝晻昢昣昤春昦昧昩昪昫昬昮昰昱昲昳昴昵昶昷昸昹昺昻昼昽昿晀晁晃晄晅晆晇晈晋晊晌晍晎晏晐晑晒晓晔晕晖晗晘晙晛晜晞晟晠晡晰晣晤晥晦晧晪晫晬晭晰晱晲晳晴晵晷晸晹晻晼晽晾晿暀暁暂暃暄暅暆暇晕晖暊暋暌暍暎暏暐暑暒暓暔暕暖暗旸暙暚暛暜暝暞暟暠暡暣暤暥暦暧暨暩暪暬暭暮暯暰昵暲暳暴暵暶暷暸暹暺暻暼暽暾暿曀曁曂曃晔曅曈曊曋曌曍曎曏曐曑曒曓曔曕曗曘曙曚曛曜曝曞曟旷曡曢曣曤曥曦曧昽曩曪曫晒曭曮曯
曰曱曵曶曷曹曺曻曽朁朂朄朅朆朇最羯
肜朊朌朎朏朐朑朒朓朕朖朘朙朚朜朞朠朡朣朤朥朦胧
朩朰朲朳枛朸朹朻朼朾朿杁杄杅圬杈杉杊杋杍杒杓杔杕杗杘杙杚杛杝杞杢杣杤杦杧杩杪杫杬杮柿杰东杲杳杴杵杶杷杸杹杺杻杼杽枀枂枃枅枆枇枈枊枋枌枍枎枏析枑枒枓枔枖枘枙枛枞枟枠枡枤枥枦枧枨枩枬枭枮枰枱枲枳枵枷枸枹枺枻枼枽枾枿柀柁柂柃柄柅柆柇柈柉柊柋柌柍柎柒柕柖柗柘柙查楂呆柙柚柛柜柝柞柟柠柡柢柣柤柦柧柨柩柪柬柭柮柯柰柲柳栅柶柷柸柹拐査柼柽柾栀栁栂栃栄栆栈栉栊栋栌栍栎栐旬栔栕栗栘栙栚栛栜栝栞栟栠栢栣栤栥栦栧栨栩株栫栬栭栮栯栰栱栲栳栴栵栶核栺栻栽栾栿桀桁桂桄桅桇桉桊桋桍桎桏桒桕桖桗桘桙桚桛桜桝桞桟桠桡桢档桤桦桧桨桩桪桫桬桭杯桯桰桱桲桳桴桵桶桷桸桹桺桻桼桽桾杆梀梁梂梃梄梅梆梇梈梉枣梌梍梎梏梐梑梒梓梕梖梗枧梙梚梛梜梞梠梡梢梣梤梥梧梩梪梫梬梭梮梯械梲梴梵梶梷梸梹梺梻梼梽梾梿检棁棂棃棅棆棇棈棉棊棋棌棍棎棏棐棒棓棔棕枨枣棘棙棚棛棜棝棞栋棠棡棢棣棤棥棦棨棩棪棫桊棭棯棰棱栖棳棴棵梾棷棸棹棺棻棼棽棾棿椀椁椂椃椄椆椇椈椉椊椋椌椎桠椐椒椓椔椕椖椗椘椙椚椛検椝椞椟椠椡椢椣椤椥椦椧椨椩椪椫椬椭椮椯椰椱椲椳椴椵椶椷椸椹椺椻椼椽椾椿楀楁楂楃楅楆楇楈楉杨楋楌楍楎楏楐楑楒楔楕楖楗楘楛楜楝楞楟楠楡楢楣楤楥楦楧桢楩楪楫楬楮椑楯楰楱楲楳楴极楶榉榊榋榌楷楸楹楺楻楽楾楿榀榁榃榄榅榆榇榈榉榊榋榌榍槝搌榑榒榓榔榕榖榗榘榙榚榛榜榝榞榟榠榡榢榣榤榥榧榨榩杩榫榬榭榯榰榱榲榳榴榵榶榷榸榹榺榻榼榽榾桤槀槁槂盘槄槅槆槇槈槉槊构槌枪槎槏槐槑槒杠槔槕槖槗様槙槚槛槜槝槞槟槠槡槢槣槥槦椠椁槩槪槫槬槭槮槯槰槱槲桨槴槵槶槷槸槹槺槻槼槽槾槿樀桩樃樄枞樆樇樈樉樊樋樌樍樎樏樐樒樔樕樖樗樘樚樛樜樝樟樠樢样樤樥樦樧樨権横樫樬樭樮樯樰樱樲樳樴樵樶樷朴树桦樻樼樽樾樿橀橁橂橃橄橅橆橇桡橉橊桥橌橍橎橏橐橑橒橓橔橕橖橗橘橙橚橛橜橝橞橠橡椭橣橤橥橧橨橩橪橬橭橮橯橰橱橲橳橴橵橶橷橸橹橺橻橼柜橿檀檩檂檃檄檅檆檇檈柽檊檋檌檍檎檏檐檑檒檓档檕檖檗檘檙檚檛桧檝檞槚檠檡检樯檤檥檦檧檨檩檪檫檬檭梼檰檱檲槟檴檵檶栎柠檹檺槛檼檽桐檿櫀櫁棹柜櫄櫅櫆櫇櫈櫉櫊櫋櫌櫍櫎櫏累櫑櫒櫔櫕櫖櫗櫘櫙榈栉櫜椟橼櫠櫡櫢櫣櫤橱櫦槠栌櫩枥橥榇櫭櫮櫯櫰櫱櫲栊櫴櫵櫶櫷榉櫹櫼櫽櫾櫿欀欁欂欃栏欅欆欇欈欉权欋欌欍欎椤欐欑栾欓欔欕榄欗欘欙欚欛欜欝棂欟
欤欥欦欨欩欪欫欬欭欮欯欰欱欳欴欵欶欷唉欹欻欼钦款欿歀歁歂歃歄歅歆歇歈歉歊歋歍欧歑歒歓歔殓歗歘歙歚歛歜歝歞欤歠欢钦
歧歨歩歫歬歭歮歯歰歱歳歴歵歶歾殁殁殂殃殄殅殆殇殈殉殌殍殎殏殐殑殒殓殔殕殖殗残殙殚殛殜殝殒殟殠殡殢殣殇殥殦殧殨殩殪殚殬殰殱歼
殶殸殹殾殿毂毃毄毅殴毇毈毉毊
毋毎毐毑毓坶拇
毖毗毘坒陛屁芘楷砒玭昆吡纰妣锴鈚秕庇沘
毜毝毞毟毠毡毢毣毤毥毦毧毨毩毪毫毬毭毮毯毰毱毲毳毴毵毶毷毸毹毺毻毼毽毾毵氀氁氂氃氋氄氅氆氇毡氉氊氍氎
氒氐抵坻坁胝阍痻泜汦茋芪柢砥奃睧眡蚳蚔呧軧軝崏弤婚怟惛忯岻貾
氕氖気氘氙氚氜氝氞氟氠氡氢氤氥氦氧氨氩氪氭氮氯氰氱氲
氶氷凼氺氻氼氽氾氿汀汃汄汅氽汈汊汋汌泛汏汐汑汒汓汔汕汖汘污汚汛汜汞汢汣汥汦汧汨汩汫汬汭汮汯汰汱汲汳汴汵汶汷汸汹汻汼汾汿沀沂沃沄沅沆沇沊沋沌冱沎沏洓沓沔沕沗沘沚沛沜沝沞沠沢沣沤沥沦沨沩沪沫沬沭沮沯沰沱沲沴沵沶沷沸沺沽泀泂泃泅泆泇泈泋泌泍泎泏泐泑泒泓泔泖泗泘泙泚泜溯泞泟泠泤泦泧泩泫泬泭泮泯泱泲泴泵泶泷泸泹泺泾泿洀洂洃洄洅洆洇洈洉洊洌洍洎洏洐洑洒洓洔洕洖洘洙洚洜洝洠洡洢洣洤洦洧洨洫洬洭洮洯洰洱洳洴洵洷洸洹洺洼洽洿浀浂浃浄浈浉浊浌浍浏浐浒浔浕浖浗浘浚浛浜浝浞浟浠浡浢浣浤浥浦浧浨浫浭浯浰浱浲浳浵浶浃浺浻浼浽浾浿涀涁涂涃涄涅涆泾涊涋涍涎涐涑涒涓涔涖涗涘涙涚涜涝涞涟涠涡涢涣涥涧涪涫涬涭涰涱涳涴涶涷涸涹涺涻凉涽涾涿淁淂淃淄淅淆淇淈淉淊淌淍淎淏淐淓淔淕淖淗淙淛淜淞淟淠淢淣淤渌淦淧沦淬淭淯淰淲淳淴涞滍淾淿渀渁渂渃渄渆渇済渋渌渍渎渏渑渒渓渕渖渘渚渜渝渞渟沨渥渧渨渪渫渮渰渱渲渳渵渶渷渹渻渼渽渿湀湁湂湄湅湆湇湈湉湋湌湍湎湏湐湑湒湓湔湕湗湙湚湜湝浈湟湠湡湢湤湥湦湨湩湪湫湬湭湮湰湱湲湳湴湵湶湷湸湹湺湻湼湽満溁溂溄溆溇沩溉溊溋溌溍溎溏溑溒溓溔溕溗溘溙溚溛溞溟溠溡溣溤溥溦溧溨溩溬溭溯溰溱溲涢溴溵溶溷溸溹溻溽溾溿滀滁滂滃沧滆滇滈滉滊涤滍荥滏滐滒滓滖滗滘滙滛滜滝滞滟滠滢滣滦滧滪滫沪滭滮滰滱渗滳滵滶滹滺浐滼滽漀漃漄漅漈漉溇漋漌漍漎漐漑澙熹漗漘漙沤漛漜漝漞漟漡漤漥漦漧漨漪渍漭漮漯漰漱漳漴溆漶漷漹漺漻漼漽漾浆潀颍潂潃潄潅潆潇潈潉潊潋潌潍潎潏潐潒潓洁潕潖潗潘沩潚潜潝潞潟潠潡潢潣润潥潦潧潨潩潪潫潬潭浔溃潱潲潳潴潵潶滗潸潹潺潻潼潽潾涠澁澄澃澅浇涝澈澉澊澋澌澍澎澏湃澐澑澒澓澔澕澖涧澘澙澚澛澜澝澞澟渑澢澣泽澥滪澧澨澪澫澬澭浍澯澰淀澲澳澴澵澶澷澸澹澺澻澼澽澾澿濂濄濅濆濇濈濉濊濋濌濍濎濏濐濑濒濓沵濖濗泞濙濚濛浕濝濞济濠濡濢濣涛濥濦濧濨濩濪滥浚濭濮濯潍滨濲濳濴濵濶濷濸濹溅濻泺濽滤濿瀀漾瀂瀃灋渎瀇瀈泻瀊沈瀌瀍瀎浏瀐瀒瀓瀔濒瀖瀗泸瀙瀚瀛瀜瀞潇潆瀡瀢瀣瀤瀥潴泷濑瀩瀪瀫瀬瀭瀮瀯弥瀱潋瀳瀴瀵瀶瀷瀸瀹瀺瀻瀼瀽澜瀿灀灁瀺灂沣滠灅灆灇灈灉灊灋灌灍灎灏灐洒灒灓漓灖灗滩灙灚灛灜灏灞灟灠灡灢湾滦灥灦灧灨灪
灮灱灲灳灴灷灸灹灺灻灼炀炁炂炃炄炅炆炇炈炋炌炍炏炐炑炓炔炕炖炗炘炙炚炛炜炝炞炟炠炡炢炣炤炥炦炧炨炩炪炫炯炰炱炲炳炴炵炶炷炻炽炾炿烀烁烃烄烅烆烇烉烊烋烌烍烎烐烑烒烓烔烕烖烗烙烚烜烝烞烠烡烢烣烥烩烪烯烰烱烲烳烃烵烶烷烸烹烺烻烼烾烿焀焁焂焃焄焇焈焉焋焌焍焎焏焐焑焒焓焔焕焖焗焘焙焛焜焝焞焟焠焢焣焤焥焧焨焩焪焫焬焭焮焯焱焲焳焴焵焷焸焹焺焻焼焽焾焿煀煁煂煃煄煅煇煈炼煊煋煌煍煎煏煐煑炜煓煔暖煗煘煚煛煜煝煞煟煠煡茕煣焕煦煨煪煫炀煭煯煰煱煲煳煴煵煶煷煸煹煺煻煼煽煾煿熀熁熂熃熄熅熆熇熈熉熋熌熍熎熏熐熑荧熓熔熕熖炝熘熚熛熜熝熞熠熡熢熣熤熥熦熧熨熩熪熫熬熭熮熯熰颎熳熴熵熶熷熸熹熺熻熼熽炽熿燀烨燂燅燆燇炖燊燋燌燍燎燏燐燑燓燔燖燗燘燚燛燝燞燠燡燢燣燤燥灿燧燨燩燪燫燮燯燰燱燲燳烩燵燵燸燹燺薰燽焘燿爀爁爂爃爄爅爇爈爉爊爋爌烁爎爏爑爒爓爔爕爖爗爘爙爚烂爜爝爞爟爠爡爢爣爤爥爦爧爨爩
爮爯爰爳爴舀
爻爼
牀牁牂牃牄牅牊牉牋牍牎牏牐牑牒牓牔牕牖牗
牚
牜牝牞牟牣牤牥牦牨牪牫牬牭牮牯牰牱牳牴牶牷牸牻牼牾牿犂犃犄犅犆犇犈犉犊犋犌犍犎犏犐犑犒犓犔犕荦犗犘犙犚牦犜犝犞犟犠犡犣犤犥犦牺犨犩犪犫
犭犰犱犲犳犴犵犷犸犹犺犻犼犽犾犿狘狁狃狄狅狆狇狉狊狋狌狍狎狏狑狒狓狔狕狖狙狚狛狜狝狞狟狡猯狢狣狤狥狦狧狨狩狪狫狭狮狯狰狱狲狳狴狵狶狷狭狺狻狾狿猀猁猂猃猄猅猆猇猈猉猊猋猌猍猑猒猓猔猕猗猘狰猚猝猞猟猠猡猢猣猤猥猦猧猨猬猭猰猱猲猳猵犹猷猸猹猺狲猼猽猾獀犸獂獆獇獈獉獊獋獌獍獏獐獑獒獓獔獕獖獗獘獙獚獛獜獝獞獟獠獡獢獣獤獥獦獧獩狯猃獬獭狝獯狞獱獳獴獶獹獽獾獿猡玁玂玃
"""

english_alphabet = """
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
"""

punctuation = """
。，、＇：∶；?‘’“”〝〞ˆˇ﹕︰﹔﹖﹑•¨….¸;！´？！～—ˉ｜‖＂〃｀@﹫﹟#﹩$﹠&﹪%*﹡﹢﹦﹤‐￣¯―﹨ˆ˜+=<＿_-\ˇ~()（）〈〉‹›﹛﹜『』〖〗［］《》〔〕{}「」【】❝❞
"""

alphabet_list = list(common_alphabet.replace('\n', '').replace(' ', '')) + \
    list(second_common_alphabet.replace('\n', '').replace(' ', '')) + \
    list(rarely_used_alphabet.replace('\n', '').replace(' ', '')) + \
    list(english_alphabet.replace('\n', '').replace(' ', '')) + \
    list(punctuation.replace('\n', '').replace(' ', ''))

alphabet = ''.join(alphabet_list) + ' '


def get_text():
    common_alphabet_list = list(common_alphabet.replace('\n', '').replace(' ', ''))
    second_common_alphabet_list = list(second_common_alphabet.replace('\n', '').replace(' ', ''))
    rarely_used_alphabet_list = list(rarely_used_alphabet.replace('\n', '').replace(' ', ''))
    english_alphabet_list = list(english_alphabet.replace('\n', '').replace(' ', ''))
    punctuation_list = list(punctuation.replace('\n', '').replace(' ', ''))

    rand = random.random()
    # print(rand)
    if 0 <= rand < 0.4:
        text = random.choice(common_alphabet_list)
    elif 0.4 <= rand < 0.75:
        text = random.choice(second_common_alphabet_list)
    elif 0.75 <= rand < 0.8:
        text = random.choice(rarely_used_alphabet_list)
    elif 0.8 <= rand < 0.9:
        text = random.choice(english_alphabet_list)
    else:
        text = random.choice(punctuation_list)

    return text


if __name__ == '__main__':
    r = get_text()
    print(r)
