import subprocess
import datetime
import sys, os
import xml.etree.ElementTree as xml
import time

curDir = os.path.abspath(os.curdir) # директория программы
screenCurDir = os.path.abspath(os.curdir) + '/screenshots/' # директория папки со скриншотами

# функция выбора формата
def getFormat():
		value = input('Формат файла:\n1) tif\n2) jpg\n3) png\n4) eps\n5) psd\n6) bmp\n7) pcx\n')
		formats = ['.tif', '.jpg', '.png', '.eps', '.psd', '.bmp', '.pcx']
		formats = tuple(formats)
		return formats[int(value) - 1]

# функция записи в XML документ
def createXML():
	files = os.listdir(screenCurDir)
	tree = xml.parse('struct.xml')
	root = tree.getroot()
	datelist = []
	for child in root:
		datelist.append(child.find('date').text)
	for i in range(len(files)):
	 	name = str(files[i])
	 	size = str(os.path.getsize(screenCurDir + files[i]))
	 	date = str(time.ctime(os.path.getctime(screenCurDir + files[i])))
	 	if date not in datelist:
	 		elem = xml.Element(name)
	 		nElem = xml.SubElement(elem, 'name')
	 		nElem.text = name
	 		dElem = xml.SubElement(elem, 'date')
	 		dElem.text = date
	 		sElem = xml.SubElement(elem, 'size')
	 		sElem.text = size
	 		root.append(elem)
	 		tree.write('struct.xml')

# функция скриншота всей области
def fastScreen():
	dtime = datetime.datetime.today()
	name = 'screenshot_' + dtime.strftime('%Y-%m-%d_%H.%M.%S')
	command = 'ffmpeg -f gdigrab -i desktop ' + screenCurDir + name + getFormat()
	subprocess.call(command)

# функция скриншота определённой области
def additionalScreen():
	beginX = input('Начальная координата X:\n')
	beginY = input('Начальная координата Y:\n')
	width = input('Ширина:\n')
	height = input('Высота:\n')
	resolution = width + 'x' + height
	dtime = datetime.datetime.today()
	name = 'screenshot_' + dtime.strftime('%Y-%m-%d_%H.%M.%S')
	command = 'ffmpeg -f gdigrab -video_size ' + resolution + ' -offset_x '+ beginX + ' -offset_y '+ beginY + ' -i desktop ' + screenCurDir + name + getFormat()
	subprocess.call(command)

# основной цикл программы
while True:	
	#os.system('cls')																									
	value = input('1) Сделать скриншот всей области\n2) Сделать скриншот выделенной области\n3) Обновить XML\n4) Выйти\n')																
	if value == '1':
		fastScreen()
	elif value == '2':
		additionalScreen()
	elif value == '3':
		createXML()
	elif value == '4':
		sys.exit()
	else: print('не распознанный выбор\n')
