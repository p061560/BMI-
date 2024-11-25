國立空中大學113上ZZZ002班 Python程式設計與實務應用 第10組報告檔案

1.推薦使用桌面板Python 3.13運行，確保安裝時已將PATH  
   【C:\Users\000\AppData\Local\Programs\Python\Python313\Scripts】
    加入環境變數中。(必做)
  2.使用本程式需要先行安裝matplotlib及openai，請先開啟CMD並輸入
   【pip install --upgrade matplotlib】跟【pip install openai==0.28】執行
    安裝。(必做)
  3.程式可以升級，請打【python.exe -m pip install --upgrade pip】。
    (可選)
  4.推薦使用windows運行，linux、mac沒測試過。
  5.如要使用AI建議功能，需申請openai api key，並將api key貼入程式
    碼中，並請注意api key不要外洩。
  6.打開【BMI圖表版.py】or【BMI圖表ai版.py】，即可開始使用。
  7.依照指示輸入數字或Y/N即可。
Q&A:	
Q:有關我的BMI數據會上傳到雲端或被駭嗎?
A:不會，py程式為離線版，皆在你的電腦運行(colab除外)。
Q:我可以一次做多筆BMI測量嗎?
A:可以，程式可以支援連續執行，而不會做完就關閉。
Q:我想看歷史數據，要去哪裡找?
A:歷史數據保存在csv檔中，預設跟程式在同一個資料夾內，路徑可從
  FILE_PATH修改，請善用ctrl+F的功能。
Q:我要怎麼看圖表?	
A:進入程式後按2再按ENTER即可(有無數據都可看)。
Q:我可以刪除特定一組數據嗎?
A:很抱歉，目前我們程式不支援單筆刪除，但你可自行在CSV檔中將特定數據
  列刪除
Q:我可以不要連線AI嗎?
A:可以，在詢問是否要ChatGPT提出建議時，按n即可。
Q:我為何不能正常使用AI?
A:請確認Openai版本為0.28，所有>=1.0的版本皆不支援py中執行，並且 
  需要在程式碼中自行設定API KEY。
Q:如何設定API KEY?
A:請參閱OPENAI官網。
Q:我看數據為什麼都是框框?
A:因為電腦中未安裝微軟正黑體(即便機率非常小)，請自行至網路尋找字形資
  源。
Q:為什麼無法打開py檔?
A:請確認你的電腦已經安裝python或是其他可以打開.py檔的程式。若你已安
  裝卻還是打不開，請執行【11.2】【11.3】步驟
Q:為何在產生圖表時會閃退?
A:可能是你曾使用了AI版或非AI版產生圖表，現在又使用了另一版本，以至
  於在產生圖表時程式發生非預期的錯誤。
