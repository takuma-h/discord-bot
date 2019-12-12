from discord.ext import commands
import random

civList = ['ローマ', 'フン', 'スペイン', 'ヴェネツィア', 'ポーランド', 'インド',
              'バビロニア', 'マヤ', 'インカ', 'ショショーニ', 'アステカ', 'シャム', 'エジプト', '朝鮮', 'アラビア', 'エチオピア', 'ギリシャ', 'イギリス', 'ペルシャ']

mapList = ['小さな陸地プラス', 'シャッフル', 'ドーナツ', 'パンゲア', 'パンゲア＋', 'フラクタル', 'フロンティア', '全世界', '全世界R', '内海', '4隅', '大地', '大島世界', '大陸', '大陸＋', '楕円', '輪', '高地']

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@bot.command()
async def map(ctx):
    await ctx.send(random.choice(mapList))

@bot.command()
async def leader(ctx, *args):
    if len(args) == 0:
        pass
    elif len(args) == 1:
        if args[0].isdecimal():
            tmpCivList = random.sample(civList, len(civList))
            res = [
                f'{i + 1}番目の人の指導者は{tmpCivList.pop()}です'
                for i in range(int(args[0]))
            ]

            await ctx.send('\n'.join(res))
    else:
        excludedDict = {
            'せみころん': ['ショショーニ', 'スペイン', '朝鮮', 'ポーランド'],
            'うぃるじん': ['スペイン', 'インカ'],
            'つっくん': ['イギリス', 'ヴェネツィア'],
            'とりん': ['ショショーニ', 'スペイン', '朝鮮', 'ポーランド']
        }
        choiced = []
        res = []

        for player in args:
            excluded = excludedDict.get(player, [])
            availableList = [
                civ
                for civ in civList
                if (civ not in excluded) and (civ not in choiced)
            ]
            civ = random.choice(availableList)
            choiced.append(civ)
            res.append(f'{player}さんの指導者は{civ}です')

        await ctx.send('\n'.join(res))

@bot.command()
async def dice(ctx, dicenum: int, diceface: int):
    total = sum([random.randrange(1, diceface) for _ in range(dicenum)])
    await ctx.send(f'{dicenum}D{diceface}の実行結果は{total}です')

@bot.command()
async def table(ctx, opt):
    if opt == 'map':
        await ctx.send(', '.join(mapList))
    elif opt == 'leader':
        await ctx.send(', '.join(civList))

# @bot.command()
# async def help(ctx):
#     rep = '''このbotのヘルプです
#     ;map → 「;map」でciv5のmapをランダムに選出、「;map list」で登録されているマップの一覧を表示します。
#     ;leader → 「;leader 数字」で指定した人数分の指導者を選出、「;leader list」で登録されている指導者の一覧を表示
#     ;dice → 「;dise 数字1 数字2」で(数字1 D 数字2)のダイスを振ります。'''
#     await ctx.send(rep)

bot.run('NjUwNjM0OTQ0ODQ2MjMzNjIx.XeOQjQ.SwG1TeRaTO6oX2EfjzQ-3o7sTv8')