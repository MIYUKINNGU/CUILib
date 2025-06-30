# CUILib
CUIを簡単に扱えるようにするPythonライブラリです

## Reference
ライブラリ構造
```
CUILib
├─console
├─CUI
├─Window
├─WindowManager
├─MainloopEventCode
├─ScreenArea
├─InitializeError
├─PropertyError
├─ScreenSize
└─Vector2
```

### console
コンソールを操作するこのライブラリで一番低レイヤなモジュールです
#### initialize(screen_width, screen_height)
スクリーンの大きさを定めてコンソールの初期化を行います。
consoleモジュールを使用する際には必ず最初に実行する必要があります。
#### clear()
NT系OSではclsを、Unix系OSではclearコマンドを実行します。
#### show(*line)
カーソルを1行目1文字目に合わせてからコンソールに文字を表示させます
#### set_cursor(l, v)
カーソルをl行目v文字目に合わせます
#### mainloop(Update) -> int
Updateを常時実行します
Updateの戻り値にはMainloopEventCode型を返すことができます
- MainloopEventCode.Continue: メインループを引き続き実行させます
- MainloopEventCode.Exit_Mainloop: メインループから抜けます

ユーザーがCtrl+Cを押した場合にもメインループから抜けます
戻り値は終了コードです。(現在は0のみ返します)
#### is_initialized() -> bool
consoleが初期化済みであるかを返します
#### get_screen_size() -> ScreenSize
スクリーンの大きさを取得します
#### set_cursor_visible(visible)
カーソルの可視状態を制御します

### CUI
コンソールを操作する基本的なモジュールです
#### initialize(screen_width, screen_height)
スクリーンの大きさを定めてコンソールの初期化を行います
consoleが未初期化状態の場合はconsoleも同時に初期化します
consoleのスクリーンの大きさと異なる場合はInitializeErrorを返します
#### textinput(x, y) -> str
座標を指定してテキスト入力待ち状態にします
#### draw(x, y, data)
座標を指定してテキストを出力します
スクリーンの大きさを超える引数が渡された場合、ValueErrorを返します
#### can_draw(x, y, data) -> bool
draw関数が実行できるかを返します
#### set_halfwidth_mode(condition)
半角のみを出力可能にします
より厳密にはASCII文字のみを出力可能にします
#### set_draw_screen(area)
出力する場所を指定します
- ScreenArea.Back_Screen: バックスクリーンに出力し、screen_update関数が呼び出されてから描画します
- ScreenArea.Real_Screen: コンソールに出力します
#### mainloop(Update) -> int
出力時のみカーソルを非表示にし、set_draw_screen(ScreenArea.Back_Screen)を実行してからconsole.mainloopを呼び出します
#### get_size() -> ScreenSize
コンソールの大きさを取得します
#### is_initialized() -> bool
CUIが初期済みであるかを返します

### Window
CUI上にWindowのようなものを出力するクラスです
#### __init__(self, name, x, y, width, height, useframe=True, isreadonly=False)
コンストラクタです
- name: Window名(タイトル)
- x, y: 座標
- width, height: Windowサイズ
- useframe: Windowのフレームを表示するか
- isreadonly: Windowの出力データ以外を読み取り専用にするか
#### draw(self, x, y, data)
Windowに対してテキストを出力します
#### clear(self)
Windowの出力済みのテキストデータを初期化します
#### show(self)
コンソールにWindowを表示させます
#### get_size(self) -> ScreenSize
現在のWindowサイズを取得します
#### get_name(self) -> str
現在のWindow名(タイトル)を取得します
#### get_pos(self) -> Vector2
現在のWindowの座標を取得します
#### is_readonly(self) -> bool
オブジェクトが読み取り専用かを取得します
#### use_frame(self) -> bool
オブジェクトが枠を描画しているか判定します
#### rename(self, name)
Window名(タイトル)を変更します
#### resize(self, width, height)
Windowサイズを変更します
#### set_pos(self, x, y)
座標を変更します

### WindowManager
Windowオブジェクトを一括管理するモジュールです
#### initialize()
WindowManagerの初期化を行います
CUIが初期化済みである必要があります
#### show()
登録済みのWindowを最背面から順に描画します
#### register_window(name, window)
Windowをnameとして登録します
#### move_front(name)
nameを最前面にします
#### get_all_windows() -> dict
すべてのWindowを辞書配列で取得します
#### get_window(name) -> Window
nameのWindowオブジェクトを取得します
#### get_windows_count()
登録済みのWindowの数を取得します
#### pop_window(name) -> Window
nameのWindowオブジェクトを除外し、そのオブジェクトを返します
#### is_initilized() -> bool
WindowManagerが初期化済みであるかを返します

### MainloopEventCode(Enum)
CUI/console.mainloopで使うイベントコード用の列挙型です
- MainloopEventCode.Continue: メインループを引き続き実行させます
- MainloopEventCode.Exit_Mainloop: メインループから抜けます

### ScreenArea(Enum)
CUI.set_draw_screenで使う設定用の列挙型です
- ScreenArea.Back_Screen: バックスクリーンに出力し、screen_update関数が呼び出されてから描画します
- ScreenArea.Real_Screen: コンソールに出力します

### InitializeError(Exception)
モジュールを初期化する際に何かしらの原因で失敗すると返される例外です。

### PropertyError(Exception)
Windowのプロパティの変更でreadonlyの時に返される例外です。

### ScreenSize
スクリーンの大きさ用のクラスです
#### __init__(self, width, height)
コンストラクタです
#### get_size(self) -> tuple[int, int]
タプルで大きさを返します
#### get_width(self) -> int
widthを取得します
#### get_height(self) -> int
heightを取得します

### Vector2
二次元座標用のクラスです
#### __init__(self, x, y)
コンストラクタです
#### get_pos(self)
座標を取得します
#### get_x(self)
X座標を取得します
#### get_y(self)
Y座標を取得します

## サンプルプログラム
```python
import CUILib
import keyboard

CUILib.CUI.initialize(100, 30)
CUILib.WindowManager.initialize()
CUILib.WindowManager.register_window("Window", CUILib.Window("Window Window Window Window", 1, 1, 20, 10))

Text = "Hello World, CUILib! This is a Window object."

l = []
c = -1
for i in range(len(Text)):
    if i%(CUILib.WindowManager.get_window("Window").get_size().get_width()-2) == 0:
        l.append("")
        c += 1
    l[c] += Text[i]

CUILib.WindowManager.get_window("Window").draw(2, 2, l)

pressedr = False
pressedl = False
pressedu = False
pressedd = False
pressedD = False
pressedA = False
def Update():
    global pressedr, pressedl, pressedu, pressedd, pressedD, pressedA
    
    window = CUILib.WindowManager.get_window("Window")
    window_size = window.get_size()
    window_position = window.get_pos()
    
    if keyboard.is_pressed("esc"):
        return CUILib.MainloopEventCode.Exit_Mainloop
    
    if not pressedr and keyboard.is_pressed("right") and window_position.get_x()+window_size.get_width()-1 < CUILib.CUI.get_size().get_width():
        window.set_pos(window_position.get_x()+1, window_position.get_y())
        pressedr = True
    if not pressedl and keyboard.is_pressed("left") and window_position.get_x() > 1:
        window.set_pos(window_position.get_x()-1, window_position.get_y())
        pressedl = True
    if not pressedu and keyboard.is_pressed("up") and window_position.get_y() > 1:
        window.set_pos(window_position.get_x(), window_position.get_y()-1)
        pressedu = True
    if not pressedd and keyboard.is_pressed("down") and window_position.get_y()+window_size.get_height()-1 < CUILib.CUI.get_size().get_height():
        window.set_pos(window_position.get_x(), window_position.get_y()+1)
        pressedd = True
    if not pressedD and keyboard.is_pressed("d") and window_position.get_x()+window_size.get_width()-1 < CUILib.CUI.get_size().get_width():
        pressedD = True
        window.resize(window_size.get_width()+1, window_size.get_height())
        window.clear()
        l = []
        c = -1
        for i in range(len(Text)):
            if i%(window.get_size().get_width()-2) == 0:
                l.append("")
                c += 1
            l[c] += Text[i]

        window.draw(2, 2, l)
    if not pressedA and keyboard.is_pressed("a") and window_size.get_width() > 21:
        pressedA = True
        window.resize(window_size.get_width()-1, window_size.get_height())
        window.clear()
        l = []
        c = -1
        for i in range(len(Text)):
            if i%(window.get_size().get_width()-2) == 0:
                l.append("")
                c += 1
            l[c] += Text[i]

        window.draw(2, 2, l)
        
    
    if not keyboard.is_pressed("right"):
        pressedr = False
    if not keyboard.is_pressed("left"):
        pressedl = False
    if not keyboard.is_pressed("up"):
        pressedu = False
    if not keyboard.is_pressed("down"):
        pressedd = False
    if not keyboard.is_pressed("d"):
        pressedD = False
    if not keyboard.is_pressed("a"):
        pressedA = False
    
    CUILib.WindowManager.show()
    
    return CUILib.MainloopEventCode.Continue

CUILib.CUI.mainloop(Update)
CUILib.console.set_cursor_visible(True)
```
## Feedback
バグはTwitterのDMかDiscordのDMで教えてください
嫌な顔しながら修正します
それ以外はどこでも構いません
エゴサはしないので直接伝えたいならDMでお願いします

あとデバッグちゃんとしてないので探せばバグはあると思います。
