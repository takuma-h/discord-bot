# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjUwNjM0OTQ0ODQ2MjMzNjIx.XeOQjQ.SwG1TeRaTO6oX2EfjzQ-3o7sTv8'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    command = message.content
    command = command.split(' ')
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if command[0] == ';neko':
        await message.channel.send('にゃーん')

    if command[0] == ';map':
        await message.channel.send(map(command))

    if command[0] == ';leader':
        await message.channel.send(leader(command))

    if command[0] == ';oppai':
        await message.channel.send('は？')

    if command[0] == ';dice':
        await message.channel.send(dice(command[1], command[2]))

    if command[0] == ';help':
        await message.channel.send(help())

# map決め関数


def map(com):
    rep = ''
    mylist = ['小さな陸地プラス', 'シャッフル', 'ドーナツ', 'パンゲア', 'パンゲア＋', 'フラクタル', 'フロンティア',
              '全世界', '全世界R', '内海', '4隅', '大地', '大島世界', '大陸', '大陸＋', '楕円', '輪', '高地']
    if len(com) == 2:
        if com[1] == 'list':
            rep = mylist
    else:
        random.shuffle(mylist)
        rep = mylist[0]
    return rep

# 指導者決め関数


def leader(com):
    num = 0
    rep = ''
    mylist = ['ローマ', 'フン', 'スペイン', 'ヴェネツィア', 'ポーランド', 'インド',
              'バビロニア', 'マヤ', 'インカ', 'ショショーニ', 'アステカ', 'シャム', 'エジプト']
    if com[1] == 'list':
        rep = mylist
    else:
        random.shuffle(mylist)
        num = int(com[1])
        for i in range(num):
            rep += str(i + 1) + '人目の指導者は' + mylist[i] + 'です\n'
    return rep

# サイコロ関数


def dice(num1, num2):
    rep = 0
    num1 = int(num1)
    num2 = int(num2)
    for _ in range(num1):
        rep += random.randrange(1, num2)
    return str(num1) + 'D' + str(num2) + 'の実行結果は' + str(rep) + 'です'

# help用


def help():
    rep = 'このbotのヘルプです\n;map → 「;map」でciv5のmapをランダムに選出、「;map list」で登録されているマップの一覧を表示します。\n;leader → 「;leader 数字」で指定した人数分の指導者を選出、「;leader list」で登録されている指導者の一覧を表示します。\n;dice → 「;dise 数字1 数字2」で(数字1 D 数字2)のダイスを振ります。'
    return rep


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
