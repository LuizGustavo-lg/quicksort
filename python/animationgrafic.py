import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches

class AnimationGrafic:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.artics = []
        self.ani = object

        self.color = {"pivo":"red", "itens":"green"}
        
        pivo_legend = mpatches.Patch(color=self.color["pivo"], label="Pivo")
        itens_legend = mpatches.Patch(color=self.color["itens"], label="Valores")
        plt.xlabel("Quicksort")
        self.ax.legend(handles=[pivo_legend, itens_legend])


    def append(self, values, destac):
        '''
        -> Adiciona um novo quadro a lista de animações
        :param values: lista a ser adicionada
        :param destac: indice do elemento em destaque
        '''
        colors = []
        for i in range(len(values)):
            if i == destac: 
                colors.append(self.color["pivo"])
            else:
                colors.append(self.color["itens"])

        container = self.ax.bar(range(len(values)), values, color=colors)
        self.artics.append(container)

    def render(self, interval=400):
        '''
        -> Renderiza todas as interações
        :param interval: tempo (em milisegundos) de cada quadro - defalt=400
        '''
        self.ani = animation.ArtistAnimation(fig=self.fig, artists=self.artics, interval=interval)

    def show(self):
        '''
        -> Exibe o grafico animado
        '''
        plt.show()

    def save(self, name="save.gif"):
        '''
        -> Salva o grafico animado como um .gif
        :param name: nome do arquivo salvo - defalt=save.gif
        '''
        self.ani.save(filename=f"./{name}", writer="pillow")
