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





---

## 📋 Exemplo de Configuração (`config.json`)
O sistema utiliza um arquivo JSON estruturado para gerenciar os alvos de forma desacoplada do código principal:

```json
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
