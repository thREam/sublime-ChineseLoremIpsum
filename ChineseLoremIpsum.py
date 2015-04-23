# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sublime
import sublime_plugin

import random
import re


class ChineseLoremIpsumCommand(sublime_plugin.TextCommand):
    WORDS_CHS = '一个 我们 时间 中国 可以 公司 没有 信息 下载 软件 注册 自己 产品 工作 论坛 企业 这个 他们 管理 已经 问题 内容 使用 进行 市场 服务 如果 系统 技术 发展 现在 作者 就是 网络 提供 相关 我的 文章 方式 电话 发表 所有 时候 因为 北京 有限公司 什么 还是 开始 本站 发布 自己的 支持 在线 国家 生活 联系 积分 主题 所以 不能 的人 上海 中心 世界 游戏 需要 价格 用户 通过 要求 不是 免费 个人 但是 地址 网站 情况 最后 设计 同时 这些 活动 手机 推荐 一些 主要 大家 发现 目前 文件 你的 不过 评论 生产 美国 图片 经济 功能 国际 的是 选择 其他 这样 会员 环境 来自 日期 成为 他的 最新 专业 一下 人员 任何 教育 资料 状态 都是 点击 为了 不会 出现 知道 社会 名称 而且 介绍 音乐 等级 可能 这种 建设 朋友 虽然 电子 资源 看到 精华 电影 如何 新闻 阅读 安全 全国 只有 回复 大学 学生 学习 关于 项目 不同 以及 有关 那么 开发 还有 只是 非常 研究 广告 首页 方法 希望 地方 也是 单位 怎么 应该 今天 以上 更新 帖子 显示 能力 电脑 记者 查看 位置 不要 由于 无法 详细 投资 是一个 一般 进入 发生 这里 感觉 更多 你们 的话 起来 标准 一样 认为 女人 那个 设备 搜索 之后 然后 学校 销售 组织 说明 提高 为什么 作品 或者 喜欢 东西 方面 简介 必须 经营 科技 作为 其中 运行 工程 解决 操作 经验 地区 重要 直接 登录 合作 结果 影响 这是 行业 对于 表示 程序 包括 留言 规定 处理 男人 各种 部门 数据 具有 商品 系列 大小 因此 关系 可是 比较 文化 一直 法律 这么 您的 城市 分析 基本 最大 类别 两个 日本 得到 一次 继续 成功 她的 责任 深圳 业务 欢迎 加入 能够 觉得 部分 中文 根据 人民 政府 控制 其实 之间 一种 威望 实现 语言 出来 谢谢 社区 品牌 是否 工具 完全 决定 很多 网上 事情 今年 国内 以后 制作 浏览 过程 完成 类型 来源 质量 有些 一起 当然 汽车 一点 帮助 增加 历史 以下 不断 应用 那些 密码 计划 如此 次数 到了 拥有 孩子 原因 参加 只要 报告 当前 客户 正在 注意 标题 空间 一定 一切 特别 全部 准备 建立 歌曲 香港 专家 授权 自动 设置 获得 广州 效果 集团 收藏 目标 发帖 才能 权限 机构 精神 利用 保护 保证 声音 建议 知识 我是 甚至 突然 行为 速度 第一 健康 经过 作用 交流 版主 别人 代表 呵呵 意见 故事 领导 爱情 自然 模式 安装 平台 美女 版权 有什么 采用 存在 人们 发布时间 我国 查询 培训 级别 编辑 努力 了解 真正 供应 机会 专辑 教学 小说 达到 广东 实施 终于 看看 简单 我也 产生 考试 身体 接受 小时 水平 原来 比赛 普通 快乐 有人 旅游 引用 左右 过去 快速 娱乐 制度 除了 分类 执行 整个 基础 老师 离线 条件 许多 台湾 调查 会议 咨询 来说 政策 建筑 交易 列表 其它 不错 哈哈 版本 之一 职业 访问 结构 银行 材料 英语 视频 记录 通知 正常 负责 申请 全面 有限 下面 找到 保持 只能 购买 他们的 数量 综合 歌词 服务器 眼睛 另外 链接 是什么 具体 计算机 增长 办法 看着 媒体 资金 全球 方案 调整 科学 推出 关注 电视 我想 造成 当时 家庭 身上 超级 公告 是不是 几个 有点 思想 重点 也许 中华 改变 加强 连接 我就 有效 实际 以前 提出 有一 先生 任务 这一 门派 消息 传真 就会 十分 表现 最近 原创 产业 时代 医院 美元 未来 是个 改革 工业 移动 力量 说道 一声 如果你 现金 打开 于是 变化 不少 幸福 我要 按照 并且 错误 现代 不知 检查 页面 商业 这次 邮件 网址 测试 根本 频道 似乎 编号 上市 不得 之前 教师 下来 美丽 离开 人才 共同 正式 登陆 经典 删除 传统 浙江 里面 随着 不仅 也不 添加 几乎 对方 开展 更加 范围 生命 照片 需求 治疗 超过 重新 大量 认识 女孩 人生 真是 互联网 行政 心里 让我 形成 永远 积极 艺术 有了 讨论 一位 总是 取得 提示 注册时间 商务 文字 进一步 结束 是在 感到 万元 名字 给我 自由 每天 创新 统计 不可 魅力 以来 方便 曾经 程度 交通 受到 授权方式 制造 金钱 歌手 本地 参与 学院 后来 铃声 心情 肯定 精彩 不用 中央 让人 都有 机械 韩国 代理 时尚 确定 越来越 维护 不再 相信 晚上 观点 过来 修改 形式 严重 引起 现场 特点 贡献 带来 来了 发行 面对 心中 告诉 考虑 两人 价值 回答 宣传 运行环境 事件 第二 人物 来到 报道 还没有 如果您 看来 首先 食品 怎样 高级 导致 同样 变成 运动 在这里 播放 影片 联系人 明显 天下 成立 目的 多少 贸易 输入 也有 有的 数字 今日 绝对 收入 长期 竞争 楼主 很好 管理员 转载 心理 行动 安排 到底 头衔 江苏 稳定 再次 昨天 是一种 最高 看见 不好 格式 坚持 女性 目录 会有 点这里 经常 回来 面前 下午 事业 那样 方向 良好 电信 山东 资讯 同学 身边 人类 丰富 规划 享受 政治 好像 出口 一天 最终 身份 马上 开放 理论 去年 一定要 立即 妈妈 而是 是因为 期间 统一 竟然 评价 招聘 一年 金币 分别 优势 姓名 它的 她们 举行 短信 参考 一条 成本 攻击 听到 很大 说话 恢复 动作 博客 南京 如下 领域 三个 相当 共有 充分 无论 不到 结合 风格 玩家 属于 然而 颜色 加工 费用 利益 实在 每个 明白 我在 面积 分享 员工 阶段 最好 容易 都会 一段 即可 战略 感情 体系 酒店 营销 启动 阳光 成了 联盟 最佳 指导 在我 真实 优秀 措施 意义 一边 下去 杭州 消费者 理解 本文 及时 不想 不敢 消费 现象 简体 文学 特色 还要 等等 本人 天津 重庆 压力 声明 发贴 数码 父亲 人数 网页 我不 机关 遇到 迅速 对象 一片 强大 样子 大型 描述 区域 发挥 欣赏 不了 让你 主页 满足 性能 特殊 上传 及其 共享 解释 重大 房地产 并不 现实 认真 成绩 英文 减少 原则 发出 监督 轻松 发送 回到 点这里下载 训练 令人 规格 英国 先进 农村 委员会 四川 组图 至少 寻找 好了 联系电话 人气 之中 风险 配置 从事 规范 还没 地点 传奇 漂亮 基地 形象 大陆 公布 意思 小姐 证明 兄弟 状况 更新时间 服装 母亲 因素 放在 合同 存款 表情 一张 人家 课程 经历 创造 充满 那种 正确 采取 日志 这时 关键 成都 体育 新手 想到 此时 促进 父母 培养 办公室 上面 广大 巨大 毕业 它们 上网 否则 出去 失去 观看 难道 尽管 即使 整理 号码 保密 脸上 暂无 法规 内部 不管 激情 设施 比如 出版 明确 协议 同意 农业 就在 清除 民族 正是 推广 投入 更好 给你 协会 很快 用于 各位 亿元 一场 全新 想要 返回 那里 完美 字节 集中 居然 留下 反应 流行 衣服 突破 女子 本来 正文 等待 规模 各地 游客 更是 国外 不可能 回家 俱乐部 群众 掌握 完善 友情 担心 实力 保险 未知 贷款 我还 独立 并没有 农民 东方 限制 带着 人士 另一 包装 德国 唯一 我会 儿子 升级 无关 一名 看了 感谢 好友 医生 代码 成员 就要 公开 自我 认证 仍然 干部 资格 高手 可爱 天空 都不 太多 组成 困难 医疗 小学 依然 字体 应当 他说 版权所有 所在 变得 著名 双方 直到 联合 出售 展示 针对 一只 也会 刚刚 型号 共和国 专题 对我 卫生 在他 热线 你是 符合 完整 见到 强烈 用品 战争 武汉 明天 界面 儿童 所谓 特别是 一家 制定 做好 土地 就像 相应 精品 金融 确实 日子 实践 相关内容 老板 关闭 本地下载 提升 人民币 进口 有个 忘记 性感 记得 当地 慢慢 魔法 在这个 指出 图书 承担 结婚 动画 智能 欧洲 死亡 连续 休闲 国产 影视 整体 放弃 计算 保障 女儿 各类 不足 答案 是他 追求 我说 去了 报价 实行 核心 出了 态度 刚才 装备 女生 采购 成人 拒绝 这位 组合 一阵 邮编 值得 专用 立场 出版社 请问 年轻 附件 眼前 平均 股份 我看 联系方式 专门 基金 降低 技巧 无门 法国 病毒 节目 附近 适合 年龄 创建 地说 理由 暂时 生物 英雄 证券 难以 装修 配合 本身 从而 距离 无派 走了 热门 立刻 清楚 有所 河南 增强 打造 避免 硬盘 创业 明星 技能 人民共和国 权利 之外 本书 告诉我 即将 报名 中华人民 检测 多种 地位 青年 往往 持续 手段 成长 解压 动态 教授 经理 数据库 性别 资产 参数 通信 相对 男子 武器 收费 消失 后面 站在 我觉得 皮肤 背景 还可以 简体中文 手中 毕竟 让他 机制 优惠 过了 财务 实用 就算 上午 一份 每次 办理 意识 指数 每年 自身 你可以 支付 不如 详细信息 习惯 高度 天使 分钟 确保 轻轻 都在 重视 合理 种子 笔记本 召开 打印 高速 严格 位于 中学 党员 大会 危险 是有 还在 平方米 档案 用户名 命令 第一个 邮箱 对手 拍摄 反映 破坏 投票 话题 秘密 地图 绿色 而已 伤害 紧张 办公 最好的 加上 时期 又是 一件 感受 劳动 登记 购物 来看 提醒 私服 素质 内存 你就 忽然 却是 痛苦 赚钱 包含 鼠标 尤其是 一眼 少女 笑话 好象 财富 那是 相同 对此 开心 一生 黑色 既然 问道 微笑 中间 少年 窗口 各项 好好 贴子 挑战 广泛 保留 做出 一款 推进 本页 复制 事实 如今 有着 所属 学会 那就 物品 股票 无限 都要 足球 大家都 坐在 吸引 机票 显得 聊天 多年 厂商 怎么办 就能 例如 举办 人大 房屋 天地 期待 扩大 给予 疯狂 让我们 免费版 周围 为主 作家 主动 随时 角色 转换 文本 福建 负责人 动物 未经 姐姐 十大 他是 校园 首次 一旦 接口 主管 也就 下载次数 理想 下降 大学生 上述 笑道 逐渐 自行 始终 熟悉 一句 色彩 关心 文明 湖南 有时 为何 专栏 河北 多个 要是 或许 世纪 许可证 维修 共享版 亚洲 情感 使得 才是 读者 队伍 空气 日报 总数 规则 将会 很难 本帖 此外 运用 公里 损失 就业 体现 加快 老婆 总结 高兴 工艺 个性 房间 只好 以为 当年 性质 观察 驱动 比例 表达 侵犯 没想到 突出 并不是 妻子 神秘 表明 刺激 记忆 不出 想法 目光 你要 接着 概念 强调 也没 愿意 失败 广场 标签 发言 众多 属性 做到 想起 保存 思考 满意 利润 批准 无线 收到 前面 尺寸 成果 进来 装饰 我和 杂志 有可能 怎么样 收集 落实 导演 深入 禁止 梦想 之下 道路 众人 本网 恐怖 下一页 最多 实验 在这 施工 相比 一把 就有 屏幕 动漫 奇怪 敌人 不够 哪里 通常 西安 对不起 操作系统 精灵 展开 发布日期 上路 华人 事项 爸爸 配件 或是 域名 尊重 成熟 鼓励 居民 灌水 观众 仿佛 动力 小组 破解 指标 一套 你会 宣布 公共 道德 网通 仔细 世界上 化工 机器 天天 接触 行情 回去 加盟 而言 求购 估计 论文 金属 预测 环保 彻底 站长 三星 患者 将在 摄影 家里 没什么 资本 在此 的说 热情 黄金 嘿嘿 生日 处于 策略 指定 改善 休息 职工 上了 复杂 设定 顺利 浪漫 丈夫 科技有限公司 本公司 老人 无奈 职位 趋势 通讯 麻烦 家族 他在 男女 高中 哪个 沟通 允许 事故 可惜 别的 也要 下载地址 情绪 同志 画面 引擎 确认 昨日 不太 一块 宠物 的确 证书 外面 大大 我有 是谁 主任 大部分 是这样 高考 湖北 文件大小 国人 不需要 有很多 双手 另一个 放心 上一页 部队 体验 教程 白色 运输 表演 战斗 光临 不停 大厦 相互 主营 他人 品种 军事 红色 家园 管理系统 数学 意外 采访 律师 疾病 大哥 工资 我都 至于 微软 药品 各个 天堂 停止 哥哥 纷纷 面临 婚姻 固定 依法 推动 给他 走到 兴趣 作出 不在 就不 厦门 贴图 批发 你也 感动 此次 具备 显然 容量 不但 开通 太阳 大师 理念 这就是 背后 排名 适应 和我 平时 进去 青岛 客人 说了 欢迎您 请点击 垃圾 怀疑 出生 不行 物业 日记 究竟 防止 缺乏 类似 渐渐 客服 栏目 书库 传播 会计 输出 唱片 上涨 厂家 写真 宝贝 承诺 招生 房子 一道 上升 温柔 一项 命运 投资者 现有 沈阳 性格 妹妹 宝宝 年度 老大 江湖 果然 独特 大连 打击 还能 创作 构成 冠军 安徽 青春 我现在 指南 高校 说完 一部分 一人 二手 一步 眼神 图文 如有 基础上 透露 反而 品质 四个 优化 电池 录入 味道 收购 帮忙 帝国 转让 大概 主人 我只 责任编辑 空调 遵守 中华人民共和国 全身 第三 旁边 不得不 市场价 和他 定位 预计 反对 提交 供求 吃饭 天气 您是 在于 什么时候 蓝色 小区 效率 物质 犯罪 站点 手册 一定会 生存 学历 无数 协调 涉及 回忆 黑暗 人体 近期 必要 可能会 热点 隐藏 判断 寂寞 警察 查找 至今 战士 改造 新浪 一看 温度 常常 优质 美容 不大 他也 站内 国有 赶紧 欧美 云南 免费电影 房产 演员 时刻 抓住 商机 某些 玻璃 特价 主板 年代 图像 心灵 很少 实际上 角度 内心 听说 进步 加大 石油 都能 门口 我一 每个人 引导 补充 打算 导航 教材 床上 选项 依据 姑娘 适用 国务院 团队 取消 矛盾 传说 电源 一部 会员价 飞机 化学 电力 奖励 市民 音乐网 都市 兴奋 露出 之处 一是 有限责任 食物 胜利 说什么 一个月 付款 他就 股份有限公司 接近 考生 研发 笑容 补丁 身后 集体 家伙 好多 特征 刷新 较大 走进 医药 反正 一时 三年 千万 什么样 读书 尽快 头发 硬件 本周 一笑 模拟 求助 工作人员 观念 互相 我真 财政 男孩 签名 已有 海外 是以 是由 陕西 死了 举报 上去 言论 印象 商家 分配 则是 今后 专区 同一 交换 塑料 大全 那天 非法 家长 翻译 基于 眼泪 都没 原本 俄罗斯 排行 把握 通用 早已 投诉 对他 想象 不必 有意 顾客 也就是 才会 找不到 哪些 明年 广西 打电话 我来 评估 审核 工商 你说 家具 一面 可以说 社会主义 还会 大人 制品 公主 传来 小心 简直 尝试 宁波 只见 答应 国语 每一个 中介 科研 望着 地球 跟着 联想 没有任何 真实性 人口 当前位置 逐步 新疆 邀请 每日 出现在 关键字 被人 信号 最低 尽量 虚拟 总经理 咱们 一股 让她 花园 并非 是指 设立 玄幻 渠道 美好 走出 就好 电子邮件 内容简介 老公 在那里 一句话 二十 常用 股市 把我 为你 是怎么 随便 几天 威胁 球员 提前 信息网 产权 车辆 点击数 重复 最重要 存储 生态 色情 阅读者 人力 先进性 菜单 从此 到达 见过 配套 普遍 恐怕 远程 也在 转移 瞬间 招商 公路 大力 男性 演出 官方 股东 算是 要有 微微 表面 岗位 地上 能否 能量 之家 准确 尚未 详细内容 彼此 电视台 违法 清晰 那时 为您 承认 差不多 和平 男生 害怕 上来 主义 各自 这么多 春节 多媒体 商城 辽宁 一路 一致 光盘 那么多 各级 你在 住宅 看出 还不 智慧 看起来 多么 点头 大赛 异常 受伤 不禁 便宜 点点 区别 名单 也能 友情链接 忍不住 两种 温州 货币 厉害 山西 一半 做什么 足够 公园 检验 灵魂 策划 信心 走向 有一种 互动 毫无 信箱 航空 精选 近日 显卡 很多人 帐号 公安 练习 出发 不然 博士 可以用 预防 维持 按钮 而来 江西 违反 激动 病人 一批 业主 情人 当中 革命 体制 随后 我对 不可以 不喜欢 机场 伙伴 将军 全市 你怎么 上下 财产 出租 温暖 整合 地面 眼中 有权 毕业生 水晶 苏州 小子 不限 帮我 已被 中文版 自主 日常 作业 得分 空中 说法 小孩 监控 担任 室内 呼吸 字幕 最快 多次 幻想 医学 斑竹 营养 主角 不良 主席 用来 他还 不对 不久 手续 新型 装置 业绩 转身 台北 造型 书记 新技术 将来 西方 大众 诚信 看法 铁通 贯彻 妇女 两年 物流 当你 不住 不多 紧紧 外挂 力度 几次 你们的 再也 一级 打了 主机 芯片 体力 怎么会 强化 法院 告诉你 睡觉 原帖 适当 平衡 探索 干什么 研究生 说着 以外 改进 一丝 镜头 标志 某个 传输 淡淡 仪器 激烈 快车 章节 官员 全文 诱惑 全体 获取 平静 定义 本次 中有 可怜 一系列 桌面 搜狐 进程 远远 连载 前往 植物 和谐 家人 保健 恋爱 人群 经销商 原理 本科 上次 印度 原料 一番 很有 反馈 能源 任意 手里 所在地 付出 生意 见面 她说 司机 工程师 场所 评分 郑州 日前 一体 案例 浏览器 常见 一切都 讲话 故意 许可 加速 不见 思维 风景 一会儿 范围内 这一点 键盘 服饰 考核 做法 又有 内置 年轻人 电器 军队 总统 引进 案件 更为 不懂 气氛 不愿 人民政府 大多数 只需 提到 感觉到 下列 试验 可见 一身 女孩子 照顾 运作 先后 形势 请您 留言板 生气 意味着 知名 试题 深深 后果 检索 看过 紧急 学术 危机 地下 感染 大声 深刻 出台 西部 对外 早上 球队 两位 填写 便是 更大 脸色 祝福 好评 森林 沉默 顾问 线路 第二天 荣誉 没人 药物 剧情 设为 早就 多多 事实上 但在 是的 退出 广播 主演 你知道 法律责任 排行榜 点评 相册 会不会 物理 你好 印刷 和你 伟大 玩具 南方 礼物 商标 推荐使用 而在 无聊 如同 语文 到来 其他的 遭遇 正好 女士 外国 一口 我这 长沙 口气 什么事 有一些 当初 星座 她是 意大利 批评 有关部门 吃了 浪费 考察 人间 临时 礼品 转帖 依旧 典型 注明 库存 仅供 彩色 快捷 魔兽 促销 帮你 亲自 三人 均为 失望 济南 该公司 出处 条款 二人 审批 法人 求职 长时间 买了 创意 孤独 集成 污染 预览 文档 基本上 细节 体会 纪念 工厂 长大 两次 聪明 特性 说过 队员 分为 专利 为此 海南 调节 身材 回应 三大 不能下载 通道 水果 开口 超市 液晶 对话 新华网 把他 宾馆 委托 大约 漫画 条例 此处 夫妻 士兵 内地 身子 到我 东莞 到处 给我们 女友 证实 用途 流程 民主 铁路 轿车 有时候 再说 决策 伤心 极大 警方 骑士 适用于 穿着 一支 我市 功夫 总体 图书馆 说是 本网站 能不能 毫不 吸收 解压密码 为止 对你 承受 国产软件 顿时 元素 上有 吉林 成就 皇帝 执法 必然 面向 上班 我又 面议 当我 新人 右键 网际 压缩 研究所 联赛 有限责任公司 手术 但我 你看 开了 主持 很久 尴尬 故障 提问 执行时间 由此 学科 经营许可证 一对 百万 下了 奇迹 显示器 什么是 同步 等方面 笑着 写作 可用 接到 一下子 十年 好处 风云 考研 会在 拿出 本论坛 对着 曝光 没事 新增 据说 房价 家电 我家 我爱 不怕 惊讶 东北 不是很 有机会 现代化 频率 请大家 一段时间 回头 一脸 辛苦 陷入 职务 本月 天然 大战 无比 网易 居住 每月 你想 生成 财经 权力 并在 图形 开发商 期限 第一章 郁闷 尤其 简历 默认 说出 插入 透明 像是 糖尿病 不代表 神话 您可以 当天 鉴定 此刻 所说 夫人 进攻 种类 我很 团结 网吧 相关图片 经济发展 您现在 一副 电子商务 我去 苹果 这个问题 规律 领先 浏览次数 只不过 说到 网游 但他 出席 北方 常委会 引发 自信 转贴 路线 全省 四周 低价 新鲜 焦点 争取 合适 后悔 加入时间 道理 无人 请求 喜爱 群发 注重 鲜花 金额 百度 较高 不说 零售 住房 宽带 好看 从来没 循环 要去 高效 无疑 回事 重量 这款 世界杯 饭店 你还 缓缓 他不 是啊 咖啡 权益 的钱 你自己 情形 民间 一座 解放 街道 体内 不详 治理 春天 国内外 像素 加油 手机铃声 杀手 不去 是从 眼光 有一定 监管 赢得 工人 思路 讨论区 数码相机 随意 高达 备案 编程 一台 公斤 自从 躺在 不论 把它 转变 惊人 新年 辅助 静静 肌肤 以往 十二 进了 他对 不承担 些什么 课堂 小游戏 予以 减肥 楼上 分公司 前来 指挥 将其 提出了 一口气 搜集 人事 以便 古代 篇文章 绝不 一颗 细胞 百姓 市委 仅仅 信誉 交友 交给 先进性教育 实业 对比 饮食 纺织 对待 近年来 想想 售价 一周 大多 爆炸 信用 所需 要在 告知 来电 一方面 它是 黑龙江 稿件 你不 本报 询问 欢迎光临 预期 对了 选手 几年 收藏本页 因而 消除 脑袋 日韩 放下 起点 很容易 请教 解决方案 也可 夏天 最初 外观 那位 网际快车 本类 降价 某种 上帝 报纸 我把 幽默 手指 主体 同事 股权 走势 抱着 认定 含有 模样 对她 第二次 一流 伊拉克 犹豫 哈尔滨 演唱 市政府 冲击 最为 大幅 权威 手上 团体 校长 围绕 建材 汉化版 临床 参观 第二章 基层 不好意思 大盘 不明白 福州 地理 遗憾 信息化 情节 上门 学者 任何人 运行平台 节省 硕士 种种 等人 跟我 主流 职责 联通 锁定 乐队 称为 感兴趣 完了 没有什么 步骤 冲突 各国 铃声下载 演唱会 环节 难得 影音 对面 怪物 订单 之类 障碍 一会 这场 记住 蔬菜 效益 作战 加拿大 竞争力 倒是 你有 长度 气息 对付 教育活动 一遍 义务 自治区 岁月 搭配 开关 所有人 坚决 字符 人大常委会 轻易 私人 点此 诺基亚 一本 事务 大门 再度 精美 这段 支撑 住了 防治 处理器 优点 外资 初步 前后 有利于 笔者 不愿意 精英 二级 梦幻 破解版 看不到 豪华 风情 发达 灵活 不起 不满 语音 警告 五金 处罚 反复 部落 不肯 把你 外贸 新闻网 模型 留学 依靠 能在 寻求 我的心 得知 证据 电视剧 身影 网路 眼里 一大 邮政编码 汉化 模块 神经 留在 招标 总部 音频 评级 五年 插件 你能 女朋友 买卖 活力 供应商 周边 协助 请在 昆明 懂得 差距 相机 盯着 搜索引擎 前进 杀人 收益 接下来 提示信息 半年 接收 模糊 版面 试试 每页'.split()
    WORDS_CHT = '一個 我們 時間 中國 可以 公司 沒有 信息 下載 軟件 註冊 自己 產品 工作 論壇 企業 這個 他們 管理 已經 問題 內容 使用 進行 市場 服務 如果 系統 技術 發展 現在 作者 就是 網絡 提供 相關 我的 文章 方式 電話 發表 所有 時候 因為 北京 有限公司 什麼 還是 開始 本站 發佈 自己的 支持 在線 國家 生活 聯繫 積分 主題 所以 不能 的人 上海 中心 世界 遊戲 需要 價格 用戶 通過 要求 不是 免費 個人 但是 地址 網站 情況 最後 設計 同時 這些 活動 手機 推薦 一些 主要 大家 發現 目前 文件 你的 不過 評論 生產 美國 圖片 經濟 功能 國際 的是 選擇 其他 這樣 會員 環境 來自 日期 成為 他的 最新 專業 一下 人員 任何 教育 資料 狀態 都是 點擊 為了 不會 出現 知道 社會 名稱 而且 介紹 音樂 等級 可能 這種 建設 朋友 雖然 電子 資源 看到 精華 電影 如何 新聞 閲讀 安全 全國 只有 回覆 大學 學生 學習 關於 項目 不同 以及 有關 那麼 開發 還有 只是 非常 研究 廣告 首頁 方法 希望 地方 也是 單位 怎麼 應該 今天 以上 更新 帖子 顯示 能力 電腦 記者 查看 位置 不要 由於 無法 詳細 投資 是一個 一般 進入 發生 這裡 感覺 更多 你們 的話 起來 標準 一樣 認為 女人 那個 設備 搜索 之後 然後 學校 銷售 組織 說明 提高 為什麼 作品 或者 喜歡 東西 方面 簡介 必須 經營 科技 作為 其中 運行 工程 解決 操作 經驗 地區 重要 直接 登錄 合作 結果 影響 這是 行業 對於 表示 程序 包括 留言 規定 處理 男人 各種 部門 數據 具有 商品 系列 大小 因此 關係 可是 比較 文化 一直 法律 這麼 您的 城市 分析 基本 最大 類別 兩個 日本 得到 一次 繼續 成功 她的 責任 深圳 業務 歡迎 加入 能夠 覺得 部分 中文 根據 人民 政府 控制 其實 之間 一種 威望 實現 語言 出來 謝謝 社區 品牌 是否 工具 完全 決定 很多 網上 事情 今年 國內 以後 製作 瀏覽 過程 完成 類型 來源 質量 有些 一起 當然 汽車 一點 幫助 增加 歷史 以下 不斷 應用 那些 密碼 計劃 如此 次數 到了 擁有 孩子 原因 參加 只要 報告 當前 客戶 正在 注意 標題 空間 一定 一切 特別 全部 準備 建立 歌曲 香港 專家 授權 自動 設置 獲得 廣州 效果 集團 收藏 目標 發帖 才能 權限 機構 精神 利用 保護 保證 聲音 建議 知識 我是 甚至 突然 行為 速度 第一 健康 經過 作用 交流 版主 別人 代表 呵呵 意見 故事 領導 愛情 自然 模式 安裝 平台 美女 版權 有什麼 採用 存在 人們 發佈時間 我國 查詢 培訓 級別 編輯 努力 瞭解 真正 供應 機會 專輯 教學 小說 達到 廣東 實施 終於 看看 簡單 我也 產生 考試 身體 接受 小時 水平 原來 比賽 普通 快樂 有人 旅遊 引用 左右 過去 快速 娛樂 制度 除了 分類 執行 整個 基礎 老師 離線 條件 許多 台灣 調查 會議 諮詢 來說 政策 建築 交易 列表 其它 不錯 哈哈 版本 之一 職業 訪問 結構 銀行 材料 英語 視頻 記錄 通知 正常 負責 申請 全面 有限 下面 找到 保持 只能 購買 他們的 數量 綜合 歌詞 服務器 眼睛 另外 連結 是什麼 具體 計算機 增長 辦法 看著 媒體 資金 全球 方案 調整 科學 推出 關注 電視 我想 造成 當時 家庭 身上 超級 公告 是不是 幾個 有點 思想 重點 也許 中華 改變 加強 連接 我就 有效 實際 以前 提出 有一 先生 任務 這一 門派 消息 傳真 就會 十分 表現 最近 原創 產業 時代 醫院 美元 未來 是個 改革 工業 移動 力量 說道 一聲 如果你 現金 打開 於是 變化 不少 幸福 我要 按照 並且 錯誤 現代 不知 檢查 頁面 商業 這次 郵件 網址 測試 根本 頻道 似乎 編號 上市 不得 之前 教師 下來 美麗 離開 人才 共同 正式 登陸 經典 刪除 傳統 浙江 裡面 隨着 不僅 也不 添加 幾乎 對方 開展 更加 範圍 生命 照片 需求 治療 超過 重新 大量 認識 女孩 人生 真是 互聯網 行政 心裡 讓我 形成 永遠 積極 藝術 有了 討論 一位 總是 取得 提示 註冊時間 商務 文字 進一步 結束 是在 感到 萬元 名字 給我 自由 每天 創新 統計 不可 魅力 以來 方便 曾經 程度 交通 受到 授權方式 製造 金錢 歌手 本地 參與 學院 後來 鈴聲 心情 肯定 精采 不用 中央 讓人 都有 機械 韓國 代理 時尚 確定 越來越 維護 不再 相信 晚上 觀點 過來 修改 形式 嚴重 引起 現場 特點 貢獻 帶來 來了 發行 面對 心中 告訴 考慮 兩人 價值 回答 宣傳 運行環境 事件 第二 人物 來到 報導 還沒有 如果您 看來 首先 食品 怎樣 高級 導致 同樣 變成 運動 在這裡 播放 影片 聯繫人 明顯 天下 成立 目的 多少 貿易 輸入 也有 有的 數字 今日 絶對 收入 長期 競爭 樓主 很好 管理員 轉載 心理 行動 安排 到底 頭銜 江蘇 穩定 再次 昨天 是一種 最高 看見 不好 格式 堅持 女性 目錄 會有 點這裡 經常 回來 面前 下午 事業 那樣 方向 良好 電信 山東 資訊 同學 身邊 人類 豐富 規劃 享受 政治 好像 出口 一天 最終 身份 馬上 開放 理論 去年 一定要 立即 媽媽 而是 是因為 期間 統一 竟然 評價 招聘 一年 金幣 分別 優勢 姓名 它的 她們 舉行 短信 參考 一條 成本 攻擊 聽到 很大 說話 恢復 動作 博客 南京 如下 領域 三個 相當 共有 充分 無論 不到 結合 風格 玩家 屬於 然而 顏色 加工 費用 利益 實在 每個 明白 我在 面積 分享 員工 階段 最好 容易 都會 一段 即可 戰略 感情 體系 酒店 營銷 啟動 陽光 成了 聯盟 最佳 指導 在我 真實 優秀 措施 意義 一邊 下去 杭州 消費者 理解 本文 及時 不想 不敢 消費 現象 簡體 文學 特色 還要 等等 本人 天津 重慶 壓力 聲明 發貼 數碼 父親 人數 網頁 我不 機關 遇到 迅速 對象 一片 強大 樣子 大型 描述 區域 發揮 欣賞 不了 讓你 主頁 滿足 性能 特殊 上傳 及其 共享 解釋 重大 房地產 並不 現實 認真 成績 英文 減少 原則 發出 監督 輕鬆 發送 回到 點這裡下載 訓練 令人 規格 英國 先進 農村 委員會 四川 組圖 至少 尋找 好了 聯繫電話 人氣 之中 風險 配置 從事 規範 還沒 地點 傳奇 漂亮 基地 形象 大陸 公佈 意思 小姐 證明 兄弟 狀況 更新時間 服裝 母親 因素 放在 合同 存款 表情 一張 人家 課程 經歷 創造 充滿 那種 正確 採取 日誌 這時 關鍵 成都 體育 新手 想到 此時 促進 父母 培養 辦公室 上面 廣大 巨大 畢業 它們 上網 否則 出去 失去 觀看 難道 儘管 即使 整理 號碼 保密 臉上 暫無 法規 內部 不管 激情 設施 比如 出版 明確 協議 同意 農業 就在 清除 民族 正是 推廣 投入 更好 給你 協會 很快 用於 各位 億元 一場 全新 想要 返回 那裡 完美 位元 集中 居然 留下 反應 流行 衣服 突破 女子 本來 正文 等待 規模 各地 遊客 更是 國外 不可能 回家 俱樂部 群眾 掌握 完善 友情 擔心 實力 保險 未知 貸款 我還 獨立 並沒有 農民 東方 限制 帶著 人士 另一 包裝 德國 唯一 我會 兒子 升級 無關 一名 看了 感謝 好友 醫生 代碼 成員 就要 公開 自我 認證 仍然 幹部 資格 高手 可愛 天空 都不 太多 組成 困難 醫療 小學 依然 字體 應當 他說 版權所有 所在 變得 著名 雙方 直到 聯合 出售 展示 針對 一隻 也會 剛剛 型號 共和國 專題 對我 衛生 在他 熱線 你是 符合 完整 見到 強烈 用品 戰爭 武漢 明天 界面 兒童 所謂 特別是 一家 制定 做好 土地 就像 相應 精品 金融 確實 日子 實踐 相關內容 老闆 關閉 本地下載 提升 人民幣 進口 有個 忘記 性感 記得 當地 慢慢 魔法 在這個 指出 圖書 承擔 結婚 動畫 智能 歐洲 死亡 連續 休閒 國產 影視 整體 放棄 計算 保障 女兒 各類 不足 答案 是他 追求 我說 去了 報價 實行 核心 出了 態度 剛才 裝備 女生 採購 成人 拒絶 這位 組合 一陣 郵編 值得 專用 立場 出版社 請問 年輕 附件 眼前 平均 股份 我看 聯繫方式 專門 基金 降低 技巧 無門 法國 病毒 節目 附近 適合 年齡 創建 地說 理由 暫時 生物 英雄 證券 難以 裝修 配合 本身 從而 距離 無派 走了 熱門 立刻 清楚 有所 河南 增強 打造 避免 硬盤 創業 明星 技能 人民共和國 權利 之外 本書 告訴我 即將 報名 中華人民 檢測 多種 地位 青年 往往 持續 手段 成長 解壓 動態 教授 經理 數據庫 性別 資產 參數 通信 相對 男子 武器 收費 消失 後面 站在 我覺得 皮膚 背景 還可以 簡體中文 手中 畢竟 讓他 機制 優惠 過了 財務 實用 就算 上午 一份 每次 辦理 意識 指數 每年 自身 你可以 支付 不如 詳細信息 習慣 高度 天使 分鐘 確保 輕輕 都在 重視 合理 種子 筆記本 召開 打印 高速 嚴格 位於 中學 黨員 大會 危險 是有 還在 平方米 檔案 用戶名 命令 第一個 郵箱 對手 拍攝 反映 破壞 投票 話題 秘密 地圖 綠色 而已 傷害 緊張 辦公 最好的 加上 時期 又是 一件 感受 勞動 登記 購物 來看 提醒 私服 素質 內存 你就 忽然 卻是 痛苦 賺錢 包含 滑鼠 尤其是 一眼 少女 笑話 好像 財富 那是 相同 對此 開心 一生 黑色 既然 問道 微笑 中間 少年 窗口 各項 好好 貼子 挑戰 廣泛 保留 做出 一款 推進 本頁 複製 事實 如今 有着 所屬 學會 那就 物品 股票 無限 都要 足球 大家都 坐在 吸引 機票 顯得 聊天 多年 廠商 怎麼辦 就能 例如 舉辦 人大 房屋 天地 期待 擴大 給予 瘋狂 讓我們 免費版 周圍 為主 作家 主動 隨時 角色 轉換 文本 福建 負責人 動物 未經 姐姐 十大 他是 校園 首次 一旦 接口 主管 也就 下載次數 理想 下降 大學生 上述 笑道 逐漸 自行 始終 熟悉 一句 色彩 關心 文明 湖南 有時 為何 專欄 河北 多個 要是 或許 世紀 許可證 維修 共享版 亞洲 情感 使得 才是 讀者 隊伍 空氣 日報 總數 規則 將會 很難 本帖 此外 運用 公里 損失 就業 體現 加快 老婆 總結 高興 工藝 個性 房間 只好 以為 當年 性質 觀察 驅動 比例 表達 侵犯 沒想到 突出 並不是 妻子 神秘 表明 刺激 記憶 不出 想法 目光 你要 接着 概念 強調 也沒 願意 失敗 廣場 標籤 發言 眾多 屬性 做到 想起 保存 思考 滿意 利潤 批准 無線 收到 前面 尺寸 成果 進來 裝飾 我和 雜誌 有可能 怎麼樣 收集 落實 導演 深入 禁止 夢想 之下 道路 眾人 本網 恐怖 下一頁 最多 實驗 在這 施工 相比 一把 就有 屏幕 動漫 奇怪 敵人 不夠 哪裡 通常 西安 對不起 操作系統 精靈 展開 發佈日期 上路 華人 事項 爸爸 配件 或是 域名 尊重 成熟 鼓勵 居民 灌水 觀眾 彷彿 動力 小組 破解 指標 一套 你會 宣佈 公共 道德 網通 仔細 世界上 化工 機器 天天 接觸 行情 回去 加盟 而言 求購 估計 論文 金屬 預測 環保 徹底 站長 三星 患者 將在 攝影 家裡 沒什麼 資本 在此 的說 熱情 黃金 嘿嘿 生日 處於 策略 指定 改善 休息 職工 上了 複雜 設定 順利 浪漫 丈夫 科技有限公司 本公司 老人 無奈 職位 趨勢 通訊 麻煩 家族 他在 男女 高中 哪個 溝通 允許 事故 可惜 別的 也要 下載地址 情緒 同志 畫面 引擎 確認 昨日 不太 一塊 寵物 的確 證書 外面 大大 我有 是誰 主任 大部分 是這樣 高考 湖北 文件大小 國人 不需要 有很多 雙手 另一個 放心 上一頁 部隊 體驗 教程 白色 運輸 表演 戰鬥 光臨 不停 大廈 相互 主營 他人 品種 軍事 紅色 家園 管理系統 數學 意外 採訪 律師 疾病 大哥 工資 我都 至於 微軟 藥品 各個 天堂 停止 哥哥 紛紛 面臨 婚姻 固定 依法 推動 給他 走到 興趣 作出 不在 就不 廈門 貼圖 批發 你也 感動 此次 具備 顯然 容量 不但 開通 太陽 大師 理念 這就是 背後 排名 適應 和我 平時 進去 青島 客人 說了 歡迎您 請點擊 垃圾 懷疑 出生 不行 物業 日記 究竟 防止 缺乏 類似 漸漸 客服 欄目 書庫 傳播 會計 輸出 唱片 上漲 廠家 寫真 寶貝 承諾 招生 房子 一道 上升 溫柔 一項 命運 投資者 現有 瀋陽 性格 妹妹 寶寶 年度 老大 江湖 果然 獨特 大連 打擊 還能 創作 構成 冠軍 安徽 青春 我現在 指南 高校 說完 一部分 一人 二手 一步 眼神 圖文 如有 基礎上 透露 反而 品質 四個 優化 電池 錄入 味道 收購 幫忙 帝國 轉讓 大概 主人 我只 責任編輯 空調 遵守 中華人民共和國 全身 第三 旁邊 不得不 市場價 和他 定位 預計 反對 提交 供求 吃飯 天氣 您是 在於 什麼時候 藍色 小區 效率 物質 犯罪 站點 手冊 一定會 生存 學歷 無數 協調 涉及 回憶 黑暗 人體 近期 必要 可能會 熱點 隱藏 判斷 寂寞 警察 查找 至今 戰士 改造 新浪 一看 溫度 常常 優質 美容 不大 他也 站內 國有 趕緊 歐美 雲南 免費電影 房產 演員 時刻 抓住 商機 某些 玻璃 特價 主板 年代 圖象 心靈 很少 實際上 角度 內心 聽說 進步 加大 石油 都能 門口 我一 每個人 引導 補充 打算 導航 教材 床上 選項 依據 姑娘 適用 國務院 團隊 取消 矛盾 傳說 電源 一部 會員價 飛機 化學 電力 獎勵 市民 音樂網 都市 興奮 露出 之處 一是 有限責任 食物 勝利 說什麼 一個月 付款 他就 股份有限公司 接近 考生 研發 笑容 補丁 身後 集體 傢伙 好多 特徵 刷新 較大 走進 醫藥 反正 一時 三年 千萬 什麼樣 讀書 儘快 頭髮 硬件 本週 一笑 模擬 求助 工作人員 觀念 互相 我真 財政 男孩 簽名 已有 海外 是以 是由 陝西 死了 舉報 上去 言論 印象 商家 分配 則是 今後 專區 同一 交換 塑料 大全 那天 非法 家長 翻譯 基於 眼淚 都沒 原本 俄羅斯 排行 把握 通用 早已 投訴 對他 想像 不必 有意 顧客 也就是 才會 找不到 哪些 明年 廣西 打電話 我來 評估 審核 工商 你說 傢俱 一面 可以說 社會主義 還會 大人 製品 公主 傳來 小心 簡直 嘗試 寧波 只見 答應 國語 每一個 中介 科研 望着 地球 跟着 聯想 沒有任何 真實性 人口 當前位置 逐步 新疆 邀請 每日 出現在 關鍵字 被人 信號 最低 儘量 虛擬 總經理 咱們 一股 讓她 花園 並非 是指 設立 玄幻 渠道 美好 走出 就好 電子郵件 內容簡介 老公 在那裡 一句話 二十 常用 股市 把我 為你 是怎麼 隨便 幾天 威脅 球員 提前 信息網 產權 車輛 點擊數 重複 最重要 存儲 生態 色情 閲讀者 人力 先進性 菜單 從此 到達 見過 配套 普遍 恐怕 遠程 也在 轉移 瞬間 招商 公路 大力 男性 演出 官方 股東 算是 要有 微微 表面 崗位 地上 能否 能量 之家 準確 尚未 詳細內容 彼此 電視台 違法 清晰 那時 為您 承認 差不多 和平 男生 害怕 上來 主義 各自 這麼多 春節 多媒體 商城 遼寧 一路 一致 光盤 那麼多 各級 你在 住宅 看出 還不 智慧 看起來 多麼 點頭 大賽 異常 受傷 不禁 便宜 點點 區別 名單 也能 友情連結 忍不住 兩種 溫州 貨幣 厲害 山西 一半 做什麼 足夠 公園 檢驗 靈魂 策劃 信心 走向 有一種 互動 毫無 信箱 航空 精選 近日 顯卡 很多人 帳號 公安 練習 出發 不然 博士 可以用 預防 維持 按鈕 而來 江西 違反 激動 病人 一批 業主 情人 當中 革命 體制 隨後 我對 不可以 不喜歡 機場 夥伴 將軍 全市 你怎麼 上下 財產 出租 溫暖 整合 地面 眼中 有權 畢業生 水晶 蘇州 小子 不限 幫我 已被 中文版 自主 日常 作業 得分 空中 說法 小孩 監控 擔任 室內 呼吸 字幕 最快 多次 幻想 醫學 斑竹 營養 主角 不良 主席 用來 他還 不對 不久 手續 新型 裝置 業績 轉身 台北 造型 書記 新技術 將來 西方 大眾 誠信 看法 鐵通 貫徹 婦女 兩年 物流 當你 不住 不多 緊緊 外掛 力度 幾次 你們的 再也 一級 打了 主機 晶片 體力 怎麼會 強化 法院 告訴你 睡覺 原帖 適當 平衡 探索 幹什麼 研究生 說著 以外 改進 一絲 鏡頭 標誌 某個 傳輸 淡淡 儀器 激烈 快車 章節 官員 全文 誘惑 全體 獲取 平靜 定義 本次 中有 可憐 一系列 桌面 搜狐 進程 遠遠 連載 前往 植物 和諧 家人 保健 戀愛 人群 經銷商 原理 本科 上次 印度 原料 一番 很有 反饋 能源 任意 手裡 所在地 付出 生意 見面 她說 司機 工程師 場所 評分 鄭州 日前 一體 案例 瀏覽器 常見 一切都 講話 故意 許可 加速 不見 思維 風景 一會兒 範圍內 這一點 鍵盤 服飾 考核 做法 又有 內置 年輕人 電器 軍隊 總統 引進 案件 更為 不懂 氣氛 不願 人民政府 大多數 只需 提到 感覺到 下列 試驗 可見 一身 女孩子 照顧 運作 先後 形勢 請您 留言板 生氣 意味着 知名 試題 深深 後果 檢索 看過 緊急 學術 危機 地下 感染 大聲 深刻 出台 西部 對外 早上 球隊 兩位 填寫 便是 更大 臉色 祝福 好評 森林 沉默 顧問 線路 第二天 榮譽 沒人 藥物 劇情 設為 早就 多多 事實上 但在 是的 退出 廣播 主演 你知道 法律責任 排行榜 點評 相冊 會不會 物理 你好 印刷 和你 偉大 玩具 南方 禮物 商標 推薦使用 而在 無聊 如同 語文 到來 其他的 遭遇 正好 女士 外國 一口 我這 長沙 口氣 什麼事 有一些 當初 星座 她是 意大利 批評 有關部門 吃了 浪費 考察 人間 臨時 禮品 轉帖 依舊 典型 註明 庫存 僅供 彩色 快捷 魔獸 促銷 幫你 親自 三人 均為 失望 濟南 該公司 出處 條款 二人 審批 法人 求職 長時間 買了 創意 孤獨 整合 污染 預覽 文檔 基本上 細節 體會 紀念 工廠 長大 兩次 聰明 特性 說過 隊員 分為 專利 為此 海南 調節 身材 回應 三大 不能下載 通道 水果 開口 超市 液晶 對話 新華網 把他 賓館 委託 大約 漫畫 條例 此處 夫妻 士兵 內地 身子 到我 東莞 到處 給我們 女友 證實 用途 流程 民主 鐵路 轎車 有時候 再說 決策 傷心 極大 警方 騎士 適用於 穿著 一支 我市 功夫 總體 圖書館 說是 本網站 能不能 毫不 吸收 解壓密碼 為止 對你 承受 國產軟件 頓時 元素 上有 吉林 成就 皇帝 執法 必然 面向 上班 我又 面議 當我 新人 右鍵 網際 壓縮 研究所 聯賽 有限責任公司 手術 但我 你看 開了 主持 很久 尷尬 故障 提問 執行時間 由此 學科 經營許可證 一對 百萬 下了 奇蹟 顯示器 什麼是 同步 等方面 笑着 寫作 可用 接到 一下子 十年 好處 風雲 考研 會在 拿出 本論壇 對著 曝光 沒事 新增 據說 房價 家電 我家 我愛 不怕 驚訝 東北 不是很 有機會 現代化 頻率 請大家 一段時間 回頭 一臉 辛苦 陷入 職務 本月 天然 大戰 無比 網易 居住 每月 你想 生成 財經 權力 並在 圖形 開發商 期限 第一章 鬱悶 尤其 簡歷 默認 說出 插入 透明 像是 糖尿病 不代表 神話 您可以 當天 鑒定 此刻 所說 夫人 進攻 種類 我很 團結 網吧 相關圖片 經濟發展 您現在 一副 電子商務 我去 蘋果 這個問題 規律 領先 瀏覽次數 只不過 說到 網遊 但他 出席 北方 常委會 引發 自信 轉貼 路線 全省 四周 低價 新鮮 焦點 爭取 合適 後悔 加入時間 道理 無人 請求 喜愛 群發 注重 鮮花 金額 百度 較高 不說 零售 住房 寬頻 好看 從來沒 循環 要去 高效 無疑 回事 重量 這款 世界盃 飯店 你還 緩緩 他不 是啊 咖啡 權益 的錢 你自己 情形 民間 一座 解放 街道 體內 不詳 治理 春天 國內外 像素 加油 手機鈴聲 殺手 不去 是從 眼光 有一定 監管 贏得 工人 思路 討論區 數碼相機 隨意 高達 備案 編程 一台 公斤 自從 躺在 不論 把它 轉變 驚人 新年 輔助 靜靜 肌膚 以往 十二 進了 他對 不承擔 些什麼 課堂 小遊戲 予以 減肥 樓上 分公司 前來 指揮 將其 提出了 一口氣 蒐集 人事 以便 古代 篇文章 絶不 一顆 細胞 百姓 市委 僅僅 信譽 交友 交給 先進性教育 實業 對比 飲食 紡織 對待 近年來 想想 售價 一週 大多 爆炸 信用 所需 要在 告知 來電 一方面 它是 黑龍江 稿件 你不 本報 詢問 歡迎光臨 預期 對了 選手 幾年 收藏本頁 因而 消除 腦袋 日韓 放下 起點 很容易 請教 解決方案 也可 夏天 最初 外觀 那位 網際快車 本類 降價 某種 上帝 報紙 我把 幽默 手指 主體 同事 股權 走勢 抱著 認定 含有 模樣 對她 第二次 一流 伊拉克 猶豫 哈爾濱 演唱 市政府 衝擊 最為 大幅 權威 手上 團體 校長 圍繞 建材 漢化版 臨床 參觀 第二章 基層 不好意思 大盤 不明白 福州 地理 遺憾 信息化 情節 上門 學者 任何人 運行平台 節省 碩士 種種 等人 跟我 主流 職責 聯通 鎖定 樂隊 稱為 感興趣 完了 沒有什麼 步驟 衝突 各國 鈴聲下載 演唱會 環節 難得 影音 對面 怪物 訂單 之類 障礙 一會 這場 記住 蔬菜 效益 作戰 加拿大 競爭力 倒是 你有 長度 氣息 對付 教育活動 一遍 義務 自治區 歲月 搭配 開關 所有人 堅決 字元 人大常委會 輕易 私人 點此 諾基亞 一本 事務 大門 再度 精美 這段 支撐 住了 防治 處理器 優點 外資 初步 前後 有利於 筆者 不願意 精英 二級 夢幻 破解版 看不到 豪華 風情 發達 靈活 不起 不滿 語音 警告 五金 處罰 反覆 部落 不肯 把你 外貿 新聞網 模型 留學 依靠 能在 尋求 我的心 得知 證據 電視劇 身影 網路 眼裡 一大 郵政編碼 漢化 模組 神經 留在 招標 總部 音頻 評級 五年 插件 你能 女朋友 買賣 活力 供應商 周邊 協助 請在 昆明 懂得 差距 相機 盯着 搜索引擎 前進 殺人 收益 接下來 提示信息 半年 接收 模糊 版面 試試 每頁'.split()

    SEPARATOR = dict(comma=u'\uff0c', period=u'\u3002')
    CHARS_LEAST_IN_SENTENCE = 10
    CHARS_MOST_IN_SENTENCE = 30
    SENTENCE_LEAST_IN_PARAGRAPH = 3
    SENTENCE_MOST_IN_PARAGRAPH = 10

    def __init__(self, *args, **kwargs):
        try:
            import emmet
            self.emmet_exist = True
        except ImportError as e:
            self.emmet_exist = False

        self.WORDS = self.WORDS_CHS
        return super(ChineseLoremIpsumCommand, self).__init__(*args, **kwargs)

    def call_emmet(self, edit):
        self.view.run_command('expand_abbreviation_by_tab')

    def gen_char(self):
        return random.choice(self.gen_word())

    def gen_word(self):
        return random.choice(self.WORDS)

    def gen_sentence(self, min_char=None, max_char=None):
        max_char = max_char or self.CHARS_MOST_IN_SENTENCE
        min_char = min_char or min(self.CHARS_LEAST_IN_SENTENCE, max_char)

        sentence = u''
        char_count = random.choice(range(min_char, max_char + 1))
        while len(sentence) < char_count:
            word = self.gen_word()
            sentence += word

        # discard chars
        if len(sentence) > char_count:
            sentence = sentence[:char_count-len(sentence)]

        return sentence

    def gen_paragraph(
            self,
            min_sentence=None,
            max_sentence=None,
            min_char=None,
            max_char=None
    ):
        least_sentence = min_sentence or self.SENTENCE_LEAST_IN_PARAGRAPH
        most_sentence = max_sentence or self.SENTENCE_MOST_IN_PARAGRAPH

        paragraph = u''
        if min_sentence or max_sentence or not (min_char and max_char):
            for i in range(random.choice(
                range(least_sentence, most_sentence)
            )):
                sentence = self.gen_sentence()
                if max_char:
                    if (len(sentence) + len(paragraph)) > max_char:
                        break
                paragraph += sentence
                paragraph += self.SEPARATOR['comma']
        elif max_char:
            while True:
                sentence = self.gen_sentence()
                if max_char:
                    if (len(sentence) + len(paragraph)) > max_char:
                        break
                paragraph += sentence
                paragraph += self.SEPARATOR['comma']

        if min_char:
            sentence_with_seperator = True
            while len(paragraph) < min_char:
                sentence_max_char = max_char - len(paragraph) - 1
                if sentence_max_char < self.CHARS_LEAST_IN_SENTENCE:
                    sentence_max_char += 1
                    sentence_with_seperator = False
                sentence = self.gen_sentence(
                    max_char=sentence_max_char
                )
                paragraph += sentence
                if sentence_with_seperator:
                    paragraph += self.SEPARATOR['comma']

        if len(paragraph) > self.CHARS_LEAST_IN_SENTENCE:
            paragraph = paragraph[:-1] + self.SEPARATOR['period']

        return paragraph

    def run(self, edit, qty=None):
        selections = self.view.sel()
        for selection in selections:

            lastchars = self.view.substr(
                sublime.Region(selection.begin()-20, selection.end())
            )

            # r'(Clorem|Clipsum)(\d+)?(\.\d+)?$'
            re_s = re.search(r'(Clorem|Clipsum)(\d+)?$', lastchars)

            if not re_s:
                re_s = re.search(r'(CTlorem|CTlipsum)(\d+)?$', lastchars)
                if re_s:
                    self.WORDS = self.WORDS_CHT

            if not re_s:
                re_s = re.search(r'(CSlorem|CSlipsum)(\d+)?$', lastchars)
                if re_s:
                    self.WORDS = self.WORDS_CHS

            if re_s:
                total_char = None
                if re_s.group(2):
                    total_char = int(re_s.group(2))

                paragraph = self.gen_paragraph(
                    min_char=total_char,
                    max_char=total_char
                )

                erase_length = len(re_s.group(0))
                erase_region = sublime.Region(
                    selection.end()-erase_length,
                    selection.end()
                )

                self.view.insert(edit, selection.begin(), paragraph)
                self.view.erase(edit, erase_region)
