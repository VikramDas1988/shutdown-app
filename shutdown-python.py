from tkinter import *
import os 

def restart():
    os.system("shutdown -r -t 1")
    
def restart_time():
    os.system("shutdown -r -t 20")

def shutdown():
    os.system("shutdown -s -t 1")    

st = Tk()
st.title("Shut Down App")
st.geometry("500x600")
st.config(bg="blue")

r_button = Button (st, text="Restart", font=("arial",30,"bold"),bg="red", cursor="plus" , command=restart)
r_button.place(x=150,y=60, width=200,height=50)

r_button = Button (st, text="Restart with time", font=("arial",30,"bold"),bg="red", cursor="plus",command=restart_time)
r_button.place(x=50,y=160, width=400,height=50)

r_button = Button (st, text="Shutdown", font=("arial",30,"bold"),bg="red", cursor="plus",command=shutdown)
r_button.place(x=150,y=260, width=200,height=50)

r_button = Button (st, text="Close", font=("arial",30,"bold"),bg="red", cursor="plus", command=st.destroy)
r_button.place(x=150,y=360, width=200,height=50)


st.mainloop()