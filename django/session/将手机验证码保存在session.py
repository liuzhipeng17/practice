# 生成随机验证码，并保存在request.session里面
def createPhoneCode(session,phone): 
	chars=['0','1','2','3','4','5','6','7','8','9'] 
	x = random.choice(chars),random.choice(chars),random.choice(chars),random.choice(chars) 
	verifyCode = "".join(x) 
	session["phoneVerifyCode"] = {"time":int(time.time()), "code":verifyCode, "phone":phone} 
	return verifyCode
	

# 通过云片网第三方服务，将随机验证码发送到手机上
def __send_sms_code(request):
	phone = request.POST.get('tel')
	tpl_id = 1460613
	tpl_value = {'#code#':createPhoneCode(request.session, phone)}
	result = tpl_send_sms(tpl_id, tpl_value, phone)
	result = ast.literal_eval(result)
	return result
	
# 云片网发送短信
import httplib
import urllib
	
version = "v2"
sms_tpl_send_uri = "/" + version + "/sms/tpl_single_send.json"

def tpl_send_sms(tpl_id, tpl_value, mobile):
	params = urllib.urlencode({'apikey': settings.SMS_YUNPIAN_APIKEY, 'tpl_id':tpl_id, 'tpl_value': urllib.urlencode(tpl_value), 'mobile':mobile})
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	conn = httplib.HTTPSConnection(settings.SMS_HOST, port=443, timeout=30)
	conn.request("POST", sms_tpl_send_uri, params, headers)
	response = conn.getresponse()
	response_str = response.read()
	conn.close()
	return response_str