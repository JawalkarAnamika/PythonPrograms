import tkinter as tk
def get_response(user_input):
    user_input=user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hi there!😊"
    elif "hoe are you" in user_input:
        return "I'am just a bunch of code,but I'am happy to chat!" 
    elif "bye" in user_input:
        return"Goodbye!🖐 Come back soon!"
    else:
        return "I'am still learning. Can yiu ask somrthing else?"

def send_message():
    user_input=entry.get()
    if user_input.strip()=="":
        return
    chat_box.insert(tk.END ,"YOU: "+user_input)
    response=get_response(user_input)
    chat_box.insert(tk.END,"Bot: "+response)
    entry.delete(0,tk.END)

window=tk.Tk()
window.title("Simple Chatbot")
window.geometry("400x400")
window.config(bg="red")

chat_box=tk.Listbox(window,height=20,width=20,font=("Arial",12))
chat_box.pack(pady=10)
entry=tk.Entry(window,width=40,font=("Arial",12))
entry.pack(side=tk.LEFT,padx=10,pady=5)
send_button=tk.Button(window,text="send",width=10, command=send_message,bg="Yellow")
send_button.pack(side=tk.LEFT)
window.mainloop()
