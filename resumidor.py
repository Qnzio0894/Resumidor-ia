import anthropic

client = anthropic.Anthropic(api_key="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")

def resumir(texto):
    mensaje = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"Resumí el siguiente texto de forma clara y concisa en español:\n\n{texto}"
            }
        ]
    )
    return mensaje.content[0].text

print("=== RESUMIDOR CON IA ===")
print("Pegá o escribí el texto que querés resumir.")
print("Cuando termines, presioná Enter dos veces.")
print("")

lineas = []
while True:
    linea = input()
    if linea == "":
        break
    lineas.append(linea)

texto = "\n".join(lineas)

if texto.strip() == "":
    print("No escribiste ningún texto.")
else:
    print("\nGenerando resumen...")
    resumen = resumir(texto)
    print("\nRESUMEN:")
    print(resumen)