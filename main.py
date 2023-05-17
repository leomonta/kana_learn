from random import shuffle
from colorama import Fore
from time import time

hiragana = [
	"あ",	"い",	"う",	"え",	"お",
	"か",	"き",	"く",	"け",	"こ",
	"さ",	"し",	"す",	"せ",	"そ",
	"た",	"ち",	"つ",	"て",	"と",
	"な",	"に",	"ぬ",	"ね",	"の",
	"は",	"ひ",	"ふ",	"へ",	"ほ",
	"ま",	"み",	"む",	"め",	"も",
	"や",	"ゆ",	"よ",
	"ら",	"り",	"る",	"れ",	"ろ",
	"わ",	"を",	"ん",
	"が",	"ぎ",	"ぐ",	"げ",	"ご",
	"ざ",	"じ",	"ず",	"ぜ",	"ぞ",
	"だ",	"ぢ",	"づ",	"で",	"ど",
	"ば",	"び",	"ぶ",	"べ",	"ぼ",
	"ぱ",	"ぴ",	"ぷ",	"ぺ",	"ぽ",
	"きゃ",	"きゅ",	"きょ",
	"しゃ",	"しゅ",	"しょ",
	"ちゃ",	"ちゅ",	"ちょ",
	"にゃ",	"にゅ",	"にょ",
	"ひゃ",	"ひゅ",	"ひょ",
	"みゃ",	"みゅ",	"みょ",
	"りゃ",	"りゅ",	"りょ",
	"ぎゃ",	"ぎゅ",	"ぎょ",
	"じゃ",	"じゅ",	"じょ",
	"びゃ",	"びゅ",	"びょ",
	"ぴゃ",	"ぴゅ",	"ぴょ"
]

katakana = [
	"ア",	"イ",	"ウ",	"エ",	"オ",
	"カ",	"キ",	"ク",	"ケ",	"コ",
	"サ",	"シ",	"ス",	"セ",	"ソ",
	"タ",	"チ",	"ツ",	"テ",	"ト",
	"ナ",	"ニ",	"ヌ",	"ネ",	"ノ",
	"ハ",	"ヒ",	"フ",	"ヘ",	"ホ",
	"マ",	"ミ",	"ム",	"メ",	"モ",
	"ヤ",	"ユ",	"ヨ",
	"ラ",	"リ",	"ル",	"レ",	"ロ",
	"ワ",	"ヲ",	"ン",
	"ガ",	"ギ",	"グ",	"ゲ",	"ゴ",
	"ザ",	"ジ",	"ズ",	"ゼ",	"ゾ",
	"ダ",	"ヂ",	"ヅ",	"デ",	"ド",
	"バ",	"ビ",	"ブ",	"ベ",	"ボ",
	"パ",	"ピ",	"プ",	"ペ",	"ポ",
	"キャ",	"キュ",	"キョ",
	"シャ",	"シュ",	"ショ",
	"チャ",	"チュ",	"チョ",
	"ニャ",	"ニュ",	"ニョ",
	"ヒャ",	"ヒュ",	"ヒョ",
	"ミャ",	"ミュ",	"ミョ",
	"リャ",	"リュ",	"リョ",
	"ギャ",	"ギュ",	"ギョ",
	"ジャ",	"ジュ",	"ジョ",
	"ビャ",	"ビュ",	"ビョ",
	"ピャ",	"ピュ",	"ピョ"
]

pronun = [
	"a",	"i",	"u",	"e",	"o",
	"ka",	"ki",	"ku",	"ke",	"ko",
	"sa",	"shi",	"su",	"se",	"so",
	"ta",	"chi",	"tsu",	"te",	"to",
	"na",	"ni",	"nu",	"ne",	"no",
	"ha",	"hi",	"fu",	"he",	"ho",
	"ma",	"mi",	"mu",	"me",	"mo",
	"ya",	"yu",	"yo",
	"ra",	"ri",	"ru",	"re",	"ro",
	"wa",	"wo",	"n",
	"ga",	"gi",	"gu",	"ge",	"go",
	"za",	"ji",	"zu",	"ze",	"zo",
	"da",	"ji",	"zu",	"de",	"do",
	"ba",	"bi",	"bu",	"be",	"bo",
	"pa",	"pi",	"pu",	"pe",	"po",
	"kya",	"kyu",	"kyo",
	"sha",	"shu",	"sho",
	"cha",	"chu",	"cho",
	"nya",	"nyu",	"nyo",
	"hya",	"hyu",	"hyo",
	"mya",	"myu",	"myo",
	"rya",	"ryu",	"ryo",
	"gya",	"gyu",	"gyo",
	"ja",	"ju",	"jo",
	"bya",	"byu",	"byo",
	"pya",	"pyu",	"pyo"
]

def rand_kana():

	indxs = [i for i in range(len(pronun)*2)]
	kana = hiragana + katakana
	pron = pronun + pronun

	num_kana = len(kana)

	errors = []

	score = 0
	counter = 0

	start, end = 0,0

	t_average = 0

	shuffle(indxs)

	for i in indxs:
		counter += 1
		start = time()
		guess = input(f"{Fore.WHITE}{counter}) {kana[i]} :: ")
		end = time()

		t_average += end-start

		if guess == pron[i]:
			print(f"{Fore.BLUE} Correct, it was {pron[i]}")
			score += 1
		else:
			print(f"{Fore.RED} Incorrect, it was {pron[i]}")
			errors.append(i)
		
	print(f"{Fore.WHITE}{len(errors)} Errors: {Fore.RED}")
	for i in errors:
		print(f"{kana[i]} was {pron[i]}")
	
	print(f"\n{Fore.WHITE}Total score {score}/{num_kana} = {score * 100 / num_kana:.2f}% in {t_average / counter:.3}s average\n")


# Main loop
while True:
	start = input(f"{Fore.WHITE}Modes:\n1) Random kana \n2) Random string of kana\n:: ")
	if start == "1":
		rand_kana()
	elif start == "2":
		# TODO: string of kana
		print(2)