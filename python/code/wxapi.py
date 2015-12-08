# -*- coding: utf-8

import urllib2
# import urllib
import json
import sys


class WXAPI(object):

	__access_token = ''

	def __init__(self):
		pass

	def Get_access_token(self,AppID,AppSecret):
		token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'%(AppID,AppSecret)
		r = urllib2.urlopen(token_url)
		html = r.read()
		info = json.loads(html)

		self.__access_token = info['access_token']

		return self.__access_token
		

	def Post(self,url, data): 
		req = urllib2.Request(url) 
		# data = urllib.urlencode(data) 
		# enable cookie 
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor()) 
		response = opener.open(req, data) 
		html  = response.read()
		info = json.loads(html)
		return info

	def Get_user_list(self):
		user_list_url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid='%self.__access_token
		r = urllib2.urlopen(user_list_url)
		html = r.read()
		info = json.loads(html)

		user_list = info['data']

		# return user_list

	def Get_user_by_group(self,groupid):

		group_id_list = []

		get_user_group_id_url = 'https://api.weixin.qq.com/cgi-bin/groups/getid?access_token=%s'%self.__access_token

		user_list_dict = self.Get_user_list()
		user_list = user_list_dict['openid']

		for openid in user_list:
			send_values = {"openid":openid}
			send_data = json.dumps(send_values)
			groupidhtml = self.Post(get_user_group_id_url,send_data)
			user_groupid = groupidhtml['groupid']
			if user_groupid == groupid:
				group_id_list.append(openid)

		return group_id_list

	def Send_template_by_list(self,userlist,notifystr):
		send_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s'%self.__access_token

		notifylist = notifystr.split('#.#')

		for openid in userlist:
			send_values = {
	        "touser":openid,
	        "template_id":[微信模板id],
	        "url":[yoururl],
	        "topcolor":"#FF0000",	
	        "data":{
	            "first": {
	                "value":u'报警平台 : %s'%notifylist[0],
	                "color":"#173177"
	            },
	            "keyword1":{
	                "value":notifylist[1],
	                "color":"#173177"
	            },
	            "keyword2":{
	                "value":notifylist[2],
	                "color":"#173177"
	            },
	            "keyword3":{
	                "value":notifylist[3],
	                "color":"#173177"
	            },
	            "keyword4":{
	                "value":notifylist[4],
	                "color":"#173177"
	            },
	            "keyword5":{
	                "value":notifylist[5],
	                "color":"#173177"
	            },
	            "remark":{
	            	"value":u'服务器IP地址 ：%s'%notifylist[6],
	            	"color":"#173177"
	            }
	    	}
	        }
			send_data = json.dumps(send_values)
			response = self.Post(send_url,send_data)



default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

wx = WXAPI()


notifystr = str(sys.argv[1])

wx.Get_access_token(AppID,AppSecret)
# userlist = wx.Get_user_by_group(101)
# print userlist

userlist = [openid1,openid2,...]

wx.Send_template_by_list(userlist,notifystr)
