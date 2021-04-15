def hangman(word):  # hamgman関数を作成。wordという引数を受け取る。これはプレーヤー2に当てて欲しい単語。
    wrong = 0  # プレーヤー2が何回間違えたかを数える変数。
    stages = ["",  # stageのリストの文字列を1行に1つずつ出力するとつられた人の絵が表現できる。
              "__________       ",
              "|                ",
              "|       O        ",
              "|      /|\       ",
              "|      / \       ",
              "|                ",
              ]
    rletters = list(word)  # wordの文字をリスト化したもの。答えなければいけない残りも文字を覚えておく用。
    board = ["_"] * len(word)  # 文字列のリストでヒント用。文字の数だけ "* len(word)" で増やしている。
    win = False  # 勝ったか負けたかの判定用。
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:  # ループは変数wrongの値がlen(stages)-1よりも小さい間繰り返される。
        # 変数wrongにはプレーヤー2がこれまで答えてきた回数が記録されるのでリストstagesの要素数と同じだけ間違えたらループが終了する。
        print("\n")
        msg = "1文字予想してね→"
        char = input(msg)  # 入力された回答を変数charに割り当てる。
        if char in rletters:  # 入力された回答がrlettersの要素にあったらプレーヤー2が入力した文字は正解。→リストの変数boardを更新
            # board変数は後でプレーヤーが答えた文字と答えてない文字を表示するために使用。
            cind = rletters.index(char)
            # indexメソッドを使って、入力された文字がrlettersの何番目にあるかのindexを取得
            board[cind] = char
            rletters[cind] = '$'  # このindex値を使ってboardのアンダースコアを正しい文字に置き換える。
        else:  # 同じ文字が複数含まれている時のために、正解した文字を$に置き換える。そうしないと、最初に見つけた要素しか返してくれない。
            wrong += 1  # プレーヤーの回答が間違っていたらwrongを1つインクリメントする。
        # boardとstagesのリストを使って、スコアボードとハングマンを出力する。スコアボードとして"".join(board)を出力。
        print(" ".join(board))
        e = wrong + 1
        print(" ".join(stages[0:e]))
        if "_" not in board:  # boardにアンダースコアがなければ全ての文字が正解＝プレーヤー2の勝ち
            print("あなたの勝ち！")  # winにTrueを割り当ててbreakでループ終了。
            print(" ".join(board))
            win = True
            break
        if not win:  # winがFalseの場合は「あなたの負け！」と表示
            print("\n".join(stages[0:wrong+1]))
            print("あなたの負け！正解は{}.".format(word))


hangman("cat")
