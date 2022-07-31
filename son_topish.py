import random

def sontop(x=10):
	tasodifiy_son = random.randint(1,x)
	print(f"Men 1dan {x} gacha son o'yladim.Uni topishga urinib ko'ring")
	taxminlar = 0
	while True:
		taxminlar += 1
		taxmin = int(input(">>>"))
		if taxmin<tasodifiy_son:
			print("Xato men o'ylagan son bundan kichik\n>>>")
		elif taxmin>tasodifiy_son:
			print("Xato men o'ylagan son bundan katta\n>>>")
		else:
			break
	print(f"Tabriklayman.Siz {taxminlar}ta taxminda topdingiz")
	return taxminlar
def sontop_pc(x=10):
	input(f"1 dan {x}gacha son o'ylang va uni kiriting")
	quyi = 1
	yuqori = x
	taxminlar = 0
	while True:
		taxminlar += 1
		if quyi != yuqori:
			taxmin = random.randint(quyi,yuqori)
		else:
			taxmin = quyi
		javob = input(f"Siz {taxmin} sonini o'ylagansiz,\nMen o'ylagan son shundan katta bo'lsa '+' aks holda '-' kiriting ")
		if javob == "-":
			yuqori =  taxmin - 1
		elif javob == "+":
			quyi = taxmin + 1
		else:
			break
	print(f"Men {taxminlar} ta taxminda topdim")
	return taxminlar

def play(x=10):
	yana = True
	while yana:
		taxminlar_user = sontop(x)
		taxminlar_pc = sontop_pc(x)

		if taxminlar_user>taxminlar_pc:
			print(f"Men {taxminlar_pc} taxmin qilib topdim va yutdim")
		elif taxminlar_user<taxminlar_user:
			print(f"Siz {taxminlar_user} taxmin qilib topdingiz va yutdingiz")
		else:
			print("Durrang")
		yana = int(input("Yana o'ynaysizmi?Ha bo'lsa 'True' deb yozing"))

play() 
