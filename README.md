# Sistema de Gestão de Feiras (CRUD)  

## Descrição  
O sistema permite a **divulgação e gestão de feiras**, incluindo o cadastro de expositores e produtos associados. Oferece operações **CRUD (Create, Read, Update, Delete)** para feiras, expositores, produtos e ingressos, com controle de acesso baseado em autenticação de usuários.  

---

## Funcionalidades  

### **Acesso Público (Sem Autenticação)**  
- **Listar feiras**: Exibe o nome de cada feira.  
- **Listar expositores de uma feira**: Exibe o nome dos expositores.  
- **Listar produtos de um expositor**: Exibe o nome dos produtos.  
- **Visualizar detalhes**:  
  - **Feira**: Nome, descrição, datas (início/término), local, cidade e estado.  
  - **Expositor**: Nome, descrição e contato.  
  - **Produto**: Nome, descrição e preço.  

### **Acesso Autenticado**  
- **Gestão de Feiras**:  
  - Criar, editar e excluir feiras.  
- **Gestão de Expositores**:  
  - Criar, editar e excluir expositores.  
- **Gestão de Produtos**:  
  - Criar, editar e excluir produtos associados a expositores.  
- **Gestão de Ingressos**:  
  - Criar, visualizar e excluir ingressos (com dados: nome da feira, número do ingresso e data de emissão).  

---

## Regras do Sistema  
1. **Controle de Acesso**:  
   - Apenas o **criador** de um registro (feira, expositor, produto ou ingresso) pode editá-lo ou excluí-lo.  
2. **Exclusão Condicional**:  
   - Um registro só pode ser excluído se **não houver registros associados** (ex.: não é possível excluir uma feira com expositores cadastrados).  

---

## Tecnologias Utilizadas  
- **Backend**: API RESTful com operações CRUD.  
- **Autenticação**: Sistema de login para acesso às funcionalidades restritas.  
- **Banco de Dados**: Armazenamento de feiras, expositores, produtos e ingressos.  

---
