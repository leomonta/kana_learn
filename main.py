from random import shuffle
from time import time

HIRAGANA = [
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

KATAKANA = [
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

PRONUNCIATIONS = [
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

class COLS:
	FG_BLACK   = '\033[30m'
	FG_RED     = '\033[31m'
	FG_GREEN   = '\033[32m'
	FG_YELLOW  = '\033[33m'
	FG_BLUE    = '\033[34m'
	FG_MAGENTA = '\033[35m'
	FG_CYAN    = '\033[36m'
	FG_WHITE   = '\033[37m'

	BG_BLACK   = '\033[40m'
	BG_RED     = '\033[41m'
	BG_GREEN   = '\033[42m'
	BG_YELLOW  = '\033[43m'
	BG_BLUE    = '\033[44m'
	BG_MAGENTA = '\033[45m'
	BG_CYAN    = '\033[46m'
	BG_WHITE   = '\033[47m'

	FG_BRIGHTBLACK   = '\033[90m'
	FG_BRIGHTRED     = '\033[91m'
	FG_BRIGHTGREEN   = '\033[92m'
	FG_BRIGHTYELLOW  = '\033[93m'
	FG_BRIGHTBLUE    = '\033[94m'
	FG_BRIGHTMAGENTA = '\033[95m'
	FG_BRIGHTCYAN    = '\033[96m'
	FG_BRIGHTWHITE   = '\033[97m'

	BG_BRIGHTBLACK   = '\033[100m'
	BG_BRIGHTRED     = '\033[101m'
	BG_BRIGHTGREEN   = '\033[102m'
	BG_BRIGHTYELLOW  = '\033[103m'
	BG_BRIGHTBLUE    = '\033[104m'
	BG_BRIGHTMAGENTA = '\033[105m'
	BG_BRIGHTCYAN    = '\033[106m'
	BG_BRIGHTWHITE   = '\033[107m'

	RESET         = '\033[0m'

def rand_kana():

	indxs = [i for i in range(len(PRONUNCIATIONS)*2)]
	kana = HIRAGANA + KATAKANA
	pron = PRONUNCIATIONS + PRONUNCIATIONS

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
		guess = input(f"{COLS.FG_WHITE}{counter}) {kana[i]} :: ")
		end = time()

		t_average += end-start

		if guess == pron[i]:
			print(f"{COLS.FG_BLUE} Correct, it was {pron[i]}")
			score += 1
		else:
			print(f"{COLS.FG_RED} Incorrect, it was {pron[i]}")
			errors.append(i)
		
	print(f"{COLS.FG_WHITE}{len(errors)} Errors: {COLS.FG_RED}")
	for i in errors:
		print(f"{kana[i]} was {pron[i]}")
	
	print(f"\n{COLS.FG_WHITE}Total score {score}/{num_kana} = {score * 100 / num_kana:.2f}% in {t_average / counter:.3}s average\n")


# Main loop
def main():
	while True:
		choise = input(f"{COLS.FG_WHITE}Modes:\n1) Random kana \n2) Random string of kana\n:: ")
		if choise == "1":
			rand_kana()
		elif choise == "2":
			# TODO: string of kana
			print(2)
		elif choise == "exit":
			quit(0)

if __name__ == "__main__":
	main()