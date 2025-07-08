# ✈️ UpSeat

Sistema de simulação de alocação de passageiros em voos desenvolvido em Python

## 📋 Sobre o Projeto

O UpSeat é um sistema de simulação que demonstra a alocação automática de passageiros em voos. O sistema gera dados fictícios de voos e passageiros brasileiros e simula o processo de alocação de assentos.

## 🏗️ Estrutura do Projeto

```
fly_alloc/
├── __init__.py          # Inicialização do módulo
├── main.py             # Aplicação principal e simulação
├── airplane.py         # Classe Airplane (aeronaves)
├── flight.py           # Classe Flight (voos)
├── seat.py             # Classe Seat (assentos)
├── passager.py         # Classe Passenger (passageiros)
├── person.py           # Classe Person (base para pessoas)
├── address.py          # Classe Address (endereços)
├── payment.py          # Classe Payment (pagamentos) # Nao implementado
├── database/           # Módulo de banco de dados # Nao implementado
└── tests/              # Testes do sistema
```

## 🚀 Funcionalidades

- **Geração de Voos**: Cria voos aleatórios entre cidades brasileiras
- **Geração de Passageiros**: Utiliza a biblioteca Faker para criar passageiros fictícios
- **Alocação Automática**: Distribui passageiros automaticamente nos voos disponíveis
- **Gerenciamento de Assentos**: Sistema de controle de ocupação de assentos
- **Relatórios**: Exibe estatísticas de alocação e ocupação
- **Dados Brasileiros**: Utiliza cidades, CEPs e dados realistas do Brasil

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior

### Passos para instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/visaoo/UpSeat.git
   cd UpSeat
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requiriments.txt
   ```

## 💻 Como Usar

Execute o sistema de simulação:

```bash
cd fly_alloc
python main.py
```

O sistema irá:
1. Criar 10 voos aleatórios entre cidades brasileiras
2. Gerar 250 passageiros fictícios
3. Alocar automaticamente os passageiros nos voos
4. Exibir relatório final com estatísticas

## 📊 Exemplo de Saída

```
🚀 SISTEMA DE ALOCAÇÃO DE PASSAGEIROS
==================================================

📋 Criando 10 voos...
Voo A1234BC-0: São Paulo (SP) → Rio de Janeiro (RJ) | ✅ COM TRIPULAÇÃO
Voo B5678DE-1: Brasília (DF) → Salvador (BA) | ✅ COM TRIPULAÇÃO
...

👥 Criando 250 passageiros...

🎯 Alocando passageiros (apenas em voos COM TRIPULAÇÃO)...
✅ Maria Silva → Voo A1234BC-0, Assento 1
...

📊 RESUMO
============================================================
👥 Passageiros alocados: 250/250
🛫 Total de voos: 10
✅ Voos com tripulação: 10
❌ Voos sem tripulação: 0
🎯 Taxa de alocação: 100.0%
```

## 🏷️ Classes Principais

### `Flight`
Representa um voo específico com origem, destino e aeronave associada.

### `Airplane` 
Representa uma aeronave com capacidade de assentos e status de tripulação.

### `Passenger`
Representa um passageiro com informações pessoais e herda de `Person`.

### `Seat`
Representa um assento individual com status de ocupação.

### `Address`
Representa endereços com informações de localização.

## 🧪 Testes

Execute os testes disponíveis:

```bash
cd fly_alloc/tests
python testing.py
```

## 📋 Dependências

- **Faker**: Geração de dados fictícios brasileiros

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

**Desenvolvedor**: visaoo  
**Email**: fillypeoliveira1@gmail.com  
**GitHub**: [@visaoo](https://github.com/visaoo) 