# ✈️ UpSeat

Sistema inteligente de alocação de assentos em aeronaves desenvolvido em Python

## 📋 Sobre o Projeto

O UpSeat é um sistema básico de gerenciamento de assentos para aeronaves, desenvolvido em Python como projeto de estudo. O sistema oferece funcionalidades fundamentais para:

- **Gestão de Aeronaves**: Cadastro simples de aeronaves com modelo e capacidade
- **Controle de Assentos**: Sistema básico de assentos com diferentes classes (Econômica, Executiva)
- **Gestão de Passageiros**: Cadastro de passageiros com informações pessoais
- **Estrutura de Endereços**: Sistema para armazenamento de endereços

## 🏗️ Arquitetura do Sistema

```
fly_alloc/
├── __init__.py          # Inicialização do módulo
├── main.py             # Ponto de entrada da aplicação
├── airplane.py         # Classe para gerenciamento de aeronaves
├── seat.py             # Classe para controle de assentos
├── passager.py         # Classe para gestão de passageiros
├── person.py           # Classe base para pessoas
├── address.py          # Classe para endereços
└── entities/           # Entidades auxiliares
```

## 🚀 Funcionalidades

### ✅ Já Implementadas
- [x] **Sistema de Aeronaves**: Criação básica de aeronaves com modelo e capacidade
- [x] **Gerenciamento de Assentos**: Sistema simples de assentos com classes Econômica e Executiva
- [x] **Cadastro de Passageiros**: Registro básico de passageiros usando herança de classes
- [x] **Sistema de Endereços**: Estrutura básica para armazenamento de endereços
- [x] **Arquitetura Modular**: Organização em classes com separação de responsabilidades

### 🔄 Próximos Passos
- [ ] Sistema de reservas e validação de conflitos
- [ ] Interface de usuário
- [ ] Relatórios de ocupação
- [ ] Persistência de dados

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/UpSeat.git
   cd UpSeat
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Como Usar

### Exemplo Básico

```python
from fly_alloc.airplane import Airplane
from fly_alloc.seat import Seat
from fly_alloc.passager import Passenger
from fly_alloc.address import Address

# Criar uma aeronave
airplane = Airplane(id=1, model="Boeing 737", capacity=30)

# Criar um assento
seat = Seat("1A", "Executiva")

# Criar um passageiro
address = Address("Rua das Flores, 123", "São Paulo", "SP", "01234-567")
passenger = Passenger(1, "João Silva", "123.456.789-00", address, "01/01/1990")

# Alocar assento
passenger.assign_seat("1A")
seat.occupy_seat()

print(f"Passageiro: {passenger}")
print(f"Assento: {seat}")
```

### Executando o Sistema

```bash
python -m fly_alloc.main
```

## 🏷️ Classes Principais

### `Airplane`
**Responsabilidade**: Gerenciamento básico de aeronaves
- Armazenamento de informações do modelo e capacidade
- Estrutura para organização de assentos

### `Seat`
**Responsabilidade**: Representação de assentos individuais
- Controle de estado (disponível/ocupado)
- Classificação por classe de serviço
- Identificação por número/letra

### `Passenger`
**Responsabilidade**: Informações de passageiros
- Herda características básicas de `Person`
- Associação com assentos
- Dados específicos de passageiros

### `Person`
**Responsabilidade**: Classe base para pessoas
- Informações pessoais básicas
- Identificação por CPF
- Dados de contato

### `Address`
**Responsabilidade**: Informações de endereço
- Estrutura para endereçamento
- Dados de localização básicos

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Código
- Siga a PEP 8 para formatação de código Python
- Use type hints quando possível
- Documente métodos e classes
- Escreva testes para novas funcionalidades

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

**Desenvolvedor**: visaoo
**Email**: fillypeoliveira1@gmail.com 
**GitHub**: [@visaoo](https://github.com/visaoo)

## 🎯 Roadmap

- [x] **v1.0**: Sistema básico de alocação
- [ ] **v1.1**: Interface web
- [ ] **v1.2**: API REST completa
- [ ] **v2.0**: Sistema de reservas avançado
- [ ] **v2.1**: Relatórios e analytics
- [ ] **v3.0**: Integração com sistemas externos

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!** 