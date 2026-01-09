import serial
import math
import asyncio
import time
import random
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent, GiftEvent, JoinEvent

# --- CONFIGURAÇÃO SERIAL --- Verifique a porta COM correta para o seu Arduino
PORTA_COM = 'COM9' 
try:
    ser = serial.Serial(PORTA_COM, 115200, timeout=0.1)
    time.sleep(2) # Aguarda o bootloader do Arduino
    print(f"✅ [SISTEMA] Arduino conectado em {PORTA_COM}")
except Exception as e:
    print(f"❌ [ERRO] Arduino não encontrado: {e}")
    ser = None

def send_to_arduino(s1, s2, led):
    if ser:
        comando = f"{s1},{s2},{led}\n"
        ser.write(comando.encode())

# --- DANÇAS ELABORADAS (INTELIGÊNCIA NO PYTHON) ---

async def danca_rosa():
    print("🌹 [DANÇA] Executando coreografia da Rosa...")
    for _ in range(20):
        send_to_arduino(random.randint(0,180), random.randint(0,180), 3)
        await asyncio.sleep(0.5)
    send_to_arduino(30, 90, 0)
    await asyncio.sleep(0.5)
    send_to_arduino(120, 60, 1)
    await asyncio.sleep(0.5)
    send_to_arduino(0, 90, 0)
    await asyncio.sleep(0.5)
    send_to_arduino(60, 120, 1)
    await asyncio.sleep(0.5)
    send_to_arduino(96, 90, 0)

async def danca_infinito():
    print("♾️ [DANÇA] Executando movimento Infinito...")
    for i in range(120):
        # S1 e S2 se movem em espelho usando seno e cosseno
        angulo_s1 = 90 + 80 * math.sin(i * 0.1)
        angulo_s2 = 90 + 80 * math.sin(i * 0.1 + math.pi) 
        led = 1 if angulo_s1 > 90 else 2
        send_to_arduino(angulo_s1, angulo_s2, led)
        await asyncio.sleep(0.2)

    # Parte 2: O "Grand Finale"
    for _ in range(3):
        send_to_arduino(0, 180, 3)
        await asyncio.sleep(0.3)
        send_to_arduino(180, 0, 3)
        await asyncio.sleep(0.3)

    send_to_arduino(90, 90, 0)

async def danca_coracao():
    print("❤️ [DANÇA] Executando batida do Coração...")
    for _ in range(3):
        send_to_arduino(110, 70, 2) # Contração
        await asyncio.sleep(0.5)
        send_to_arduino(70, 110, 2) # Expansão
        await asyncio.sleep(0.5)
    send_to_arduino(90, 90, 0)

async def danca_especial():
    print("🎉 [DANÇA] Comemoração Aleatória!")
    for _ in range(20):
        send_to_arduino(random.randint(0,180), random.randint(0,180), 3)
        await asyncio.sleep(0.5)
    send_to_arduino(30, 90, 0)
    await asyncio.sleep(0.5)
    send_to_arduino(120, 60, 1)
    await asyncio.sleep(0.5)
    send_to_arduino(0, 90, 0)
    await asyncio.sleep(0.5)
    send_to_arduino(60, 120, 1)
    await asyncio.sleep(0.5)
    send_to_arduino(96, 90, 0)

# --- EVENTOS TIKTOK ---
client = TikTokLiveClient(unique_id="@wagnermaker")
# Evento de entrada de usuário (desativado para evitar spam)

# @client.on(JoinEvent)
# async def on_join(event: JoinEvent):
#     print(f"👤 [JOIN] {event.user.nickname}")
#     send_to_arduino(120, 60, 1)
#     await asyncio.sleep(1)
#     send_to_arduino(90, 90, 0)

@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    print(f"💬 [CHAT] {event.user.unique_id}: {event.comment}")
    
    # Feedback visual rápido no LED para qualquer comentário
    # The code snippet 
    # send_to_arduino(0, 10, 1)` followed by `await asyncio.sleep(0.5)` and then
    #send_to_arduino(90, 90, 0)
    # send_to_arduino(0, 10, 1)
    # await asyncio.sleep(0.5) 
    
    comentario = event.comment.lower()
    if "dança" in comentario or "danca" in comentario:
        await danca_especial()
    if "rosa" in comentario:
        await danca_rosa()
    if "coração" in comentario or "coracao" in comentario:
        await danca_coracao()
    if "especial" in comentario:
        await danca_especial()
    if "infinito" in comentario:
        await danca_infinito()


@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    nome_presente = event.gift.name.lower()
    print(f"🎁 [GIFT] {event.user.nickname} enviou {event.gift.name}")

    if "rose" in nome_presente or "rosa" in nome_presente:
        await danca_rosa()
    elif "heart" in nome_presente or "coração" in nome_presente:
        await danca_coracao()
    else:
        await danca_especial()

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    print("🚀 [SISTEMA] Iniciando monitoramento da Live...")
    try:
        client.run()
    except KeyboardInterrupt:
        print("\n🛑 [SISTEMA] Encerrando...")
        if ser:
            send_to_arduino(90, 90, 0) # Reseta posição antes de sair
            ser.close()