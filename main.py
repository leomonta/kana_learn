#!/usr/bin/env python3

from random import randint, shuffle
from time import time

HIRAGANA = [
    "あ", "い", "う", "え", "お",
    "か", "き", "く", "け", "こ",
    "さ", "し", "す", "せ", "そ",
    "た", "ち", "つ", "て", "と",
    "な", "に", "ぬ", "ね", "の",
    "は", "ひ", "ふ", "へ", "ほ",
    "ま", "み", "む", "め", "も",
    "や", "ゆ", "よ",
    "ら", "り", "る", "れ", "ろ",
    "わ", "を", "ん",
    "が", "ぎ", "ぐ", "げ", "ご",
    "ざ", "じ", "ず", "ぜ", "ぞ",
    "だ", "ぢ", "づ", "で", "ど",
    "ば", "び", "ぶ", "べ", "ぼ",
    "ぱ", "ぴ", "ぷ", "ぺ", "ぽ",
    "きゃ", "きゅ", "きょ",
    "しゃ",	"しゅ", "しょ",
    "ちゃ", "ちゅ", "ちょ",
    "にゃ", "にゅ", "にょ",
    "ひゃ", "ひゅ", "ひょ",
    "みゃ", "みゅ", "みょ",
    "りゃ", "りゅ", "りょ",
    "ぎゃ", "ぎゅ", "ぎょ",
    "じゃ", "じゅ", "じょ",
    "びゃ", "びゅ", "びょ",
    "ぴゃ", "ぴゅ", "ぴょ"
]

KATAKANA = [
    "ア", "イ", "ウ", "エ", "オ",
	"カ", "キ", "ク", "ケ", "コ",
	"サ", "シ", "ス", "セ", "ソ",
	"タ", "チ", "ツ", "テ", "ト",
	"ナ", "ニ", "ヌ", "ネ", "ノ",
	"ハ", "ヒ", "フ", "ヘ", "ホ",
	"マ", "ミ", "ム", "メ", "モ",
	"ヤ", "ユ", "ヨ",
	"ラ", "リ",	"ル", "レ", "ロ",
	"ワ", "ヲ", "ン",
    "ガ", "ギ", "グ", "ゲ", "ゴ",
	"ザ", "ジ", "ズ", "ゼ", "ゾ",
	"ダ", "ヂ", "ヅ", "デ", "ド",
	"バ", "ビ", "ブ", "ベ", "ボ",
	"パ", "ピ", "プ", "ペ", "ポ",
	"キャ", "キュ", "キョ",
	"シャ", "シュ", "ショ",
	"チャ", "チュ", "チョ",
	"ニャ", "ニュ", "ニョ",
	"ヒャ", "ヒュ", "ヒョ",
	"ミャ", "ミュ", "ミョ",
	"リャ", "リュ", "リョ",
	"ギャ", "ギュ", "ギョ",
	"ジャ", "ジュ", "ジョ",
	"ビャ", "ビュ", "ビョ",
	"ピャ", "ピュ", "ピョ"
]

PRONUNCIATIONS = [
    "a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "sa", "shi", "su", "se", "so", "ta", "chi", "tsu", "te",
    "to", "na", "ni", "nu", "ne", "no", "ha", "hi", "fu", "he", "ho", "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo",
    "ra", "ri", "ru", "re", "ro", "wa", "wo", "n", "ga", "gi", "gu", "ge", "go", "za", "ji", "zu", "ze", "zo", "da",
    "ji", "zu", "de", "do", "ba", "bi", "bu", "be", "bo", "pa", "pi", "pu", "pe", "po", "kya", "kyu", "kyo", "sha",
    "shu", "sho", "cha", "chu", "cho", "nya", "nyu", "nyo", "hya", "hyu", "hyo", "mya", "myu", "myo", "rya", "ryu",
    "ryo", "gya", "gyu", "gyo", "ja", "ju", "jo", "bya", "byu", "byo", "pya", "pyu", "pyo"
]

# number of kana / pronuncuations in an array

NUM_KANA = len(HIRAGANA)  # 104


class COLS:

	FG_BLACK = '\033[30m'
	FG_RED = '\033[31m'
	FG_GREEN = '\033[32m'
	FG_YELLOW = '\033[33m'
	FG_BLUE = '\033[34m'
	FG_MAGENTA = '\033[35m'
	FG_CYAN = '\033[36m'
	FG_WHITE = '\033[37m'

	BG_BLACK = '\033[40m'
	BG_RED = '\033[41m'
	BG_GREEN = '\033[42m'
	BG_YELLOW = '\033[43m'
	BG_BLUE = '\033[44m'
	BG_MAGENTA = '\033[45m'
	BG_CYAN = '\033[46m'
	BG_WHITE = '\033[47m'

	FG_LIGHT_BLACK = '\033[90m'
	FG_LIGHT_RED = '\033[91m'
	FG_LIGHT_GREEN = '\033[92m'
	FG_LIGHT_YELLOW = '\033[93m'
	FG_LIGHT_BLUE = '\033[94m'
	FG_LIGHT_MAGENTA = '\033[95m'
	FG_LIGHT_CYAN = '\033[96m'
	FG_LIGHT_WHITE = '\033[97m'

	BG_LIGHT_BLACK = '\0[i33[100m'
	BG_LIGHT_RED = '\033[101m'
	BG_LIGHT_GREEN = '\033[102m'
	BG_LIGHT_YELLOW = '\033[103m'
	BG_LIGHT_BLUE = '\033[104m'
	BG_LIGHT_MAGENTA = '\033[105m'
	BG_LIGHT_CYAN = '\033[106m'
	BG_LIGHT_WHITE = '\033[107m'

	RESET = '\033[0m'


def rand_kana() -> None:

	# create an array of twice the lenght of PRONUNCIATIONS filled with integers from 0 -> 2 * len(PRONUNCIATIONS)
	# I use these integers as indexes for a kana
	indxs = [i for i in range(len(PRONUNCIATIONS) * 2)]

	# I combine all the kana in a single array
	all_kana = HIRAGANA + KATAKANA

	# Idem with pronunciations since they are the same for the kana i use the same array twice
	all_pron = PRONUNCIATIONS + PRONUNCIATIONS

	num_all_kana = NUM_KANA * 2

	errors = []

	# number of correctly answered kanas
	score = 0

	# keep track of the number of kana answered
	counter = 0

	t_start, t_end = 0, 0

	# time intervals accumulator
	t_average = 0

	# randomize order
	shuffle(indxs)

	for i in indxs:
		counter += 1

		# prompt the kana
		print(f"{COLS.FG_WHITE}{counter}) {all_kana[i]} :: ", end="")

		# keep track of the time taken to answer
		t_start = time()
		guess = input()
		t_end = time()

		t_average += t_end - t_start

		# since no kana translate to q i can use it as an exit command
		if guess == "q":
			break

		# if the guess is correct update the score and print the correct answer in green
		if guess == all_pron[i]:
			print(f"{COLS.FG_LIGHT_GREEN} Correct, it was {all_pron[i]}")
			score += 1
		# if the guess is incorrect record the error and print the correct answer in red
		else:
			print(f"{COLS.FG_RED} Incorrect, it was {all_pron[i]}")
			errors.append(i)

	# print all the errors recorded in red
	print(f"{COLS.FG_WHITE}{len(errors)} Errors: {COLS.FG_RED}")
	for i in errors:
		print(f"{all_kana[i]} was {all_pron[i]}")

	# print the score the correct percentage and the average time
	print(
	    f"\n{COLS.FG_WHITE}Total score {score}/{num_all_kana} = {score * 100 / num_all_kana:.2f}% in {t_average / counter:.3}s average\n"
	)


def rand_kana_mult(amount: int) -> None:
	MIN_LEN: int = 3
	MAX_LEN: int = 7

	extended_kana = HIRAGANA + HIRA_TSU + KATAKANA + KATA_TSU
	extended_pron = PRONUNCIATIONS + ["-"] + PRONUNCIATIONS + ["-"]

	len_extended_kana: int = len(extended_kana)

	sentence_len = randint(MIN_LEN, MAX_LEN)

	sentence: str = ""
	answer: str = ""
	for i in range(sentence_len):
		indx = randint(0, len_extended_kana - 1)

		curr_kana = extended_kana[indx]
		curr_pron = extended_pron[indx]

		sentence += curr_kana
		answer += curr_pron

	print(sentence)
	print(answer)


# Main loop
def main():
	while True:
		choise = input(f"{COLS.FG_WHITE}Modes:\n1) Random kana \n2) Random string of kana\n3) exit\n:: ")
		if choise == "1":
			rand_kana()
		elif choise == "2":

			amount = input("How many sentences? \n:: ")

			rand_kana_mult(amount)

		elif choise == "3":
			break

	print(COLS.RESET)
	quit(0)


if __name__ == "__main__":
	main()
