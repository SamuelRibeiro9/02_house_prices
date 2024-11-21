from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"

# Caminho para os arquivos de dados do projeto
DADOS_ORIGINAIS = PASTA_DADOS / "housing.csv"
DADOS_LIMPOS = PASTA_DADOS / "housing_clean.parquet"
DADOS_GEO_ORIGINAIS = PASTA_DADOS / "california_counties.geojson"
DADOS_GEO_MEDIAN = PASTA_DADOS / "gdf_counties.parquet"

# Caminho para os arquivos de modelos do projeto
PASTA_MODELOS = PASTA_PROJETO / "modelos"
MODELO_FINAL = PASTA_MODELOS / "ridge_polyfeat_target_quantile.joblib"

# Caminhos auxiliares
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"
