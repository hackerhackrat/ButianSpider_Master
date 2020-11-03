#author:hackerhack@qq.com
#coding=utf-8

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time

def get_data(id):
    headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    print("[*]你的补天个人url地址为:https://butian.net/WhiteHat/d/{}".format(id))
    url = "https://butian.net/WhiteHat/d/{}".format(id)
    print("[*]你目前的状况是：")
    response = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    for another in soup.select('em'):
        anothers = BeautifulSoup(str(another),"html.parser")
        if anothers == None:
            pass
        else:
            print(anothers.string)
    '''
    for other in soup.select('span'):
        others = BeautifulSoup(str(other),"html.parser")
        if others == None:
            pass
        else:
            print(others.string)''' #此段功能点输出太乱
    #print(soup.select('a[href="#@"]'))
    for datas in soup.find_all('a',href='#@'):
        data = BeautifulSoup(str(datas),"html.parser")
        print(data.a.string)
    send_mail(id)
def send_mail(id):
    content = []
    mail_host = "smtp.qq.com"
    mail_user = "xxxx@qq.com" #发件人的邮箱账号
    mail_pass = "xxxxxxxxxxxxx" #发件人smtp的第三方授权码
    mail_recv = "xxxxx@qq.com" #收件人的邮箱账号
    subject = "补天漏洞平台爬虫提醒"
    headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = "https://www.butian.net/WhiteHat/d/" + id
    response = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    for datas in soup.find_all('a',href='#@'):
        data = BeautifulSoup(str(datas),"html.parser")
        content.append(data.a.string)
    for another in soup.select('em'):
        anothers = BeautifulSoup(str(another),"html.parser")
        content.append(anothers.string)
    content = str(content)
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = mail_user
    msg['To'] = mail_recv
    try:
        test = smtplib.SMTP_SSL(mail_host,465)
        test.login(mail_user, mail_pass)
        test.sendmail(mail_user, mail_recv, msg.as_string())
        print("[*]发送成功")
    except Exception as e:
            print("[!]发送失败" + str(e))
    finally:
        test.quit()
        content = []

def main():
    id = input("Please input your butian id>>>")
    while True:
        get_data(id)
        time.sleep(1800)

if __name__ == '__main__':
    main()