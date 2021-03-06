import curses
import time
import datetime

big_numbers=[
'''\
  ████████████████  \
  ████████████████  \
  ████        ████  \
  ████        ████  \
  ████        ████  \
  ████        ████  \
  ████        ████  \
  ████        ████  \
  ████████████████  \
  ████████████████  \
''',
'''\
              ████  \
              ████  \
              ████  \
              ████  \
              ████  \
              ████  \
              ████  \
              ████  \
              ████  \
              ████  \
''',
'''\
  ████████████████  \
  ████████████████  \
              ████  \
              ████  \
  ████████████████  \
  ████████████████  \
  ████              \
  ████              \
  ████████████████  \
  ████████████████  \
''',
'''\
  ████████████████  \
  ████████████████  \
              ████  \
              ████  \
  ████████████████  \
  ████████████████  \
              ████  \
              ████  \
  ████████████████  \
  ████████████████  \
''',
'''\
  ████        ████  \
  ████        ████  \
  ████        ████  \
  ████        ████  \
  ████████████████  \
  ████████████████  \
              ████  \
              ████  \
              ████  \
              ████  \
''',
'''\
  ████████████████  \
  ████████████████  \
  ████              \
  ████              \
  ████████████████  \
  ████████████████  \
              ████  \
              ████  \
  ████████████████  \
  ████████████████  \
''',
'''\
  ████████████████  \
  ████████████████  \
  ████              \
  ████              \
  ████████████████  \
  ████████████████  \
  ████        ████  \
  ████        ████  \
  ████████████████  \
  ████████████████  \
''',
'''\
  ████████████████  \
  ████████████████  \
  ████        ████  \
  ████        ████  \
              ████  \
              ████  \
              ████  \
              ████  \
              ████  \
              ████  \
''',
'''\
  ████████████████  \
  ████████████████  \
  ████        ████  \
  ████        ████  \
  ████████████████  \
  ████████████████  \
  ████        ████  \
  ████        ████  \
  ████████████████  \
  ████████████████  \
''',
'''\
  ████████████████  \
  ████████████████  \
  ████        ████  \
  ████        ████  \
  ████████████████  \
  ████████████████  \
              ████  \
              ████  \
  ████████████████  \
  ████████████████  \
''',
'''\
                    \
                    \
        ████        \
        ████        \
                    \
                    \
        ████        \
        ████        \
                    \
                    \
''',
]

small_numbers=[
'''\
  ██████  \
  ██  ██  \
  ██  ██  \
  ██  ██  \
  ██████  \
''',
'''\
      ██  \
      ██  \
      ██  \
      ██  \
      ██  \
''',
'''\
  ██████  \
      ██  \
  ██████  \
  ██      \
  ██████  \
''',
'''\
  ██████  \
      ██  \
  ██████  \
      ██  \
  ██████  \
''',
'''\
  ██  ██  \
  ██  ██  \
  ██████  \
      ██  \
      ██  \
''',
'''\
  ██████  \
  ██      \
  ██████  \
      ██  \
  ██████  \
''',
'''\
  ██████  \
  ██      \
  ██████  \
  ██  ██  \
  ██████  \
''',
'''\
  ██████  \
  ██  ██  \
      ██  \
      ██  \
      ██  \
''',
'''\
  ██████  \
  ██  ██  \
  ██████  \
  ██  ██  \
  ██████  \
''',
'''\
  ██████  \
  ██  ██  \
  ██████  \
      ██  \
  ██████  \
''',
'''\
          \
    ██    \
          \
    ██    \
          \
''',
]

blink=[
'''\
        \
        \
    ████\
    ████\
        \
        \
    ████\
    ████\
        \
        \
''',
'''\
          \
      ██  \
          \
      ██  \
          \
''',
]

stdscr = curses.initscr()

curses.noecho()
curses.curs_set(0)

size = (0,0)
numbers = []

if curses.COLS>=100:
    numbers = big_numbers[:]
    size = (20,10)
else:
    numbers = small_numbers[:]
    size = (10,5)

def drawNumber(number, x, y):
    global stdscr
    for i in range(0,size[1]):
        stdscr.addstr(i+y,x,numbers[number][i*size[0]:(i+1)*size[0]],curses.color_pair(1))
def drawBlink(x, y):
    drawNumber(10,x,y)

def tick(blink_flag):
    global stdscr
    stdscr.clear()
    now = now = datetime.datetime.now()
    t = now.time().strftime('%H:%M')
    h1 = int(t[0])
    h2 = int(t[1])
    m1 = int(t[3])
    m2 = int(t[4])
    drawNumber(h1,int(curses.COLS/2)-int(2*size[0]+size[0]/2),int(curses.LINES/2)-int(size[1]/2)) 
    drawNumber(h2,int(curses.COLS/2)-int(size[0]+size[0]/2),int(curses.LINES/2)-int(size[1]/2))
    if blink_flag:
        drawBlink(int(curses.COLS/2)-int(size[0]/2),int(curses.LINES/2)-int(size[1]/2))
    drawNumber(m1,int(curses.COLS/2)+int(size[0]/2),int(curses.LINES/2)-int(size[1]/2))  
    drawNumber(m2,int(curses.COLS/2)+int(size[0]+size[0]/2),int(curses.LINES/2)-int(size[1]/2))
    stdscr.refresh()

def main(stdscr):
    k=0
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    stdscr.nodelay(True)
    

    blink_flag = True
    while (k != ord('q')):
        tick(blink_flag)
        time.sleep(0.5)
        if blink_flag:
            blink_flag = False
        else:
            blink_flag = True

        k = stdscr.getch()


curses.wrapper(main)