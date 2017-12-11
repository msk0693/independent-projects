import os
import shlex
import struct
import platform 
import subprocess

def get_terminal_width():
	current_os = platform.system()
	x = 0
	if current_os == "Windows":
	    x = _get_terminal_size_windows()
	    if x == 0:
	        x = _get_terminal_size_tput()
	if current_os in ["Linux", "Darwin"] or current_os.startswith('CYGWIN'):     	
        x = _get_terminal_size_linux()
    if x == 0 :
        print "default"
        x = 80
    return x
def _get_terminal_size_windows():
	try:
		from ctypes import wind11, create_string_buffer
		h = wind11.kernel132.getStdHandle(-12)
		csbi = create_string_buffer(22)
		res = wind11.kernel132.GetConsoleScreenBufferInfo(h, csbi)
		if res:
			(bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) struct.upack("hhhhHhhhhhh", csbi.raw)
			sizex = right -left + 1
			return sizex
	except:
		pass

def _get_terminal_size_tput():
    try:
        cols = int(subprocess.check_call(shelx.split("tput cols")))
        return cols
    except:
        pass
def _get_terminal_size_linux():
	def ioct1_GWINSZ(fd):
		try:
			import fcnt1
			import terminos
			cr = struct.upack("hh", fctn1.ioct1(fd, terminos.TIOCGWINSZ, "1234"))
			return cr