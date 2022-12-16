"""
    Stage: Development-01
    @author: Mert Şen, 119200031
    @author: Bükre Yağmur Türkoğlu, 120200054
"""

import tkinter as library


class LoginWindow:
    # constructor
    def __init__(self):
        self.window = library.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()
        self.window.title("Library")
        # start the GUI frame
        self.window.mainloop()
        


    """
    +++
        Initialize GUI elements. If it is necessary, you can add
        more elements.
        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.lbl01 = library.Label(text="Username")
        self.lbl02 = library.Label(text="Password")

        self.txt01 = library.Entry(width=30)
        self.txt02 = library.Entry(width=30)

        self.btn01 = library.Button(text="Login")
        self.btn02 = library.Button(text="Forgot Password")
        self.btn03 = library.Button(text="Cancel")


        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-2>", self.handle_click)
        self.btn03.bind("<Button-3>", self.handle_click)
        
     


    """
    +++
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=5, pady=5)
        self.btn02.grid(row=2, column=1, padx=5, pady=5)
        self.btn03.grid(row=2, column=2, padx=5, pady=5)

    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.
        :param event: action event for detecting which button is clicked
    """
    window01 = library.Tk()
    window01.title("New Tab")
    
    def handle_click(self, event):
        if event.widget == self.btn01: 
            if self.txt01.get() == "test" and self.txt02.get() == 'test123': 
                
               self.login()

    
    def login(self):
        # open the new page after login
        
        NewPage()


class NewPage:#create new book search page
    books = [["1", "Suc ve Ceza"], ["2", "cocuk kalbi"], ["3", "Fareler ve Insanlar"]]
                   
    #new constructor
    def __init__(self):
        self.window = library.Tk()
            # set the title of the window
        self.window.title("Book Search")

             # initialize GUI elements
        self._initializeGUI2()
        self._addGUIElementsToFrame()

            # start the GUI frame
        self.window.mainloop()  

    #new elements bookname booknum lables and search button
    def _initializeGUI2(self):
        self.lbBookl01 = library.Label(text="Book Name")
        self.lbBookl02 = library.Label(text="Book ID")

        self.txtBook01 = library.Entry(width=30)
        self.txtBook02 = library.Entry(width=30)

        self.btnBookSearch01 = library.Button(text="Search")
       


        self.btnBookSearch01.bind("<Button-1>", self.handle_click)

    
    def _addGUIElementsToFrame2(self):
        self.lblbook01.grid(row=0, column=0, padx=10, pady=5)
        self.txtbook01.grid(row=0, column=1, padx=10, pady=5)

        self.lblbook02.grid(row=1, column=0, padx=10, pady=5)
        self.txtbook02.grid(row=1, column=1, padx=10, pady=5)

        self.btnbook01.grid(row=2, column=0, padx=5, pady=5)
            

    def handle_click(self, event):
        # button event start serach operation if clicked
        if event.widget == self.btnBookSearch01:
            self.search()
        
    def search(self):
        bookNumber = self.txtBook01.get()
        

# main method for testing the application
if __name__ == "__main__":
    LoginWindow()