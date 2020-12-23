d = input('請問你是否開過車')
if d != '是' and d != '否':
    print('只能輸入是否，懂嗎?') 
    raise SystemExit
age = input('你幾歲?')
age = int(age)
if d == '是':
    if age >= 18:
    	print('你通過測驗')
    else:
    	print('異常發生')
elif d == '否':
	if age >= 18:
		print('還不快去考?')
	else:
		print('等毛長齊再來吧')