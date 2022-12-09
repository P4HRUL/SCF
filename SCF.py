import os,re,sys,bs4,time,json,random,datetime,requests

m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

def jalan(xnxx):
	for hengker in xnxx + '\n':
		sys.stdout.write(hengker);sys.stdout.flush();time.sleep(0.05)

logo = ('''\033[1;97m
 .d8888b.  8888888b.     d8888 888b     d888 
d88P  Y88b 888   Y88b   d88888 8888b   d8888 
Y88b.      888    888  d88P888 88888b.d88888 
 "Y888b.   888   d88P d88P 888 888Y88888P888 
    "Y88b. 8888888P" d88P  888 888 Y888P 888 
      "888 888      d88P   888 888  Y8P  888 
Y88b  d88P 888     d8888888888 888   "   888 
 "Y8888P"  888    d88P     888 888       888 
                                                                                      
\033[1;97m(\033[1;92m•\033[1;97m) facebook : Pahrul Aguspriana XD.
\033[1;97m(\033[1;92m•\033[1;97m) whatsapp : -
\033[1;97m(\033[1;92m•\033[1;97m) version  : 0.2
''')

def login():
	os.system('clear')
	print(logo)
	cookie = str(input(f"(+) cookie : "))
	with requests.Session() as xyz:
		try:
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			jalan ("\n(+) sedang masuk tunggu sebentar...")
			menu()
		except requests.exceptions.ConnectionError:
			print ("(+) koneksi internet bermasalah !!!")
			exit()
		except (KeyError,IOError):
			print ("\033[1;97m(+) cookie anda invalid !!!")
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login()

def menu():
	os.system('clear')
	token  = open('token.txt','r').read()
	cookie = {'cookie':open('cookie.txt','r').read()}
	get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
	jsx = json.loads(get.text)
	nama = jsx["name"]
	id = jsx["id"]
	os.system('clear')
	print(logo)
	print ("(+) Active User : "+ nama + "")
	print ("(+) Facebook Id : "+ id + "")
	print ("")
	print ("(1) spam coment posts facebook ")
	print ("(0) log out ( keluar )")
	pahrul = input ("\n(+) choose : ")
	if pahrul =="1":
		os.system('clear')
		komen()
	elif pahrul =="0":
		jalan ("(+) tunggu sebentar sedang menghapus cookie...")
		os.system("rm cookie.txt")
		os.system("rm token.txt")
		login()
	else:
		print("(+) ngetik apaan lu kambing !!!")
		exit()
	
def komen():
	ok,no=[],[]
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	os.system("clear")
	print(logo)
	id = input(f"(+) id postingan: ")
	komen = input("(+) komentar : ")
	limit = int(input("(+) limit : "))
	print ("")
	for x in range(limit):
		_pahrul_ = requests.post(f'https://graph.facebook.com/{id}/comments/?message={komen}&access_token={token}',cookies={'cookie':cookie})
		cek_st = json.loads(_pahrul_.text)
		print(f'\r[✓] SUCCES : {len(ok)} FAILED : {len(no)}', end=' ')
		if 'id' in cek_st:
			ok.append('succes')
		else:
			no.append('failed')
               
	
	
login()