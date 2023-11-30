import os
import random

def gerar_grafo(num_vertices=1000, num_arcos=1000, peso_max=999):
    # Inicializa o grafo com dois vértices conectados
    grafo = {1: [2], 2: [1]}
    arcos = [(1, 2, random.randint(1, peso_max))]

    for i in range(3, num_vertices + 1):
        # Escolhe um vértice para conectar com base na distribuição de grau
        vertices = list(grafo.keys())
        graus = [len(grafo[v]) for v in vertices]
        total_graus = sum(graus)
        probabilidades = [grau / total_graus for grau in graus]
        v = random.choices(vertices, probabilidades)[0]

        # Adiciona o novo vértice ao grafo
        grafo[v].append(i)
        grafo[i] = [v]
        arcos.append((v, i, random.randint(1, peso_max)))

    # Adiciona arcos adicionais aleatoriamente
    while len(arcos) < num_arcos:
        origem = random.randint(1, num_vertices)
        destino = random.randint(1, num_vertices)
        if origem != destino and destino not in grafo[origem]:
            grafo[origem].append(destino)
            grafo[destino].append(origem)
            arcos.append((origem, destino, random.randint(1, peso_max)))

    return arcos

def salvar_grafo(arcos, nome_arquivo='teste.gr'):
    with open(nome_arquivo, 'w') as f:
        # Adiciona 6 linhas vazias no início do arquivo
        for _ in range(6):
            f.write('\n')

        # Escreve os arcos a partir da 7ª linha
        for arco in arcos:
            f.write(f'a {arco[0]} {arco[1]} {arco[2]}\n')

def main():
    # Apaga o arquivo anterior se existir
    if os.path.exists('teste.gr'):
        os.remove('teste.gr')

    # Gera o grafo e salva no arquivo
    arcos = gerar_grafo()
    salvar_grafo(arcos)

if __name__ == '__main__':
    main()