# chouseisan_script
[調整さん](https://chouseisan.com/)の候補日程を自動生成

## 使い方
1. 本リポジトリを**fork**
2. **Actions >> I understand my workflows, go ahead and enable them**をクリック
![screen_shot_1](./pic/screen_shot_1.png)
2. [setting.csv](./setting.csv)を変更して**push**
3. **Github Actions**を用いて自動実行
4. [output.txt](./output.txt)を[調整さん](https://chouseisan.com/)にコピペ

## setting.csvについて
- setting.csvの例
  - 2022年07月11日~07月19日の期間, 13時から19時の間に2時間おきに候補日程が生成されます。
    - 曜日の行を0にすると、その曜日は候補日から除外されます。
      - この例だと土曜、日曜を除く平日のみ候補日程が生成されます。
    - exlusion date : 7月18日は候補日から除外
    - exlusion time : 15時は除外 
  
~~~
year,2022
start date,07,11
finish date,07,19
Monday,1
Tuesday,1
Wednesday,1
Thursday,1
Friday,1
Saturday,0
Sunday,0
time start,13
time finish,19
time span,2
exclusion date,7,18
exclusion time,15
~~~

## 生成されたoutput.txt
~~~
7/11(月) 13:00~
7/11(月) 17:00~
7/11(月) 19:00~
7/12(火) 13:00~
7/12(火) 17:00~
7/12(火) 19:00~
7/13(水) 13:00~
7/13(水) 17:00~
7/13(水) 19:00~
7/14(木) 13:00~
7/14(木) 17:00~
7/14(木) 19:00~
7/15(金) 13:00~
7/15(金) 17:00~
7/15(金) 19:00~
7/19(火) 13:00~
7/19(火) 17:00~
7/19(火) 19:00~
~~~