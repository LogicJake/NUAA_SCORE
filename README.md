# NUAA_SCORE
验证码获取地址：http://ded.nuaa.edu.cn/mss/Account/Vcode/signinid  
登陆地址：http://ded.nuaa.edu.cn/mss/Account/SignIn
http://ded.nuaa.edu.cn/mss/account/dedsignin?u=161540209&t=10:38:59&v=0.1&s=b7e27253fd0ee336cdd48a1f76b3bf8b&p=/studentresults/show/161540209

1. 先访问验证码地址，假如访问没有带上cookie项ASP.NET_SessionId，将会返回cookie项ASP.NET_SessionId和对应的验证码，后台将两者绑定
2. 登陆时，post数据{'VCodeId': 'signinid', 'UserName':'','Password':'','VaildCode':code,'RememberMe':'true'}，并带上cookie项ASP.NET_SessionId进行验证码验证，验证通过则会在本地设置cookie项.aspx_auth_ded_mss，从而能够利用此cookie查看成绩
# 使用方法
1. 新建1.ini文件作为配置文件，文件中有五行，由上到下依次是  
//教务处账号  
//教务处密码  
//邮件收信人的邮箱账号  
//程序登陆的qq邮箱的QQ账号  
//程序登陆的qq邮箱的授权码    
2. 命令行运行python main.py
