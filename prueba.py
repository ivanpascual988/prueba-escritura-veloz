"""
App donde se medira tu habilidad/velocidad para escribir una frase completamente aleatoria
"""

# Importo los modulos necesarios
from logging import root
import random
import time
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class PruebaVelocidad(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Prueba de velocidad de escritura by Ivan Pascual") # Titulo de la app
        #self.geometry("600x400")
        self.window_definition()

    def window_definition(self):
        """
        Funcion para definir la ventana de la app
        """
        # Boton para generar frase aleatoria
        self.boton_frase_aleatoria = ttk.Button(self, text="GENERAR FRASE ALEATORIA", command=self.generar_frase)
        self.boton_frase_aleatoria.pack(side="top", pady=20)
        # Área de entrada de texto para que el usuario escriba la frase
        self.input_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=5, width=50, font=("Arial", 15))
        self.input_text.pack(padx=20)

        # Boton para iniciar la prueba de velocidad
        self.boton_frase_aleatoria = ttk.Button(self, text="INICIAR PRUEBA DE VELOCIDAD", command=self.iniciar_prueba)
        self.boton_frase_aleatoria.pack(pady=20) 
        # Area donde aparecera la frase alearotoria
        self.text_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=5, width=50, font=("Arial", 15))
        self.text_box.pack(padx=20, side="bottom")
        self.text_box.config(state="disabled")  # Deshabilitar la edición del cuadro de texto

    def generar_frase(self):
        """
        Funcion que nos da una frase aleatoria para probar nuestra escritura
        """
        num_rd = random.randint(0,9)
        frases = [
            "En el mundo de la inteligencia artificial, Python es el lenguaje de elección para desarrollar algoritmos de aprendizaje automático que pueden predecir resultados deportivos con precisión.",
            "Como programador, siempre me impresiona cómo la IA puede analizar datos deportivos en tiempo real y proporcionar estadísticas detalladas que ayudan a los entrenadores a tomar decisiones estratégicas.",
            "El desarrollo de una IA capaz de jugar al ajedrez a nivel de Gran Maestro es un logro destacado en el campo de la inteligencia artificial, y Python desempeña un papel crucial en ese proceso.",
            "Python es un lenguaje versátil que se utiliza en la programación de robots deportivos autónomos, como los utilizados en competencias de fútbol robótico.",
            "En el mundo de la programación en Python, la biblioteca TensorFlow se ha convertido en una herramienta imprescindible para construir modelos de IA que pueden analizar datos de rendimiento deportivo con gran precisión.",
            "Los programadores de IA están trabajando en algoritmos avanzados que pueden predecir resultados de juegos deportivos con una precisión sorprendente, lo que está revolucionando la forma en que vemos y apostamos en deportes.",
            "Python es el idioma de la elección para los científicos de datos que desean analizar el rendimiento de los atletas utilizando estadísticas detalladas y modelos de IA.",
            "La combinación de Python y el aprendizaje profundo ha permitido el desarrollo de sistemas de seguimiento de movimiento que mejoran el rendimiento de los atletas en deportes como el ciclismo y la natación.",
            "La inteligencia artificial está cambiando la forma en que se entrenan a los atletas de élite, utilizando datos recopilados por sensores para optimizar sus movimientos y estrategias.",
            "La programación en Python es esencial para construir simuladores deportivos realistas que ayudan a los atletas y equipos a practicar y perfeccionar sus habilidades antes de los grandes eventos."
            ]
        self.text_box.config(state="normal")
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, frases[num_rd])
        self.text_box.config(state="disabled")
    
    def iniciar_prueba(self):
        """
        Funcion para comenzar la prueba de escritura donde cronometrara el tiempo que se tarda en escribir
        la frase generada tal cual esta escrita
        """
        # Obtengo la frase aleatoria
        texto_aleatorio = self.text_box.get("1.0", tk.END)

        # Compruebo que haya frase aleatoria
        if len(texto_aleatorio) == 1:
            messagebox.showerror("Error", "Primero debe de generar una frase aleatoria")
        else:
            # Primero compruebo que no haya nada escrito al comenzar la prueba
            texto_comprobar = self.input_text.get("1.0", tk.END)
            if len(texto_comprobar) != 1:
                messagebox.showerror("Error", "La prueba debe de comenzar con la caja de texto vacia")
            else:
                messagebox.showinfo("Información", "Para finalizar la prueba de escritura pulse INTRO." 
                                    "Si la frase esta escrita correctamente saldra el tiempo que ha tardado " 
                                    "en escribirla, sino le mostrara un mensaje de error diciendo que la frase "
                                    "no esta escrita correctamente.\n\nLA PRUEBA COMIENZA CUANDO PULSE ACEPTAR Y "
                                    "TERMINARA CUNADO APAREZCA EL TIEMPO")
                self.input_text.focus_force()
                self.tiempo_inicio = time.time()
                self.bind('<Return>', self.comprobar_texto)
    
    def comprobar_texto(self):
        print("Has pulsado enter")

if __name__ == "__main__":
    app = PruebaVelocidad()
    app.mainloop()