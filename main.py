import csv
from matplotlib.pyplot import close

with open("pcWmi.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")
    arquivoSaida = open("pcWmi.sql", "w")

    for i, linha in enumerate(arquivo_csv):
        if i > 0:
            arquivoSaida = open("pcWmi.sql", "a")
            arquivoSaida.write("INSERT INTO `wmi_infra`.`computador` (`tipoArmazenamento`, `armazenamentoTotal`, `sistemaOperacional`, `modeloCpu`, `modeloGpu`, `observacao`, `num`, `memRam`) VALUES ('" +
                               linha[0]+"', '"+linha[1]+"', '"+linha[2]+"', '"+linha[3]+"', '"+linha[4]+"', '"+linha[5]+"', '"+linha[6]+"', '"+linha[7]+"');")
            arquivoSaida.write('\n')
            arquivoSaida = close()
