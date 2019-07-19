# -*- coding: utf-8 -*-
# File  : 触摸操作和多点触控.py
# Date  : 2019/5/24

#TouchAction
#TouchAction方法是appium自已定义的新方法
# * 短按 (press) * 释放 (release) * 移动到 (moveTo) * 点击 (tap) * 等待 (wait) * 长按 (longPress)  * 执行 (perform)
#以python为例
from appium.webdriver.common.touch_action import TouchAction

TouchAction(driver).press(el0).moveTo(el1).release()
#TouchAction 在python中是一个类它下面的方法有

#长按
long_press(self, el=None, x=None, y=None, duration=1000(ms))
#短按
press(self, el=None, x=None, y=None)
#点击
tap(self,el=None,x=None,y=None,count=1)
#释放
release(self)
#移动到
move_to(self,el=None,x=None,y=None)
#等待
wait(self,ms=0)
#执行
perform(self)



#关于perform 官网给的伪代码中讲
TouchAction().tap(el).perform()
#与
driver.perform(TouchAction().tap(el))
#效果一致


#MultiTouch
#MultiTouch 多点触控 它只提供了两个方法 一个add 一个执行perform.官网例子为
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

action0 = TouchAction().tap(el1)
action1 = TouchAction().tap(el2)
MultiTouch().add(action0).add(action1).perform