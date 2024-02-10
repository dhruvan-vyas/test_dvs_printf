# Enhance your Python project's console output with stylish printing animations using the dvs_printf module.
# from time import sleep
ranchoice = [
    "b","c","d","e","f","g","h","i","c",
    "d","l","a","w","t","r","s","v","x",
    "z","n","o","-","p","q","r","s","t"]
"random letters for matrix style animation"

def listfunction(*values: tuple , getMat: str | None= False) -> list[str]:
    """
return list with each element given.
takes any DataType and gives `str(list)` with all elements by index 

`set, dict, list, tuple` breake this kind 
of DataSet and add Them into a list by index.

getMat: `detult getMat = False`
  if matrix is given, set `getMat=True`
  it breaks metix in `rows by index` and
  convet that in to string and add that in to list
    """
    if len(values)==1:
        values=values[0]  
    
    newa_a=[]
    # try:
    # return values
    # except:pass

    for value in values:
        if getMat:
            try:
                if "numpy" in  str(type(value)):
                    newa_a.extend(
                [str(sublist.tolist()) for sublist in value.reshape(-1, value.shape[-1])]
                    )
                    if "show" in str(getMat).lower():
                        newa_a.extend([
    "<class 'numpy.ndarray'","dtype="+str(value.dtype)+" ","shape="+str(value.shape)+">"
                    ])
                    continue
                elif "tensorflow" in str(type(value)):    
                    from tensorflow import reshape,shape;newa_a.extend(
                [str(sublist.numpy().tolist()) for sublist in reshape(value, [-1, shape(value)[-1]])]
                    )
                    if "show" in str(getMat).lower():newa_a.extend([
    "<class 'Tensorflow'",(str(value.dtype).replace("<","")).replace(">","") +" ","shape: "+str(value.shape)+">"
                    ])
                    continue  
                elif "torch" in str(type(value)):
                    newa_a.extend(
                [str(sublist.tolist()) for sublist in value.view(-1, value.size(-1))]
                    )
                    if "show" in str(getMat).lower():newa_a.extend([
    "<class 'torch.Tensor'", " dtype="+str(value.dtype)+" "," shape="+str(value.shape)+">"
                    ])
                    continue
                elif "pandas" in str(type(value)):
                    newa_a.extend(value.stack().apply(lambda x: str(x)).tolist())
                    if "show" in str(getMat).lower():
                        newa_a.extend(["<class 'pandas'"," shape="+str(value.shape)+" "+">"])
                        newa_a.extend(
    (str(value.dtypes).replace("\n","@#$@")).replace("    ",": ").split("@#$@")
                    )
                    continue
                else: 
                    if isinstance(value,list) and isinstance(value[0],list):newa_a.extend(listfunction(value, getMat=True))
                    elif isinstance(value,list):newa_a.append(str(value).replace("\n"," "))
                    continue
            except:pass

        if type(value)==dict:
            for i in value:newa_a.extend(f"{i}: {value[i]}".replace("\n","@#$%#$@"+" "*(len(i)+2)).split("@#$%#$@"))
        elif (type(value)==list)or(type(value)==tuple)or(type(value)==set):newa_a.extend(listfunction(value))
        elif (type(value)==str)and("\n" in value): newa_a.extend(value.split("\n"))
        else: newa_a.extend(str(value).split("\n"))

    return newa_a


from time import sleep
from os import get_terminal_size

def printf(*values: object, 
            style: str | None = 'typing', 
            speed: int | None = 3, 
         interval: int | None = 2,  
            stay: bool | None = True,
            getMat: bool | str | None = False) :
    ''' 
### prints values to a stream.

style
   style is defins different types of print animation. `default a "typing"`. 
    [typing, headline, newsline, mid, gunshort, snip, matrix, matrix2, \n     left, right, center, centerAC, centerAL, centerAR, f2b, b2f, help] 
speed
   speed is defins printf's animation speed `from 1 to 6` `default a 3`
interval
   waiting time between printing animation of two lines `default a 2`.
    `(interval in second >= 0)` from 0 to 5 or greater
stay 
   stay decides after style animation whether you want the 
    stream on terminal OR Not. `default a True`. don't work some style

# getMat
#     "hello worlsd

`style="help" for more info`.
    '''
    values=listfunction(values, getMat=getMat)
    style=str(style).lower()
    if interval<0:interval=2
    elif style in ["right","left"]:speed=(.032/speed)if(speed>=1 and speed<=6)else .016
    elif style=="gunshort":speed=(.064/speed)if(speed>=1 and speed<=6)else .016
    elif style=="newsline":speed=(.18/speed)if(speed>=1 and speed<=6)else .06
    elif style=="snip":speed=(.016/speed)if(speed>=1 and speed<=6)else .008
    elif style=="mid":speed=(.16/speed)if(speed>=1 and speed<=6)else .08
    else:speed=(.16/speed)if(speed>=1 and speed<=6)else .08

    print('\033[?25l', end="")
    if style == "typing":
        for x in values:
            for i in x:
                print(i+"|\b", end="",flush=True)
                sleep(speed)
            print(" ")
            sleep(interval)
    elif style == "headline":
        for x in values:
            line = ""
            x = str(x)
            for y in range(0, len(x)):
                line = line + x[y].replace("\n","")
                print(line+"⎮",end="\r",flush=True)
                sleep(speed)
                print(line[:len(line)],end="\r",flush=True)
                print(end="\x1b[2K")
            sleep(interval)
            for i in range(0, len(x)):
                delete_last = x[:len(x)-i-1].replace("\n","")
                print(delete_last+"|",end="\r",flush=True)
                sleep(speed)
                print(end="\x1b[2K")
    elif style == "newsline":
        longLineLen = 30
        for L in values:
            if len(L)>longLineLen:longLineLen=len(L)
        for value in values:
            for i in range(longLineLen+1):
                emptyL = longLineLen-i
                start_point = "|"
                if i+1 > len(value):
                    start_point = " "*(i-len(value)+1) +"|"
                print('|'+" "*(emptyL)+value[0:i+1]+start_point, end="\r" , flush=True)
                sleep(speed)
            for i in range(1,len(value)+1):
                end_point = "|"+value[i:len(value)]
                end_line = longLineLen-len(value)+i+1
                print(end_point+" "*end_line+"|", end="\r" , flush=True)
                sleep(speed)
                print(end="\x1b[2K")
            sleep(interval*.06)
    elif style == "mid":
        for x in values:
            x = x if len(x)%2==0 else x+" "
            lan = len(x)//2
            front,back="",""
            for i in range(lan):
                front = x[lan-i-1]+front
                back = back +x[lan+i]
                print(" "*(lan-i-1)+front+back,end="\r",flush=True)
                sleep(speed)
            print(end="\x1b[2K")
            if stay==True:print(x)
            sleep(interval)
    elif style=="right":
        for i in values:
            for j in range(len(i)+1):
                temlen = get_terminal_size()[0]
                print(i[0:j].rjust(temlen),end="\r",flush=True)
                sleep(speed)
            sleep(interval)
            if stay:print(end="\n")
            else:
                for j in range(len(i)+1):
                    temlen = get_terminal_size()[0]
                    print(i[0:len(i)-j].rjust(temlen),end="\r",flush=True)
                    print(end="\x1b[2K")
                    sleep(speed)
                sleep(.4)
    elif style=="left":
        for i in values:
            for j in range(len(i)+1):
                temlen = get_terminal_size()[0]
                print(i[len(i)-j:j],end="\r",flush=True)
                sleep(speed)
            sleep(interval)
            if stay:print(end="\n")
            else:
                for j in range(len(i)+1):
                    temlen = get_terminal_size()[0]
                    print(i[j:len(i)],end="\r", flush=True)
                    print(end="\x1b[2K")
                    sleep(speed)
                sleep(.4)
    elif style=="center":
        for i in values:
            for j in range(len(i)+1):
                if j < len(i):endline="|"
                else:endline=""
                temlen = (get_terminal_size()[0]/2)-(len(i)/2) 
                print(" "*int(temlen)+i[0:j]+endline+" "*(len(i)-j-1),end="\r",flush=True)
                sleep(speed)
            sleep(interval)
            if stay==True:print(end="\n")
            else:print(end="\x1b[2K");sleep(.4)
    elif style=="centerac":
        for i in values:
            for j in range(len(i)+1):
                if j < len(i):endline="|"
                else:endline=""
                temlen = get_terminal_size()[0]
                print((i[0:j]+endline).center(temlen),end="\r",flush=True)
                sleep(speed)
            sleep(interval)
            if stay==True:print(end="\n")
            else:print(end="\x1b[2K");sleep(.4)
    elif style=="centeral":
        longlen = 0
        for strlen in values: 
            if longlen<len(strlen):longlen=len(strlen)
        for i in values:
            for j in range(len(i)+1):
                if j < len(i):endline="|"
                else:endline=""
                temlen = get_terminal_size()[0]
                print(" "*int(temlen/2-(longlen/2))+i[0:j]+endline,end="\r")
                sleep(speed)
            sleep(interval)
            if stay==True:print(end="\n")
            else:print(end="\x1b[2K");sleep(.4)
        return 0
    elif style=="centerar":
        longlen = 0
        for A_len in values:
            if longlen<len(A_len):longlen=len(A_len)
        for i in values:
            for j in range(len(i)+1):
                temlen = get_terminal_size()[0]
                print(" "*int(temlen/2+(longlen/2-len(i))) +  i[0:j],end="\r")
                sleep(speed)
            sleep(interval)
            if stay==True:print(end="\n")
            else:print(end="\x1b[2K");sleep(.4)
    elif style=="gunshort":
        for x in values:
            short=""
            len_x = len(x)
            for i in range(len_x):
                try:
                    next_let = x[i+1] if " " != x[i+1] else "_"
                    index = x[i] if " " != x[i] else "_"
                except:next_let=" "; index = x[len_x-1]
                for j in range(len_x-i):
                    print(short+" "*(len_x-j-2-len(short))+index+(" "*j)+f"  <==[{next_let}]=|",end="\r")
                    sleep(speed)
                sleep(speed)
                short = short + x[i]
            print(end="\x1b[2K", flush=True)
            if stay:print(short);sleep(interval)
            else:print(short,end="\r");sleep(interval);print(end="\x1b[2K", flush=True)
    elif style=="snip":
        for x in values:
            short,addone="",0
            for i in range(len(x)):
                try:next_let = x[i+1] if " " != x[i+1] else "_";index = x[i] if " " != x[i] else "_"
                except:next_let=" ";index = x[len(x)-1]
                temlen = get_terminal_size()[0]
                for j in range(0,temlen-i-len(short)+addone-10):
                    print(short+" "*(temlen-j-len(short)-11)+index+" "*(j)+f" <===[{next_let}]=|",end="\r")
                    sleep(speed)
                sleep(speed)
                print(end="\x1b[2K")
                addone+=1
                short=short+x[i]
            if stay==True:print(x)
            else:print(x,end="\r");print(end="\x1b[2K")
            sleep(interval)
    elif style=="f2b":
        for x in values:
            x = str(x)
            for y in range(0, len(x)+1):
                print(x[:y], end="\r", flush = True)
                sleep(speed)
            sleep(interval)
            for y in range(0, len(x)+1):
                print(" "*y, end="\r", flush = True)
                sleep(speed)
            print(end="\x1b[2K")
            print(end="\r")
    elif style=="b2f":
        for x in values:
            for y in range(0, len(x)+1):
                print(x[:y], end="\r",flush=True)
                sleep(speed)
            sleep(interval)
            for i in range(0, len(x)+1):
                print(x[:len(x)-i], end="\r", flush=True)
                sleep(speed)
                print(end="\x1b[2K")
            print(end="\r")
    elif style=="matrix":
        from random import choice
        for value in values:
            entry=""
            for i in range(len(value)): 
                entry=entry+value[i] 
                for _ in range(5):
                    nxt=""
                    for _ in range(len(value)-i-1):
                        nxt=nxt+choice(ranchoice) 
                    print(entry+nxt, end="\r")
                    sleep(speed)
            sleep(interval)
            if stay:print(end="\x1b[2K");print(value)
            else:print(value,end="\r");print(end="\x1b[2K")
    elif style == "matrix2":
        from random import randint,choice
        for ab in values:
            entry=""
            for i in range(len(ab)-1):
                entry = entry+ ab[i]
                for _ in range(randint(5,20)):
                    print(entry+choice(ranchoice), end="\n")
                    sleep(speed)
            print(end="\x1b[2K");print(ab);sleep(interval)
    elif style == "help":
        print("""\n
        >>>>>>>>  DVS_PRINTF Function  <<<<<<<<\n\n
keywords --> printf(values, style='typing', speed=3, interval=2, stay=True)\n\n
values --> main stream input values  
           value can be any-data-Type 
        Ex. printf(str, list, [tuple, set], dict, int,...)\n\n
style -->  style is different type if printing animation 
        styles, from this list each style type works 
        differently according to description below\n
        ["typing", "headline","newsline", "mid","left","right",
        "center", "centerAC","centerAL","centerAR", "f2b", "b2f",
        "gunshort", "snip", "matrix", "matrix2", "help"]\n
        typing   => print like typing
        headline => print headlines animation
        newsline => print running newslines animation
        mid      => print line from mid
        left     => value coming from left side of the terminal
        right    => value coming from right side of the terminal
        center   => values appear at center of the terminal 
        centerAC => values arrang at center of the terminal 
        centerAL => arrang list-item at center-Left on terminal
        centerAR => arrang list-item at center-Right on terminal
        gunshort => firing the words from short gun
        snip     => sniping the words from end of the terminal
        matrix   => print random words to real line 
        matrix2  => print 1st word and 2nd random word
        f2b      => typing and remove word from (back to front)
        b2f      => typing and remove word from (front to back)\n\n
speed -->  speed of printf's animation 
           defult speed is 3, from (1 to 6)\n
           1 = Very Slow  
           2 = Slow  
           3 = Mediam
           4 = Fast
           5 = Fast+
           6 = Very Fast\n\n
interval --> interval is waiting time between printing 
             of each values, (interval in second) 
             defult interval is 2, you can set from 0 to grater\n\n    
stay --> after style animation whether you want the stream OR Not
         `defult stay is True`, can be `True or False`\n
         but some styles take `No action on stay`
         whether it is True OR False 
         Ex. ( typing, headline, newsline, f2b,  b2f, matrix2 )\n""")
        for i in values:print(i)
    else:
        print(f"\n\n  >>>>  no paramiter '{style}' for style  <<<<   \n")
        print("  >>>>  please enter name of style=''  from the list <<<<   \n")
        print('''[typing, headline, newsline, mid, gunshort, snip,\n left, right, center, centerAC, centerAL, centerAR,\n matrix, matrix2, f2b, b2f, help]\n\n''')
        for i in values:
            print(i)

    print('\033[?25h', end="")
    del values


# printf("hello world","my name is dhruvan","and i am coder",
#     style="headline", 
#     speed = 5,
#     interval = .5,
#     stay = False,
#     )