import time
from selenium import webdriver

#ドライバーを読み込む
driver = webdriver.Chrome('./driver/850418387/chromedriver')
#googleのURLを設定
driver.get('http://www.google.com/');
#1秒sleep（sleepを入れる意味はありません。技術メモの為入れています）
#検索ボックスを指定
search_box = driver.find_element_by_name('q')
#search_box.send_keys('成田ゆめ牧場 オートキャンプ場')
#検索ボックスに検索ワード設定
search_box.send_keys('yahoo')
#検索実行
search_box.submit()
#先頭の検索結果を選択
search_box = driver.find_element_by_class_name('LC20lb')
#クリック
search_box.click()
#yahooニュース等に指定されているクラスの一覧を取得
search_box = driver.find_elements_by_class_name('_2bBRLhI5ZpVYu0tuHZEFrn')
#yahooニュースをクリック
search_box[9].click()
print('10秒後にブラウザを終了します。')
#10秒sleep
time.sleep(10)
#終了（ブラウザを閉じる）
driver.quit()


