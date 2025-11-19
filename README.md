# Weather Bertioga (2019–2025) ⛈️

Dataset meteorológico da estação de Bertioga totalmente limpo, padronizado e pronto para uso em modelagem. Sem dores de cabeça com encoding, separadores estranhos ou buracos invisíveis nos dados.

---

## 1. Como usar

Se você quer o **dataset final**, já limpo, é só baixar:

```bash
wget https://raw.githubusercontent.com/owsei-data/bertioga-weather/main/weather-bertioga-2019-2025.csv
```

Ou clique aqui: **weather-bertioga-2019-2025.csv**

---

## 2. Fonte dos dados

Os dados brutos vieram do **INMET – Instituto Nacional de Meteorologia**.

Para transparência, o link da fonte oficial e orientações de download estão registrados em:

📄 `data/raw/reference.txt`

---

## 3. O que foi feito (Step-by-step)

### 🔹 Download e Bagunça Inicial  
- Baixei os zips anuais do INMET e coloquei em `data/raw`.  
- Os arquivos vieram com **encoding Latin-1** e **separador `;`**, o que quebra facilmente ao ler no Python.

### 🔹 Limpeza Pesada  
- Criei um script para padronizar tudo:  
  - converte encoding → UTF-8  
  - ajusta separador  
  - normaliza decimais  
  - salva a versão limpa em `data/processed`  

🛠️ Script utilizado: `scripts/converter.py`

### 🔹 Auditoria e Buracos  
Antes de juntar tudo, fiz uma auditoria exploratória. Achados:  
- 2020 e o fim de 2025 têm **quase sem dados de chuva**.  
- 2023 está **sem dados de vento**.  

📊 Análise completa: `notebooks/data.ipynb`

### 🔹 Resultado Final  
- Unifiquei todos os anos em um único CSV.  
- Apliquei uma **máscara de qualidade**:  
  - se o mês possui < **70% de dados válidos**, recebe `NaN` (evitando enviesar o modelo com valores artificiais).  
- Arquivo final disponível na raiz:  
  - **weather-bertioga-2019-2025.csv**
