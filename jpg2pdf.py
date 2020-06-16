from PIL import Image as im
import PySimpleGUI as sg


class Tela:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown2')

        #Layout

        layout = [
            [sg.FileBrowse('Escolha uma imagem',target='img'), sg.In(key='img')],
            [sg.SaveAs('Escolha uma pasta para salvar',target='path'),sg.In(key='path')],
            [sg.OK()],
            [sg.Output()]
        ]

        #Janela

        self.janela = sg.Window('JPG para PDF').layout(layout)

        #Extrair dados da tela

        
    def Iniciar(self):
        while True:
            self.button,self.values = self.janela.Read()
            img = self.values['img']
            path = self.values['path']
            image = im.open(img)
            im1 = image.convert('RGB')
            im1.save(path)


tela = Tela()
tela.Iniciar()

