# Script para gerar configurações do WhatsApp Business para Pousada Praia de Ponta Negra
# Rode com: python gerador_mensagens.py
# Ajuste as variáveis abaixo se precisar mudar algo

# Dados da pousada
nome_pousada = "Pousada Praia de Ponta Negra"
endereco = "Rua Luiz Estevam, 2277 – Vila de Ponta Negra, Natal/RN"
link_maps = "https://maps.app.goo.gl/SiKSsQR7CaRCb42V9"
link_reserva = "https://bookings.hospedin.com/pousada-praia-da-ponta-negra"
link_canva = "https://pousadapraiadepontanegra.my.canva.site/"
pix_chave = "84 99608-5491"
pix_titular = "Giuliano Liciardi (Banco Neon)"
link_insta = "https://www.instagram.com/pousadapraiadpontanegra/"

# Respostas rápidas (atalho: mensagem)
respostas_rapidas = {
    "ola": f"Olá! 😊 Bem-vindo(a) à {nome_pousada}! Como podemos ajudá-lo(a) hoje?",
    "local": f"Estamos na {endereco}, a 5 minutos da praia! 🗺️ {link_maps}",
    "horario": "🕒 Check-in: a partir das 14h 🕛 Check-out: até às 12h. Precisa de horário especial? Avise-nos com antecedência! 😊",
    "servicos": "Oferecemos: ✅ Wi-Fi gratuito ✅ Piscina ✅ Estacionamento ✅ Localização a metros da praia! Quer saber mais sobre algo específico?",
    "reservar": f"Faça sua reserva rapidinho aqui: 🔗 {link_reserva} Ou veja fotos e detalhes: {link_canva}",
    "pix": f"💳 PIX para reserva/pagamento: {pix_chave} Titular: {pix_titular}",
    "insta": f"Siga a gente para ver fotos da pousada e ofertas! 🌴 → {link_insta}",
    "obrigado": f"Agradecemos seu contato! 😊 Esperamos você em breve na {nome_pousada}! Qualquer dúvida, é só chamar."
}

# Mensagens automáticas
saudacao = f"""
Olá! 👋 Bem-vindo(a) à {nome_pousada}!
Estamos a poucos metros da praia, com Wi-Fi, piscina e estacionamento gratuitos.

💬 Digite:
• reservar para fazer sua reserva
• local para ver nossa localização
• servicos para saber o que oferecemos

Em breve te responderemos! 😊
"""

ausencia = f"""
Olá! 👋
No momento estamos fora do expediente, mas retornaremos seu contato em breve — geralmente em até 12 horas.

Enquanto isso, você pode:
• Fazer sua reserva: {link_reserva}
• Ver fotos no Instagram: {link_insta}

Agradecemos seu interesse! 😊
"""

# Gera o arquivo de saída
with open("whatsapp_config.txt", "w", encoding="utf-8") as file:
    file.write("# Respostas Rápidas\n\n")
    for atalho, msg in respostas_rapidas.items():
        file.write(f"Atalho: {atalho}\nMensagem: {msg}\n\n")
    
    file.write("# Mensagem de Saudação\n")
    file.write(saudacao + "\n\n")
    
    file.write("# Mensagem de Ausência\n")
    file.write(ausencia + "\n\n")
    
    file.write("# Pronto! Copie e cole no WhatsApp Business.")

print("Script rodado! Arquivo 'whatsapp_config.txt' gerado. Abra e copie para o app.")
