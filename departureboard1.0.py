import requests
import tkinter as tk

def sys_get():
    requesttime = requests.get('http://ctabustracker.com/bustime/api/v2/gettime?key=2P4GNvx7RbVfUQd6Tq8hSGZgf&format=json')
    tum = ''
    tum = requesttime.text
    tum1 = tum.split("{")
    if tum1[2].__contains__('error'):
        SYSHourMinute = (0, 0)
        return SYSHourMinute
    else:
        tum2 = tum1[2].split(' ')
        tum3 = tum2[2].split(':')
        SystemHour = int(tum3[0])
        SystemMinute = int(tum3[1])
        SYSHourMinute = (SystemHour, SystemMinute)
        return SYSHourMinute

def pb_get():
    requestpb = requests.get('http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=87ac2b92ef2a4787a0bffd4a9532ceee&max=1&stpid=30254&outputType=JSON')
    num = ''
    num = requestpb.text
    num1 = num.split("{")
    if num1.__contains__('prdt'):
        num2 = num1[3].split(',')
        num3 = num2[10].split('T')
        num4 = num3[2].split(':')
        PBHourMinute = (int(num4[0]), int(num4[1]))
        return PBHourMinute
    else:
        PBHourMinute = (0, 0)
        return PBHourMinute

def pb_get1():
    requestpb = requests.get('http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=87ac2b92ef2a4787a0bffd4a9532ceee&max=2&stpid=30254&outputType=JSON')
    num = ''
    num = requestpb.text
    num1 = num.split("{")
    if num1.__contains__('prdt'):
        num2 = num1[4].split(',')
        num3 = num2[10].split('T')
        num4 = num3[2].split(':')
        PB1HourMinute = (int(num4[0]), int(num4[1]))
        return PB1HourMinute
    else:
        PB1HourMinute = (0, 0)
        return PB1HourMinute

def bh_get():
    requestbh = requests.get('http://www.ctabustracker.com/bustime/api/v2/getpredictions?key=2P4GNvx7RbVfUQd6Tq8hSGZgf&rt=77&stpid=9277&top=1&format=json')
    num = ''
    num = requestbh.text
    num1 = num.split(',')
    if num1.__contains__('prdtm'):
        num2 = num1[10].split(' ')
        num3 = num2[2].split(':')
        min = int(num3[1][0:2])
        BHHourMinute = (int(num3[0]), min)
        return BHHourMinute
    else:
        BHHourMinute = (0, 0)
        return BHHourMinute

def bh_get1():
    requestdr = requests.get('http://www.ctabustracker.com/bustime/api/v2/getpredictions?key=2P4GNvx7RbVfUQd6Tq8hSGZgf&rt=77&stpid=9277&top=2&format=json')
    num = ''
    num = requestdr.text
    num1 = num.split(',')
    if num1.__contains__('prdtm'):
        num2 = num1[26].split(' ')
        num3 = num2[2].split(':')
        min = int(num3[1][0:2])
        BH1HourMinute = (int(num3[0]), min)
        return BH1HourMinute
    else:
        BH1HourMinute = (0, 0)
        return BH1HourMinute

def dr_get():
    requestdr = requests.get('http://www.ctabustracker.com/bustime/api/v2/getpredictions?key=2P4GNvx7RbVfUQd6Tq8hSGZgf&rt=50&stpid=8833&top=1&format=json')
    num = ''
    num = requestdr.text
    num1 = num.split(',')
    if num1.__contains__('prdtm'):
        num2 = num1[10].split(' ')
        num3 = num2[2].split(':')
        min = int(num3[1][0:2])
        DRHourMinute = (int(num3[0]), min)
        return DRHourMinute
    else:
        DRHourMinute = (0, 0)
        return DRHourMinute

def dr_get1():
    requestdr = requests.get('http://www.ctabustracker.com/bustime/api/v2/getpredictions?key=2P4GNvx7RbVfUQd6Tq8hSGZgf&rt=50&stpid=8833&top=2&format=json')
    num = ''
    num = requestdr.text
    num1 = num.split(',')
    if num1.__contains__('prdtm'):
        num2 = num1[26].split(' ')
        num3 = num2[2].split(':')
        min = int(num3[1][0:2])
        DR1HourMinute = (int(num3[0]), min)
        return DR1HourMinute
    else:
        DR1HourMinute = (0, 0)
        return DR1HourMinute

def countdown(Harrival, Marrival, Hactual, Mactual):
    if Harrival == Hactual:
        Down = Marrival - Mactual
    else:
        Down = (60 - Mactual) + Marrival
    return Down

def main(paulina, paulina1, belmont, belmont1, damen, damen1):
    def count():
        global pb
        global pb1
        global bh
        global bh1
        global dr
        global dr1
        global sys
        pb = pb_get()
        pb1 = pb_get1()
        bh = bh_get()
        bh1 = bh_get1()
        dr = dr_get()
        dr1 = dr_get1()
        sys = sys_get()
        paulina.config(text=str(countdown(pb[0], pb[1], sys[0], sys[1])))
        paulina.after(10000, count)
        paulina1.config(text=str(countdown(pb1[0], pb1[1], sys[0], sys[1])))
        paulina1.after(10000, count)
        if countdown(bh[0], bh[1], sys[0], sys[1]) > 0 and countdown(bh1[0], bh1[1], sys[0], sys[1]) > 0:
            belmont.config(text=str(countdown(bh[0], bh[1], sys[0], sys[1])))
            belmont.after(10000, count)
            belmont1.config(text=str(countdown(bh1[0], bh1[1], sys[0], sys[1])))
            belmont1.after(10000, count)
        elif countdown(bh[0], bh[1], sys[0], sys[1]) > 0 and countdown(bh1[0], bh1[1], sys[0], sys[1]) <= 0:
            belmont.config(text=str(countdown(bh[0], bh[1], sys[0], sys[1])))
            belmont.after(10000, count)
            belmont1.config(text= '0')
            belmont1.after(10000, count)
        else:
            belmont.config(text= '0')
            belmont.after(10000, count)
            belmont1.config(text= '0')
            belmont1.after(10000, count)
        if countdown(dr[0], dr[1], sys[0], sys[1]) > 0:
            damen.config(text=str(countdown(dr[0], dr[1], sys[0], sys[1])))
            damen.after(10000, count)
            damen1.config(text=str(countdown(dr1[0], dr1[1], sys[0], sys[1])))
            damen1.after(10000, count)
        elif countdown(dr[0], dr[1], sys[0], sys[1]) > 0 and countdown(dr1[0], dr1[1], sys[0], sys[1]) <= 0:
            damen.config(text=str(countdown(dr[0], dr[1], sys[0], sys[1])))
            damen.after(10000, count)
            damen1.config(text= '0')
            damen1.after(10000, count)
        else:
            damen.config(text= '0')
            damen.after(10000, count)
            damen1.config(text= '0')
            damen1.after(10000, count)
    count()

root = tk.Tk()
root.title('Departure Countdown')
label = tk.Label(root, fg = 'brown')
label.pack()
label.config(text='Paulina (Loop):')
paulina = tk.Label(root, fg = 'brown')
paulina.pack()
paulina1 = tk.Label(root, fg='brown')
paulina1.pack()
label1 = tk.Label(root, fg = 'red')
label1.pack()
label1.config(text='Belmont (East):')
belmont = tk.Label(root, fg = 'red')
belmont.pack()
belmont1 = tk.Label(root, fg='red')
belmont1.pack()
label2 = tk.Label(root, fg = 'blue')
label2.pack()
label2.config(text='Damen (South):')
damen = tk.Label(root, fg = 'blue')
damen.pack()
damen1 = tk.Label(root, fg='blue')
damen1.pack()
main(paulina, paulina1, belmont, belmont1, damen, damen1)
button = tk.Button(root, text='stop', width=30, command=root.destroy)
button.pack()
root.mainloop()