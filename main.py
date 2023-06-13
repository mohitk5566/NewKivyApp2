from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.image import Image
import qrcode
kv='''
MainWidget:
<MainWidget>:
    canvas.before:
        Color:
            rgba: 0.4, 0.4, 0.4, 0.4
        Rectangle:
            pos: self.pos
            size: self.size
    Button:
        text:"<- close"
        size: "80dp", "40dp"
        pos: "0dp", "751dp"
        on_release:app.stop()
        font_size:"20dp"        
    Label:
        text: "Link to QR-code maker"
        pos:"80dp", "751.5dp"
        size:"300dp","40dp"
        font_size:"23dp"
        background_color: (0.5, 0.5, 0.5, 0.5)
        canvas.before:
        	Color:
        	    rgba: self.background_color
            Rectangle:
           	 size: self.size
           	 pos: self.pos
    TextInput:        
        size:"360dp", "25dp"
        pos:"10dp","500dp"
        font_size:"20dp"
        multiline:False
        on_text_validate: root.text_velidate(self)
        on_text_velidate:
    Label:
        text: root.mytext
        font_size:"15dp"
        pos:"172dp", "470dp"
    Label:
    	text:"Made by Mohit Kumar"
    	pos:"172dp","0dp"
'''
class ImageToQR(App):    	
    mytext=StringProperty("Please pate a Link or URL above and hit Enter to save.")
    class MainWidget(Widget):
        mytext=StringProperty("Please pate a Link or URL above and hit Enter to save.")
        def text_velidate(self, widget):
            self.mytext="Done, The Output shown below:"
            link=widget.text
            img=qrcode.make(link)
            img.save("NewQR.png")
            img.show()
            with self.canvas:
                Image(source="NewQR.png",pos=self.pos,size=self.size)
    def build(self):
    	return Builder.load_string(kv)
ImageToQR().run()