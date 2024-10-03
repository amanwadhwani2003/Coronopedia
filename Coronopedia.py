from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import turtle
import webbrowser


root=Tk()
root.configure(bg='black')
root.title('Coronopedia')
root.geometry('10000x10000')

def intro():
    intro=Toplevel()
    intro.configure(bg='lightcyan')
    intro.title('What is a Coronavirus ?')


    def origin():
        Origin=Toplevel()
        Origin.title("Origin")
        Origin.configure(bg='aqua')

        
        def evolution():
            Origin=Toplevel()
            Origin.title("Origin")
            Origin.configure(bg='yellow')
            Origin.geometry('20000x20000')
            
            Prologue=Label(Origin,text="Natural Evolution",font=('Times New Roman',40,'bold italic underline'),bg="purple",fg="Seagreen1")
            text1=Label(Origin,text="The scientists found that the RBD portion of the SARS-CoV-2 spike proteins",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            text2=Label(Origin,text="had evolved to effectively target a molecular feature on effectively target",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            text3=Label(Origin,text="a molecular feature on the outside of human cells, called ACE2, a receptor",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            text4=Label(Origin,text="involved in regulating blood pressure. The SARS-CoV-2 spike protein was so",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            text5=Label(Origin,text="effective at binding the human cells, in fact, that the scientists concluded",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            text6=Label(Origin,text="it was the result of natural selection and not the product of genetic engineering.This evidence for natural evolution was",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            image1=ImageTk.PhotoImage(Image.open('1-s2.0-S2090123220300540-ga1.jpg'))
            image1_label=Label(Origin, image=image1,bg='magenta')

            #step 2
            text7=Label(Origin,text="supported by data on SARS-CoV-2's backbone -- its overall molecular struvture. If",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            text8=Label(Origin,text="someone is seeking to engineer a new coronavirus as a pathogen, they constructed it",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            text10=Label(Origin,text="from the backbone of a virus known to cause illness. But scientist found that the",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            text11=Label(Origin,text="SARS-CoV-2 backbone was found to be differed substantially from those of already",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            image2= ImageTk.PhotoImage(Image.open('images (13).jpg'))
            image2_label = Label(Origin, image=image2,height=300)
            #ADDITIONAL

            #step3
            text13=Label(Origin,text="known coronaviruses and mostly resembled related viruses found in bats and",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            text14=Label(Origin,text="pangolins. These two features of the virus, the mutations in the RBD portion",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")
            text15=Label(Origin,text="of the spike protein and its distinct backbone, rules out laboratory.",font=('Monotype Corsiva',24),bg='yellow',fg="dodgerblue3")

            #step 1
            Prologue.grid(row=0,column=0,columnspan=4,sticky=E)
            text1.grid(row=1,column=0,columnspan=4,sticky=E)
            text2.grid(row=2,column=0,columnspan=4,sticky=W)
            text3.grid(row=3,column=0,columnspan=4,sticky=W)
            text4.grid(row=4,column=0,columnspan=4,sticky=W)
            text5.grid(row=5,column=0,columnspan=4,sticky=W)
            text6.grid(row=6,column=0,columnspan=15,sticky=W)
            image1_label.grid(row=1,column=4,rowspan=5,sticky=E,pady=25)

            #step 2
            text7.grid(row=7,column=0,columnspan=15,sticky=W,padx=375)
            text8.grid(row=8,column=0,columnspan=15,sticky=W,padx=375)
            text10.grid(row=9,column=0,columnspan=15,sticky=W,padx=375)
            text11.grid(row=10,column=0,columnspan=15,sticky=W,padx=375)
            image2_label.grid(row=7,column=0,rowspan=10,sticky=W,padx=25)

            #step 3
            text13.grid(row=11,column=0,columnspan=15,sticky=W,padx=375)
            text14.grid(row=12,column=0,columnspan=15,sticky=W,padx=375)
            text15.grid(row=13,column=0,columnspan=15,sticky=W,padx=375)

            def back():
                Origin.destroy()
            end = Button(Origin, text='< Back', font=('',10),command=back).place(x=15,y=15)

            Origin.mainloop()
            

        def conclusion():
            Origin=Toplevel()
            Origin.title("Origin")
            Origin.configure(bg='red')
            Origin.geometry('20000x20000')
            
            Prologue=Label(Origin,text="Conclusion",font=('Times New Roman',40,'bold italic underline'),bg="blue",fg="white")
            text1=Label(Origin,text="The novel coronavirus originated from the Hunan seafood market at Wuhan, China,",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            text2=Label(Origin,text="where bats,snakes, raccoon dogs, palm civets, and other animals are sold, and rapidly",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            text3=Label(Origin,text="spread up to 109 countries. The zoonotic source of SARS-CoV-2 is not confirmed,",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            text4=Label(Origin,text="sequence-based analysis suggested bats as the key reservoir. DNA recombination",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            text5=Label(Origin,text="was found to be involved at spike glycoprotein which assorted SARS-CoV(CoVZXC21",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            image1=ImageTk.PhotoImage(Image.open('download.jpg'))
            image1_label=Label(Origin, image=image1,bg='magenta')

            #step 2
            text7=Label(Origin,text="or CoVZC45) with the RBD of another Beta CoV, thus could be the cross-species",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            text8=Label(Origin,text="transmission and rapid infection. According to phylogenetic trees, SARS-CoV is ",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            text9=Label(Origin,text="closer to SARS-like bat CoVs. Until now, no promising clinical treatments or ",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            text10=Label(Origin,text="prevention strategies have been developed against human coronaviruses. However,",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            text11=Label(Origin,text="the researchers are working to develop efficient therapeutic strategies to cope",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            
            image2= ImageTk.PhotoImage(Image.open('covid-300x200.jpg'))
            image2_label = Label(Origin, image=image2)
            #ADDITIONAL

            #step3
            text13=Label(Origin,text="with the novel coronaviruses.The risk of similar coronavirus outbreaks in the future remains",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            text14=Label(Origin,text="high.In addition to controlling the COVID-19 pandemic we must undertake vigorous scientific",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            text15=Label(Origin,text="and societal actions, including significantly increased funding for research institutes",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            text16=Label(Origin,text="addressing disease emergence to prevent this tragic history from repeating itself.",font=('Monotype Corsiva',24),bg='red',fg="yellow")
            image3=ImageTk.PhotoImage(Image.open('images.jpg'))
            image3_label=Label(Origin, image=image3,bg='magenta')

            #step 1
            Prologue.grid(row=0,column=0,columnspan=3)
            text1.grid(row=1,column=0,columnspan=2,sticky=W)
            text2.grid(row=2,column=0,columnspan=2,sticky=W)
            text3.grid(row=3,column=0,columnspan=2,sticky=W)
            text4.grid(row=4,column=0,columnspan=2,sticky=W)
            text5.grid(row=5,column=0,columnspan=2,sticky=W)
            image1_label.grid(row=1,column=2,rowspan=5,sticky=W)

            #step 2
            text7.grid(row=7,column=1,columnspan=2,sticky=W)
            text8.grid(row=8,column=1,columnspan=2,sticky=W)
            text9.grid(row=9,column=1,columnspan=2,sticky=W)
            text10.grid(row=10,column=1,columnspan=2,sticky=W)
            text11.grid(row=11,column=1,columnspan=2,sticky=W)
            image2_label.grid(row=7,column=0,rowspan=5,sticky=W,padx=25,pady=20)

            #step 3
            text13.grid(row=13,column=0,columnspan=2,sticky=W)
            text14.grid(row=14,column=0,columnspan=2,sticky=W)
            text15.grid(row=15,column=0,columnspan=2,sticky=W)
            text16.grid(row=16,column=0,columnspan=2,sticky=W)
            image3_label.grid(row=13,column=2,rowspan=4,sticky=W,padx=20)

            def back():
                Origin.destroy()
            end = Button(Origin, text='< Back', font=('',10),command=back).place(x=15,y=15)


            Origin.mainloop()


        #step 1
        Prologue=Label(Origin,text="Prologue",font=('Times New Roman',40),bg="Black",fg="Orange",bd=7)
        text1=Label(Origin,text="The  COVID-19  Pandemic  Is  Among  The  Deadliest  Infectious  diseases  to  have  emerged  in",font=('Monotype Corsiva',22),bg='aqua')
        text2=Label(Origin,text="recent  history.  As  with  all  past  pandemics,  the  specific  mechanism  of  its  emergence  in  our",font=('Monotype Corsiva',22),bg='aqua')
        text3=Label(Origin,text="humans  remains  unknown.  Nevertheless,  a  large  body  of  virologic,  epidemiologic,  veterinary,",font=('Monotype Corsiva',22),bg='aqua')
        text4=Label(Origin,text="and  ecologic  data,  establishes  that  the  new  virus,  SARS-CoV-2  evolved  directly  or  maybe",font=('Monotype Corsiva',22),bg='aqua')
        text5=Label(Origin,text="indirectly  from  a  β-coronavirus  in  the  sarbecovirus  (SARS-like virus)  group",font=('Monotype Corsiva',22),bg='aqua')
        image1=ImageTk.PhotoImage(Image.open('prologue1.jpg'))
        image1_label=Label(Origin, image=image1,bg='magenta')

        #step 2
        text7=Label(Origin,text="that  naturally  infect  bat  sand  pangolins  in  Asia  and  Southeast  Asia.  Scientists",font=('Monotype Corsiva',22),bg='aqua')
        text8=Label(Origin,text="have  warned  for  decades  that  such  sarbecoviruses  are  poised  to  emerge  again  and",font=('Monotype Corsiva',22),bg='aqua')
        text9=Label(Origin,text="again,  identified  risk  factors,  and  argued  for  enhanced  pandemic  prevention  and",font=('Monotype Corsiva',22),bg='aqua')
        text10=Label(Origin,text="control  efforts.  Unfortunately,  few  such  preventive  actions  were  taken  resulting",font=('Monotype Corsiva',22),bg='aqua')
        text11=Label(Origin,text="in  the  latest  Covid-19  i.e.  Coronavirus  Disease  2019,  which  is  said  to  be  a  huge",font=('Monotype Corsiva',22),bg='aqua')
        text12=Label(Origin,text="pandemic  due  to  its  huge  replicating  action  on  human  beings.",font=('Monotype Corsiva',22),bg='aqua')
        image2= ImageTk.PhotoImage(Image.open('prologue2.jpg'))
        image2_label = Label(Origin, image=image2, height=225, width=375)
        #ADDITIONAL

        #step 3
        text13=Label(Origin,text="coronavirus  emergence  detected  in  late  2019  which  quickly ",font=('Monotype Corsiva',22),bg='aqua')
        text14=Label(Origin,text="spread  globally.  On  31  December  2019,  a  cluster  of  cases  of ",font=('Monotype Corsiva',22),bg='aqua')
        text15=Label(Origin,text="pneumonia  of  unknown  cause,  in  the  city  of  Wuhan,  Hubei  province",font=('Monotype Corsiva',22),bg='aqua')
        text16=Label(Origin,text="in  China,  was  reported  to  the  World  Health  Organisation(WHO).",font=('Monotype Corsiva',22),bg='aqua')
        button1=Button(Origin,text="Natural Evolution", padx=20,pady=10,fg="orange",bg="Navy",font=("Trajan",20,'bold'), command=evolution)
        button2=Button(Origin,text="Conclusion",padx=55,pady=10,fg="orange",bg="Navy",font=("Trajan",20,'bold'), command=conclusion)


        #step 1
        Prologue.grid(row=0,column=0,columnspan=121,sticky=E+W+N+S)
        text1.grid(row=1,column=0,columnspan=4,sticky=E)
        text2.grid(row=2,column=0,columnspan=4,sticky=W)
        text3.grid(row=3,column=0,columnspan=4,sticky=W)
        text4.grid(row=4,column=0,columnspan=4,sticky=W)
        text5.grid(row=5,column=0,columnspan=4,sticky=W)
        image1_label.grid(row=1,column=4,rowspan=5, padx=30)

        #step 2
        text7.grid(row=7,column=2,columnspan=4,sticky=W)
        text8.grid(row=8,column=2,columnspan=4,sticky=W)
        text9.grid(row=9,column=2,columnspan=4,sticky=W)
        text10.grid(row=10,column=2,columnspan=4,sticky=W)
        text11.grid(row=11,column=2,columnspan=4,sticky=W)
        text12.grid(row=12,column=2,columnspan=4,sticky=W)
        image2_label.grid(row=7,column=0,rowspan=6)

        #step 3
        text13.grid(row=13,column=0,columnspan=4,sticky=W)
        text14.grid(row=14,column=0,columnspan=4,sticky=W)
        text15.grid(row=15,column=0,columnspan=4,sticky=W)
        text16.grid(row=16,column=0,columnspan=4,sticky=W)
        button1.grid(row=13,column=4,rowspan=2)
        button2.grid(row=15,column=4,rowspan=2)

        def back():
            Origin.destroy()
        end = Button(Origin, text='< Back', font=('',10),command=back).place(x=15,y=15)

        Origin.mainloop()


    def symptoms():
        symptoms=Toplevel()
        symptoms.configure(bg='orangered')
        symptoms.title('Symptoms')
        symptoms.geometry('1500x1500')
        

        def s1():
            s1=Toplevel()
            s1.configure(bg='black')
            s1.geometry('1500x1500')
            image1=ImageTk.PhotoImage(Image.open('corona10.png'))
            image1_label=Label(s1, image=image1,bg='black')
            image1_label.grid(padx=250,pady=125)
            def back():
                s1.destroy()
            end = Button(s1, text='< Back', font=('',10),command=back).place(x=15,y=15)
            s1.mainloop()

            
        def s2():
            s2=Toplevel()
            s2.configure(bg='black')
            s2.geometry('1500x1500')
            image1=ImageTk.PhotoImage(Image.open('corona13.png'))
            image1_label=Label(s2, image=image1,bg='black')
            image1_label.grid(padx=250,pady=125)
            def back():
                s2.destroy()
            end = Button(s2, text='< Back', font=('',10),command=back).place(x=15,y=15)
            s2.mainloop()
            
        
        mainline=Label(symptoms, text='What are Symptoms?',font=('times new roman bold italic',35,'underline'),fg='yellow',bg='orangered')   
        line1=Label(symptoms,text='Symptoms are the feelings of physical or mental change',font=('helvetica',18,'bold'),fg='yellow',bg='orangered')
        line2=Label(symptoms,text='which are regarded as an indication of some diseases.',font=('helvetica',18,'bold'),fg='yellow',bg='orangered')
        line8=Label(symptoms,text='Symptomatology (also called semiology) is a branch of',font=('helvetica',18,'bold'),fg='yellow',bg='orangered')
        line9=Label(symptoms,text='medicine dealing with symptoms.',font=('helvetica',18,'bold'),fg='yellow',bg='orangered')
        #line10=Label(symptoms,text='with the signs and indications of a disease.',font=('helvetica',18,'bold'),fg='yellow',bg='red')
        image1=ImageTk.PhotoImage(Image.open('corona12.jpg'))
        image1_label=Label(symptoms,image=image1,bg='pink')
        image2=ImageTk.PhotoImage(Image.open('corona9.jpg'))
        image2_label=Label(symptoms,image=image2,bg='pink',height=350)
        line3=Label(symptoms, text='Symptoms of Corona Virus',bg='orangered',fg='cyan',font=('times new roman bold italic',35,'underline'))
        line5=Label(symptoms,text='Symptoms of corona virs are changing since its origin.',font=('helvetica',18,'bold'),fg='cyan',bg='orangered')
        line6=Label(symptoms,text='Noadays patients are found corona positive when tested',font=('helvetica',18,'bold'),fg='cyan',bg='orangered')
        line7=Label(symptoms, text='even when they didn\'t show single symptom of corona.', font=('helvetica',18,'bold'),fg='cyan',bg='orangered')
        line4=Button(symptoms, text='A. Common Symptoms',font=('helvetica',20,'bold'),bg='red', fg='green yellow',command=s1)
        line11=Button(symptoms, text='B. Serious Symptoms',font=('helvetica',21,'bold'),bg='red', fg='green yellow',command=s2)

        mainline.grid(row=0, column=0)
        line1.grid(row=1, column=0)
        line2.grid(row=2, column=0)
        line3.grid(row=0, column=1,padx=50)
        line4.grid(row=5, column=1, rowspan=2, sticky=N, pady=75)
        line5.grid(row=1, column=1,padx=20)
        line6.grid(row=2, column=1, padx=20)
        line7.grid(row=3, column=1, padx=20)
        line8.grid(row=3, column=0)
        line9.grid(row=4, column=0)
        #line10.grid(row=5,column=0)
        line11.grid(row=6, column=1, sticky=S, pady=40)
        image1_label.grid(row=5,column=0, rowspan=3, pady=30)
        image2_label.grid(row=6, column=1)
        
        def back():
            symptoms.destroy()
        end = Button(symptoms, text='< Back', font=('',10),command=back).place(x=15,y=15)

        symptoms.mainloop()
    

    line1 = Label(intro, text='What is a Coronavirus ?', font=('forte', 30), fg='red', anchor=E, bg='lightcyan',padx=200)
    empty_line = Label(intro, text='', bg='lightcyan')
    line2 = Label(intro, text='A virus is a submicroscopic infectious agent that replicates only inside the living cells of', font=('Times New Roman',18), fg='blue', bg='lightcyan')
    line3 = Label(intro, text='an organism. Coronavirus is kind of a normal virus that causes infection in your nose, sinsus',font=('Times New Roman',18), fg='blue', bg='lightcyan')
    line4 = Label(intro, text='or upper throat. The COVID-19 is a pandemic or disease caused by *SARS-CoV-2* i.e. a type of ', font=('Times New Roman',18), fg='blue', bg='lightcyan')
    line5 = Label(intro, text='coronavirus and can trigger what doctors call a respiratory tract infection. It spreads mainly', font=('Times New Roman',18), fg='blue', bg='lightcyan')
    line6 = Label(intro, text='through person to person contact. The infections caused by this coronavirus range from mild to', font=('Times New Roman',18), fg='blue', bg='lightcyan')
    line7 = Label(intro, text='deadly. The other coronaviruses cause most of the colds that affect us during the whole year but', font=('Times New Roman',18), fg='blue', bg='lightcyan')
    line8 = Label(intro, text='aren’t any serious threat for otherwise healthy people. It’s normal for a virus to change, or ', font=('Times New Roman',18), fg='blue', bg='lightcyan')
    line9 = Label(intro, text='mutate, as it infects people. A Chinese study of 103 COVID-19 cases suggests the virus that ', font=('Times New Roman',18), fg='blue', bg='lightcyan')
    line10= Label(intro, text='causes it has totally done just that. They found two strains of it, which they named as L and S.', font=('Times New Roman',18), fg='blue', bg='lightcyan')
    image1 = ImageTk.PhotoImage(Image.open('corona3.png'))
    image1_line = Label(intro, image=image1, height=270, bg='orange', bd=10)
    image2 = ImageTk.PhotoImage(Image.open('corona6.png'))
    image2_line = Label(intro, image=image2)

    frame = LabelFrame(intro, text='More about Corona Virus...', padx=20, pady=15, bd=20, font=('forte',26), bg='cyan', fg='red')
    l1_frame = Label(frame, text='To know about Origin of Coronavirus >', font=('forte',20),fg='orangered' ,bg='aqua')
    l2_frame = Label(frame, text='To know about symptoms of Coronavirus >', font=('forte',20),fg='orangered' ,bg='aqua')
    b1 = Button(frame, text='Click Here', bg='yellow', fg='orangered', font=('museo slab',14), padx=5, pady=5, command=origin)
    b2 = Button(frame, text='Click Here', bg='yellow', fg='orangered', font=('museo slab',14), padx=5, pady=5, command=symptoms)

    line1.grid(row=0, column=0, sticky=W)
    empty_line.grid(row=1, column=0)
    line2.grid(row=2, column=0, sticky=W)
    line3.grid(row=3, column=0, sticky=W)
    line4.grid(row=4, column=0, sticky=W)
    line5.grid(row=5, column=0, sticky=W)
    line6.grid(row=6, column=0, sticky=W)
    line7.grid(row=7, column=0, sticky=W)
    line8.grid(row=8, column=0, sticky=W)
    line9.grid(row=9, column=0, sticky=W)
    line10.grid(row=10, column=0, sticky=W)
    image1_line.grid(row=2, column=1, rowspan=9)
    image2_line.grid(row=11, column=0, columnspan=40, padx=850)
    frame.grid(row=11, column=0, padx=40 ,pady=60, sticky=W)
    l1_frame.grid(row=0, column=0)
    l2_frame.grid(row=1, column=0)
    b1.grid(row=0, column=1, pady=10, padx=10)
    b2.grid(row=1, column=1, pady=10, padx=10)

    def back():
        intro.destroy()
    end = Button(intro, text='< Back', font=('',10),command=back).place(x=15,y=15)


    intro.mainloop()


def ecoenviro():
    eco = Toplevel()
    eco.title('Economy & Environment')
    eco.configure(bg='lightcyan')
    eco.geometry('10000x10000')


    def econo():
        root=Toplevel()
        root.configure(bg='green')
        root.geometry('16000x16000')
        
        line1=Label(root,text='ECONOMY',bg='green',fg='blue2',padx=50,font=('MV Boli',40,'bold'))
        line1.grid(row=0,column=0,columnspan=5,padx=300)
        line2=Label(root,text='>GDP:- If the economy is growing, that generally means more wealth and more new jobs. It\'s measured by looking at the',bg='green',fg='dark orange',font=('Segoe print',16,'bold'))
        line2.grid(row=1,column=0,columnspan=5,sticky=W)
        line3=Label(root,text='percentage change in gross domestic product. IMF says that the global economy will shrink by 3% this year. India, Fance',bg='green',fg='dark orange',font=('segoe print',16,'bold'))
        line3.grid(row=2,column=0,columnspan=5,sticky=W)
        line4=Label(root,text='and Italy are the three out of five countries that suffered the highest eductions in trade volume over that period. China',bg='green',fg='dark orange',font=('segoe print',16,'bold'))
        line4.grid(row=3,column=0,columnspan=5,sticky=W)
        line5=Label(root,text='is one out of three countries that recorded an increase in trade.',bg='green',fg='dark orange',font=('segoe print',16,'bold'))
        line5.grid(row=4,column=0,columnspan=5,sticky=W)

        def show():
            a=[-23.9,-21.7,-18.9,-17.7,-13,-11.3,-9.9,-9.1,3.2]
            b=['India(-23.9)','UK(-21.7)','France(-18.9)','Italy(-17.7)','Canada(-13)',
               'Germany(-11.3)','Japan(-9.9)','USA(-9.1)','China(+3.2)']
            plt.subplot(2,1,1)
            plt.bar(b,a,color='green',align='center',width=0.4,label='GDP')
            plt.xlabel('Countries',fontsize=16)
            plt.ylabel('GDP growth',fontsize=16)
            plt.legend()
            plt.title('GDP growth(%) of April-June, 2020',fontsize=24)
            plt.subplots_adjust(hspace=0.8,wspace=0.8)
            c=[-42,-18,-33,-32,-29,-27,-21,-25,+4]
            d=['India(-42)','UK(-18)','France(-33)','Italy(-32)','Canada(-29)',
               'Germany(-27)','Japan(-21)','USA(-25)','China(+4.0)']
            plt.subplot(2,1,2)
            plt.bar(d,c,color='blue',align='center',width=0.4,label='Trade')
            plt.xlabel('Countries',fontsize=16)
            plt.ylabel('Trade growth in %',fontsize=16)
            plt.legend()
            plt.title('Trade growth(%) of April-June, 2020',fontsize=24)
            plt.show()
            
        line7=Button(root,text='Graph',bg='darkgoldenrod1',fg='blue2',font=('MV Boli',18,'bold'),bd=7,command=show)
        line7.grid(row=4,column=4,sticky=E)
        line8=Label(root,text='>Healthcare and Employment:- The global healthcare services market is expected to decline from $7102.7 billion in 2019',bg='green',fg='dark orange',font=('Segoe print',16,'bold'))
        line8.grid(row=5,column=0,columnspan=5,sticky=W)
        line9=Label(root,text='to $6657.1 billion in 2020. The decline is mainly due to the COVID-19 outbreak and the measures to contain it. The',bg='green',fg='dark orange',font=('Segoe print',16,'bold'))
        line9.grid(row=6,column=0,columnspan=5,sticky=W)
        #line10=Label(root,text='',bg='gold',fg='deep pink',font=('Segoe print',16,'bold'))
        #line10.grid(row=8,column=0,columnspan=5,sticky=W)
        line11=Label(root,text='International Labour Organization reports that “over one in six young people surveyed have stopped working since the',bg='green',fg='dark orange',font=('Segoe print',16,'bold'))
        line11.grid(row=7,column=0,columnspan=5,sticky=W)
        line12=Label(root,text='onset of the COVID‑19 crisis." International Labor Organization (ILO) estimates that more than 25 million jobs have been',bg='green',fg='dark orange',font=('Segoe print',16,'bold'))
        line12.grid(row=8,column=0,columnspan=5,sticky=W)
        line13=Label(root,text='threatened due to the spread of novel coronavirus globally. It is shown that four out of five that is around 81% of the 3.3',bg='green',fg='dark orange',font=('Segoe print',16,'bold'))
        line13.grid(row=9,column=0,columnspan=5,sticky=W)
        line14=Label(root,text='billion people worldwide have been affected by either partial or full workplace closure.  The UK, US, Canada, and various',bg='green',fg='dark orange',font=('Segoe print',16,'bold'))
        line14.grid(row=10,column=0,columnspan=5,sticky=W)
        line15=Label(root,text='Europian and Asian countries have registered a huge loss in jobs which increases their rate of unemployment.',bg='green',fg='dark orange',font=('Segoe print',16,'bold'))
        line15.grid(row=11,column=0,columnspan=5,sticky=W)

        def show1():
            a=[2.4,3.2,3.8,5.7,8.5,10,3.7]
            b=['Japan','Germany','UK','Canada','France','Italy','USA']
            c=[3.0,3.9,4.8,7.5,10.4,12.7,10.4]
            plt.subplot(2,1,1)
            plt.scatter(b,a)
            plt.plot(b,a,linewidth=3,label='2019')
            plt.scatter(b,c,c='y')
            plt.plot(b,c,'y',linewidth=3,label='2020')
            plt.legend()
            plt.ylabel('Countries',fontsize=16)
            plt.xlabel('Rates',fontsize=16)
            plt.title('Yearly unemployment rate change',fontsize=20)
            plt.subplots_adjust(hspace=0.8)
            plt.subplot(2,1,2)
            x=['March','April','May','June']
            y=[18,-10,-18,-35]
            z=[-43.5,-20,+5.0,+1.0]
            w=[15,-14,-35,-35]
            v=[9,-18,-45,-35]
            u=[16,-52,-57,-25]
            t=[11,-23,-36,-38]
            plt.plot(x,y,'r',label='Australia')
            plt.plot(x,z,'b',label='China')
            plt.plot(x,w,'y',label='USA')
            plt.plot(x,v,'g',label='Brazil')
            plt.plot(x,u,'orange',label='France')
            plt.plot(x,t,'purple',label='UK')
            plt.title('LinkedIn Hiring Rates',fontsize=20)
            plt.xlabel('Months',fontsize=20)
            plt.ylabel('Rates',fontsize=20)
            plt.legend(loc='best')
            plt.grid('true')
            plt.show()
            
        line16=Button(root,text='Graph',bg='darkgoldenrod1',fg='blue2',font=('MV Boli',18,'bold'),bd=7,command=show1)
        line16.grid(row=11,column=4,sticky=E)
        line17=Label(root,text='>Market and Travel:- The travel industry has been badly damaged, with airlines cutting flights and customers cancelling',bg='green',fg='dark orange',font=('Segoe print',16,'bold'))
        line17.grid(row=12,column=0,columnspan=5,sticky=W)
        line18=Label(root,text='business trips and holidays. Many countries introduced travel restrictions to try to contain the virus. Retail footfall also',bg='green',fg='dark orange',font=('Segoe print',16,'bold'))
        line18.grid(row=13,column=0,columnspan=5,sticky=W)
        line19=Label(root,text='saw unprecedented lows as shoppers stayed at home in a bid to stop the spread of Covid-19.',bg='green',fg='dark orange',font=('Segoe print',16,'bold'))
        line19.grid(row=14,column=0,columnspan=5,sticky=W)

        def show2():
            a=['March','','April','','May','','June','']
            a_pos=np.arange(len(a))
            plt.subplot(2,1,1)
            b=[168,160,80,75,80,92,115,122]
            c=[180,170,167,194,193,203,214,190]
            d=[160,171,145,163,175,174,184,185]
            plt.plot(a_pos,b,'g',linewidth=3,label='2020')
            plt.plot(a_pos,c,'b',linewidth=3,label='2019')
            plt.plot(a_pos,d,'y',linewidth=3,label='2018')
            plt.legend(loc='lower right')
            plt.title('Number of Total Monthly Flights',fontsize=20)
            plt.xlabel('Months',fontsize=20)
            plt.ylabel('Flights(x1000)',fontsize=20)
            plt.xticks(a_pos,a)
            plt.subplots_adjust(hspace=0.75)
            plt.subplot(2,1,2)
            d=['Mexico(-80)','France(-50)','UK(-78)','Italy(-54)','Canada(-72)',
              'Germany(-49)','Japan(-37)','USA(-52)','China(-32)']
            p=[-80,-50,-78,-54,-72,-49,-37,-52,-32]
            plt.barh(d,p)
            plt.title('Change in footfall in %',fontsize=20)
            plt.ylabel('Countries',fontsize=20)
            plt.xlabel('Change',fontsize=20)
            plt.show()
            
        line20=Button(root,text='Graph',bg='darkgoldenrod1',fg='blue2',font=('MV Boli',18,'bold'),bd=7,command=show2)
        line20.grid(row=14,column=4,sticky=E)

        def back():
            root.destroy()
        end = Button(root, text='< Back', font=('',10),command=back).place(x=15,y=15)

        root.mainloop()

    def envi():
        Environment=Toplevel()
        Environment.title("Environment")
        Environment.configure(bg='navy')

        heading=Label(Environment,text="Environment",font=('Times New Roman',36,'bold'),bg="black",fg="orange",bd=7,padx=240,pady=15)
        heading.grid(row=0,column=1,sticky=W)

        def show():
              objects=('1970','1980','1990','2000','2010','2020','2020.5')
              percent=[38,53,62,65,83,100,80]
              plt.scatter(objects,percent)
              plt.plot(objects,percent)
              plt.xlabel('Year',fontsize=26)
              plt.ylabel('Global daily fossil CO2 Emissions(MtCO2d-1)',fontsize=20)
              plt.title('Reduction In Global CO2 Emissions',fontsize=24)
              plt.grid()
              plt.show()

        text1=Label(Environment,text=">Carbon emission:-",font=('Times New Roman',20,'bold'),bg='navy',fg="yellow")
        text2=Label(Environment,text="A study published in May 2020 found that the daily global carbon emissions during the",font=('Monotype Corsiva',20),bg='navy',fg="white")
        text3=Label(Environment,text="lockdown measures in early April fell by 17% and could lead to an annual carbon emissions decline of up to",font=('Monotype Corsiva',20),bg='navy',fg="white")
        text4=Label(Environment,text="7% which would be the biggest drop since World War II according to the researchers.They ascribec decreases",font=('Monotype Corsiva',20),bg='navy',fg="white")
        text5=Label(Environment,text=" mainly to the reduction of transportation usage and industrial activities.",font=('Monotype Corsiva',20),bg='navy',fg="white")
        button1=Button(Environment,text="Graph",font=('Elephant',15),bg="purple",fg="aqua",padx=50,command=show)
        image1=ImageTk.PhotoImage(Image.open('5120.jpg'))
        image1_label=Label(Environment, image=image1)

        text1.grid(row=1,column=0,sticky=W)
        text2.grid(row=1,column=1,sticky=W)
        text3.grid(row=2,column=0,columnspan=2)
        text4.grid(row=3,column=0,columnspan=2)
        text5.grid(row=4,column=1,sticky=W)
        button1.grid(row=4,column=0,sticky=E)
        image1_label.grid(row=1,column=2,rowspan=4,sticky=W,pady=20)

        #step 2
        def show2():
              objects=('Bejing,China','Mumbai,India','Madrid,Spain','Sau Paula,Brazil','Alberta,Canada','Los Angeles,California')
              percent1=[18,78,37,35,38,17]
              #plt.subplot(2,1,2)
              #plt.grid(color='teal')
              plt.bar(objects,percent1,label='After Pandemic',width=0.25)
              percent2=[90,155,40,40,58,37]
              plt.bar(objects,percent2,label='Before Pandemic',width=0.15,align='edge')
              plt.xlabel('Countries',fontsize=26)
              plt.ylabel('Pollution measured(in P.M. 2.5)',fontsize=16)
              plt.legend()
              
              plt.title('Decrease in P.M. level(due to pandemic)',fontsize=30)
              #plt.grid(color='green')
              plt.show()
                  
        image4=ImageTk.PhotoImage(Image.open('blue-12.png'))
        image4_label=Label(Environment, image=image4)
        text6=Label(Environment,text=">Particulate Matter:-",font=('Times New Roman',20,'bold'),bg='navy',fg="yellow")
        text7=Label(Environment,text="COVID-19 pandemic elicited a global response to limit associated mortality, with social",font=('Monotype Corsiva',20),bg='navy',fg="white")
        text8=Label(Environment,text="distancing and lockdowns being imposed. Temporary reduction in fine particulate matter due ‘anthropogenic emissions ",font=('Monotype Corsiva',20),bg='navy',fg="white")
        text9=Label(Environment,text="switch-off’ during COVID-19 lockdown Modelling revealed fewer extreme PM2.5 values during the lockdown in all ",font=('Monotype Corsiva',20),bg='navy',fg="white")
        text10=Label(Environment,text="cities.PM2.5 reductions prevented ∼630 premature deaths, valued at 0.69 billion USD.",font=('Monotype Corsiva',20),bg='navy',fg="white")
        button2=Button(Environment,text="Graph",font=('Elephant',15),bg="purple",fg="aqua",padx=50,command=show2)

        text6.grid(row=5,column=0,sticky=W)
        text7.grid(row=5,column=1,sticky=W)
        text8.grid(row=6,column=0,columnspan=2,sticky=W)
        text9.grid(row=7,column=0,columnspan=2,sticky=W)
        text10.grid(row=8,column=1,sticky=W)
        button2.grid(row=8,column=0,sticky=E)
        image4_label.grid(row=5,column=2,rowspan=4,sticky=W,pady=25)


        #step3
        def show3():
              objects=('China(30)','Europe(25)','Italy(35)','France(20)','Spain(35)','USA(30)')
              percent=[30,25,35,20,35,30]
              plt.bar(objects,percent,color="Purple")
              plt.xlabel('Location',fontsize=26)
              plt.ylabel('% Reduction',fontsize=26)
              plt.title('NO2 Emissions Reduction Across Different Region',fontsize=24)
              plt.show()
                  
        text11=Label(Environment,text=">Nirogen emission:-",font=('Times New Roman',20,'bold'),bg='navy',fg="yellow")
        text12=Label(Environment,text="NO2 (nitrogen dioxide) is a dangerous,highly reactive pollutant and emitted especially from ",font=('Monotype Corsiva',20),bg='navy',fg="white")
        text13=Label(Environment,text="the combustion of fossil fuels.NASA (National Aeronautics and Space Administration) and ESA (European Space",font=('Monotype Corsiva',20),bg='navy',fg="white")
        text14=Label(Environment,text="Agency) released fresh evidence which suggests that environmental quality improved and the emission of NO2 ",font=('Monotype Corsiva',20),bg='navy',fg="white")
        text15=Label(Environment,text="reduced up to 30%.",font=('Monotype Corsiva',20),bg='navy',fg="white")
        button3=Button(Environment,text="Graph",font=('Elephant',15),bg="purple",fg="aqua",padx=50,command=show3)
        image5=ImageTk.PhotoImage(Image.open('NO2_Emission_China_Italy_shareable2-1000x600.jpg'))
        image5_label=Label(Environment, image=image5)

        text11.grid(row=9,column=0,sticky=W)
        text12.grid(row=9,column=1,sticky=W)
        text13.grid(row=10,column=0,columnspan=2)
        text14.grid(row=11,column=0,columnspan=2)
        text15.grid(row=12,column=1,sticky=W)
        button3.grid(row=12,column=0,sticky=E)
        image5_label.grid(row=9,column=2,rowspan=4,sticky=W,pady=20)

        def back():
            Environment.destroy()
        end = Button(Environment, text='< Back', font=('',10),command=back).place(x=15,y=15)

        Environment.mainloop()

    economy = Label(eco, text='ECONOMY', fg='purple', bg='cyan', font=('elephant',24,'bold'))
    And = Label(eco, text='AND', fg='red', bg='lightcyan', font=('quikhand',24,'underline'))
    environment = Label(eco, text='ENVIRONMENT', fg='purple', bg='cyan', font=('elephant',24,'bold'))

    dash1 = Label(eco, text='|', fg='red', bg='lightcyan')
    dash2 = Label(eco, text='|', fg='red', bg='lightcyan')
    dash3 = Label(eco, text='|', fg='red', bg='lightcyan')
    dash4 = Label(eco, text='|', fg='red', bg='lightcyan')
    dash5 = Label(eco, text='|', fg='red', bg='lightcyan')
    dash6 = Label(eco, text='|', fg='red', bg='lightcyan')
    dash7 = Label(eco, text='|', fg='red', bg='lightcyan')
    dash8 = Label(eco, text='|', fg='red', bg='lightcyan')
    dash9 = Label(eco, text='|', fg='red', bg='lightcyan')
    dash10= Label(eco, text='|', fg='red', bg='lightcyan')
    dash11= Label(eco, text='|', fg='red', bg='lightcyan')
    dash12= Label(eco, text='|', fg='red', bg='lightcyan')
    dash13= Label(eco, text='|', fg='red', bg='lightcyan')
    dash14= Label(eco, text='|', fg='red', bg='lightcyan')
    dash15= Label(eco, text='|', fg='red', bg='lightcyan')
    dash16= Label(eco, text='|', fg='red', bg='lightcyan')
    dash17= Label(eco, text='|', fg='red', bg='lightcyan')
    dash18= Label(eco, text='|', fg='red', bg='lightcyan')
    dash19= Label(eco, text='|', fg='red', bg='lightcyan')
    dash20= Label(eco, text='|', fg='red', bg='lightcyan')
    dash21= Label(eco, text='|', fg='red', bg='lightcyan')
    dash22= Label(eco, text='|', fg='red', bg='lightcyan')


    economy_line1 = Label(eco, text='Covid-19 impact: According to IMF, the global economy is expected to shrink', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    economy_line2 = Label(eco, text='by over 3% in 2020  –  the steepest slowdown since the Great Depression', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    economy_line3 = Label(eco, text='of the 1930s.', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    economy_image = ImageTk.PhotoImage(Image.open('coronaeconomy.png'))
    economy_image_label = Label(eco, image=economy_image, bg='indigo', bd=5)
    economy_line4 = Label(eco, text='The IMF’s estimate of the global economy growing at  -  3% in 2020 is', fg='indigo', bg='lightcyan', font=('pixer regular',16))
    economy_line5 = Label(eco, text='“far worse” than 2009 global financial crises. Economies such as the', fg='indigo', bg='lightcyan', font=('pixer regular',16))
    economy_line6 = Label(eco, text='US, Japan, UK, Germany, France, Italy and Spain are expected to the ', fg='indigo', bg='lightcyan', font=('pixer regular',16))
    economy_line7 = Label(eco, text='this year by (5.9, 5.2, 6.5, 7, 7.2, 9.1 and 8)% respectively.', fg='indigo', bg='lightcyan', font=('pixer regular',16))
    economy_line8 = Label(eco, text='', fg='indigo', bg='lightcyan', font=('pixer regular',16))
    economy_frame  = LabelFrame(eco, text='To know more about Economy : ',  font=('roboto',15,'bold'), bg='cyan', fg='indigo', bd=10)
    economy_button= Button(economy_frame, text='Click Here',  font=('forte',18), bg='yellow', fg='red', command=econo)

    enviro_line1 = Label(eco, text='Some sources argue that the Covid-19 outbreak reduces the pollution', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    enviro_line2 = Label(eco, text='environmentally, while others say that the environmentally significant', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    enviro_line3 = Label(eco, text='damages await us in the future.', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    enviro_image = ImageTk.PhotoImage(Image.open('coronaenviro.jpg'))
    enviro_image_label = Label(eco, image=enviro_image, bg='indigo', bd=5)
    enviro_line4 = Label(eco, text='It is presented that Covid-19 outbreak has serious environmental impacts', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    enviro_line5 = Label(eco, text='such as increased environmental waste. Covid-19 outbreak provides a', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    enviro_line6 = Label(eco, text='reduction in greenhouse gas emissions, but more efforts are needed to', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    enviro_line7 = Label(eco, text='prevent the pollution to be done in the future.', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    enviro_line8 = Label(eco, text='', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    enviro_line9 = Label(eco, text='', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    enviro_line10= Label(eco, text='', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    enviro_line11= Label(eco, text='', fg='indigo', bg='lightcyan', font=('pixer regular',14))
    enviro_frame  = LabelFrame(eco, text='To know more about Environment : ',  font=('roboto',15,'bold'), bg='cyan', fg='indigo', bd=10)
    enviro_button= Button(enviro_frame, text='Click Here',  font=('forte',18), bg='yellow', fg='red',command=envi)


    economy.grid(row=0,column=0, pady=15)
    And.grid(row=0,column=1)
    environment.grid(row=0,column=2)
    dash1.grid(row=1,column=1)
    dash2.grid(row=2,column=1)
    dash3.grid(row=3,column=1)
    dash4.grid(row=4,column=1)
    dash5.grid(row=5,column=1)
    dash6.grid(row=6,column=1)
    dash7.grid(row=7,column=1)
    dash8.grid(row=8,column=1)
    dash9.grid(row=9,column=1)
    dash10.grid(row=10,column=1)
    dash11.grid(row=11,column=1)
    dash12.grid(row=12,column=1)
    dash13.grid(row=13,column=1)
    dash14.grid(row=14,column=1)
    dash15.grid(row=15,column=1)
    dash16.grid(row=16,column=1)
    dash17.grid(row=17,column=1)
    dash18.grid(row=18,column=1)
    dash19.grid(row=19,column=1)
    dash20.grid(row=20,column=1)
    dash21.grid(row=21,column=1)
    dash22.grid(row=22,column=1)

    economy_line1.grid(row=1,column=0)
    economy_line2.grid(row=2,column=0)
    economy_line3.grid(row=3,column=0)
    economy_image_label.grid(row=4,column=0, rowspan=9, pady=20)
    economy_line4.grid(row=13,column=0)
    economy_line5.grid(row=14,column=0)
    economy_line6.grid(row=15,column=0)
    economy_line7.grid(row=16,column=0)
    economy_button.grid(row=17,column=0, padx=90, pady=10)
    economy_frame.grid(row=17, column=0, pady=20, rowspan=5)

    enviro_line1.grid(row=1,column=2)
    enviro_line2.grid(row=2,column=2)
    enviro_line3.grid(row=3,column=2)
    enviro_image_label.grid(row=4,column=2, rowspan=9, pady=20)
    enviro_line4.grid(row=13,column=2)
    enviro_line5.grid(row=14,column=2)
    enviro_line6.grid(row=15,column=2)
    enviro_line7.grid(row=16,column=2)
    enviro_button.grid(row=17,column=2, padx=110, pady=10)
    enviro_frame.grid(row=17, column=2, pady=20, rowspan=5)

    def back():
        eco.destroy()
    end = Button(eco, text='< Back', font=('',10),command=back).place(x=15,y=15)

    eco.mainloop()


def journy():
    globe = Toplevel()
    globe.title('Journy Across The Globe')
    globe.configure(bg='black')
    globe.geometry('10000x10000')


    def dates():
        glob = Tk()
        glob.geometry("10000x10000")
        glob.configure(bg='black')

        my_connect = mysql.connector.connect(
          host="localhost",
          user="root", 
          passwd="",
          database="global"
        )

        my_conn = my_connect.cursor()


        #January_1
        if month.get()=='January' and date.get()==1:
            glob.title('January_1')
            my_conn.execute("SELECT * FROM january_1")
            i=0
            for january_1 in my_conn: 
                for j in range(len(january_1)):
                    e = Entry(glob, width=16, font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_1[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1


        #January_2
        elif month.get()=='January' and date.get()==2:
            glob.title('January_2')
            my_conn.execute("SELECT * FROM january_2")
            i=0
            for january_2 in my_conn: 
                for j in range(len(january_2)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_2[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_3
        elif month.get()=='January' and date.get()==3:
            glob.title('January_3')
            my_conn.execute("SELECT * FROM january_3")
            i=0
            for january_3 in my_conn: 
                for j in range(len(january_3)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_3[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_4
        elif month.get()=='January' and date.get()==4:
            glob.title('January_4')
            my_conn.execute("SELECT * FROM january_4")
            i=0
            for january_4 in my_conn: 
                for j in range(len(january_4)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_4[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_5
        elif month.get()=='January' and date.get()==5:
            glob.title('January_5')
            my_conn.execute("SELECT * FROM january_5")
            i=0
            for january_5 in my_conn: 
                for j in range(len(january_5)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_5[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_6
        elif month.get()=='January' and date.get()==6:
            glob.title('January_6')
            my_conn.execute("SELECT * FROM january_6")
            i=0
            for january_6 in my_conn: 
                for j in range(len(january_6)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_6[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_7
        elif month.get()=='January' and date.get()==7:
            glob.title('January_7')
            my_conn.execute("SELECT * FROM january_7")
            i=0
            for january_7 in my_conn: 
                for j in range(len(january_7)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_7[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_8
        elif month.get()=='January' and date.get()==8:
            glob.title('January_8')
            my_conn.execute("SELECT * FROM january_8")
            i=0
            for january_8 in my_conn: 
                for j in range(len(january_8)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_8[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_9
        elif month.get()=='January' and date.get()==9:
            glob.title('January_9')
            my_conn.execute("SELECT * FROM january_9")
            i=0
            for january_9 in my_conn: 
                for j in range(len(january_9)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_9[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_10
        elif month.get()=='January' and date.get()==10:
            glob.title('January_10')
            my_conn.execute("SELECT * FROM january_10")
            i=0
            for january_10 in my_conn: 
                for j in range(len(january_10)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_10[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_11
        elif month.get()=='January' and date.get()==11:
            glob.title('January_11')
            my_conn.execute("SELECT * FROM january_11")
            i=0
            for january_11 in my_conn: 
                for j in range(len(january_11)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_11[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_12
        elif month.get()=='January' and date.get()==12:
            glob.title('January_12')
            my_conn.execute("SELECT * FROM january_12")
            i=0
            for january_12 in my_conn: 
                for j in range(len(january_12)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_12[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_13
        elif month.get()=='January' and date.get()==13:
            glob.title('January_13')
            my_conn.execute("SELECT * FROM january_13")
            i=0
            for january_13 in my_conn: 
                for j in range(len(january_13)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_13[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_14
        elif month.get()=='January' and date.get()==14:
            glob.title('January_14')
            my_conn.execute("SELECT * FROM january_14")
            i=0
            for january_14 in my_conn: 
                for j in range(len(january_14)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_14[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_15
        elif month.get()=='January' and date.get()==15:
            glob.title('January_15')
            my_conn.execute("SELECT * FROM january_15")
            i=0
            for january_15 in my_conn: 
                for j in range(len(january_15)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_15[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_16
        elif month.get()=='January' and date.get()==16:
            glob.title('January_16')
            my_conn.execute("SELECT * FROM january_16")
            i=0
            for january_16 in my_conn: 
                for j in range(len(january_16)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_16[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_17
        elif month.get()=='January' and date.get()==17:
            glob.title('January_17')
            my_conn.execute("SELECT * FROM january_17")
            i=0
            for january_17 in my_conn: 
                for j in range(len(january_17)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_17[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1



        #January_18
        elif month.get()=='January' and date.get()==18:
            glob.title('January_18')
            my_conn.execute("SELECT * FROM january_18")
            i=0
            for january_18 in my_conn: 
                for j in range(len(january_18)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_18[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_19
        elif month.get()=='January' and date.get()==19:
            glob.title('January_19')
            my_conn.execute("SELECT * FROM january_19")
            i=0
            for january_19 in my_conn: 
                for j in range(len(january_19)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_19[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_20
        elif month.get()=='January' and date.get()==20:
            glob.title('January_20')
            my_conn.execute("SELECT * FROM january_20")
            i=0
            for january_20 in my_conn: 
                for j in range(len(january_20)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_20[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_21
        elif month.get()=='January' and date.get()==21:
            glob.title('January_21')
            my_conn.execute("SELECT * FROM january_21")
            i=0
            for january_21 in my_conn: 
                for j in range(len(january_21)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_21[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_22
        elif month.get()=='January' and date.get()==22:
            glob.title('January_22')
            my_conn.execute("SELECT * FROM january_22")
            i=0
            for january_22 in my_conn: 
                for j in range(len(january_22)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_22[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_23
        elif month.get()=='January' and date.get()==23:
            glob.title('January_23')
            my_conn.execute("SELECT * FROM january_23")
            i=0
            for january_23 in my_conn: 
                for j in range(len(january_23)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_23[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_24
        elif month.get()=='January' and date.get()==24:
            glob.title('January_24')
            my_conn.execute("SELECT * FROM january_24")
            i=0
            for january_24 in my_conn: 
                for j in range(len(january_24)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_24[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_25
        elif month.get()=='January' and date.get()==25:
            glob.title('January_25')
            my_conn.execute("SELECT * FROM january_25")
            i=0
            for january_25 in my_conn: 
                for j in range(len(january_25)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_25[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_26
        elif month.get()=='January' and date.get()==26:
            glob.title('January_26')
            my_conn.execute("SELECT * FROM january_26")
            i=0
            for january_26 in my_conn: 
                for j in range(len(january_26)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_26[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_27
        elif month.get()=='January' and date.get()==27:
            glob.title('January_27')
            my_conn.execute("SELECT * FROM january_27")
            i=0
            for january_27 in my_conn: 
                for j in range(len(january_27)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_27[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_28
        elif month.get()=='January' and date.get()==28:
            glob.title('January_28')
            my_conn.execute("SELECT * FROM january_28")
            i=0
            for january_28 in my_conn: 
                for j in range(len(january_28)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_28[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_29
        elif month.get()=='January' and date.get()==29:
            glob.title('January_29')
            my_conn.execute("SELECT * FROM january_29")
            i=0
            for january_29 in my_conn: 
                for j in range(len(january_29)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_29[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_30
        elif month.get()=='January' and date.get()==30:
            glob.title('January_30')
            my_conn.execute("SELECT * FROM january_30")
            i=0
            for january_30 in my_conn: 
                for j in range(len(january_30)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_30[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #January_31
        elif month.get()=='January' and date.get()==31:
            glob.title('January_31')
            my_conn.execute("SELECT * FROM january_31")
            i=0
            for january_31 in my_conn: 
                for j in range(len(january_31)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, january_31[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_1
        elif month.get()=='February' and date.get()==1:
            glob.title('February_1')
            my_conn.execute("SELECT * FROM february_1")
            i=0
            for february_1 in my_conn: 
                for j in range(len(february_1)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_1[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_2
        elif month.get()=='February' and date.get()==2:
            glob.title('February_2')
            my_conn.execute("SELECT * FROM february_2")
            i=0
            for february_2 in my_conn: 
                for j in range(len(february_2)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_2[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_3
        elif month.get()=='February' and date.get()==3:
            glob.title('February_3')
            my_conn.execute("SELECT * FROM february_3")
            i=0
            for february_3 in my_conn: 
                for j in range(len(february_3)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_3[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_4
        elif month.get()=='February' and date.get()==4:
            glob.title('February_4')
            my_conn.execute("SELECT * FROM february_4")
            i=0
            for february_4 in my_conn: 
                for j in range(len(february_4)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_4[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_5
        elif month.get()=='February' and date.get()==5:
            glob.title('February_5')
            my_conn.execute("SELECT * FROM february_5")
            i=0
            for february_5 in my_conn: 
                for j in range(len(february_5)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_5[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_6
        elif month.get()=='February' and date.get()==6:
            glob.title('February_6')
            my_conn.execute("SELECT * FROM february_6")
            i=0
            for february_6 in my_conn: 
                for j in range(len(february_6)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_6[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_7
        elif month.get()=='February' and date.get()==7:
            glob.title('February_7')
            my_conn.execute("SELECT * FROM february_7")
            i=0
            for february_7 in my_conn: 
                for j in range(len(february_7)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_7[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1
        #February_8
        elif month.get()=='February' and date.get()==8:
            glob.title('February_8')
            my_conn.execute("SELECT * FROM february_8")
            i=0
            for february_8 in my_conn: 
                for j in range(len(february_8)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_8[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_9
        elif month.get()=='February' and date.get()==9:
            glob.title('February_9')
            my_conn.execute("SELECT * FROM february_9")
            i=0
            for february_9 in my_conn: 
                for j in range(len(february_9)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_9[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_10
        elif month.get()=='February' and date.get()==10:
            glob.title('February_10')
            my_conn.execute("SELECT * FROM february_10")
            i=0
            for february_10 in my_conn: 
                for j in range(len(february_10)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_10[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_11
        elif month.get()=='February' and date.get()==11:
            glob.title('February_11')
            my_conn.execute("SELECT * FROM february_11")
            i=0
            for february_11 in my_conn: 
                for j in range(len(february_11)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_11[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_12
        elif month.get()=='February' and date.get()==12:
            glob.title('February_12')
            my_conn.execute("SELECT * FROM february_12")
            i=0
            for february_12 in my_conn: 
                for j in range(len(february_12)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_12[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_13
        elif month.get()=='February' and date.get()==13:
            glob.title('February_13')
            my_conn.execute("SELECT * FROM february_13")
            i=0
            for february_13 in my_conn: 
                for j in range(len(february_13)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_13[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_14
        elif month.get()=='February' and date.get()==14:
            glob.title('February_14')
            my_conn.execute("SELECT * FROM february_14")
            i=0
            for february_14 in my_conn: 
                for j in range(len(february_14)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_14[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_15
        elif month.get()=='February' and date.get()==15:
            glob.title('February_15')
            my_conn.execute("SELECT * FROM february_15")
            i=0
            for february_15 in my_conn: 
                for j in range(len(february_15)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_15[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_16
        elif month.get()=='February' and date.get()==16:
            glob.title('February_16')
            my_conn.execute("SELECT * FROM february_16")
            i=0
            for february_16 in my_conn: 
                for j in range(len(february_16)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_16[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_17
        elif month.get()=='February' and date.get()==17:
            glob.title('February_17')
            my_conn.execute("SELECT * FROM february_17")
            i=0
            for february_17 in my_conn: 
                for j in range(len(february_17)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_17[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_18
        elif month.get()=='February' and date.get()==18:
            glob.title('February_18')
            my_conn.execute("SELECT * FROM february_18")
            i=0
            for february_18 in my_conn: 
                for j in range(len(february_18)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_18[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_19
        elif month.get()=='February' and date.get()==19:
            glob.title('February_19')
            my_conn.execute("SELECT * FROM february_19")
            i=0
            for february_19 in my_conn: 
                for j in range(len(february_19)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_19[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_20
        elif month.get()=='February' and date.get()==20:
            glob.title('February_20')
            my_conn.execute("SELECT * FROM february_20")
            i=0
            for february_20 in my_conn: 
                for j in range(len(february_20)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_20[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_21
        elif month.get()=='February' and date.get()==21:
            glob.title('February_21')
            my_conn.execute("SELECT * FROM february_21")
            i=0
            for february_21 in my_conn: 
                for j in range(len(february_21)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_21[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_22
        elif month.get()=='February' and date.get()==22:
            glob.title('February_22')
            my_conn.execute("SELECT * FROM february_22")
            i=0
            for february_22 in my_conn: 
                for j in range(len(february_22)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_22[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_23
        elif month.get()=='February' and date.get()==23:
            glob.title('February_23')
            my_conn.execute("SELECT * FROM february_23")
            i=0
            for february_23 in my_conn: 
                for j in range(len(february_23)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_23[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_24
        elif month.get()=='February' and date.get()==24:
            glob.title('February_24')
            my_conn.execute("SELECT * FROM february_24")
            i=0
            for february_24 in my_conn: 
                for j in range(len(february_24)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_24[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_25
        elif month.get()=='February' and date.get()==25:
            glob.title('February_25')
            my_conn.execute("SELECT * FROM february_25")
            i=0
            for february_25 in my_conn: 
                for j in range(len(february_25)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_25[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_26
        elif month.get()=='February' and date.get()==26:
            glob.title('February_26')
            my_conn.execute("SELECT * FROM february_26")
            i=0
            for february_26 in my_conn: 
                for j in range(len(february_26)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_26[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_27
        elif month.get()=='February' and date.get()==27:
            glob.title('February_27')
            my_conn.execute("SELECT * FROM february_27")
            i=0
            for february_27 in my_conn: 
                for j in range(len(february_27)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_27[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_28
        elif month.get()=='February' and date.get()==28:
            glob.title('February_28')
            my_conn.execute("SELECT * FROM february_28")
            i=0
            for february_28 in my_conn: 
                for j in range(len(february_28)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_28[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #February_29
        elif month.get()=='February' and date.get()==29:
            glob.title('February_29')
            my_conn.execute("SELECT * FROM february_29")
            i=0
            for february_29 in my_conn: 
                for j in range(len(february_29)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, february_29[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_1
        elif month.get()=='March' and date.get()==1:
            glob.title('March_1')
            my_conn.execute("SELECT * FROM march_1")
            i=0
            for march_1 in my_conn: 
                for j in range(len(march_1)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_1[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_2
        elif month.get()=='March' and date.get()==2:
            glob.title('March_2')
            my_conn.execute("SELECT * FROM march_2")
            i=0
            for march_2 in my_conn: 
                for j in range(len(march_2)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_2[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_3
        elif month.get()=='March' and date.get()==3:
            glob.title('March_3')
            my_conn.execute("SELECT * FROM march_3")
            i=0
            for march_3 in my_conn: 
                for j in range(len(march_3)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_3[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_4
        elif month.get()=='March' and date.get()==4:
            glob.title('March_4')
            my_conn.execute("SELECT * FROM march_4")
            i=0
            for march_4 in my_conn: 
                for j in range(len(march_4)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_4[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_5
        elif month.get()=='March' and date.get()==5:
            glob.title('March_5')
            my_conn.execute("SELECT * FROM march_5")
            i=0
            for march_5 in my_conn: 
                for j in range(len(march_5)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_5[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_6
        elif month.get()=='March' and date.get()==6:
            glob.title('March_6')
            my_conn.execute("SELECT * FROM march_6")
            i=0
            for march_6 in my_conn: 
                for j in range(len(march_6)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_6[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_7
        elif month.get()=='March' and date.get()==7:
            glob.title('March_7')
            my_conn.execute("SELECT * FROM march_7")
            i=0
            for march_7 in my_conn: 
                for j in range(len(march_7)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_7[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_8
        elif month.get()=='March' and date.get()==8:
            glob.title('March_8')
            my_conn.execute("SELECT * FROM march_8")
            i=0
            for march_8 in my_conn: 
                for j in range(len(march_8)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_8[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_9
        elif month.get()=='March' and date.get()==9:
            glob.title('March_9')
            my_conn.execute("SELECT * FROM march_9")
            i=0
            for march_9 in my_conn: 
                for j in range(len(march_9)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_9[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_10
        elif month.get()=='March' and date.get()==10:
            glob.title('March_10')
            my_conn.execute("SELECT * FROM march_10")
            i=0
            for march_10 in my_conn: 
                for j in range(len(march_10)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_10[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_11
        elif month.get()=='March' and date.get()==11:
            glob.title('March_11')
            my_conn.execute("SELECT * FROM march_11")
            i=0
            for march_11 in my_conn: 
                for j in range(len(march_11)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_11[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_12
        elif month.get()=='March' and date.get()==12:
            glob.title('March_12')
            my_conn.execute("SELECT * FROM march_12")
            i=0
            for march_12 in my_conn: 
                for j in range(len(march_12)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_12[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_13
        elif month.get()=='March' and date.get()==13:
            glob.title('March_13')
            my_conn.execute("SELECT * FROM march_13")
            i=0
            for march_13 in my_conn: 
                for j in range(len(march_13)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_13[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_14
        elif month.get()=='March' and date.get()==14:
            glob.title('March_14')
            my_conn.execute("SELECT * FROM march_14")
            i=0
            for march_14 in my_conn: 
                for j in range(len(march_14)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_14[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1


        #March_15
        elif month.get()=='March' and date.get()==15:
            glob.title('March_15')
            my_conn.execute("SELECT * FROM march_15")
            i=0
            for march_15 in my_conn: 
                for j in range(len(march_15)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_15[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_16
        elif month.get()=='March' and date.get()==16:
            glob.title('March_16')
            my_conn.execute("SELECT * FROM march_16")
            i=0
            for march_16 in my_conn: 
                for j in range(len(march_16)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_16[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_17
        elif month.get()=='March' and date.get()==17:
            glob.title('March_17')
            my_conn.execute("SELECT * FROM march_17")
            i=0
            for march_17 in my_conn: 
                for j in range(len(march_17)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_17[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_18
        elif month.get()=='March' and date.get()==18:
            glob.title('March_18')
            my_conn.execute("SELECT * FROM march_18")
            i=0
            for march_18 in my_conn: 
                for j in range(len(march_18)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_18[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_19
        elif month.get()=='March' and date.get()==19:
            glob.title('March_19')
            my_conn.execute("SELECT * FROM march_19")
            i=0
            for march_19 in my_conn: 
                for j in range(len(march_19)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_19[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_20
        elif month.get()=='March' and date.get()==20:
            glob.title('March_20')
            my_conn.execute("SELECT * FROM march_20")
            i=0
            for march_20 in my_conn: 
                for j in range(len(march_20)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_20[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_21
        elif month.get()=='March' and date.get()==21:
            glob.title('March_21')
            my_conn.execute("SELECT * FROM march_21")
            i=0
            for march_21 in my_conn: 
                for j in range(len(march_21)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_21[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_22
        elif month.get()=='March' and date.get()==22:
            glob.title('March_22')
            my_conn.execute("SELECT * FROM march_22")
            i=0
            for march_22 in my_conn: 
                for j in range(len(march_22)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_22[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_23
        elif month.get()=='March' and date.get()==23:
            glob.title('March_23')
            my_conn.execute("SELECT * FROM march_23")
            i=0
            for march_23 in my_conn: 
                for j in range(len(march_23)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_23[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_24
        elif month.get()=='March' and date.get()==24:
            glob.title('March_24')
            my_conn.execute("SELECT * FROM march_24")
            i=0
            for march_24 in my_conn: 
                for j in range(len(march_24)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_24[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_25
        elif month.get()=='March' and date.get()==25:
            glob.title('March_25')
            my_conn.execute("SELECT * FROM march_25")
            i=0
            for march_25 in my_conn: 
                for j in range(len(march_25)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_25[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_26
        elif month.get()=='March' and date.get()==26:
            glob.title('March_26')
            my_conn.execute("SELECT * FROM march_26")
            i=0
            for march_26 in my_conn: 
                for j in range(len(march_26)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_26[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_27
        elif month.get()=='March' and date.get()==27:
            glob.title('March_27')
            my_conn.execute("SELECT * FROM march_27")
            i=0
            for march_27 in my_conn: 
                for j in range(len(march_27)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_27[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_28
        elif month.get()=='March' and date.get()==28:
            glob.title('March_28')
            my_conn.execute("SELECT * FROM march_28")
            i=0
            for march_28 in my_conn: 
                for j in range(len(march_28)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_28[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_29
        elif month.get()=='March' and date.get()==29:
            glob.title('March_29')
            my_conn.execute("SELECT * FROM march_29")
            i=0
            for march_29 in my_conn: 
                for j in range(len(march_29)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_29[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_30
        elif month.get()=='March' and date.get()==30:
            glob.title('March_30')
            my_conn.execute("SELECT * FROM march_30")
            i=0
            for march_30 in my_conn: 
                for j in range(len(march_30)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_30[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #March_31
        elif month.get()=='March' and date.get()==31:
            glob.title('March_31')
            my_conn.execute("SELECT * FROM march_31")
            i=0
            for march_31 in my_conn: 
                for j in range(len(march_31)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, march_31[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1


        #April_1
        elif month.get()=='April' and date.get()==1:
            glob.title('April_1')
            my_conn.execute("SELECT * FROM april_1")
            i=0
            for april_1 in my_conn: 
                for j in range(len(april_1)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_1[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_2
        elif month.get()=='April' and date.get()==2:
            glob.title('April_2')
            my_conn.execute("SELECT * FROM april_2")
            i=0
            for april_2 in my_conn: 
                for j in range(len(april_2)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_2[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_3
        elif month.get()=='April' and date.get()==3:
            glob.title('April_3')
            my_conn.execute("SELECT * FROM april_3")
            i=0
            for april_3 in my_conn: 
                for j in range(len(april_3)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_3[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_4
        elif month.get()=='April' and date.get()==4:
            glob.title('April_4')
            my_conn.execute("SELECT * FROM april_4")
            i=0
            for april_4 in my_conn: 
                for j in range(len(april_4)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_4[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_5
        elif month.get()=='April' and date.get()==5:
            glob.title('April_5')
            my_conn.execute("SELECT * FROM april_5")
            i=0
            for april_5 in my_conn: 
                for j in range(len(april_5)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_5[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_6
        elif month.get()=='April' and date.get()==6:
            glob.title('April_6')
            my_conn.execute("SELECT * FROM april_6")
            i=0
            for april_6 in my_conn: 
                for j in range(len(april_6)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_6[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_7
        elif month.get()=='April' and date.get()==7:
            glob.title('April_7')
            my_conn.execute("SELECT * FROM april_7")
            i=0
            for april_7 in my_conn: 
                for j in range(len(april_7)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_7[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_8
        elif month.get()=='April' and date.get()==8:
            glob.title('April_8')
            my_conn.execute("SELECT * FROM april_8")
            i=0
            for april_8 in my_conn: 
                for j in range(len(april_8)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_8[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_9
        elif month.get()=='April' and date.get()==9:
            glob.title('April_9')
            my_conn.execute("SELECT * FROM april_9")
            i=0
            for april_9 in my_conn: 
                for j in range(len(april_9)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_9[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_10
        elif month.get()=='April' and date.get()==10:
            glob.title('April_10')
            my_conn.execute("SELECT * FROM april_10")
            i=0
            for april_10 in my_conn: 
                for j in range(len(april_10)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_10[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_11
        elif month.get()=='April' and date.get()==11:
            glob.title('April_11')
            my_conn.execute("SELECT * FROM april_11")
            i=0
            for april_11 in my_conn: 
                for j in range(len(april_11)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_11[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_12
        elif month.get()=='April' and date.get()==12:
            glob.title('April_12')
            my_conn.execute("SELECT * FROM april_12")
            i=0
            for april_12 in my_conn: 
                for j in range(len(april_12)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_12[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_13
        elif month.get()=='April' and date.get()==13:
            glob.title('April_13')
            my_conn.execute("SELECT * FROM april_13")
            i=0
            for april_13 in my_conn: 
                for j in range(len(april_13)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_13[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_14
        elif month.get()=='April' and date.get()==14:
            glob.title('April_14')
            my_conn.execute("SELECT * FROM april_14")
            i=0
            for april_14 in my_conn: 
                for j in range(len(april_14)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_14[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_15
        elif month.get()=='April' and date.get()==15:
            glob.title('April_15')
            my_conn.execute("SELECT * FROM april_15")
            i=0
            for april_15 in my_conn: 
                for j in range(len(april_15)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_15[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_16
        elif month.get()=='April' and date.get()==16:
            glob.title('April_16')
            my_conn.execute("SELECT * FROM april_16")
            i=0
            for april_16 in my_conn: 
                for j in range(len(april_16)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_16[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_17
        elif month.get()=='April' and date.get()==17:
            glob.title('April_17')
            my_conn.execute("SELECT * FROM april_17")
            i=0
            for april_17 in my_conn: 
                for j in range(len(april_17)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_17[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_18
        elif month.get()=='April' and date.get()==18:
            glob.title('April_18')
            my_conn.execute("SELECT * FROM april_18")
            i=0
            for april_18 in my_conn: 
                for j in range(len(april_18)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_18[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_19
        elif month.get()=='April' and date.get()==19:
            glob.title('April_19')
            my_conn.execute("SELECT * FROM april_19")
            i=0
            for april_19 in my_conn: 
                for j in range(len(april_19)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_19[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_20
        elif month.get()=='April' and date.get()==20:
            glob.title('April_20')
            my_conn.execute("SELECT * FROM april_20")
            i=0
            for april_20 in my_conn: 
                for j in range(len(april_20)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_20[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_21
        elif month.get()=='April' and date.get()==21:
            glob.title('April_21')
            my_conn.execute("SELECT * FROM april_21")
            i=0
            for april_21 in my_conn: 
                for j in range(len(april_21)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_21[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_22
        elif month.get()=='April' and date.get()==22:
            glob.title('April_22')
            my_conn.execute("SELECT * FROM april_22")
            i=0
            for april_22 in my_conn: 
                for j in range(len(april_22)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_22[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_23
        elif month.get()=='April' and date.get()==23:
            glob.title('April_23')
            my_conn.execute("SELECT * FROM april_23")
            i=0
            for april_23 in my_conn: 
                for j in range(len(april_23)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_23[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_24
        elif month.get()=='April' and date.get()==24:
            glob.title('April_24')
            my_conn.execute("SELECT * FROM april_24")
            i=0
            for april_24 in my_conn: 
                for j in range(len(april_24)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_24[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_25
        elif month.get()=='April' and date.get()==25:
            glob.title('April_25')
            my_conn.execute("SELECT * FROM april_25")
            i=0
            for april_25 in my_conn: 
                for j in range(len(april_25)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_25[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_26
        elif month.get()=='April' and date.get()==26:
            glob.title('April_26')
            my_conn.execute("SELECT * FROM april_26")
            i=0
            for april_26 in my_conn: 
                for j in range(len(april_26)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_26[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_27
        elif month.get()=='April' and date.get()==27:
            glob.title('April_27')
            my_conn.execute("SELECT * FROM april_27")
            i=0
            for april_27 in my_conn: 
                for j in range(len(april_27)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_27[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_28
        elif month.get()=='April' and date.get()==28:
            glob.title('April_28')
            my_conn.execute("SELECT * FROM april_28")
            i=0
            for april_28 in my_conn: 
                for j in range(len(april_28)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_28[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_29
        elif month.get()=='April' and date.get()==29:
            glob.title('April_29')
            my_conn.execute("SELECT * FROM april_29")
            i=0
            for april_29 in my_conn: 
                for j in range(len(april_29)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_29[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #April_30
        elif month.get()=='April' and date.get()==30:
            glob.title('April_30')
            my_conn.execute("SELECT * FROM april_30")
            i=0
            for april_30 in my_conn: 
                for j in range(len(april_30)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, april_30[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_1
        elif month.get()=='May' and date.get()==1:
            glob.title('May_1')
            my_conn.execute("SELECT * FROM may_1")
            i=0
            for may_1 in my_conn: 
                for j in range(len(may_1)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_1[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_2
        elif month.get()=='May' and date.get()==2:
            glob.title('May_2')
            my_conn.execute("SELECT * FROM may_2")
            i=0
            for may_2 in my_conn: 
                for j in range(len(may_2)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_2[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_3
        elif month.get()=='May' and date.get()==3:
            glob.title('May_3')
            my_conn.execute("SELECT * FROM may_3")
            i=0
            for may_3 in my_conn: 
                for j in range(len(may_3)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_3[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_4
        elif month.get()=='May' and date.get()==4:
            glob.title('May_4')
            my_conn.execute("SELECT * FROM may_4")
            i=0
            for may_4 in my_conn: 
                for j in range(len(may_4)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_4[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_5
        elif month.get()=='May' and date.get()==5:
            glob.title('May_5')
            my_conn.execute("SELECT * FROM may_5")
            i=0
            for may_5 in my_conn: 
                for j in range(len(may_5)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_5[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_6
        elif month.get()=='May' and date.get()==6:
            glob.title('May_6')
            my_conn.execute("SELECT * FROM may_6")
            i=0
            for may_6 in my_conn: 
                for j in range(len(may_6)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_6[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_7
        elif month.get()=='May' and date.get()==7:
            glob.title('May_7')
            my_conn.execute("SELECT * FROM may_7")
            i=0
            for may_7 in my_conn: 
                for j in range(len(may_7)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_7[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_8
        elif month.get()=='May' and date.get()==8:
            glob.title('May_8')
            my_conn.execute("SELECT * FROM may_8")
            i=0
            for may_8 in my_conn: 
                for j in range(len(may_8)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_8[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_9
        elif month.get()=='May' and date.get()==9:
            glob.title('May_9')
            my_conn.execute("SELECT * FROM may_9")
            i=0
            for may_9 in my_conn: 
                for j in range(len(may_9)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_9[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_10
        elif month.get()=='May' and date.get()==10:
            glob.title('May_10')
            my_conn.execute("SELECT * FROM may_10")
            i=0
            for may_10 in my_conn: 
                for j in range(len(may_10)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_10[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_11
        elif month.get()=='May' and date.get()==11:
            glob.title('May_11')
            my_conn.execute("SELECT * FROM may_11")
            i=0
            for may_11 in my_conn: 
                for j in range(len(may_11)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_11[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_12
        elif month.get()=='May' and date.get()==12:
            glob.title('May_12')
            my_conn.execute("SELECT * FROM may_12")
            i=0
            for may_12 in my_conn: 
                for j in range(len(may_12)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_12[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_13
        elif month.get()=='May' and date.get()==13:
            glob.title('May_13')
            my_conn.execute("SELECT * FROM may_13")
            i=0
            for may_13 in my_conn: 
                for j in range(len(may_13)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_13[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_14
        elif month.get()=='May' and date.get()==14:
            glob.title('May_14')
            my_conn.execute("SELECT * FROM may_14")
            i=0
            for may_14 in my_conn: 
                for j in range(len(may_14)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_14[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_15
        elif month.get()=='May' and date.get()==15:
            glob.title('May_15')
            my_conn.execute("SELECT * FROM may_15")
            i=0
            for may_15 in my_conn: 
                for j in range(len(may_15)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_15[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_16
        elif month.get()=='May' and date.get()==16:
            glob.title('May_16')
            my_conn.execute("SELECT * FROM may_16")
            i=0
            for may_16 in my_conn: 
                for j in range(len(may_16)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_16[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_17
        elif month.get()=='May' and date.get()==17:
            glob.title('May_17')
            my_conn.execute("SELECT * FROM may_17")
            i=0
            for may_17 in my_conn: 
                for j in range(len(may_17)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_17[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1


        #May_18
        elif month.get()=='May' and date.get()==18:
            glob.title('May_18')
            my_conn.execute("SELECT * FROM may_18")
            i=0
            for may_18 in my_conn: 
                for j in range(len(may_18)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_18[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_19
        elif month.get()=='May' and date.get()==19:
            glob.title('May_19')
            my_conn.execute("SELECT * FROM may_19")
            i=0
            for may_19 in my_conn: 
                for j in range(len(may_19)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_19[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_20
        elif month.get()=='May' and date.get()==20:
            glob.title('May_20')
            my_conn.execute("SELECT * FROM may_20")
            i=0
            for may_20 in my_conn: 
                for j in range(len(may_20)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_20[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_21
        elif month.get()=='May' and date.get()==21:
            glob.title('May_21')
            my_conn.execute("SELECT * FROM may_21")
            i=0
            for may_21 in my_conn: 
                for j in range(len(may_21)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_21[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_22
        elif month.get()=='May' and date.get()==22:
            glob.title('May_22')
            my_conn.execute("SELECT * FROM may_22")
            i=0
            for may_22 in my_conn: 
                for j in range(len(may_22)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_22[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_23
        elif month.get()=='May' and date.get()==23:
            glob.title('May_23')
            my_conn.execute("SELECT * FROM may_23")
            i=0
            for may_23 in my_conn: 
                for j in range(len(may_23)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_23[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_24
        elif month.get()=='May' and date.get()==24:
            glob.title('May_24')
            my_conn.execute("SELECT * FROM may_24")
            i=0
            for may_24 in my_conn: 
                for j in range(len(may_24)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_24[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_25
        elif month.get()=='May' and date.get()==25:
            glob.title('May_25')
            my_conn.execute("SELECT * FROM may_25")
            i=0
            for may_25 in my_conn: 
                for j in range(len(may_25)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_25[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_26
        elif month.get()=='May' and date.get()==26:
            glob.title('May_26')
            my_conn.execute("SELECT * FROM may_26")
            i=0
            for may_26 in my_conn: 
                for j in range(len(may_26)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_26[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_27
        elif month.get()=='May' and date.get()==27:
            glob.title('May_27')
            my_conn.execute("SELECT * FROM may_27")
            i=0
            for may_27 in my_conn: 
                for j in range(len(may_27)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_27[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_28
        elif month.get()=='May' and date.get()==28:
            glob.title('May_28')
            my_conn.execute("SELECT * FROM may_28")
            i=0
            for may_28 in my_conn: 
                for j in range(len(may_28)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_28[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_29
        elif month.get()=='May' and date.get()==29:
            glob.title('May_29')
            my_conn.execute("SELECT * FROM may_29")
            i=0
            for may_29 in my_conn: 
                for j in range(len(may_29)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_29[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_30
        elif month.get()=='May' and date.get()==30:
            glob.title('May_30')
            my_conn.execute("SELECT * FROM may_30")
            i=0
            for may_30 in my_conn: 
                for j in range(len(may_30)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_30[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #May_31
        elif month.get()=='May' and date.get()==31:
            glob.title('May_31')
            my_conn.execute("SELECT * FROM may_31")
            i=0
            for may_31 in my_conn: 
                for j in range(len(may_31)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, may_31[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1


        #June_1
        elif month.get()=='June' and date.get()==1:
            glob.title('June_1')
            my_conn.execute("SELECT * FROM june_1")
            i=0
            for june_1 in my_conn: 
                for j in range(len(june_1)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_1[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_2
        elif month.get()=='June' and date.get()==2:
            glob.title('June_2')
            my_conn.execute("SELECT * FROM june_2")
            i=0
            for june_2 in my_conn: 
                for j in range(len(june_2)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_2[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_3
        elif month.get()=='June' and date.get()==3:
            glob.title('June_3')
            my_conn.execute("SELECT * FROM june_3")
            i=0
            for june_3 in my_conn: 
                for j in range(len(june_3)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_3[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_4
        elif month.get()=='June' and date.get()==4:
            glob.title('June_4')
            my_conn.execute("SELECT * FROM june_4")
            i=0
            for june_4 in my_conn: 
                for j in range(len(june_4)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_4[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1
        #June_5
        elif month.get()=='June' and date.get()==5:
            glob.title('June_5')
            my_conn.execute("SELECT * FROM june_5")
            i=0
            for june_5 in my_conn: 
                for j in range(len(june_5)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_5[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_6
        elif month.get()=='June' and date.get()==6:
            glob.title('June_6')
            my_conn.execute("SELECT * FROM june_6")
            i=0
            for june_6 in my_conn: 
                for j in range(len(june_6)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_6[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_7
        elif month.get()=='June' and date.get()==7:
            glob.title('June_7')
            my_conn.execute("SELECT * FROM june_7")
            i=0
            for june_7 in my_conn: 
                for j in range(len(june_7)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_7[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_8
        elif month.get()=='June' and date.get()==8:
            glob.title('June_8')
            my_conn.execute("SELECT * FROM june_8")
            i=0
            for june_8 in my_conn: 
                for j in range(len(june_8)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_8[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_9
        elif month.get()=='June' and date.get()==9:
            glob.title('June_9')
            my_conn.execute("SELECT * FROM june_9")
            i=0
            for june_9 in my_conn: 
                for j in range(len(june_9)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_9[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_10
        elif month.get()=='June' and date.get()==10:
            glob.title('June_10')
            my_conn.execute("SELECT * FROM june_10")
            i=0
            for june_10 in my_conn: 
                for j in range(len(june_10)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_10[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_11
        elif month.get()=='June' and date.get()==11:
            glob.title('June_11')
            my_conn.execute("SELECT * FROM june_11")
            i=0
            for june_11 in my_conn: 
                for j in range(len(june_11)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_11[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_12
        elif month.get()=='June' and date.get()==12:
            glob.title('June_12')
            my_conn.execute("SELECT * FROM june_12")
            i=0
            for june_12 in my_conn: 
                for j in range(len(june_12)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_12[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_13
        elif month.get()=='June' and date.get()==13:
            glob.title('June_13')
            my_conn.execute("SELECT * FROM june_13")
            i=0
            for june_13 in my_conn: 
                for j in range(len(june_13)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_13[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_14
        elif month.get()=='June' and date.get()==14:
            glob.title('June_14')
            my_conn.execute("SELECT * FROM june_14")
            i=0
            for june_14 in my_conn: 
                for j in range(len(june_14)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_14[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_15
        elif month.get()=='June' and date.get()==15:
            glob.title('June_15')
            my_conn.execute("SELECT * FROM june_15")
            i=0
            for june_15 in my_conn: 
                for j in range(len(june_15)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_15[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_16
        elif month.get()=='June' and date.get()==16:
            glob.title('June_16')
            my_conn.execute("SELECT * FROM june_16")
            i=0
            for june_16 in my_conn: 
                for j in range(len(june_16)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_16[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_17
        elif month.get()=='June' and date.get()==17:
            glob.title('June_17')
            my_conn.execute("SELECT * FROM june_17")
            i=0
            for june_17 in my_conn: 
                for j in range(len(june_17)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_17[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_18
        elif month.get()=='June' and date.get()==18:
            glob.title('June_18')
            my_conn.execute("SELECT * FROM june_18")
            i=0
            for june_18 in my_conn: 
                for j in range(len(june_18)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_18[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_19
        elif month.get()=='June' and date.get()==19:
            glob.title('June_19')
            my_conn.execute("SELECT * FROM june_19")
            i=0
            for june_19 in my_conn: 
                for j in range(len(june_19)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_19[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_20
        elif month.get()=='June' and date.get()==20:
            glob.title('June_20')
            my_conn.execute("SELECT * FROM june_20")
            i=0
            for june_20 in my_conn: 
                for j in range(len(june_20)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_20[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_21
        elif month.get()=='June' and date.get()==21:
            glob.title('June_21')
            my_conn.execute("SELECT * FROM june_21")
            i=0
            for june_21 in my_conn: 
                for j in range(len(june_21)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_21[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_22
        elif month.get()=='June' and date.get()==22:
            glob.title('June_22')
            my_conn.execute("SELECT * FROM june_22")
            i=0
            for june_22 in my_conn: 
                for j in range(len(june_22)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_22[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_23
        elif month.get()=='June' and date.get()==23:
            glob.title('June_23')
            my_conn.execute("SELECT * FROM june_23")
            i=0
            for june_23 in my_conn: 
                for j in range(len(june_23)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_23[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_24
        elif month.get()=='June' and date.get()==24:
            glob.title('June_24')
            my_conn.execute("SELECT * FROM june_24")
            i=0
            for june_24 in my_conn: 
                for j in range(len(june_24)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_24[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_25
        elif month.get()=='June' and date.get()==25:
            glob.title('June_25')
            my_conn.execute("SELECT * FROM june_25")
            i=0
            for june_25 in my_conn: 
                for j in range(len(june_25)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_25[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_26
        elif month.get()=='June' and date.get()==26:
            glob.title('June_26')
            my_conn.execute("SELECT * FROM june_26")
            i=0
            for june_26 in my_conn: 
                for j in range(len(june_26)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_26[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_27
        elif month.get()=='June' and date.get()==27:
            glob.title('June_27')
            my_conn.execute("SELECT * FROM june_27")
            i=0
            for june_27 in my_conn: 
                for j in range(len(june_27)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_27[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_28
        elif month.get()=='June' and date.get()==28:
            glob.title('June_28')
            my_conn.execute("SELECT * FROM june_28")
            i=0
            for june_28 in my_conn: 
                for j in range(len(june_28)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_28[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_29
        elif month.get()=='June' and date.get()==29:
            glob.title('June_29')
            my_conn.execute("SELECT * FROM june_29")
            i=0
            for june_29 in my_conn: 
                for j in range(len(june_29)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_29[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #June_30
        elif month.get()=='June' and date.get()==30:
            glob.title('June_30')
            my_conn.execute("SELECT * FROM june_30")
            i=0
            for june_30 in my_conn: 
                for j in range(len(june_30)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, june_30[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_1
        elif month.get()=='July' and date.get()==1:
            glob.title('July_1')
            my_conn.execute("SELECT * FROM july_1")
            i=0
            for july_1 in my_conn: 
                for j in range(len(july_1)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_1[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_2
        elif month.get()=='July' and date.get()==2:
            glob.title('July_2')
            my_conn.execute("SELECT * FROM july_2")
            i=0
            for july_2 in my_conn: 
                for j in range(len(july_2)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_2[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_3
        elif month.get()=='July' and date.get()==3:
            glob.title('July_3')
            my_conn.execute("SELECT * FROM july_3")
            i=0
            for july_3 in my_conn: 
                for j in range(len(july_3)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_3[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_4
        elif month.get()=='July' and date.get()==4:
            glob.title('July_4')
            my_conn.execute("SELECT * FROM july_4")
            i=0
            for july_4 in my_conn: 
                for j in range(len(july_4)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_4[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_5
        elif month.get()=='July' and date.get()==5:
            glob.title('July_5')
            my_conn.execute("SELECT * FROM july_5")
            i=0
            for july_5 in my_conn: 
                for j in range(len(july_5)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_5[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_6
        elif month.get()=='July' and date.get()==6:
            glob.title('July_6')
            my_conn.execute("SELECT * FROM july_6")
            i=0
            for july_6 in my_conn: 
                for j in range(len(july_6)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_6[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_7
        elif month.get()=='July' and date.get()==7:
            glob.title('July_7')
            my_conn.execute("SELECT * FROM july_7")
            i=0
            for july_7 in my_conn: 
                for j in range(len(july_7)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_7[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_8
        elif month.get()=='July' and date.get()==8:
            glob.title('July_8')
            my_conn.execute("SELECT * FROM july_8")
            i=0
            for july_8 in my_conn: 
                for j in range(len(july_8)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_8[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_9
        elif month.get()=='July' and date.get()==9:
            glob.title('July_9')
            my_conn.execute("SELECT * FROM july_9")
            i=0
            for july_9 in my_conn: 
                for j in range(len(july_9)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_9[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_10
        elif month.get()=='July' and date.get()==10:
            glob.title('July_10')
            my_conn.execute("SELECT * FROM july_10")
            i=0
            for july_10 in my_conn: 
                for j in range(len(july_10)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_10[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_11
        elif month.get()=='July' and date.get()==11:
            glob.title('July_11')
            my_conn.execute("SELECT * FROM july_11")
            i=0
            for july_11 in my_conn: 
                for j in range(len(july_11)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_11[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_12
        elif month.get()=='July' and date.get()==12:
            glob.title('July_12')
            my_conn.execute("SELECT * FROM july_12")
            i=0
            for july_12 in my_conn: 
                for j in range(len(july_12)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_12[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_13
        elif month.get()=='July' and date.get()==13:
            glob.title('July_13')
            my_conn.execute("SELECT * FROM july_13")
            i=0
            for july_13 in my_conn: 
                for j in range(len(july_13)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_13[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_14
        elif month.get()=='July' and date.get()==14:
            glob.title('July_14')
            my_conn.execute("SELECT * FROM july_14")
            i=0
            for july_14 in my_conn: 
                for j in range(len(july_14)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_14[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_15
        elif month.get()=='July' and date.get()==15:
            glob.title('July_15')
            my_conn.execute("SELECT * FROM july_15")
            i=0
            for july_15 in my_conn: 
                for j in range(len(july_15)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_15[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_16
        elif month.get()=='July' and date.get()==16:
            glob.title('July_16')
            my_conn.execute("SELECT * FROM july_16")
            i=0
            for july_16 in my_conn: 
                for j in range(len(july_16)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_16[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_17
        elif month.get()=='July' and date.get()==17:
            glob.title('July_17')
            my_conn.execute("SELECT * FROM july_17")
            i=0
            for july_17 in my_conn: 
                for j in range(len(july_17)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_17[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_18
        elif month.get()=='July' and date.get()==18:
            glob.title('July_18')
            my_conn.execute("SELECT * FROM july_18")
            i=0
            for july_18 in my_conn: 
                for j in range(len(july_18)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_18[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_19
        elif month.get()=='July' and date.get()==19:
            glob.title('July_19')
            my_conn.execute("SELECT * FROM july_19")
            i=0
            for july_19 in my_conn: 
                for j in range(len(july_19)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_19[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_20
        elif month.get()=='July' and date.get()==20:
            glob.title('July_20')
            my_conn.execute("SELECT * FROM july_20")
            i=0
            for july_20 in my_conn: 
                for j in range(len(july_20)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_20[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_21
        elif month.get()=='July' and date.get()==21:
            glob.title('July_21')
            my_conn.execute("SELECT * FROM july_21")
            i=0
            for july_21 in my_conn: 
                for j in range(len(july_21)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_21[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_22
        elif month.get()=='July' and date.get()==22:
            glob.title('July_22')
            my_conn.execute("SELECT * FROM july_22")
            i=0
            for july_22 in my_conn: 
                for j in range(len(july_22)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_22[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_23
        elif month.get()=='July' and date.get()==23:
            glob.title('July_23')
            my_conn.execute("SELECT * FROM july_23")
            i=0
            for july_23 in my_conn: 
                for j in range(len(july_23)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_23[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_24
        elif month.get()=='July' and date.get()==24:
            glob.title('July_24')
            my_conn.execute("SELECT * FROM july_24")
            i=0
            for july_24 in my_conn: 
                for j in range(len(july_24)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_24[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_25
        elif month.get()=='July' and date.get()==25:
            glob.title('July_25')
            my_conn.execute("SELECT * FROM july_25")
            i=0
            for july_25 in my_conn: 
                for j in range(len(july_25)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_25[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_26
        elif month.get()=='July' and date.get()==26:
            glob.title('July_26')
            my_conn.execute("SELECT * FROM july_26")
            i=0
            for july_26 in my_conn: 
                for j in range(len(july_26)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_26[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_27
        elif month.get()=='July' and date.get()==27:
            glob.title('July_27')
            my_conn.execute("SELECT * FROM july_27")
            i=0
            for july_27 in my_conn: 
                for j in range(len(july_27)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_27[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_28
        elif month.get()=='July' and date.get()==28:
            glob.title('July_28')
            my_conn.execute("SELECT * FROM july_28")
            i=0
            for july_28 in my_conn: 
                for j in range(len(july_28)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_28[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_29
        elif month.get()=='July' and date.get()==29:
            glob.title('July_29')
            my_conn.execute("SELECT * FROM july_29")
            i=0
            for july_29 in my_conn: 
                for j in range(len(july_29)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_29[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_30
        elif month.get()=='July' and date.get()==30:
            glob.title('July_30')
            my_conn.execute("SELECT * FROM july_30")
            i=0
            for july_30 in my_conn: 
                for j in range(len(july_30)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_30[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #July_31
        elif month.get()=='July' and date.get()==31:
            glob.title('July_31')
            my_conn.execute("SELECT * FROM july_31")
            i=0
            for july_31 in my_conn: 
                for j in range(len(july_31)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, july_31[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_1
        elif month.get()=='August' and date.get()==1:
            glob.title('August_1')
            my_conn.execute("SELECT * FROM august_1")
            i=0
            for august_1 in my_conn: 
                for j in range(len(august_1)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_1[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_2
        elif month.get()=='August' and date.get()==2:
            glob.title('August_2')
            my_conn.execute("SELECT * FROM august_2")
            i=0
            for august_2 in my_conn: 
                for j in range(len(august_2)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_2[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_3
        elif month.get()=='August' and date.get()==3:
            glob.title('August_3')
            my_conn.execute("SELECT * FROM august_3")
            i=0
            for august_3 in my_conn: 
                for j in range(len(august_3)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_3[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_4
        elif month.get()=='August' and date.get()==4:
            glob.title('August_4')
            my_conn.execute("SELECT * FROM august_4")
            i=0
            for august_4 in my_conn: 
                for j in range(len(august_4)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_4[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_5
        elif month.get()=='August' and date.get()==5:
            glob.title('August_5')
            my_conn.execute("SELECT * FROM august_5")
            i=0
            for august_5 in my_conn: 
                for j in range(len(august_5)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_5[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_6
        elif month.get()=='August' and date.get()==6:
            glob.title('August_6')
            my_conn.execute("SELECT * FROM august_6")
            i=0
            for august_6 in my_conn: 
                for j in range(len(august_6)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_6[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_7
        elif month.get()=='August' and date.get()==7:
            glob.title('August_7')
            my_conn.execute("SELECT * FROM august_7")
            i=0
            for august_7 in my_conn: 
                for j in range(len(august_7)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_7[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_8
        elif month.get()=='August' and date.get()==8:
            glob.title('August_8')
            my_conn.execute("SELECT * FROM august_8")
            i=0
            for august_8 in my_conn: 
                for j in range(len(august_8)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_8[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_9
        elif month.get()=='August' and date.get()==9:
            glob.title('August_9')
            my_conn.execute("SELECT * FROM august_9")
            i=0
            for august_9 in my_conn: 
                for j in range(len(august_9)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_9[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_10
        elif month.get()=='August' and date.get()==10:
            glob.title('August_10')
            my_conn.execute("SELECT * FROM august_10")
            i=0
            for august_10 in my_conn: 
                for j in range(len(august_10)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_10[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_11
        elif month.get()=='August' and date.get()==11:
            glob.title('August_11')
            my_conn.execute("SELECT * FROM august_11")
            i=0
            for august_11 in my_conn: 
                for j in range(len(august_11)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_11[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_12
        elif month.get()=='August' and date.get()==12:
            glob.title('August_12')
            my_conn.execute("SELECT * FROM august_12")
            i=0
            for august_12 in my_conn: 
                for j in range(len(august_12)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_12[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_13
        elif month.get()=='August' and date.get()==13:
            glob.title('August_13')
            my_conn.execute("SELECT * FROM august_13")
            i=0
            for august_13 in my_conn: 
                for j in range(len(august_13)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_13[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_14
        elif month.get()=='August' and date.get()==14:
            glob.title('August_14')
            my_conn.execute("SELECT * FROM august_14")
            i=0
            for august_14 in my_conn: 
                for j in range(len(august_14)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_14[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_15
        elif month.get()=='August' and date.get()==15:
            glob.title('August_15')
            my_conn.execute("SELECT * FROM august_15")
            i=0
            for august_15 in my_conn: 
                for j in range(len(august_15)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_15[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_16
        elif month.get()=='August' and date.get()==16:
            glob.title('August_16')
            my_conn.execute("SELECT * FROM august_16")
            i=0
            for august_16 in my_conn: 
                for j in range(len(august_16)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_16[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_17
        elif month.get()=='August' and date.get()==17:
            glob.title('August_17')
            my_conn.execute("SELECT * FROM august_17")
            i=0
            for august_17 in my_conn: 
                for j in range(len(august_17)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_17[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_18
        elif month.get()=='August' and date.get()==18:
            glob.title('August_18')
            my_conn.execute("SELECT * FROM august_18")
            i=0
            for august_18 in my_conn: 
                for j in range(len(august_18)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_18[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1
                
        #August_19
        elif month.get()=='August' and date.get()==19:
            glob.title('August_19')
            my_conn.execute("SELECT * FROM august_19")
            i=0
            for august_19 in my_conn: 
                for j in range(len(august_19)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_19[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_20
        elif month.get()=='August' and date.get()==20:
            glob.title('August_20')
            my_conn.execute("SELECT * FROM august_20")
            i=0
            for august_20 in my_conn: 
                for j in range(len(august_20)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_20[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_21
        elif month.get()=='August' and date.get()==21:
            glob.title('August_21')
            my_conn.execute("SELECT * FROM august_21")
            i=0
            for august_21 in my_conn: 
                for j in range(len(august_21)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_21[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_22
        elif month.get()=='August' and date.get()==22:
            glob.title('August_22')
            my_conn.execute("SELECT * FROM august_22")
            i=0
            for august_22 in my_conn: 
                for j in range(len(august_22)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_22[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_23
        elif month.get()=='August' and date.get()==23:
            glob.title('August_23')
            my_conn.execute("SELECT * FROM august_23")
            i=0
            for august_23 in my_conn: 
                for j in range(len(august_23)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_23[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_24
        elif month.get()=='August' and date.get()==24:
            glob.title('August_24')
            my_conn.execute("SELECT * FROM august_24")
            i=0
            for august_24 in my_conn: 
                for j in range(len(august_24)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_24[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_25
        elif month.get()=='August' and date.get()==25:
            glob.title('August_25')
            my_conn.execute("SELECT * FROM august_25")
            i=0
            for august_25 in my_conn: 
                for j in range(len(august_25)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_25[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_26
        elif month.get()=='August' and date.get()==26:
            glob.title('August_26')
            my_conn.execute("SELECT * FROM august_26")
            i=0
            for august_26 in my_conn: 
                for j in range(len(august_26)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_26[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_27
        elif month.get()=='August' and date.get()==27:
            glob.title('August_27')
            my_conn.execute("SELECT * FROM august_27")
            i=0
            for august_27 in my_conn: 
                for j in range(len(august_27)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_27[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_28
        elif month.get()=='August' and date.get()==28:
            glob.title('August_28')
            my_conn.execute("SELECT * FROM august_28")
            i=0
            for august_28 in my_conn: 
                for j in range(len(august_28)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_28[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_29
        elif month.get()=='August' and date.get()==29:
            glob.title('August_29')
            my_conn.execute("SELECT * FROM august_29")
            i=0
            for august_29 in my_conn: 
                for j in range(len(august_29)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_29[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_30
        elif month.get()=='August' and date.get()==30:
            glob.title('August_30')
            my_conn.execute("SELECT * FROM august_30")
            i=0
            for august_30 in my_conn: 
                for j in range(len(august_30)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_30[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #August_31
        elif month.get()=='August' and date.get()==31:
            glob.title('August_31')
            my_conn.execute("SELECT * FROM august_31")
            i=0
            for august_31 in my_conn: 
                for j in range(len(august_31)):
                    e = Entry(glob, width=16, fg='blue', font=('verdana',18,'bold'),bd=3) 
                    e.grid(row=i, column=j, pady=20) 
                    e.insert(END, august_31[j])
                    if i==0:
                        e.configure(state=DISABLED,disabledforeground='#ffa31a',disabledbackground='black')
                    else :
                        e.configure(state=DISABLED,disabledforeground='green2',disabledbackground='black')
                i=i+1

        #default entry
        elif (month.get()=='Select Month' or date.get()=='Select Date') or (month.get()=='Select Month' and date.get()=='Select Date'):
            popup = messagebox.showerror('Error','Please select valid Month/Date.')

        # Any other date
        else:
            webbrowser.open_new("https://www.worldometers.info/coronavirus/")
            glob.destroy()
            #popup = messagebox.showerror('Error','Sorry! Information not available.')
            #glob.destroy()

        glob.mainloop()
        

    date = IntVar()
    month = StringVar()

    date.set('Select Date')
    month.set('Select Month')

    heading = Label(globe, text='Journy Across The Globe', font=('forte',50),  bg='black', fg='white')
    empty = Label(globe, text='', font=('forte',15),  bg='black', fg='white')
    l1 = Label(globe, text='Coronavirus is not a danger only for India, it has its affect on whole world. It has became a dangerous', font=('monotype corsiva',27),  bg='black', fg='cyan')
    l2 = Label(globe, text='Pandemic for the Earth. The virus originated from a laboratry in China and startedspreading in China.', font=('monotype corsiva',27),  bg='black', fg='cyan')
    l3 = Label(globe, text='After that, its worst condition initiated in many countries like Brazil,United States of America, Italy', font=('monotype corsiva',27),  bg='black', fg='cyan')
    l4 = Label(globe, text='and many more other countries including India. We are trying this pandemic but till now (September 2020)', font=('monotype corsiva',27),  bg='black', fg='cyan')
    l5 = Label(globe, text='none of the countries had been successful in making the vaccinal or medicinal cure for the disease. To', font=('monotype corsiva',27),  bg='black', fg='cyan')
    l6 = Label(globe, text='date, there are nospecific vaccines or medicines for COVID-19.The treatments are under investigation, and', font=('monotype corsiva',27),  bg='black', fg='cyan')
    l7 = Label(globe, text='will be tested through clinical trials.', font=('monotype corsiva',27),  bg='black', fg='cyan')


    frame = LabelFrame(globe, text='More Information : ', bg='#00e6e6', bd=20, font=('forte',30), fg='#0039e6')

    month_dd = OptionMenu(frame, month,'January','February','March','April','May','June','July','August','September','October','November','December')
    date_dd = OptionMenu(frame, date,'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
    get = Button(frame, text='Get Information', command=dates,font=('forte',15),bg='yellow',fg='red')

    month_dd.configure(font=('forte',20),bg='#80ffff',fg='#0039e6')
    date_dd.configure(font=('forte',20),bg='#80ffff',fg='#0039e6')


    heading.grid(row=0,column=0)
    empty.grid(row=1,column=0)
    l1.grid(row=2,column=0)
    l2.grid(row=3,column=0)
    l3.grid(row=4,column=0)
    l4.grid(row=5,column=0)
    l5.grid(row=6,column=0)
    l6.grid(row=7,column=0)
    l7.grid(row=8,column=0)
    frame.grid(row=9,column=0,pady=30)
    month_dd.grid(row=0,column=0,padx=20,pady=10)
    date_dd.grid(row=0,column=1,padx=20,pady=10)
    get.grid(row=1,column=0,columnspan=2,pady=20)

    def back():
        globe.destroy()
    end = Button(globe, text='< Back', font=('',10),command=back).place(x=15,y=15)
            
    globe.mainloop()



def prevention():
    prev = Toplevel()
    prev.configure(bg='lightcyan')
    prev.title('Prevention from Coronavirus')
    prev.geometry('10000x10000')


    def community_precautions():
        precautions=Toplevel()
        precautions.configure(bg='hot pink')
        precautions.geometry('2000x2000')
        
        
        line1=Label(precautions,text='Obstructions to Community Spread',font=('MS Sherrif', 32,'bold italic underline'),bg='hot pink',fg='Olive Drab1')
        line1.grid(row=0,column=1,columnspan=2,sticky=W)
        
        line2=Label(precautions,text='',bg='hot pink')
        line2.grid(row=1,column=1)
        
        line3=Label(precautions,text='1. Sanitation:-',bg='hot pink',fg='dark violet',font=('MS Sherrif', 26, 'bold italic'))
        line3.grid(row=2,column=1,sticky=W,columnspan=2)
        
        line4=Label(precautions,text='Commonly touched surfaces like handrails etc are more likely sources', bg='hot pink', font=('MS Sherrif',16,' bold italic'),fg='dark violet')
        line4.grid(row=3,column=1,columnspan=2,sticky=W)
        
        line5=Label(precautions,text='of infection but spraying disinfactant into the air will have the effect of', bg='hot pink', font=('MS Sherrif',16,' bold italic'),fg='dark violet')
        line5.grid(row=4,column=1,columnspan=2,sticky=W)
        
        line6=Label(precautions,text='reducing the amount of virus that is suspended as aerosols.', bg='hot pink', font=('MS Sherrif',16,' bold italic'),fg='dark violet')
        line6.grid(row=5,column=1,columnspan=2,sticky=W)
        
        image1=ImageTk.PhotoImage(Image.open('prevention1.jpg'))
        image1_label=Label(precautions,image=image1,bg='hot pink')
        image1_label.grid(row=2,column=0,rowspan=5, padx=30)
        
        image2=ImageTk.PhotoImage(Image.open('prevention2.jpg'))
        image2_label=Label(precautions,image=image2,bg='hot pink')
        image2_label.grid(row=2,column=4,rowspan=5,sticky=W,padx=25)
        
        line7=Label(precautions, text='2. Lockdown:-',bg='hot pink',fg='dark violet',font=('MS Sherrif', 26, 'bold italic'))
        line7.grid(row=7,column=1,sticky=W,columnspan=2)
        
        line8=Label(precautions,text='Nationwide lockdown in India was imposed on 25TH March,1616 for 21',bg='hot pink',fg='dark violet',font=('MS Sherrif',16,'bold italic'))
        line8.grid(row=8,column=1,columnspan=2,sticky=W)
        
        line9=Label(precautions,text='which kept on extending till now on weekends as a preventive measure',bg='hot pink',fg='dark violet',font=('MS Sherrif', 16, 'bold italic'))
        line9.grid(row=9,column=1,columnspan=2,sticky=W)
        
        line10=Label(precautions, text='against Novel Corona Virus(COVID-16).The lockdown restricted people',bg='hot pink',fg='dark violet',font=('MS Sherrif', 16, 'bold italic'))
        line10.grid(row=10,column=1,columnspan=2,sticky=W)
        
        line11=Label(precautions, text='from stepping out of their homes. All transport services–road,air and',bg='hot pink',fg='dark violet',font=('MS Sherrif', 16, 'bold italic'))
        line11.grid(row=11,column=1,columnspan=2,sticky=W)
        
        line12=Label(precautions, text='rail–were suspended, with exceptions for transportation of essential',bg='hot pink',fg='dark violet',font=('MS Sherrif', 16, 'bold italic'))
        line12.grid(row=12,column=1,columnspan=2,sticky=W)
        
        line13=Label(precautions, text='goods, fire, police and emergency services. Also educational institutes,',bg='hot pink',fg='dark violet',font=('MS Sherrif', 16, 'bold italic'))
        line13.grid(row=13,column=1,columnspan=2,sticky=W)
        
        line14=Label(precautions, text='gyms, parks, malls, theatres etc were prohibited from opening.',bg='hot pink',fg='dark violet',font=('MS Sherrif', 16, 'bold italic'))
        line14.grid(row=14,column=1,columnspan=2,sticky=W)
        
        line15=Label(precautions,text='',bg='hot pink')
        line15.grid(row=6,column=1)
        
        image3=ImageTk.PhotoImage(Image.open('prevention3.jpg'))
        image3_label=Label(precautions,image=image3,bg='hot pink')
        image3_label.grid(row=7,column=0,rowspan=8,padx=25)
        
        image4=ImageTk.PhotoImage(Image.open('prevention4.jpg'))
        image4_label=Label(precautions,image=image4,bg='hot pink')
        image4_label.grid(row=7,column=4,rowspan=8,padx=25)
        
        line16=Label(precautions,text='',bg='hot pink')
        line16.grid(row=15,column=1)
        
        line17=Label(precautions,text='3. Thermal Screening:-',bg='hot pink',fg='dark violet',font=('MS Sherrif', 26, 'bold italic'))
        line17.grid(row=16,column=1,sticky=W,columnspan=2)
        
        line18=Label(precautions,text='Thermal imaging systems generally have been adopted to accurately',bg='hot pink',fg='dark violet',font=('MS Sherrif', 16, 'bold italic'))
        line18.grid(row=17,column=1,sticky=W,columnspan=2)
        
        line19=Label(precautions,text='measure someone’s surface skin temperature without being physically',bg='hot pink',fg='dark violet',font=('MS Sherrif', 16, 'bold italic'))
        line19.grid(row=18,column=1,sticky=W,columnspan=2)
        
        line20=Label(precautions,text='close to the person being evaluated. If someone has a fever, thermal',bg='hot pink',fg='dark violet',font=('MS Sherrif', 16, 'bold italic'))
        line20.grid(row=19,column=1,sticky=W,columnspan=2)
        
        line21=Label(precautions,text='screening will allow to detect them and they can further be tested for',bg='hot pink',fg='dark violet',font=('MS Sherrif', 16, 'bold italic'))
        line21.grid(row=20,column=1,sticky=W,columnspan=2)
        
        line22=Label(precautions,text='coronavirus.',bg='hot pink',fg='dark violet',font=('MS Sherrif', 16, 'bold italic'))
        line22.grid(row=21,column=1,sticky=W,columnspan=2)
        
        image5=ImageTk.PhotoImage(Image.open('prevention5.jpg'))
        image5_label=Label(precautions,image=image5,bg='hot pink')
        image5_label.grid(row=16,column=0,rowspan=5, padx=30)
        
        image6=ImageTk.PhotoImage(Image.open('prevention6.jpg'))
        image6_label=Label(precautions,image=image6,bg='hot pink')
        image6_label.grid(row=16,column=4,rowspan=5)

        def back():
            precautions.destroy()
        end = Button(precautions, text='< Back', font=('',10),command=back).place(x=15,y=15)
        
        precautions.mainloop()

        
    def individual_precautions():
        prevention=Toplevel()
        prevention.title("Prevention")
        prevention.configure(bg="hot pink")

        heading=Label(prevention,text="As an individual",font=("elephant",35,'underline'),fg="Olive Drab1",bg="hot pink").grid(row=0,column=1, padx=180)
        empty1=Label(prevention,text='',padx=100,bg='hot pink').grid(row=0,column=0)
        empty2=Label(prevention,text='',padx=50,bg='hot pink').grid(row=0,column=3)

        #step1
        image1=ImageTk.PhotoImage(Image.open('blue-1.png'))
        image1_label=Label(prevention,image=image1, height=180).grid(row=1,column=0,rowspan=6,sticky=W, padx=20)
        text1=Label(prevention,text="1.Wash Your Hands Often:",font=('Times New Roman',20),bg='hot pink',fg="dark violet").grid(row=1,column=1,sticky=W,columnspan=2)
        text1=Label(prevention,text="Wash your hands often with soap and water for at least 20 seconds especially after you have",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=2,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="been in a public place, or after blowing your nose, coughing,coughing,or sneezing.If soap and",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=3,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="water are not readily available, use a hand sanitizer that contains t least 60% alcohol .Cover",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=4,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="all surfaces of your hands and rub them  together  until they feel dry.Do avoid touching your eyes,",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=5,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="nose, and mouth with unwashed hands.",font=('MS Sherrif',14),bg='hot pink',fg='dark violet').grid(row=6,column=1,columnspan=2,sticky=W)
        image2=ImageTk.PhotoImage(Image.open('images(1123).JPG'))
        image2_label=Label(prevention,image=image2,height=180).grid(row=1,column=3,rowspan=6)

        #step2
        image3=ImageTk.PhotoImage(Image.open('images (112).JPG'))
        image3_label=Label(prevention,image=image3).grid(row=7,column=0,rowspan=6,sticky=W, pady=10,padx=10)
        text1=Label(prevention,text="2.Avoid close contact:",font=('Times New Roman',20),bg='hot pink',fg="green").grid(row=7,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="*INSIDE YOUR HOME: Avoid close contact with people who are sick.If possible, maintain 6  ",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=8,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="feet between the person who is sick and other household members.",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=9,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="*OUTSIDE YOUR HOME: Put 6 feet of distance between yourself and people who don’t live  ",font=('MS Sherrif',14),fg="dark violet",bg='hot pink').grid(row=10,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="in.your household.Try to avoid physical contacts as much as possible.Keeping distance ",font=('MS Sherrif',14),fg="dark violet",bg='hot pink').grid(row=11,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="from others is especially important for people who are at higher risk of getting very sick.",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=12,column=1,columnspan=2,sticky=W)
        image4=ImageTk.PhotoImage(Image.open('social-distancing-6ft-1080x1080.jpg'))
        image4_label=Label(prevention,image=image4).grid(row=7,column=3,rowspan=6)

        #step3
        image5=ImageTk.PhotoImage(Image.open('Advisory-on-Masks-ENG-min-845x321.jpg'))
        image5_label=Label(prevention,image=image5, height=190).grid(row=13,column=0,rowspan=6,sticky=W,padx=20)
        text1=Label(prevention,text="3.Cover your mouth and nose with a mask when around others :",font=('Times New Roman',20),bg='hot pink',fg="green").grid(row=13,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="The mask is meant to protect other people in case you are infected.Everyone should wear a mask",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=14,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="in public settings and when around people who don’t live in your household,especially when other",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=15,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="social distancing measures are difficult to maintain.Masks should not be placed on young",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=16,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="children under age 2, anyone who has trouble breathing, or is unconscious,incapacitated or ",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=17,column=1,columnspan=2,sticky=W)
        text1=Label(prevention,text="otherwise unable to remove the mask without assistance.",font=('MS Sherrif',14),bg='hot pink',fg="dark violet").grid(row=18,column=1,columnspan=2,sticky=W)
        image6=ImageTk.PhotoImage(Image.open('images (2).jpg'))
        image6_label=Label(prevention,image=image6, height=190).grid(row=13,column=3,rowspan=6,pady=15)

        def back():
            prevention.destroy()
        end = Button(prevention, text='< Back', font=('',10),command=back).place(x=15,y=15)

        prevention.mainloop()

        
    def vaccination():
        vaccination=Toplevel()
        vaccination.configure(bg='aquamarine')
        vaccination.geometry('2500x2500')
        line1=Label(vaccination,text='Vaccination',bg='aquamarine',fg='red',font=('courier new',50,'bold italic underline'))
        line1.grid(row=0,column=0,columnspan=5,padx=50)
        image1=ImageTk.PhotoImage(Image.open('vaccine1.jpg'))
        image1_label=Label(vaccination,image=image1,bg='aquamarine')
        image1_label.grid(row=0,column=0,columnspan=5,sticky=W,padx=50)
        image2=ImageTk.PhotoImage(Image.open('vaccine2.jpg'))
        image2_label=Label(vaccination,image=image2,bg='aquamarine')
        image2_label.grid(row=0,column=0,columnspan=5,sticky=E)
        line2=Label(vaccination,text='Vacciation is a process of doing treatment with the vaccine to produce immunity',font=('verdana',22,'bold italic'),bg='aquamarine',fg='magenta3')
        line2.grid(row=2,column=0,columnspan=5,sticky=W)
        line3=Label(vaccination,text='against disease. Vaccine is uder production in various countries at various labs',font=('verdana',22,'bold italic'),bg='aquamarine',fg='magenta3')
        line3.grid(row=3,column=0,columnspan=5,sticky=W)
        line4=Label(vaccination,text='and universities like in America at Oxford University, in Russia at Gamaleya ',bg='aquamarine',fg='magenta3',font=('verdana',22,'bold italic'))
        line4.grid(row=4,column=0,columnspan=5,sticky=W)
        line5=Label(vaccination,text='Research Institute, in India at National Institue of Virology, in China at Wuhan',bg='aquamarine',fg='magenta3',font=('verdana',22,'bold italic'))
        line5.grid(row=5,column=0,columnspan=5,sticky=W)
        line6=Label(vaccination,text='and Beijing Institute of Biological Products -Sinopharm etc.', bg='aquamarine',fg='magenta3',font=('verdana',22,'bold italic'))
        line6.grid(row=6,column=0,columnspan=5,sticky=W)
        line7=Label(vaccination,text='Vaccine Update',bg='aquamarine',fg='red',font=('courier new',40,'bold italic'))
        line7.grid(row=8,column=0,columnspan=5)
        
        name=[['mRNA-1237 ','America','Phase-3','Moderna'],
              ['Ad5-nCoV ','China','Phase-3','CanSino Biologics'],
              ['Sputnik V','Russia','Phase-3','Gamaleya Institute'],
              ['Covishield','USA','Phase-3','AstraZeneca'],
              ['BNT162b2 ','Germany','Phase-3','BioNTech'],
              ['Covaxin ','India','Phase-2','Bharat Biotech']]
        
        b=pd.DataFrame(name,columns=['Name ','Country','Trial','Fund'],index=['|','|','|','|','|','|'])
        line8=Label(vaccination,text=b.iloc[0:,0:1],bg='aquamarine',fg='navy',font=('verdana',26,'italic'))
        line8.grid(row=9,column=0,sticky=W)
        line9=Label(vaccination,text=b.iloc[0:,1:2],bg='aquamarine',fg='navy',font=('verdana',26,'italic'))
        line9.grid(row=9,column=0,padx=350)
        line10=Label(vaccination,text=b.iloc[0:,2:3],bg='aquamarine',fg='navy',font=('verdana',26,'italic'))
        line10.grid(row=9,column=0,sticky=E)
        line9=Label(vaccination,text=b.iloc[0:,3:4],bg='aquamarine',fg='navy',font=('verdana',26,'italic'))
        line9.grid(row=9,column=1,sticky=E)

        def back():
            vaccination.destroy()
        end = Button(vaccination, text='< Back', font=('',10),command=back).place(x=15,y=15)

        vaccination.mainloop()
        

    heading = Label(prev, text='Prevention', font=('elephant', 37, 'underline'), fg='red', bg='lightcyan')
    empty_line = Label(prev, text='', font=('', 3), bg='lightcyan')
    line1 = Label(prev, text='Protect yourself and others around you by knowing the facts and taking appropriate precautions.                        ', font=('roboto', 20), fg='orange', bg='lightcyan')
    line2 = Label(prev, text='                        If you have a fever, cough and difficulty breathing, seek medical attention asa soon as possible.', font=('roboto', 20), fg='orange', bg='lightcyan')
    line3 = Label(prev, text='Calling in advance allows your healthcare provider to quickly direct you to the right health facility.                        ', font=('roboto', 20), fg='orange', bg='lightcyan')
    line4 = Label(prev, text='                        Informing the authaurities in advanced can aslo help in preventing the further spread of disease.', font=('roboto', 20), fg='orange', bg='lightcyan')
    line5 = Label(prev, text='Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover                        ', font=('roboto', 20), fg='orange', bg='lightcyan')
    line6 = Label(prev, text='                        without any special treatment, but they should be taken care off and have to be quarantined as', font=('roboto', 20), fg='orange', bg='lightcyan')
    line7 = Label(prev, text='soon as they are tested Corona positive. You may also keep your mouth clean by chewing some                          ', font=('roboto', 20), fg='orange', bg='lightcyan')
    line8 = Label(prev, text='                        ayrvedic stuff like tulsi, ginger, cinnamon, etc. You can be infected by breathing in the virus if', font=('roboto', 20), fg='orange', bg='lightcyan')
    line9 = Label(prev, text='you are within close proximity of someone who has COVID-19, or by touching any surface which                        ', font=('roboto', 20), fg='orange', bg='lightcyan')
    line10= Label(prev, text='                        These were some of the common preventive measures in brief. To know many more about the', font=('roboto', 20), fg='orange', bg='lightcyan')
    line11= Label(prev, text='preventive measures of Coronavirus at different basis in detail, click on the given buttons below...                        ', font=('roboto', 20), fg='orange', bg='lightcyan')
    empty_line2=Label(prev, text='', font=('', 10), bg='lightcyan')
    image = ImageTk.PhotoImage(Image.open('Corona9.jpg'))
    image_label = Label(prev, image=image, bd=5, bg='orangered')
    button1 = Button(prev, text='preventive measures to be\ntaken as an individual', bg='yellow', fg='red', font=('forte', 17), command=individual_precautions)
    button2 = Button(prev, text='preventive measures to be\ntaken as a community', bg='yellow', fg='red', font=('forte', 17), command=community_precautions)
    button3 = Button(prev, text='Curing through\nVACCINE', bg='yellow', fg='red', font=('forte', 20),command=vaccination)

    heading.grid(row=0, column=0)
    empty_line.grid(row=1, column=0)
    line1.grid(row=2, column=0)
    line2.grid(row=3, column=0)
    line3.grid(row=4, column=0)
    line4.grid(row=5, column=0)
    line5.grid(row=6, column=0)
    line6.grid(row=7, column=0)
    line7.grid(row=8, column=0)
    line8.grid(row=9, column=0)
    line9.grid(row=10, column=0)
    line10.grid(row=11, column=0)
    line11.grid(row=12, column=0)
    empty_line2.grid(row=13, column=0)
    image_label.grid(row=14, column=0, rowspan=2)
    button1.grid(row=14, column=0, sticky=W, padx=50)
    button2.grid(row=15, column=0, sticky=W, padx=50)
    button3.grid(row=14, column=0, rowspan=2, sticky=E, padx=90)

    def back():
        prev.destroy()
    end = Button(prev, text='< Back', font=('',10),command=back).place(x=15,y=15)

    prev.mainloop()



def future():
    future = Tk()
    future.title('Future Impacts')
    future.configure(bg='lightcyan')
    future.geometry('10000x10000')

    heading = Label(future, text='Future Impacts of COVID-19', bg='lightcyan', font=('aerolite regular',33,'underline italic bold'), fg='indigo', pady=10)

    number1 = Label(future, text='Digitalisation  =>', bg='lightcyan', font=('forte',24), fg='green')
    line1 = Label(future, text='Even as the COVID-19 pandemic exacts a bitter toll on the economy, it is catalysing digital transformation', bg='lightcyan', font=('forte',17), fg='#00ff00')
    line2 = Label(future, text='across the business models, the channels and touch points. Underlying this shift is the need for the greater', bg='lightcyan', font=('forte',17), fg='#00ff00')
    line3 = Label(future, text='organisational agility as well as the closer ties with the customers in today\'s changing world order.', bg='lightcyan', font=('forte',17), fg='#00ff00')

    number2 = Label(future, text='  <=  Unemployement', bg='lightcyan', font=('forte',24), fg='#884dff')
    line4 = Label(future, text='The coronavirus (COVID-19) crisis has led to a spike in the unemployment rate to 27.11% for the week', bg='lightcyan', font=('forte',17), fg='dark turquoise')
    line5 = Label(future, text='ended May 3, up from the under 7% level before the start of the pandemic in mid-March. Analysts have', bg='lightcyan', font=('forte',17), fg='dark turquoise')
    line6 = Label(future, text='been warning about the spectre of unemployment ever since the many parts of the world was put under', bg='lightcyan', font=('forte',17), fg='dark turquoise')
    line7 = Label(future, text='a lockdown to arrest the spread of the Coronavirus infection (COVID-19).', bg='lightcyan', font=('forte',17), fg='dark turquoise')

    number3 = Label(future, text='Ayurveda  =>  ', bg='lightcyan', font=('forte',24), fg='green')
    line8 = Label(future, text='Ayurveda helps people to build their immunity, to a great extinct which is nowadays very important to', bg='lightcyan', font=('forte',17), fg='#00ff00')
    line9 = Label(future, text='fight from the Coronavirus pandemic. People are looking towards the mehods of Ayurveda like having', bg='lightcyan', font=('forte',17), fg='#00ff00')
    line10= Label(future, text='ginger, cinnamon and cardamom tea, regular chai made with tulsi (holy basil, one or two leaves), or', bg='lightcyan', font=('forte',17), fg='#00ff00')
    line11= Label(future, text='even mint, cinnamon and cardamom tea. These herbal medicinal things helps to boost ones immunity.', bg='lightcyan', font=('forte',17), fg='#00ff00')

    number4 = Label(future ,text=' <=  Startups/Expansion', bg='lightcyan', font=('forte',24), fg='#884dff')
    line12=Label(future, text='Many small companies are taking initiative to come up and bring the innovative ideas into our lives,', bg='lightcyan', font=('forte',17), fg='dark turquoise')
    line13=Label(future, text='            which is really appreciable and will be on a larger scale very soon in the future. And the big', bg='lightcyan', font=('forte',17), fg='dark turquoise')
    line14=Label(future, text='      companies like Amazon are also taking initiative to launch new and customer-convinient services.', bg='lightcyan', font=('forte',17), fg='dark turquoise')
    line15=Label(future, text='', bg='lightcyan', font=('forte',17))
    line16=Label(future, text='', bg='lightcyan', font=('forte',17))

    empty_line = Label(future, text='', bg='lightcyan')
    empty_line2= Label(future, text='', bg='lightcyan')
    empty_line3= Label(future, text='', bg='lightcyan')
    empty_line4= Label(future, text='', bg='lightcyan')


    heading.grid(row=0, column=0, columnspan=2, pady=10)
    empty_line.grid(row=1, column=0)
    number1.grid(row=2, column=0, rowspan=3, padx=20)
    line1.grid(row=2, column=1, sticky=W)
    line2.grid(row=3, column=1, sticky=W)
    line3.grid(row=4, column=1, sticky=W)
    empty_line2.grid(row=5, column=0, pady=10)
    number2.grid(row=6, column=1, sticky=E, rowspan=4)
    line4.grid(row=6, column=0, columnspan=2, sticky=W, padx=32)
    line5.grid(row=7, column=0, columnspan=2, sticky=W)
    line6.grid(row=8, column=0, columnspan=2, sticky=W, padx=20)
    line7.grid(row=9, column=0, columnspan=2)
    empty_line3.grid(row=10, column=0, pady=10)
    number3.grid(row=11, column=0, rowspan=4)
    line8.grid(row=11, column=1, sticky=W)
    line9.grid(row=12, column=1, sticky=W)
    line10.grid(row=13, column=1, sticky=W)
    line11.grid(row=14, column=1, sticky=W)
    empty_line4.grid(row=16, column=0, pady=10)
    number4.grid(row=17, column=1, rowspan=3, sticky=E)
    line12.grid(row=17, column=0, sticky=W, columnspan=2)
    line13.grid(row=18, column=0, sticky=W, columnspan=2)
    line14.grid(row=19, column=0, sticky=W, columnspan=2)

    def back():
        future.destroy()
    end = Button(future, text='< Back', font=('',10),command=back).place(x=15,y=15)

    future.mainloop()



def feedback():
    feed = Toplevel()
    feed.title('Feedback')
    feed.geometry('10000x10000')
    feed.configure(bg='cyan')

    def submit():
        if first_name_entry.get()=="":
            popup = messagebox.showerror('Error',"Sorry! Feedback not submiited due to an empty field 'First Name'")
            feed.destroy()
        elif second_name_entry.get()=="":
            popup = messagebox.showerror('Error',"Sorry! Feedback not submiited due to an empty field 'Last Name'")
            feed.destroy()
        elif mail_id_entry.get()=="":
            popup = messagebox.showerror('Error',"Sorry! Feedback not submiited due to an empty field 'Mail ID'")
            feed.destroy()
        elif feedback_entry.get()=="":
            popup = messagebox.showerror('Error',"Sorry! Feedback not submiited due to an empty field 'Feedback'")
            feed.destroy()
        else:
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='python',
            )
            mycsr = mydb.cursor()
            a=first_name_entry.get()
            b=second_name_entry.get()
            c=mail_id_entry.get()
            d=feedback_entry.get()
            mycsr.execute("insert into feedback (First_name,Last_name,Mail_ID,Feedback) values (%s,%s,%s,%s)",(a,b,c,d))
            mydb.commit()
            mydb.close()
            popup = messagebox.showinfo('Sumbitted','Feedback Submitted !')
            if popup==1:
                first_name_entry.delete(0,END)
                second_name_entry.delete(0,END)
                mail_id_entry.delete(0,END)
                feedback_entry.delete(0,END)
                feed.destroy()
            else:
                first_name_entry.delete(0,END)
                second_name_entry.delete(0,END)
                mail_id_entry.delete(0,END)
                feedback_entry.delete(0,END)
                feed.destroy()
                
    def quiz():
        webbrowser.open_new("https://forms.gle/9foZLscpvHJCuRu76")
        frrd.destroy()
 

    heading = Label(feed, text='Feedback', font=('forte 50'), bg='cyan', fg='blue')
    empty_line = Label(feed, text='', font=('20'), bg='cyan')
    entries = Label(feed, text='Please fill the required fields :-', font=('roboto 15 bold'), bg='cyan')
    first_name = Label(feed, text='First Name : ', font=('roboto 17 bold'), bg='cyan')
    second_name = Label(feed, text='Last Name : ', font=('roboto 17 bold'), bg='cyan')
    mail_id = Label(feed, text='E-Mail ID : ', font=('roboto 17 bold'), bg='cyan')
    feedback = Label(feed, text='Feedback : ', font=('roboto 17 bold'), bg='cyan')
    first_name_entry = Entry(feed, width=100, borderwidth=5, font='15')
    second_name_entry = Entry(feed, width=100, borderwidth=5, font='15')
    mail_id_entry = Entry(feed, width=100, borderwidth=5, font='15')
    feedback_entry = Entry(feed, width=100, borderwidth=5, font='15')
    submit = Button(feed, text='Submit', font=('roboto 20 bold'), bg='pink', fg='red', bd=0, command=submit)
    frame = LabelFrame(feed, text='', bd=22, bg='#ff80b3')
    quiz_label = Label(frame, text='Here is a small quiz for you >', bg='#ff80b3', fg='red', font=('verdana',26,'bold'))
    quiz_button = Button(frame, text='Quiz', bg='fuchsia', fg='dark blue', font=('verdana',20,'bold'), padx=20, command=quiz)

    heading.grid(row=0, column=0, columnspan=2, padx=510)
    empty_line.grid(row=1, column=0)
    entries.grid(row=2, column=0, columnspan=2, sticky=W, padx=100, pady=20)
    first_name.grid(row=3, column=0, pady=20, padx=50)
    second_name.grid(row=4, column=0, pady=20, padx=50)
    mail_id.grid(row=5, column=0, pady=20, padx=50)
    feedback.grid(row=6, column=0, pady=20, padx=50)
    first_name_entry.grid(row=3, column=1)
    second_name_entry.grid(row=4, column=1)
    mail_id_entry.grid(row=5, column=1)
    feedback_entry.grid(row=6, column=1)
    submit.grid(row=7, column=0, columnspan=2, pady=30)
    frame.grid(row=8, column=0, columnspan=2)
    quiz_label.grid(row=0, column=0)
    quiz_button.grid(row=0, column=1, pady=20, padx=20)

    def back():
        feed.destroy()
    end = Button(feed, text='< Back', font=('',10),command=back).place(x=15,y=15)

    feed.mainloop()



main_label = Label(root, text='Coronopedia', font=('forte',60), fg='white', bg='black', anchor=E)
empty_line = Label(root, text='', bg='black')
b1 = Button(root, text='Introduction to Coronavirus', padx=90, pady=20,font=('forte',17,'bold'),bg='dark green', fg='orange',borderwidth=10,command=intro)
b2 = Button(root, text='Journey across the Globe', padx=98, pady=18, font=('forte',17,'bold'), bg='purple',borderwidth=10, fg='aqua',command=journy)
b3 = Button(root, text='Economy & Environment', padx=108, pady=20, font=('forte',17,'bold'), bg='dark green',borderwidth=10, fg='orange',command=ecoenviro)
b4 = Button(root, text='Prevention & Cure', padx=132, pady=18, font=('forte',17,'bold'), bg='purple', fg='aqua',borderwidth=10, command=prevention)
b5 = Button(root, text='Future Impacts', padx=120, pady=20, font=('forte',17,'bold'), bg='dark green', fg='orange',borderwidth=10, command=future)
b6 = Button(root, text='Feedback', padx=120, pady=15, font=('forte',17,'bold'), bg='purple', fg='aqua',borderwidth=10,command=feedback)


canvas = Canvas(root, width = 320, height = 410, bd=0, highlightthickness=0, relief='ridge')
canvas.grid(padx=40, pady=2, row=2, column=1, rowspan=6)
#canvas.create_text(200,250, fill="darkblue", font=("helvetica",15),text="CORONAVIRUS")
draw = turtle.RawTurtle(canvas)
canvas.configure(bg='black')
paint=['aqua','green','orange','red','#997a00']

def corona(colour):
    draw.speed(0)
    draw.pencolor('red')
    draw.hideturtle()
    draw.color(colour)
    draw.begin_fill()

    for a in range(20):
        draw.forward(2)
        draw.left(2)
    draw.right(90)
    draw.forward(25)
    draw.right(70)
    draw.forward(5)
    draw.left(70)
    draw.forward(3)
    draw.left(2)
    draw.forward(2)
    draw.left(88)
    draw.forward(18)
    draw.left(75)
    draw.forward(7)
    draw.left(95)
    draw.forward(5)
    draw.right(85)
    draw.forward(25)
    draw.right(90)
    for a in range(20):
        draw.forward(2)
        draw.left(2)
    draw.right(90)
    draw.forward(25)
    draw.right(70)
    draw.forward(5)
    draw.left(70)
    draw.forward(3)
    draw.left(2)
    draw.forward(2)
    draw.left(88)
    draw.forward(18)
    draw.left(75)
    draw.forward(7)
    draw.left(95)
    draw.forward(5)
    draw.right(85)
    draw.forward(25)
    draw.right(90)
    for a in range(20):
        draw.forward(2)
        draw.left(2)
    draw.right(90)
    draw.forward(25)
    draw.right(70)
    draw.forward(5)
    draw.left(70)
    draw.forward(3)
    draw.left(2)
    draw.forward(2)
    draw.left(88)
    draw.forward(18)
    draw.left(75)
    draw.forward(7)
    draw.left(95)
    draw.forward(5)
    draw.right(85)
    draw.forward(25)
    draw.right(90)
    for a in range(21):
        draw.forward(2)
        draw.left(2)
    draw.right(90)
    draw.forward(25)
    draw.right(70)
    draw.forward(5)
    draw.left(70)
    draw.forward(3)
    draw.left(2)
    draw.forward(2)
    draw.left(88)
    draw.forward(18)
    draw.left(75)
    draw.forward(7)
    draw.left(95)
    draw.forward(5)
    draw.right(85)
    draw.forward(25)
    draw.right(90)
    for a in range(20):
        draw.forward(2)
        draw.left(2)
    draw.right(90)
    draw.forward(25)
    draw.right(70)
    draw.forward(5)
    draw.left(70)
    draw.forward(3)
    draw.left(2)
    draw.forward(2)
    draw.left(88)
    draw.forward(18)
    draw.left(75)
    draw.forward(7)
    draw.left(95)
    draw.forward(5)
    draw.right(85)
    draw.forward(25)
    draw.right(90)
    for a in range(21):
        draw.forward(2)
        draw.left(2)
    draw.right(90)
    draw.forward(25)
    draw.right(70)
    draw.forward(5)
    draw.left(70)
    draw.forward(3)
    draw.left(2)
    draw.forward(2)
    draw.left(88)
    draw.forward(18)
    draw.left(75)
    draw.forward(7)
    draw.left(95)
    draw.forward(5)
    draw.right(85)
    draw.forward(25)
    draw.right(90)
    for a in range(20):
        draw.forward(2)
        draw.left(2)
    draw.right(90)
    draw.forward(25)
    draw.right(70)
    draw.forward(5)
    draw.left(70)
    draw.forward(3)
    draw.left(2)
    draw.forward(2)
    draw.left(88)
    draw.forward(18)
    draw.left(75)
    draw.forward(7)
    draw.left(95)
    draw.forward(5)
    draw.right(85)
    draw.forward(25)
    draw.right(90)
    for a in range(20):
        draw.forward(2)
        draw.left(2)
    draw.right(90)
    draw.forward(25)
    draw.right(70)
    draw.forward(5)
    draw.left(70)
    draw.forward(3)
    draw.left(2)
    draw.forward(2)
    draw.left(88)
    draw.forward(18)
    draw.left(75)
    draw.forward(7)
    draw.left(95)
    draw.forward(5)
    draw.right(85)
    draw.forward(25)
    draw.right(90)
    for a in range(21):
        draw.forward(2)
        draw.left(2)
    draw.right(90)
    draw.forward(25)
    draw.right(70)
    draw.forward(5)
    draw.left(70)
    draw.forward(3)
    draw.left(2)
    draw.forward(2)
    draw.left(88)
    draw.forward(18)
    draw.left(75)
    draw.forward(7)
    draw.left(95)
    draw.forward(5)
    draw.right(85)
    draw.forward(25)
    draw.right(90)
    for a in range(21):
        draw.forward(2)
        draw.left(2)
    draw.right(90)
    draw.forward(25)
    draw.right(70)
    draw.forward(5)
    draw.left(70)
    draw.forward(3)
    draw.left(2)
    draw.forward(2)
    draw.left(88)
    draw.forward(18)
    draw.left(75)
    draw.forward(7)
    draw.left(95)
    draw.forward(5)
    draw.right(85)
    draw.forward(25)
    draw.right(90)
    for a in range(1):
        draw.forward(2)
        draw.left(2)
    draw.end_fill()

main_label.grid(row=0, column=0, columnspan=3)
empty_line.grid(row=1, column=1, pady=5)
b1.grid(row=2, column=0, pady=5)
b2.grid(row=3, column=2, pady=5)
b3.grid(row=4, column=0, pady=5)
b4.grid(row=5, column=2, pady=5)
b5.grid(row=6, column=0, pady=5)
b6.grid(row=7, column=2, pady=5,sticky=N)

for x in paint:
    corona(x)

canvas.rotate(20)

root.mainloop()
