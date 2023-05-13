import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
from openpyxl import load_workbook

def play(self):
    import numpy as np
    import pandas as pd
    
    archivopreg = 'QyA.xlsx'
    preguntas = pd.read_excel(archivopreg)
    lives = 3
    livestr = str(lives)
    score = 0
    used = []
    self.liveslabel.setText(livestr)
    while lives > 0:
        num = np.random.randint(0,5)
        
        self.reset_question()
        if (num not in used):
            preg= preguntas['Pregunta'][num]
            self.labelpregunta.setText(preg)
            respa=preguntas['A'][num]
            self.RB1.setText(respa)
            respb=preguntas['B'][num]
            self.RB2.setText(respb)
            respc=preguntas['C'][num]
            self.RB3.setText(respc)
            respd=preguntas['D'][num]
            self.RB4.setText(respd)
            respcorrect= preguntas['Correcta'][num]
            used.append(num)
            print(used)
            answered = False
            while answered == False:
                if self.BotonAceptar.clicked:
                    answer = self.submit_answer()
                    print(answer)
                    if answer == respcorrect.lower():
                        score += 100
                    else:
                        lives = lives - 1
                        livestr = str(lives)
                        self.liveslabel.setText(livestr)
                    print(score)
                    print("Lives: ",lives)
                    answered = True

import numpy as np
import pandas as pd
    
archivopreg = 'QyA.xlsx'
preguntas = pd.read_excel(archivopreg)
tam = len(preguntas)

num=[]
for i in range(0,tam):
    num.append(preguntas['Pregunta'][i])
print(num)