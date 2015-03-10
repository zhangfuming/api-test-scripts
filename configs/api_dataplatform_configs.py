# coding=utf-8
__author__ = 'zhangfuming'

apis = {
    'desc':'数据平台api',
    'list':[
         {
            'desc':'获取图片验证码',
            'url_dev':'http://test.api.baidao.com/api/2/bjwd/verify/apply/imagecode/default/json?imageToken=bjwd123456789',
            'url_pro':'http://TODO/dataplatform/api/2/bjwd/verify/apply/imagecode/default/json?imageToken=bjwd123456789',
            'method':'GET'
        },
         {
            'desc':'事件通知',
            'url_dev':'http://test.api.baidao.com/api/1/events/notify/json',
            'url_pro':'http://TODO/dataplatform/api/1/events/notify/json',
            'method':'POST',
            'header':['Content-Type:application/x-www-form-urlencoded'],
            'params':{"event":"acc","token":"token","server":"tt"}
        } 
    ]
}
