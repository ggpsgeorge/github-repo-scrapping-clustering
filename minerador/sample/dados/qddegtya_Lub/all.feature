Feature: 测试用例集
    Scenario: 百度首页
      Given 打开 "http://www.baidu.com"
      When 在 "id" 为 "kw1" 的框中输入 "lub"
      And 点击 "id" 为 "su1" 的按钮