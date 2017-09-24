# NUAA_SCORE
验证码获取地址：http://ded.nuaa.edu.cn/mss/Account/Vcode/signinid  
登陆地址：http://ded.nuaa.edu.cn/mss/Account/SignIn  
1. 先访问验证码地址，假如访问没有带上cookie项ASP.NET_SessionId，将会返回cookie项ASP.NET_SessionId和对应的验证码，后台将两者绑定
2. 登陆时，post数据{'VCodeId': 'signinid', 'UserName':'','Password':'','VaildCode':code,'RememberMe':'true'}，并带上cookie项ASP.NET_SessionId进行验证码验证，验证通过则会在本地设置cookie项.aspx_auth_ded_mss，从而能够利用此cookie查看成绩
