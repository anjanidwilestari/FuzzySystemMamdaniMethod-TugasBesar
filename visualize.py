import cv2
from tkinter import *
from tkinter import ttk, messagebox
from pekabelproject import layak


class visualize():
    def __init__(self):

        self.window = Tk()

        self.window.title("Fuzzy Neural Network Systems")
        self.window.geometry('600x750')

        self.tab_control = ttk.Notebook(self.window)

        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab2, text='Uji Kelayakan Kayu')
        self.tab_control.add(self.tab3, text='Info')

        self.introframe = ttk.Labelframe(self.tab1, )
        self.info_1 = ttk.Labelframe(self.tab3,text= "Dosen Pengampu")
        self.info_2 = ttk.Labelframe(self.tab3,text= "Disusun oleh")
        self.l_frame = ttk.Labelframe(self.tab1, width=100, height=100)
        self.v_frame = ttk.Labelframe(self.tab1,text='visualize')

        submited_to = Label(self.info_1, text="Kol. Lek. Prof. Dr. Ir. Arwin Datumaya Wahyudi Sumari, S.T., M.T.\n ",
                        font=("Arial", 12))
        submited_to.grid(column=0, row=1, sticky=N)

        submited_by = Label(self.info_2, text="Anjani Dwilestari (2041720180)\n Deatrisya Mirela Harahap (2041720013)\n Siti Aisyah (2041720061)\n\n PROGRAM STUDI D-IV TEKNIK INFORMATIKA\n JURUSAN TEKNOLOGI INFORMASI\n POLITEKNIK NEGERI MALANG",
                            font=("Arial", 12))
        submited_by.grid(column=0, row=1, sticky=N)

        #............................................................................................
        #START OF UJI KELAYAKAN KAYU
        #............................................................................................

        self.introframe2 = ttk.Labelframe(self.tab2, )
        self.l_frame2 = ttk.Labelframe(self.tab2, width=100, height=100)
        self.v_frame2 = ttk.Labelframe(self.tab2, text='visualize')

        heading2 = Label(self.introframe2, text="Fuzzy Neural Network Systems\n Uji Kelayakan Kayu Menggunakan Metode Tsukamoto",
                        font=("Arial", 12))
        heading2.grid(column=0, row=0, sticky=N)

        self.Result2 = Label(self.l_frame2, text="N/A", font=("Arial", 14))
        self.Result2.grid(column=1, row=5, sticky=N)

        input_txt1 = Label(self.l_frame2, text="Masukkan Kelembapan\n (0~10) : ", font=("Arial", 12))
        input_txt1.grid(column=0, row=2, sticky=N)
        self.txt11 = Entry(self.l_frame2, width=10)
        self.txt11.grid(column=1, row=2, sticky=N)

        input_txt_2 = Label(self.l_frame2, text="Masukkan Ketebalan\n (0~10) : ", font=("Arial", 12))
        input_txt_2.grid(column=0, row=3, sticky=N)
        self.txt12 = Entry(self.l_frame2, width=10)
        self.txt12.grid(column=1, row=3, sticky=N)

        input_txt_3 = Label(self.l_frame2, text="Masukkan Umur\n (0~10) : ", font=("Arial", 12))
        input_txt_3.grid(column=0, row=4, sticky=N)
        self.txt13 = Entry(self.l_frame2, width=10)
        self.txt13.grid(column=1, row=4, sticky=N)
        
        btn2 = Button(self.l_frame2, text="Hitung Kelayakan", command=self.clicked)
        btn2.grid(column=3, row=3, sticky=N)

        self.canvas2 = Canvas(self.v_frame2, width=700, height=800)
        # canvas.pack()

        self.canvas2.grid(row=0)

        self.tab_control.pack(expand=1, fill='both')

        self.introframe.pack()
        self.introframe2.pack()
        self.info_1.pack()
        self.info_2.pack()

        self.l_frame.pack()
        self.l_frame2.pack()

        self.v_frame.pack()
        self.v_frame2.pack()


        self.window.mainloop()

    def clicked(self):

        input_txt1 = self.txt11.get()
        input_txt2 = self.txt12.get()
        input_txt3 = self.txt13.get()
        if len(input_txt1) == 0 or len(input_txt2) == 0 or len(input_txt3) == 0 :
            messagebox.showwarning('Input Error', 'Input can not be empty')
        else:
            try:
                kelembapan = float(input_txt1)
                ketebalan = float(input_txt2)
                umur = float(input_txt3)

                if kelembapan < 0.0 or kelembapan > 100.0 or ketebalan < 0.0 or ketebalan > 100.0 or umur < 0.0 or umur > 100.0:
                    messagebox.showwarning('Input Error', 'value Out of range.\n Input should be 0 ~ 10')
                else:
                    out = layak(kelembapan,ketebalan,umur)
                    self.Result2.configure(text='{:02f}'.format(out))
                    img2 = cv2.imread('output/out2.png')
                    resize2 = cv2.resize(img2, (600, 700))
                    cv2.imwrite('output/out2.png', resize2)
                    self.img2 = PhotoImage(file="output/out2.png")

                    self.canvas2.create_image(20, 20, anchor=NW, image=self.img2)


            except:
                messagebox.showwarning('Input Error', 'Input Should be Integer or Float Value')


