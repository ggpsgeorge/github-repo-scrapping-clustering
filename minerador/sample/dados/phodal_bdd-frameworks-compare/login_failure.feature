# language: zh-CN
功能: 失败的登录

  激光干涉引力波天文台和室女座干涉仪首次观测到因两颗中子星合并引发的引力波。
  联合国海地稳定特派团成员全数撤出海地，正式结束为期13年的维持和平行动任务。
  在德国法兰克福书展最后一天，加拿大作家玛格丽特·阿特伍德获颁德国书商和平奖。

  场景大纲: 失败的登录
    假设 当我在网站的首页
    当 输入用户名 <用户名>
    当 输入密码 <密码>
    当 提交登录信息
    那么 页面应该返回 "Error Page"

    例子:
      |用户名     |密码      |
      |'Jan1'    |'password'|
      |'Jan2'    |'password'|