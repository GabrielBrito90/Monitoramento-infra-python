import time
import logging
from datetime import datetime

# Configuração do sistema de logs (padrão NOC)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def verificar_servidor(servidor_ip):
    """Simula a verificação de ping/latência em um servidor crítico."""
    logging.info(f"Verificando status de conectividade para o IP: {servidor_ip}")
    
    # Simulação de latência de rede estável
    latencia_ms = 24.5
    status = "ONLINE"
    
    return status, latencia_ms

def executar_monitoramento():
    """Loop de monitoramento proativo de infraestrutura."""
    servidores_criticos = ["10.0.1.15 (AWS-Prod-DB)", "10.0.1.20 (AWS-App-API)"]
    
    logging.info("=== INICIANDO VARREDURA DE MONITORAMENTO NOC ===")
    
    for servidor in servidores_criticos:
        status, latencia = verificar_servidor(servidor)
        
        if status == "ONLINE":
            logging.info(f"Servidor {servidor} -> Status: {status} | Latência: {latencia}ms [OK]")
        else:
            logging.warning(f"ALERTA: Servidor {servidor} com falha de resposta! Acionando plantão.")

if __name__ == "__main__":
    executar_monitoramento()
