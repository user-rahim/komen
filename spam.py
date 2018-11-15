W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan

from time import sleep
from requests import post as put
from sys import exit as keluar
from json import loads as beban
print G+"""
+=+=+=+=+=+=+=+=+=+=+=+=+=+
++=== SPAMER KOMENTAR ===++
+=+=+=+=+=+=+=+=+=+=+=+=+=+=
	  
"""
class main():
	def __init__(self,*args):
		self.persiapan()
		try:
			self.spam()
		except Exception as wibu:
			print wibu
			print O+"finished."
			keluar()
	def persiapan(self):
		try:
			self.file=raw_input('file token list: ')
			self.buka=open(self.file)
			self.id=raw_input('+ target post id: ')
			self.message=raw_input('- type <space> untuk spasi.\n+ message: ').replace('<space>','\n')
			print G+("starting jobs ...")
			print R+("+ post url: https://facebook.com/"+self.id)
		except Exception as f:
			print G+f
			self.persiapan()
	def spam(self):
		o=open(self.file).readlines()
		for x in o:
			icha=x.split('\n')[0]
			payload = {'access_token' :icha, 'message' : self.message}
			rr=put("https://graph.facebook.com/"+self.id+"/comments",data=payload)
			if "error" in rr.text.lower():
				js=beban(rr.text)
				print B+("- Error msg: "+js['error']['message'])
				keluar()
			else:
				print P+"send successfully"
			sleep(00.01)
		self.spam()
try:
	main()
except:
	print W+"\n- spammer finished."
