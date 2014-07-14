import sys, re, urllib2, urllib, httplib, PIL.Image, ImageTk, StringIO, time, os, datetime
from Tkinter import *

if os.path.isfile("aerogui_config.py"):
  import aerogui_config
  sleeptime = aerogui_config.sleeptime
  reconnectfile = aerogui_config.reconnect
else:
  sleeptime = 30
  reconnectcommand = "sh reconnect.sh"
  
def czas():
  return("[" + str(datetime.datetime.now().time())[0:-7]+ "] ")
  
def getsessid():
  global sessid
  sessid = re.search(r' value="\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w" ', urllib2.urlopen("http://10.2.37.78:8080", urllib.urlencode({'viewForm': 'true'})).read()).group()[8:-2]
  print czas() + "ID sesji PHP: " + sessid

def reconnect():
  print czas() + "Restartowanie polaczenia"
  os.system(reconnectfile)
  time.sleep(60)

def okno(info="nope"):
  root = Tk()
  root.title('Captcha Aero2')
  root.resizable(0, 0)
  img1 = PIL.Image.open(StringIO.StringIO(urllib2.urlopen("http://10.2.37.78:8080/getCaptcha.html?PHPSESSID=" + sessid).read()))
  root.geometry('%dx%d' % (img1.size[0],img1.size[1]+30))
  tkimg = ImageTk.PhotoImage(img1)
  label_image = Label(root, image=tkimg)
  label_image.place(x=0,y=0,width=img1.size[0],height=img1.size[1])
  
  if info!="nope":
    info = Label(root, text=info, bg='white')
    info.pack()

  textFrame = Frame(root)

  napis = Label(textFrame, text="Wpisz kod captcha:")
  napis.pack(side = LEFT)

  cap = Entry(textFrame, width=10)
  cap.pack(side = LEFT)

  def sub(*args):
    global wpisana
    wpisana = cap.get()
    root.destroy()
    root.quit()

  przycisk = Button(textFrame, text="Sprawdz", command=sub)
  przycisk.pack(side = LEFT)

  root.bind('<Return>', sub)

  textFrame.pack(side = BOTTOM)

  root.protocol('WM_DELETE_WINDOW', sys.exit)

  root.mainloop()

  print czas() + "Captcha wpisana przez uzytkownika: " + wpisana

  wynik = urllib2.urlopen("http://10.2.37.78:8080", urllib.urlencode({'viewForm': 'true', 'PHPSESSID': sessid, 'captcha': wpisana})).read()
  if (wynik.find("prawid") > -1) or (wynik.find(" z Internetem.") > -1):
    print czas() + "Captcha prawidlowa"
    reconnect()
  else:
    print czas() + "Zle wpisana captcha lub inny blad"
    okno("Zle wpisana captcha, wpisz ponownie")

print czas() + "Od teraz sprawdzanie czy wymagana jest captcha bedzie sie odbywac co " + str(sleeptime) + " sekund"

while 1:
  print czas() + "Sprawdzanie czy wymagana jest captcha"
  con = httplib.HTTPConnection("google.com")
  con.request("GET", "")
  res = con.getresponse()
  if(res.status == 302) and (res.getheader('Location') == "http://bdi.free.aero2.net.pl:8080/"):
    print czas() + "Wykryto wymaganie captchy"
    getsessid()
    okno()
  else:
    print czas() + "Captcha nie jest narazie wymagana"
  time.sleep(sleeptime)
