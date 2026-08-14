# 🛡️ Monitor Proativo de Infraestrutura e Serviços (NOC)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Domain-NOC_%2F_DevOps-orange.svg" alt="Domain">
  <img src="https://img.shields.io/badge/Status-Active-success.svg" alt="Status">
</p>

## 🎯 Sobre o Projeto
Script em Python desenvolvido para o monitoramento proativo de infraestrutura, redes e serviços de missão crítica (Ambiente NOC). A ferramenta realiza checagens automatizadas de disponibilidade (*uptime/downtime*), latência e integridade de servidores ou aplicações, registrando eventos para auditoria rápida e prevenção de falhas sistêmicas.

---

## 🏗️ Arquitetura de Monitoramento
O fluxo operacional do script simula a rotina de um Centro de Operações de Rede (NOC):

```mermaid
graph LR
    A[Alvos / Servidores / Endpoints] -->|Requisições de Teste| B(Script de Monitoramento Python)
    B -->|Análise de Status & Latência| C{Condição OK?}
    C -->|Sim| D[Log de Sucesso / Normalidade]
    C -->|Não| E[Geração de Alerta / Registro de Incidente]
C -->|Sim| D[Log de Sucesso / Normalidade]
    C -->|Não| E[Geração de Alerta / Registro de Incidente]

📦 Monitoramento-infra-python
 ┣ 📂 logs           # Diretório de armazenamento de logs de execução
 ┣ 📂 src
 ┃ ┣ 📜 checker.py   # Lógica principal de verificação de hosts e serviços
 ┃ ┗ 📜 logger.py    # Módulo de estruturação e salvamento de logs
 ┣ 📜 config.json    # Arquivo de configuração de alvos e timeouts
 ┣ 📜 main.py        # Ponto de entrada do script de monitoramento
 ┣ 📜 requirements.txt
 ┗ 📜 README.md

{
  "targets": [
    {
      "name": "Servidor de Produção Principal",
      "type": "http",
      "endpoint": "[https://api.exemplo.com/health](https://api.exemplo.com/health)",
      "timeout_seconds": 5
    },
    {
      "name": "Banco de Dados Central",
      "type": "ping",
      "host": "192.168.1.10",
      "timeout_seconds": 3
    }
  ]
}

[2026-08-14 18:30:15] [INFO] Iniciando varredura de alvos monitorados...
[2026-08-14 18:30:15] [SUCCESS] Target 'Servidor de Produção Principal' [HTTP] - Status: 200 OK - Latência: 120ms
[2026-08-14 18:30:16] [SUCCESS] Target 'Banco de Dados Central' [PING] - Status: Online - Latência: 15ms
[2026-08-14 18:30:16] [INFO] Ciclo de monitoramento finalizado com sucesso. Nenhum incidente detectado.


