import subprocess
import datetime
import sys, os
import xml.etree.ElementTree as xml

curDir = os.path.abspath(os.curdir) # директория программы
screenCurDir = os.path.abspath(os.curdir) + '/screenshots/' # директория папки со скриншотами

# функция выбора формата
def getFormat():
		value = input('Формат файла:\n1) tif\n2) jpg\n3) png\n4) eps\n5) psd\n6) bmp\n7) pcx\n')
		formats = ['.tif', '.jpg', '.png', '.eps', '.psd', '.bmp', '.pcx']
		formats = tuple(formats)
		return formats[int(value) - 1]

# функция записи в XML документ
def addToXML(name, dtime):
	root = xml.Element(name)
	screenName = xml.SubElement(root, 'Name')
	screenName.text = name
	screenDtime = xml.SubElement(root, 'Datetime')
	screenDtime.text = dtime
	tree = xml.ElementTree(root)	
	tree.write('struct.xml')

# функция скриншота всей области
def fastScreen():
	dtime = datetime.datetime.today()
	name = 'screenshot_' + dtime.strftime('%Y-%m-%d_%H.%M.%S')
	command = 'ffmpeg -f gdigrab -i desktop ' + screenCurDir + name + getFormat()
	subprocess.call(command)
	addToXML(name, dtime.strftime('%Y-%m-%d_%H.%M.%S'))

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
	addToXML(name, dtime.strftime('%Y-%m-%d_%H.%M.%S'))

# основной цикл программы
while True:	
	os.system('cls')																									
	value = input('1) Сделать скриншот всей области\n2) Сделать скриншот выделенной области\n3) Выйти\n')																
	if value == '1':
		fastScreen()
	elif value == '2':
		additionalScreen()
	elif value == '3':
		sys.exit()
	else: print('не распознанный выбор\n')
