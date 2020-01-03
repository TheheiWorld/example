#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2019/3/22 上午11:07

import getpass
import requests
from pyquery import PyQuery as pq

class Login(object):

    def __init__(self):
        base_url = 'https://github.com/'
        self.login_url = base_url + 'login'
        self.post_url = base_url + 'session'
        self.logined_url = base_url + 'settings/profile'
        self.session = requests.Session()
        self.session.headers= {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }

    def token(self):
        response = self.session.get(self.login_url)
        doc = pq(response.text)
        token = doc('input[name="authenticity_token"]').attr('value').strip()
        return token

    def login(self, email, password):
        token = self.token()
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': token,
            'login': email,
            'password': password
        }

        response = self.session.post(self.post_url, data=post_data)
        print(f"\n请求 url:{response.url} ")
        if response.status_code == 200:
            print("status_code : 200")
            self.home(response.text)
        response = self.session.get(self.logined_url)
        if response.status_code == 200:
            print("status_code : 200")
            self.profile(response.text)

    def home(self, text):
        doc = pq(text)
        user_name = doc("summary> span").text().strip()
        print(f"用户名：{user_name}")
        repositories = doc("div.Box-body > ul > li").text().strip()
        for repository in repositories:
            print(repository)

    def profile(self, text):
        doc = pq(text)
        page_title = doc('title').text()
        user_profile_bio = doc("#user_profile_bio").text()
        user_profile_company = doc("#user_profile_company").attr("value")
        user_profile_location = doc("#user_profile_location").attr("value")
        print(f"页面标题：{page_title}")
        print(f"用户资料描述：{user_profile_bio}")
        print(f"用户资料公司：{user_profile_company}")
        print(f"用户资料地点：{user_profile_location}")

    def main(self):
        email = input("email or username")
        password = getpass.getpass('password:')
        self.login(email=email, password=password)

if __name__ == '__main__':
    login = Login()
    login.main()


