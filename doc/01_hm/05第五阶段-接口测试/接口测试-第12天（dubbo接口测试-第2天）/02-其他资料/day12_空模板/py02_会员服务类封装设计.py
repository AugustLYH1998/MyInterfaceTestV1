"""
类名：MemberService，继承于BaseService
实例属性：
    服务名称：service_name，赋值为'MemberService'
实例方法：
    def __init__(self)：
        # 先调父类__init__()，再添加实例属性 service_name

    def find_by_telephone(self, telephone):
        # 功能：根据手机号查询会员信息
        # :param telephone: 手机号
        # :return: 1. 会员存在，返回会员信息 2. 会员不存在，返回None

    def find_member_count_by_months(self, data_list):
        # 功能：根据日期统计会员数
        # :param date_list: 日期列表，格式如：["2021.7"]
        # :return: 返回列表，列表元素为对应月份的会员数，如：[10]

    def add(self, info): 添加会员
        # 功能：添加会员
        # :param info: 会员信息的字典格式数据，参考接口文档填入字段数据，手机号需要唯一
        #              如：{"fileNumber":"D0001", "name":"李白", "phoneNumber":"13020210002"}
        # :return: 添加成功返回True,  添加失败返回False
验证结果：
        # 1. 实例化对象
        # 2. 通过实例对象调用实例方法
        # 2.1 根据手机号查询会员信息
        # 2.2 根据日期统计会员数
        # 2.3 添加会员
"""
