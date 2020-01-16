# -*- coding:utf-8 -*-
import subprocess as sp
import json
import os
import requests
import urllib
import time
import logging
import datetime

class Connector():

    def __init__(self):
        now = int(time.time())     
        timeArray = time.localtime(now)
        _time = time.strftime("%Y-%m-%d-%H-%M-%S", timeArray)
        self.logfile = 'log_' + _time + '.log'
        self.config()
        self.set_logger()
    

    def set_logger(self):
        
        self.logger = logging.getLogger()
        self.logger.setLevel(level=logging.INFO)
        handler = logging.FileHandler(self.log_folder + self.logfile, encoding='utf-8')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        console = logging.StreamHandler()
        console.setLevel(logging.WARNING)

        
        self.logger.addHandler(handler)
        self.logger.addHandler(console)


    def is_connected(self):
        result = os.system('ping ' + self.ping_ip)
        if result == 0:
            return True
        else:
            return False


    def config(self):
        conf = open('conf.conf', 'r')
        s = conf.read()
        s = s.replace('\n', '')
        s = s.replace('\t', '')
        data = json.loads(s)
        conf.close()

        connect_info = data['connect']
        self.headers = connect_info['header']
        self.login_url = connect_info['url']
        self.send = connect_info['data-send']
        self.send['DDDDD'] = data['user']
        self.send['upass'] = data['pwd']
        self.ping_ip = connect_info['ip-ping']
        self.retry_connected = connect_info['retry']['connected']
        self.retry_disconnected = connect_info['retry']['disconnected']

        self.log_folder = './log/'
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)
        with open(self.log_folder + self.logfile,'w') as f:
            f.write(self.logfile+'\n')
            

    def connect(self):
        requests.packages.urllib3.disable_warnings()
        session = requests.session()
        r = session.post(self.login_url, headers=self.headers, data=self.send, verify=False)
        print(r.text)


    def run(self):
        while True:
            try:
                if self.is_connected():
                    self.logger.info('Connected')
                    time.sleep(60 * self.retry_connected)
                else:
                    self.logger.warning('Disconnected')
                    self.connect()
                    if self.is_connected():
                        self.logger.warning('Connection repaired')
                        time.sleep(60 * self.retry_connected)
                    else:
                        self.logger.warning('Connection not repaired')
                        time.sleep(60 * self.retry_disconnected)
            except Exception as e:
                self.logger.error('Unkown error, detail infomation: ' + str(e))
                time.sleep(60 * self.retry_disconnected)
