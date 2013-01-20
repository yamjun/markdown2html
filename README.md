markdown2html
=============

markdown to html like a github

##使い方
python とmarkdownのライブラリーが必要  
>$ easy_install markdown  
>$ python markdown2html ○○.mkd   
>(○○.mkd.html＝github風のhtmlが作成される  )

##作った動機
人の日報っていろんなフォーマットがあって見にくいなーと感じたので，  
表示形式がリッチになればまだ見やすくなるかなと考えた．

#フォーマットが決まっていることが重要！#
>
>    ただ，フォーマットが決まりすぎていても，堅苦しいのである程度の自由度も欲しい．  
>    何がどこに書かれているのか分かればいいのにな．
>
>##要件は
>   - 日報のフォーマットをある程度固める．
>   - ＋HTMLでリッチに表示して読みやすくする．  
>   - 出来るだけ自動化して，継続するモチベーションを損なわないようにする(todo)
>
>
>#プログラマへの改善案
>##Markdownを使おう！！##
>   Markdownならお気に入りのテキストエディタで書ける.  
>   プレーンテキストなので，version管理もしやすい.
>
>##ちなみに[vim + markdown + marked](http://blog.glidenote.com/blog/2013/01/10/vim-quickrun-marked/)がすごく便利##
>    vimでMarkdownファイルを編集してまとまったら，プレビューという形が使いやすいので試してみて下さい．
>    
>#TODO(今後の展望)
>   日報なので最終的にはメールで出さないといけない．
>   そのあたりも自動化したい．  
>   今の所，MarkdownファイルをGitで管理してpushした時にhtmlをメールで送信するようにしたら面白いと考えている．  
>   その際，Markdownをhtmlに変換しないといけなさそうなので，そのプログラムを片手間に書いた．  
>   
#Markdownで日報が流行ればいいな





<!--
># 動作 想定 #
>>1. commit or 実行(quick run)でmarkedが走り整形されたプレビューが見られる 
>>2. push requestでメールに送信
>
------------------------

>
># やればいいこと #
>- 一日の流れをシミュレーションする  
>- Todoとの兼ね合いも出来る
>
>- テンプレートの作成  
>- 日報をただの報告書ではなく，作業の指針とすることが可能  
>
>
># プログラム 動作
>- #git hook スクリプトを編集 #
>>    - markdown to html
>>    - cssだけ当てはめる
>>    - html保存
>
>- #メール送信
>>    - push request Hookしてメールを投げる処理を書く
>>       [参考ページ](http://www.exgear.jp/blog/2009/08/gitで更新時にメールを送信する/)
>>
>>    - htmlを送信
>>     [参考ページ](http://www.exgear.jp/blog/2009/08/gitで更新時にメールを送信する/)
>>
>>    - markdownのタイトルをメールタイトルにする
>>
-->

