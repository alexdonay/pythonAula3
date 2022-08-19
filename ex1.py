class ponto:
    x: float
    y: float
    coordenadas: str
    def __init__(self, coordenadas: str):
        self.coordenadas = coordenadas
        self.x = float(coordenadas.split(",")[0])
        self.y = float(coordenadas.split(",")[1])
    def pede(self):
        coordenadas = str(input("Digite as coordenadas do ponto (no formato x,y): "))
        self.x = float(coordenadas.split(",")[0])
        self.y = float(coordenadas.split(",")[1])

class segmento:
    x1: float
    x2: float
    y1: float
    y2: float
    def __init__(self, pontoA: ponto, pontoB: ponto):
        self.x1 = pontoA.x
        self.x2 = pontoB.x
        self.y1 = pontoA.y
        self.y2 = pontoB.y
    def tamanho(self):
        return calculaHipotenusa(abs(self.x1-self.x2), abs(self.y1-self.y2))

def calculaHipotenusa(a, b):
    return pow(pow(a,2) + pow(b, 2),1/2)

def verificaTriangulo(seg1, seg2, seg3): 
    return seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2

ponto1 = ponto("0,0")
ponto2 = ponto("0,0")
ponto3 = ponto("0,0")
ponto1.pede()
ponto2.pede()
ponto3.pede()
seg1 = segmento(ponto1, ponto2)
seg2 = segmento(ponto2, ponto3)
seg3 = segmento(ponto1, ponto3)
if verificaTriangulo(seg1.tamanho(), seg2.tamanho(), seg3.tamanho()):
    print("Os segmentos formam um triangulo") 
    if seg1 == seg2 == seg3:
        print("É um triângulo equilátero")
    elif calculaHipotenusa(seg1, seg2) == seg3 or calculaHipotenusa(seg1, seg3) == seg2 or calculaHipotenusa(seg2, seg3) == seg1:
        print("É um triângulo Retangulo")
    elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
        print("É um triângulo isósceles")
    elif seg1 != seg2 != seg3:
        print("É um triângulo escaleno")

else: print("Não é um triângulo")
