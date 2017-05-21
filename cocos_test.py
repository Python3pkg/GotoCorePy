import cocos
from cocos.actions import RotateBy

from core.service import coreservice

from core.base.corecallback import CoreCallback
from core.logger.corelogger import CoreLogger

from core.cocos.corelayer import CoreLayer
from core.logger.coreloggerdebug import CoreLoggerDebug


class CocosTest(CoreLayer):
    def __init__(self):
        super(CocosTest, self).__init__()
        CoreLogger.getInstance([CoreLoggerDebug()])
        self.circle = cocos.sprite.Sprite("breaking-bad.jpg")
        self.add(self.circle)

        self.sc.registerService("press.service", self.pressService)
        self.sc.registerService("release.service", self.releaseService)
        self.sc.registerService("motion.service", self.motionService)

        CoreCallback.addCallback(self, CoreLayer.PRESS, self.sc.getService("press.service"))
        CoreCallback.addCallback(self, CoreLayer.RELEASE, self.sc.getService("release.service"))
        CoreCallback.addCallback(self, CoreLayer.MOTION, self.sc.getService("motion.service"))

    def pressService(self, params):
        print(params[CoreLayer.DATA])
        self.circle.do(RotateBy(360, duration=.5))

    def releaseService(self, params):
        print(params[CoreLayer.DATA])
        # self.circle.position =params[CoreLayer.DATA].get('x'), params[CoreLayer.DATA].get('y')

    def motionService(self, params):
        print(params[CoreLayer.DATA])
        self.circle.position =params[CoreLayer.DATA].get('x'), params[CoreLayer.DATA].get('y')

cocos.director.director.init()
cocos.director.director.run(cocos.scene.Scene(CocosTest()))
