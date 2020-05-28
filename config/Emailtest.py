import os
import smtplib
import time
from email.mime.text import MIMEText  # 发送正文
from email.mime.multipart import MIMEMultipart  # 发送多个部分
from email.mime.application import MIMEApplication  # 发送附件
from email.header import Header  # 从email包引入Header()方法，是用来构建邮件头

from utils.emailConfig import ReadConfig
from utils.findpath import BASE_PATH

read_conf = ReadConfig()
mail_host = read_conf.get_email('mail_host')  # 从配置文件中读取，邮件host
mail_user = read_conf.get_email('mail_user')  # 从配置文件中读取，登录邮箱用户名
mail_pass = read_conf.get_email('mail_pass')  # 从配置文件中读取，登录邮箱密码
subject = read_conf.get_email('subject')  # 从配置文件中读取，邮件主题
sender = read_conf.get_email('sender')  # 从配置文件中读取，邮件发送人
receivers = read_conf.get_email('receivers')  # 从配置文件中读取，邮件收件人
mail_path = os.path.join(BASE_PATH,"report","测试报告.html") # 获取测试报告路径


class TestMail(object):

     def send_mail(self):
         # 构造一个邮件体：正文、附件
         msg = MIMEMultipart()  # 邮件体
         msg['From'] = sender  # 发件人
         msg['To'] = receivers  # 收件人
         tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # 获取系统时间
         msg['Subject'] = Header(subject + '_' + tm, 'utf-8')  # 邮件主题
         # 构建正文
         content = """
                    XXXXXXXXXXXX
                   """
         email_body = MIMEText(content, 'plain', 'utf-8')
         msg.attach(email_body)  # 将正文添加到邮件体中
         # 构建附件
         att = MIMEApplication(open(mail_path, 'rb').read())  # 打开附件
         att.add_header("Content-Disposition", "attachment", filename='测试报告.html')  # 为附件命名
         msg.attach(att)  # 添加附件到邮件体中

         try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 使用smtp协议发送邮件，SSL协议来进行加密传输，465为端口号
            smtpObj.login(mail_user, mail_pass)  # 邮箱登录
            smtpObj.sendmail(sender, receivers, msg.as_string())  # 发送邮件
            print('邮件已发送')
            smtpObj.quit()
         except smtplib.SMTPException:
             print('发送失败')


if __name__ == "__main__":
    send = TestMail()
    send.send_mail()
    print(mail_path)