from tkinter import*
import random
import time;
import datetime
from tkinter import Tk, StringVar, ttk
#pip install tk



root=Tk()
root.geometry("1350x1100+0+0")
root.title("BILABILA")


Tops = Frame(root,width = 1350, height = 100, bd=12, relief = "raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('Times New Roman',50 , 'bold'), text= "\tBILABILA \t\t")                
lblTitle.grid(row=0, column=0)


BottomMainFrame =Frame(root, width = 1350, height=100, bd=12,relief = "raise")
BottomMainFrame.pack(side=BOTTOM)


f1 = Frame (BottomMainFrame, width = 600, height=1100, bd=12,relief = "raise")
f1.pack(side=LEFT)


f2 = Frame (BottomMainFrame, width = 450, height=1100, bd=12,relief = "raise")
f2.pack(side=LEFT)
f2TOP = Frame (f2, width = 450, height=350, bd=12,relief = "raise")
f2TOP.pack(side=TOP)


f2BOTTOM = Frame(f2, width = 450, height=750, bd=12,relief = "raise")
f2BOTTOM.pack(side=BOTTOM)


f3 = Frame (BottomMainFrame, width = 450, height=1100, bd=12,relief = "raise")
f3.pack(side=RIGHT)


var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()
var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()
var17= IntVar()
var18= IntVar()
var19= IntVar()
var20= IntVar()


var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)


varAgamemnon =StringVar()
varAgamemnon.set("0")
varAtlas =StringVar()
varAtlas.set("0")
varBiblis =StringVar()
varBiblis.set("0")
varBolina =StringVar()
varBolina.set("0")
varCrysalis =StringVar()
varCrysalis.set("0")
varDemoleus =StringVar()
varDemoleus.set("0")
varDozon =StringVar()
varDozon.set("0")
varGlava =StringVar()
varGlava.set("0")
varKotzebeua =StringVar()
varKotzebeua.set("0")
varLeuconoe =StringVar()
varLeuconoe.set("0")
varLin =StringVar()
varLin.set("0")
varLowi =StringVar()
varLowi.set("0")
varPalinuros =StringVar()
varPalinuros.set("0")
varPalipatos =StringVar()
varPalipatos.set("0")
varPolytes =StringVar()
varPolytes.set("0")
varRadamentos =StringVar()
varRadamentos.set("0")
varRomansovia =StringVar()
varRomansovia.set("0")
varSamia =StringVar()
varSamia.set("0")
varSempa =StringVar()
varSempa.set("0")
varSylvia =StringVar()
varSylvia.set("0")




def costofbutterfly():


    butterfly1= float(varAgamemnon.get())
    butterfly2= float(varAtlas.get())
    butterfly3= float(varBiblis.get())
    butterfly4= float(varBolina.get())
    butterfly5= float(varCrysalis.get())
    butterfly6= float(varDemoleus.get())
    butterfly7= float(varDozon.get())
    butterfly8= float(varGlava.get())
    butterfly9= float(varKotzebeua.get())
    butterfly10= float(varLeuconoe.get())
    butterfly11= float(varLin.get())
    butterfly12= float(varLowi.get())
    butterfly13= float(varPalinuros.get())
    butterfly14= float(varPalipatos.get())
    butterfly15= float(varPolytes.get())
    butterfly16= float(varRadamentos.get())
    butterfly17= float(varRomansovia.get())
    butterfly18= float(varSamia.get())
    butterfly19= float(varSempa.get())
    butterfly20= float(varSylvia.get())
##****************************************
lblTypes =Label(f1, font=('arial',12, 'bold'),text= "BILA-BILA")
lblTypes.grid(row = 0, column=0)
##****************************************
Agamemnon = Checkbutton(f1, text ="Agamemnon\t\t1.00", variable =var1, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=1,column=0, sticky=W)                
txtAgamemnon= Entry(f1,font=('arial', 12, 'bold'),textvariable = varAgamemnon, width =6, state=DISABLED, justify= RIGHT)
txtAgamemnon.grid(row=1,column=1)


Atlas = Checkbutton(f1, text ="Atlas\t\t\t1.00", variable =var2, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=2,column=0, sticky=W)                
txtAtlas= Entry(f1,font=('arial', 12, 'bold'),textvariable = varAtlas, width =6, state=DISABLED, justify= RIGHT)
txtAtlas.grid(row=2,column=1)


Biblis = Checkbutton(f1, text ="Biblis\t\t\t1.00", variable =var3, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=3,column=0, sticky=W)                
txtBiblis= Entry(f1,font=('arial', 12, 'bold'),textvariable = varBiblis, width =6, state=DISABLED, justify= RIGHT)
txtBiblis.grid(row=3,column=1)


Bolina = Checkbutton(f1, text ="Bolina\t\t\t1.00", variable =var4, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=4,column=0, sticky=W)                
txtBolina= Entry(f1,font=('arial', 12, 'bold'),textvariable = varBolina, width =6, state=DISABLED, justify= RIGHT)
txtBolina.grid(row=4,column=1)


Crysalis = Checkbutton(f1, text ="Crysalis\t\t\t1.00", variable =var5, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=5,column=0, sticky=W)                
txtCrysalis= Entry(f1,font=('arial', 12, 'bold'),textvariable = varCrysalis, width =6, state=DISABLED, justify= RIGHT)
txtCrysalis.grid(row=5,column=1)
                     
Demoleus = Checkbutton(f1, text ="Demoleus\t\t1.00", variable =var6, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=6,column=0, sticky=W)                
txtDemoleus= Entry(f1,font=('arial', 12, 'bold'),textvariable = varDemoleus, width =6, state=DISABLED, justify= RIGHT)
txtDemoleus.grid(row=6,column=1)


Dozon = Checkbutton(f1, text ="Dozon\t\t\t1.00", variable =var7, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=7,column=0, sticky=W)                
txtDozon= Entry(f1,font=('arial', 12, 'bold'),textvariable = varCrysalis, width =6, state=DISABLED, justify= RIGHT)
txtDozon.grid(row=7,column=1)


Glava = Checkbutton(f1, text ="Glava\t\t\t1.00", variable =var8, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=8,column=0, sticky=W)                
txtGlava= Entry(f1,font=('arial', 12, 'bold'),textvariable = varGlava, width =6, state=DISABLED, justify= RIGHT)
txtGlava.grid(row=8,column=1)


Kotzebeua = Checkbutton(f1, text ="Kotzebeua\t\t1.00", variable =var9, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=9,column=0, sticky=W)                
txtKotzebeua= Entry(f1,font=('arial', 12, 'bold'),textvariable = varKotzebeua, width =6, state=DISABLED, justify= RIGHT)
txtKotzebeua.grid(row=9,column=1)


Leuconoe = Checkbutton(f1, text ="Leuconoe\t\t1.00", variable =var10, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=10,column=0, sticky=W)                
txtLeuconoe= Entry(f1,font=('arial', 12, 'bold'),textvariable = varLeuconoe, width =6, state=DISABLED, justify= RIGHT)
txtLeuconoe.grid(row=10,column=1)


Lin = Checkbutton(f1, text ="Lin\t\t\t1.00", variable =var11, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=11,column=0, sticky=W)                
txtLin= Entry(f1,font=('arial', 12, 'bold'),textvariable = varLin, width =6, state=DISABLED, justify= RIGHT)
txtLin.grid(row=11,column=1)


Lowi = Checkbutton(f1, text ="Lowi\t\t\t1.00", variable =var12, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=12,column=0, sticky=W)                
txtLowi= Entry(f1,font=('arial', 12, 'bold'),textvariable = varLowi, width =6, state=DISABLED, justify= RIGHT)
txtLowi.grid(row=12,column=1)
                     
Palinuros = Checkbutton(f1, text ="Palinuros\t\t1.00", variable =var13, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=13,column=0, sticky=W)                
txtPalinuros= Entry(f1,font=('arial', 12, 'bold'),textvariable = varPalinuros, width =6, state=DISABLED, justify= RIGHT)
txtPalinuros.grid(row=13,column=1)


Palipatos = Checkbutton(f1, text ="Palipatos\t\t\t1.00", variable =var14, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=14,column=0, sticky=W)                
txtPalipatos= Entry(f1,font=('arial', 12, 'bold'),textvariable = varPalipatos, width =6, state=DISABLED, justify= RIGHT)
txtPalipatos.grid(row=14,column=1)
 
Polytes = Checkbutton(f1, text ="Polytes\t\t\t1.00", variable =var15, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=15,column=0, sticky=W)                
txtPolytes= Entry(f1,font=('arial', 12, 'bold'),textvariable = varPolytes, width =6, state=DISABLED, justify= RIGHT)
txtPolytes.grid(row=15,column=1)


Radamentos = Checkbutton(f1, text ="Radamentos\t\t1.00", variable =var16, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=16,column=0, sticky=W)                
txtRadamentos= Entry(f1,font=('arial', 12, 'bold'),textvariable = varRadamentos, width =6, state=DISABLED, justify= RIGHT)
txtRadamentos.grid(row=16,column=1)


Romansovia = Checkbutton(f1, text ="Romansovia\t\t1.00", variable =var17, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=17,column=0, sticky=W)                
txtRomansovia= Entry(f1,font=('arial', 12, 'bold'),textvariable = varRomansovia, width =6, state=DISABLED, justify= RIGHT)
txtRomansovia.grid(row=17,column=1)


Samia = Checkbutton(f1, text ="Samia\t\t\t1.00", variable =var18, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=18,column=0, sticky=W)                
txtSamia= Entry(f1,font=('arial', 12, 'bold'),textvariable = varSamia, width =6, state=DISABLED, justify= RIGHT)
txtSamia.grid(row=18,column=1)
                     
Sempa = Checkbutton(f1, text ="Sempa\t\t\t1.00", variable =var19, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=19,column=0, sticky=W)                
txtSempa= Entry(f1,font=('arial', 12, 'bold'),textvariable = varSempa, width =6, state=DISABLED, justify= RIGHT)
txtSempa.grid(row=19,column=1)


Sylvia = Checkbutton(f1, text ="Sylvia\t\t\t1.00", variable =var20, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=20,column=0, sticky=W)                
txtSylvia= Entry(f1,font=('arial', 12, 'bold'),textvariable = varSylvia, width =6, state=DISABLED, justify= RIGHT)
txtSylvia.grid(row=20,column=1)
                     
##****************************************
lblTypes =Label(f2, font=('arial',12, 'bold'),text= "Payment Method")
lblTypes.grid(row = 0, column=0)
##****************************************
Agamemnon = Checkbutton(f1, text ="Agamemnon\t\t1.00", variable =var1, onvalue =1, offvalue =0, font=('arial',12 , 'bold')). grid(row=1,column=0, sticky=W)                
txtAgamemnon= Entry(f2,font=('arial', 12, 'bold'),textvariable = varAgamemnon, width =6, state=DISABLED, justify= RIGHT)
txtAgamemnon.grid(row=1,column=2)


root.mainloop()

