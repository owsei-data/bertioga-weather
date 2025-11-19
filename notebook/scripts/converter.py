import pandas as pd
import os

# configura caminhos e encoding
DIRETORIO_ORIGEM = os.path.join('data', 'interim')
DIRETORIO_DESTINO = os.path.join('data', 'processed')
CODIFICACAO_ENTRADA = 'latin1'

# define lista de arquivos pra processar
arquivos_base = [f'bertioga-{ano}.CSV' for ano in range(2019, 2026)]

print(f"Iniciando processamento: {DIRETORIO_ORIGEM} -> {DIRETORIO_DESTINO}")
print("-" * 70)

# cria pasta de destino se nao existir
if not os.path.exists(DIRETORIO_DESTINO):
    os.makedirs(DIRETORIO_DESTINO)
    print(f"📁 Diretório '{DIRETORIO_DESTINO}' criado.")

for nome_base in arquivos_base:
    caminho_origem = os.path.join(DIRETORIO_ORIGEM, nome_base)
    caminho_destino = os.path.join(DIRETORIO_DESTINO, nome_base)

    if not os.path.exists(caminho_origem):
        print(f"⚠️ Aviso: Arquivo '{caminho_origem}' não encontrado. Verifique se 'organize_project.sh' foi executado.")
        continue

    try:
        # le o csv corrigindo separador e encoding
        df_temp = pd.read_csv(
            caminho_origem,
            sep=';',
            decimal=',',
            skiprows=8,
            encoding=CODIFICACAO_ENTRADA,
            na_values=['null', 'NaN', ''],
            header=0
        )

        # salva o arquivo limpo em utf8
        df_temp.to_csv(caminho_destino, index=False)

        print(f"✅ Sucesso: '{nome_base}' processado e salvo em 'data/processed/'.")

    except Exception as e:
        print(f"❌ Erro ao processar '{nome_base}': {e}")

print("-" * 70)
print("Conversão concluída. Dados prontos em 'data/processed/'.")
