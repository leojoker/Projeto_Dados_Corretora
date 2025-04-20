# 🛣️ Roadmap - Projeto de Análise de Leads da Corretora

Este roadmap define as próximas etapas para o crescimento, automação e visualização de dados neste projeto.

## ✅ Etapas concluídas
- [x] Estrutura de diretórios criada (Data/RAW, PROCESSED, FINAL)
- [x] Notebook de ETL estruturado com pathlib e funções auxiliares
- [x] Módulos utilitários criados (paths.py, io.py)
- [x] Arquivos CSV gerados com dados simulados realistas
- [x] Estrutura de documentação criada (README, estrutura.md)
- [x] Início do dashboard em Streamlit

---

## 🔜 Próximas etapas
- [ ] Criar gráficos no Streamlit: funil de conversão, barras por canal, mapa de calor por país
- [ ] Adicionar filtros interativos (origem, país, status)
- [ ] Análise exploratória por cohort (tempo de cadastro x conversão)
- [ ] Implementar modelos de previsão de conversão e churn
- [ ] Integração com repositório GitHub e deploy do app

---

## 💡 Ideias futuras
- Conexão direta com banco de dados ou CRM real
- Automatização do ETL com agendamento (Airflow ou crontab)
- Enriquecimento dos dados com fontes externas (país, dispositivo, comportamento)
- Dashboard comparativo de campanhas de marketing
