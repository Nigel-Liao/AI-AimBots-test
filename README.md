# AI-AimBots-test
Two python-based low-performance AI auto-targeting robots, with two apex game scripts.

[76自瞄狗](https://www.youtube.com/watch?v=ZFnbLfQuMcE)
[輕彈測試](https://www.youtube.com/watch?v=ZQdYYQfw6YM)
[重彈測試](https://www.youtube.com/watch?v=m1YIJfu5JHk)

The first AI automatic aiming robot uses the yolov5 api, which is the fastest in the open source game AI automatic robot I know so far. The other is to use the mediapipe api, which is efficient and has a skeleton effect, making it easier to identify the head, but less efficient when there are multiple people.
Because I am not an expert in AI design, and the environment is not well set up, so that the effect is low, I think it can be improved 1. Recognition efficiency (increase fps, and aiming accuracy) 2. Do not repeat aiming for corpses 3. Lock range and automatic Turn to fire etc...more on that later.

The scripts are all based on autohotkey. The pressure gun script I found on the Internet and slightly modified, the array is really cool. The burst is researched by myself, it is useless, at most let your 30-30 upgrade from M1 Garand to M14, ㄏ ㄏ.

The above are all translated with google translate, why? Because my English suck and I'm almost failing QAQ.

ㄜㄜ ㄜ 翻譯有誤怪谷歌，別在那邊靠杯

找ㄍ喜翻ㄉ資料夾 
```
git clone git@github.com:RinNoOtto/AI-AimBots-test.git
```
或是沒綁github ssh 可以
```
git clone https://github.com/RinNoOtto/AI-AimBots-test.git
```
我乳果詪新則在同資料夾打git pull，雖然應該不會ㄏㄏ


闢化區:
ㄜ 原本沒打算做這ㄍㄉ 隨便找之前做過的js pacman或是c++跟docker做ㄉwordle應該都ㄎ過關 之前研究ㄉpygame也有做ㄍ東方同人作做到一半 但我覺得老師pygame愛教不教連class都沒怎麼講所以老師一定是希望我們做出不一樣ㄉ東西--遊戲外的輔助軟體。 我唬洨ㄉ 主要是受一個之前就看過的中國影片啟發 yt不知怎ㄉ重新推薦。 話說 自己做ai training真的蠻好玩ㄉ 跟opencv也搏鬥一段時間(畢竟之前只是知道 but沒怎麼碰) 雖然最後發現我的ai比原本更爛而放棄(笑) 話說做完才突然想到我有ㄍ之前ㄉkahoot爬蟲自動連刷機器好像也可以改一改交出去 乾 可Cㄌ
