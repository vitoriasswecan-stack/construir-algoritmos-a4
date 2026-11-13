from solution import regressao_linear

resultado = regressao_linear("imoveis_lar_perfeito.csv")

print("Coeficientes encontrados:")
print(resultado)

print(
    f"Preço = {resultado[0]:.2f} "
    f"+ {resultado[1]:.2f} * Área "
    f"+ {resultado[2]:.2f} * Quartos"
)