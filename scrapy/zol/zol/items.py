# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZolItem(scrapy.Item):
    id = scrapy.Field()  # 机型id
    name = scrapy.Field()  # 机型名称
    brand = scrapy.Field()  # 机型品牌

    ReleaseDate = scrapy.Field()  # 发布时间
    eCommerceQuotation = scrapy.Field()  # 电商报价
    listingDate = scrapy.Field()  # 上市日期
    usageScenarios = scrapy.Field()  # 使用场景
    bodyMaterial = scrapy.Field()  # 机身材质
    bodyColor = scrapy.Field()  # 机身颜色
    fingerprintRecognition = scrapy.Field()  # 指纹识别
    facialRecognition = scrapy.Field()  # 面部识别

    length = scrapy.Field()  # 长度
    width = scrapy.Field()  # 宽度
    thickness = scrapy.Field()  # 厚度
    weight = scrapy.Field()  # 重量

    cpu = scrapy.Field()  # CPU型号
    cpuHZ = scrapy.Field()  # CPU频率
    cpuNum = scrapy.Field()  # CPU核心数
    gpu = scrapy.Field()  # GPU 型号

    ram = scrapy.Field()    # 运行内存容量
    ramType = scrapy.Field()    # 运行内存类型

    rom = scrapy.Field()    # 存储容量
    romType = scrapy.Field()    # 存储类型

    memoryCard = scrapy.Field()    # 存储卡
    expandCapacity = scrapy.Field()    # 存储卡扩展容量

    factorySystemKernel = scrapy.Field()    # 出厂系统内核
    OS = scrapy.Field()    # 出厂系统
    heatDissipation = scrapy.Field()    # 散热
    speaker = scrapy.Field()    # 扬声器

    screenSize = scrapy.Field()    # 屏幕尺寸
    screenType = scrapy.Field()    # 屏幕类型
    resolution = scrapy.Field()    # 分辨率
    screenMaterial = scrapy.Field()    # 屏幕材质
    screenRefreshRate = scrapy.Field()    # 屏幕刷新率
    screenManufacturer = scrapy.Field()    # 屏幕厂商
    pixelDensity = scrapy.Field()    # 像素密度
    screenToBodyRatio = scrapy.Field()    # 屏占比
    touchSamplingRate = scrapy.Field()    # 触控采样率
    screenColor = scrapy.Field()    # 屏幕色彩
    otherScreenParameters = scrapy.Field()    # 其他屏幕参数
    screenTechnology = scrapy.Field()    # 屏幕技术

    totalNumberCameras = scrapy.Field()    # 摄像头总数
    cameraName = scrapy.Field()    # 摄像头名称
    pixel = scrapy.Field()    # 像素
    aperture = scrapy.Field()    # 光圈
    focusMode = scrapy.Field()    # 对焦方式
    focalLength = scrapy.Field()    # 焦距
    antiShakeFunction = scrapy.Field()    # 防抖功能
    rearVideoShooting = scrapy.Field()    # 后置视频拍摄
    frontFacingVideoShooting = scrapy.Field()    # 前置视频拍摄
    flash = scrapy.Field()    # 闪光灯
    ZoomFactor = scrapy.Field()    # 变焦倍数

    NetworkType = scrapy.Field()    # 网络类型
    simCardType = scrapy.Field()    # SIM卡类型
    wlanFunction = scrapy.Field()    # WLAN功能
    positioningNavigation = scrapy.Field()    # 定位导航
    bluetooth = scrapy.Field()    # 蓝牙
    nfc = scrapy.Field()    # NFC
    infraredFunction = scrapy.Field()    # 红外功能
    BodyInterface = scrapy.Field()    # 机身接口
    batteryType = scrapy.Field()    # 电池类型
    batteryCapacity = scrapy.Field()    # 电池容量
    wiredCharging = scrapy.Field()    # 有线充电

    sensor = scrapy.Field()    # 传感器
    packingList = scrapy.Field()    # 包装清单
    warrantyPolicy = scrapy.Field()    # 保修政策
    warrantyTime = scrapy.Field()    # 质保时间
    warrantyNotes = scrapy.Field()    # 质保备注
    servicePhoneNumber = scrapy.Field()    # 客服电话
