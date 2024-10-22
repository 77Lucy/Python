#同时抓取多个网页信息，本例子有误，因为url现在已经不存在


import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor
import time
import random
import logging
import threading

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 线程锁
lock = threading.Lock()

# 打开 CSV 文件，用于存储抓取到的数据
with open("data.csv", mode="w", encoding="utf-8", newline="") as f:
    csvwriter = csv.writer(f)

    def download_one_page(url):
        try:
            # 获取网页源代码
            resp = requests.get(url)
            resp.encoding = "utf-8"  # 设置编码
            html = etree.HTML(resp.text)

            # 提取页面中表格的内容
            table = html.xpath("//html/body/div[2]/div[4]/div[1]/table")
            if not table:
                logging.warning(f"{url} 中未找到表格")
                return

            table = table[0]  # 取第一个表格
            trs = table.xpath(".//tr[position()>1]")  # 忽略表头

            # 遍历每行数据
            for tr in trs:
                txt = tr.xpath("./td/text()")
                # 数据清理：移除斜杠
                txt = [item.replace("\\", "").replace("/", "") for item in txt]

                # 确保写入时是线程安全的
                with lock:
                    csvwriter.writerow(txt)  # 写入 CSV 文件

            logging.info(f"{url} 提取完毕！")

        except requests.RequestException as e:
            logging.error(f"请求失败：{url} - {e}")
        except Exception as e:
            logging.error(f"{url} 解析时出现错误：{e}")


    # 主函数，使用多线程抓取多个页面
    def main():
        with ThreadPoolExecutor(max_workers=50) as executor:
            base_url = "http://www.xinfadi.com.cn/marketanalysis/0/List/{}.shtml"
            # 假设有 200 页需要抓取
            urls = [base_url.format(i) for i in range(1, 200)]

            for url in urls:
                # 提交任务给线程池时不延迟
                executor.submit(download_one_page, url)

                # 延迟在每次提交任务后
                time.sleep(random.uniform(0.5, 1.5))


    if __name__ == "__main__":
        main()
        logging.info("全部页面下载完成！")
