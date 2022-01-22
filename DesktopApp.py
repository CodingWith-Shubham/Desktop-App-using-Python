from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox as tmsg
root = Tk()
root.geometry("700x500")

root.minsize(300,300)
root.maxsize(380,500)
root.title("CYGNUS")
icouns = PhotoImage(file="D:\my photos\icouns.png")
root.iconphoto(False, icouns)
a = Canvas(width="300" , height="500", bg="black")
a.pack(fill=BOTH)
gif1 = PhotoImage(file="D:\\my photos\\space.png")
a.create_image(0,0,image=gif1,anchor="nw")

#a.create_image(0,0,image=gif1,anchor="nw")
#def rating():
def quiz():
    tmsg.showinfo("simple quiz", "Q1.what is the name of our galaxy?\nANS milky way\nQ2.which is the hottest planet in the solar system?\nANS venus\nQ3.which planet is smallest?\nANS mercury\nQ4.which star is closest to the sun?\nANS proxima centuary\nQ5.how many planets are there in our solar system?\nANS eight\nQ6.which planet is dwarf now?\nANS pluto\nQ7.what is cygnus?\nANS constellation\nQ8.what is the name of star which does not change its position?\nANS pole star\nQ9.who was the first person landed on moon?\nANS Neil Armstrong\nQ10.which is the biggest planet in our solar system?\nANS jupiter")
def newwindow():
    window = Toplevel()
    window.geometry("500x600")
    l1 = Label(window,text="MERCURY IS THE CLOSEST PLANET TO THE SUN\n\nMERCURY IS ALSO THE SMALLEST PLANET IN THE SOLAR SYSTEM\n\nMERCURY HAS MOST CRATERS IN THE SOLAR SYSTEM\n\nTHE BIGGEST CRATER IN MERCUTY COULD FIT WESTERN EUROPE",bg="brown",fg="white",font="arial 10 underline",padx=30,pady=250)
    l1.pack(fil=BOTH)
def newwindow1():
    window = Toplevel()
    window.geometry("500x400")
    l2 = Label(window,text="A DAY ON VENUS IS LONGER THAN A YEAR\n\nVENUS IS HOTTEST PLANET IN SOLAR SYSTEM\n\nVENUS SPINS CLOCKWISE ON ITS AXIS\n\nVENUS IS THE SECOND BRIGHTEST NATURAL OBJECT ",bg="orange",fg="white",font="arial 10 underline",padx=30,pady=250)
    l2.pack(fill=BOTH)
def newwindow2():
    window = Toplevel()
    window.geometry("500x400")
    l3 = Label(window,text="EARTH IS ALMOST A SPHERE\n\nEARTH IS MOSTLY IRON , OXYGEN AND SILICON\n\n70% OF THE EARTH'S SURFACE IS COVERED IN WATER\n\nTHE EARTH'S ATMOSPHERE EXTENDS TO DISTANCE OF 10000 KM",bg="green",fg="white",font="arial 10 underline",padx=30,pady=250)
    l3.pack(fill=BOTH)
def newwindow3():
    window = Toplevel()
    window.geometry("500x400")
    l4 = Label(window,text="MARS IS ALSO KNOWN AS RED PLANET\n\nMARS HAS TWO MOONS\n\MARS IS THE SECOND SMALLEST PLANET IN SOLAR SYSTEM\n\nMARS HAD WATER IN ANCIENT PAST\n\nMARS HAS EXTREME HIGH AND LOW TERRAIN",bg="maroon",fg="white",font="arial 10 underline",padx=30,pady=250)
    l4.pack(fill=BOTH)
def newwindow4():
    window = Toplevel()
    window.geometry("500x400")
    l5 = Label(window,text="JUPITER IS THE FASTEST SPINING PLANET IN THE SOLAR SYSTEM\n\nTHE CLOUDS ON JUPITER IS ONLY 50 KM THICK\n\nJUPITER'S MAGNETIC FIELD IS 14 TIMES STRONGER THAN EARTH\n\nJUPITER HAS A RED SPOT AND RINGS ALSO",bg="brown",fg="white",font="arial 10 underline",padx=30,pady=250)
    l5.pack(fill=BOTH)
def newwindow5():
    window = Toplevel()
    window.geometry("500x400")
    l6 = Label(window,text="SATURN IS THE MOST DISTANT PLANET THAT CAN BE SEEN WITH NAKED EYES\n\nSATURN IS THE FLATTEST PLANET IN THE SOLAR SYSTEM\n\nSATURN'S UPPER ATMOSPHERE IS DIVIDED INTO BANDS OF CLOUDS\n\nSATURN HAS 62 MOONS",bg="grey",fg="white",font="arial 10 underline",padx=30,pady=250)
    l6.pack(fill=BOTH)
def newwindow6():
    window = Toplevel()
    window.geometry("500x400")
    l7 = Label(window,text="URANUS IS THE COLDEST PLANET IN THE SOLAR SYSTEM\n\nURANUS IS SECOND LEAST DENSE PLANET\n\nURANUS HAS 27 MOONS\n\nTHE ATMOSPHERE OF URANUS CONTAINS ICES\n\nURANUS IS VISIBLE TO OUR NAKED EYES",bg="blue",fg="white",font="arial 10 underline",padx=30,pady=250)
    l7.pack(fill=BOTH)
def newwindow7():
    window = Toplevel()
    window.geometry("500x400")
    l8 = Label(window,text="NEPTUNE IS THE MOST DISTANT PLANET\n\nNEPTUNE HAS THE STRONGEST WINDS IN THE SOLAR SYSTEM\n\nNEPTUNE'S SURFACE GRAVITY IS ALMOST LIKE EARTH\n\nTHE DISCOVERY OF NEPTUNE IS STILL A CONTROVERSY",bg="navy blue",fg="white",font="arial 10 underline",padx=30,pady=250)
    l8.pack(fill=BOTH)
    
def response():
        tmsg.showinfo("user comment","YOUR RESPONSE WAS SUBMITTED THANK YOU")
def jupiter():
	#j1 = tmsg.showinfo("ABOUT JUPITER","Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined, but slightly less than one-thousandth the mass of the Sun. Jupiter is the third-brightest natural object in the Earth's night sky after the Moon and Venus. It has been observed since pre-historic times and is named after the Roman god Jupiter, the king of the gods, because of its observed size.")
        #if j1=="yes":
        j1 = tmsg.askquestion("ALERT","Do you wish to know about jupiter")
        if j1=="yes":
                tmsg.showinfo("ABOUT JUPITER","Jupiter is the fifth planet from the Sun and the lhird-brightest natural object")
        else:
                None
def saturn():
	s1 = tmsg.askquestion("ALERT", "Do you wish to know about saturn?")
	if s1 == "yes":
		tmsg.showinfo("saturn" , "Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth.[22][23] It only has one-eighth the average density of Earth; however, with its larger volume, Saturn is over 95 times more massive.[24][25][26] Saturn is named after the Roman god of wealth and agriculture. Its astronomical symbol (♄) has been traced back to the Greek Oxyrhynchus Papyri, where it can be seen to be a Greek kappa-rho with a cross-bar, as an abbreviation for Κρονος (Cronos), the Greek name for the planet.[27] It later came to look like a lower-case Greek eta, with the cross added at the top in the 16th century.")
	else:
		None
def earth():
        e1 = tmsg.askquestion("ALERT","Do you wish to konw about earth?")
        if e1 == "yes":
                tmsg.showinfo("EARTH","")
        else:
                None
def venus():
	v1 = tmsg.askquestion("ALERT", "Do you wish to know about venus?")
	if v1 == "yes":
		tmsg.showinfo("VENUS","Venus is the second planet from the Sun. It is named after the Roman goddess of love and beauty. As the brightest natural object in Earth's night sky after the Moon, Venus can cast shadows and can be, on rare occasions, visible to the naked eye in broad daylight.[17][18] Venus lies within Earth's orbit, and so never appears to venture far from the Sun, either setting in the west just after dusk or rising in the east a little while before dawn. Venus orbits the Sun every 224.7 Earth days.[19] It has a synodic day length of 117 Earth days and a sidereal rotation period of 243 Earth days. As a consequence, it takes longer to rotate about its axis than any other planet in the Solar System, and does so in the opposite direction to all but Uranus. This means the Sun rises in the west and sets in the east.[20] Venus does not have any moons, a distinction it shares only with Mercury among the planets in the Solar System")
	else:
		None
def tech():
    window = Toplevel()
    window.geometry("700x300")
    space = Label(window,text="Space technology is technologydeveloped by space science\n\n It is for use in spaceflight, or space exploration\n\n Space technology includes spacecraft, satellites, and support infrastructure\n\n Space is such a environment that attempting to work in it requires new tools and techniques\n\n Many common services such as weather forecasting, remote sensing, GPS systems,rely on space infrastructure\n\nThe Hubble Space Telescope and other tech. is also in use",bg="navy blue",fg="white",font="arial 10 bold",padx=30,pady=250)
    space.pack(fil=BOTH)
def galaxy1():
    window = Toplevel()
    window.geometry("700x300")
    spacex = Label(window,text="A galaxy is a huge collection of gas, dust, and billions of stars and their solar systems\n\nall held together by gravity\n\nThere are many galaxies besides ours, though\n\nThere are so many, we can’t even count them all yet! Some galaxies are spiral-shaped like ours/n/nThey have curved arms that make it look like a pinwheel\n\nSometimes galaxies get too close and smash into each other.",bg="black",fg="white",font="arial 10 bold",padx=30,pady=250)
    spacex.pack(fil=BOTH)
def isro1():
    window = Toplevel()
    window.geometry("700x300")
    isro1 = Label(window,text="India decided to go to space when Indian National Committee for Space Research (INCOSPAR) was set up by the Government of India in 1962\n\nWith the visionary Dr Vikram Sarabhai at its helm, INCOSPAR set up the Thumba Equatorial Rocket Launching Station (TERLS) in Thiruvananthapuram for upper atmospheric research\n\nISRO has upheld its mission of bringing space to the service of the common man, to the service of the Nation\n\nIn the processit has become one of the six largest space agencies in the world\n\nISRO has also contributed to science and science education in the country",bg="red",fg="white",font="arial 12 bold",padx=30,pady=250)
    isro1.pack(fil=BOTH)
def robot1():
    window = Toplevel()
    window.geometry("700x300")
    robot1 = Label(window,text="Microgravity Robotics includes manipulation and mobility for scenarios such as International Space Station (ISS) operations and satellite servicing\n\nPlanetary Robot systems address scenarios such as Mars and lunar exploration using manipulation or mobility on or near the surface\n\nISRO uses robots in many different ways\n\nRobotic arms on spacecraft can move large objects in space\n\nRobotic spacecraft can visit other worlds\n\nRobotic airplanes can fly without a pilotsome robots currently exploring space include Dextre, Voyager 1 and 2, Hubble Space Telescope, Cassini, Robonaut 2, Rosetta, Dawn, Mars Express, Curiosity, Opportunity, 2001 Mars Odyssey, Advanced Composition Explorer, Hayabusa 2, Juno, Mars Orbiter Mission, New Horizons and more to come\n\nSpacecraft that explore other worlds, like the moon or Mars, are all robotic. These robots include rovers and landers on the surface of other planets\n\nUnlike the robotic arm on the space station, these robots are autonomous",bg="green",fg="white",font="arial 10 bold",padx=30,pady=250)
    robot1.pack(fil=BOTH)
def explore1():
    window = Toplevel()
    window.geometry("700x300")
    explore1 = Label(window,text="Human space exploration helps to address fundamental questions about our place in the Universe and the history of our solar system\n\nThrough addressing the challenges related to human space exploration we expand technology, create new industries, and help to foster a peaceful connection with other nations\n\nWhile the exploration of space is carried out mainly by astronomers with telescopes\n\nTo date, scientists have explored about 4 percent of the visible universe\n\nThat's made up of planetsstars and galaxies that astronomers can see\n\nYet, there's a vast part – the other 96 percent – that scientists cannot see",bg="orange",fg="white",font="arial 12 bold",padx=30,pady=250)
    explore1.pack(fil=BOTH)
def abtus():
    tmsg.showinfo("ABOUT US","THE APP IS CREATED AND DEVELOPED BY SHUBHAM AND ADITYA FROM CYGNUS TEAM\n\nTHE APP TOOK SO MUCH HARDWORK TO BUILD\n\nWE ARE FROM NAVYUG SCHOOL IN NEW DELHI\n\nWE HOPE YOU LIKED THE APP\n\nDONT FORGET TO GIVE REVIEW")
    
    
    
    
    
    

#frame1 = Frame(root).place()
b1 = Button(root,text='   I   S   R   O   ',bd=5,fg="white",relief=SUNKEN,font="andalus",bg="black",command=isro1).place(x=30,y=50)
b2 = Button(root,text='ROBOTICS    ',bd=5,fg="white",relief=SUNKEN,font="andalus",bg="black",command=robot1).place(x=30,y=100)
b3 = Button(root,text='OUR GALAXY',bd=5,fg="white",relief=SUNKEN,font="andalus",bg="black",command=galaxy1).place(x=30,y=150)
b4 = Button(root,text='SPACE TECHNOLOGY',bd=5,fg="white",relief=SUNKEN,font="andalus",bg="black",command=tech).place(x=180,y=50)
b5 = Button(root,text='    SPACE QUIZ              ',bd=5,fg="white",relief=SUNKEN,font="andalus",bg="black",command=quiz).place(x=180,y=100)
b6 = Button(root,text='   EXPLORE SPACE     ',bd=5,fg="white",relief=SUNKEN,font="andalus",bg="black",command=explore1).place(x=180,y=150)
b7 = Frame(root).place(x=80,y=200)
l1 = Label(b7,text="OUR PLANETS",font="arial 20 bold",bg="black",fg="white").place(x=80,y=200)
b8 = Frame(root).place(x=120,y=320)
l2 = Label(b8,text="YOUR REVIEW",font="arial 12 bold",bg="black",fg="white").place(x=120,y=320)
mybutton = Button(root,text="MERCURY",font="arial 9 bold",bg="black",fg="white",command=newwindow)
mybutton.place(x=90,y=240)
mybutton1 = Button(root,text="  VENUS   ",font="arial 9 bold",bg="black",fg="white",command=newwindow1)
mybutton1.place(x=90,y=260)
mybutton2 = Button(root,text="   EARTH   ",font="arial 9 bold",bg="black",fg="white",command=newwindow2)
mybutton2.place(x=90,y=280)
mybutton3 = Button(root,text="   MARS   ",font="arial 9 bold",bg="black",fg="white",command=newwindow3)
mybutton3.place(x=160,y=240)
mybutton4 = Button(root,text=" JUPITER ",font="arial 9 bold",bg="black",fg="white",command=newwindow4)
mybutton4.place(x=160,y=280)
mybutton5 = Button(root,text=" SATURN ",font="arial 9 bold",bg="black",fg="white",command=newwindow5)
mybutton5.place(x=240,y=240)
mybutton6 = Button(root,text="URANUS ",font="arial 9 bold",bg="black",fg="white",command=newwindow6)
mybutton6.place(x=240,y=280)
mybutton7 = Button(root,text="NEPTUNE",font="arial 9 bold",bg="black",fg="white",command=newwindow7)
mybutton7.place(x=240,y=260)












e1 = Entry(root,bd = 5,)
e1.place(x=110,y=350)
b1 = Button(root,text="submit", relief = SUNKEN,bd=5,font="arial",bg="black",fg="white",command=response).place(x=140,y=380)
b2 = Button(root,text="ABOUT US", relief = SUNKEN,bd=5,font="arial",bg="black",fg="white",command=abtus).place(x=130,y=460)






root.mainloop()

