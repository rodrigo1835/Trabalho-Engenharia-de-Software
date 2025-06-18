# Documento de Visão e Escopo

## 1. Introdução
O documento de visão tem como objetivo definir o escopo e o propósito do sistema de gerenciamento de feiras.
Ele estabelece expectativas claras quanto às funcionalidades do produto, visando reduzir riscos no desenvolvimento e garantir um alinhamento entre as necessidades dos usuários e as soluções oferecidas. 

## 1.1. Escopo
O sistema de gerenciamento de feiras tem como objetivo principal facilitar a organização, divulgação e participação em eventos do tipo feira, permitindo que usuários realizem o gerenciamento completo de feiras, expositores, produtos e ingressos.

O sistema fornece funcionalidades, acessíveis para qualquer usuario interessados, como listar feiras cadastradas, visualizar suas informações, expositores que iram participar e produtos que estão disponíveis. Usuários autenticados terão poderes especiais como o cadastro, edição e exclusão de feiras, expositores e produtos, e também a gestão de ingressos.

Cada elemento (feira, expositor, produto ou ingresso) será vinculado ao usuário que o criou, assim garatindo que apenas o usuário que a criou possa fazer alterações ou exclusões.

O escopo do projeto abrange:
* Cadastro e autenticação de usuários.

* Gerenciamento de feiras(**CRUD**).

* Gerenciamento de expositores vinculados a feiras (**CRUD**).

* Geração e gerenciamento de ingressos(**CRUD limitado**).

* Visualização pública de informações básicas (**feiras, expositores, produtos**).

* Restrições de autorização e regras de negócio conforme especificado.

Este escopo não contempla funcionalidades de pagamento, integração com plantaformas externas ou personalização de layout por usuário. O foco princial está na entrega de um sistema funcional e de fácil utilização.

## 2. Análise de Contexto

A organização de feiras e eventos de pequeno e médio porte ainda é , em muitos casos, realizada por meio de ferramentas genérica como planilhas, e-mails e sistemas desconectados. Isso gera dificuldades na gestão de participantes, divulgação e controle de acessos. Além disso, expositores e visitantes muitas vezes não possuem um canal centralizado para obter informações ou gerenciar suas interações com a feira.

Diante desse cenário, surge a necessidade de um sistema que centraliza e automatize as operações relacionadas à organização e participação em feiras.

## 2.1. Detalhamento da Necessidade

Como descrito acima surge a necessidade de um sistema que centralize tudo e permita que:

* Criar e gerencia feiras de forma simples;

* Cadastrar expositores e seus produtos;

* Gerar e controlar ingressos de acesso;

* Permitir a visualização das informações da feira;

* Garantir que apenas usuários autenticados e autorizados possam editar ou excluir dados.

Esse sistema é necessário para melhorar a organização das feiras, profissionalizar a divulgação e permitir um experiência mais eficiente para usuários e expositores. 

## 2.1.1 Descrição do Problema

Os organizadores de feiras enfrentam problemas na gestão manual de expositores, produtos e acessos, o que pode gerar confusões, retrabalho e perda de dados. Já os visitantes, por sua vez, tem acesso limitado ou muita vezes desorganizado às informações relevantes. A ausência de um sistema centralizado dificulta a claridade e o controle de dados, o que impacta diretamente a qualidade e a experiência.

**Exemplo:** um organizador precisa divulgar rapidamente uma mudança de horário na feira, mas como usa apenas planilhas e e-mail, a informação não chega a todos os participantes de forma eficiente.

## 2.1.2. Partes afetadas

* **Organizadores de Feiras**: Tem dificuldade para cadastrar e controlar expositores e ingressos.

* **Expositores**: Não tem um canal prático para divulgar seus produtos e informações.

* **Visitantes**: Enfrentam dificuldades para encontrar dados de expositores, produtos ou acessar eventos.

## 2.1.3. Impacto

A falta de um sistema especéfico e centralizado causa:

* Baixa eficiência na organização de eventos;
* Dificuldade na comunição entre organizadores e expositores;
* Perda de tempo com atividades manuais repetitivas;
* Experiência fragmentada e pouco atrativa para os visistantes;
* Maior risco de erros e perda de dados importantes.

## 2.1.4 Requisitos para uma Solução Eficaz

Uma solução de sucesso deve seguir os seguintes artefatos:

* Permitir autenticação de usuários e controle de permissões;
* Viabilizar operações de CRUD para feiras, expositores, produtos e ingressos;
* Possibilitar a visualização de feiras, expositores e produtos;
* Impedir alterações não autorizadas;
* Ser intuitiva e acessível;

## 2.2. Alternativas

Alternativa    | Pontos Fortes                     | Pontos fracos
-------------- | -------------                     | --------------
Google Forms   |  Gratuito, fácil de configurar.   | Falta de controle de acesso, não escalável, visualização limitada.
Sympla         | Robusto, pronto para uso          | Custo mensal, funcionalidades genéricas, pouca personalição.
Organização Manual | Sem custos imediatos | Ineficiente, propenso a erros, inviável para eventos maiores.
Sistema Proposto | Personalizado, alinhado às regras de negócios, completo. | Exige tempo de desenvolvimento e testes.

## 3. Partes Interessadas

Nesta parte do sistema estamos interessados em identifica as pessoas e entitades que possuem algum interesse no sistema, seja por serem afetadas por eles, por tomarem decisões durante o projeto ou serem usuários finais.


Unidade | Representante | Envolvimento com o projeto
------- | ------------- | --------------------------
Disciplina Eng. de Software | Prof. Fernando Chacon | Responsável por supervisionar o projeto e avaliar os resultados com os critérios da disciplina.
Equipe de desenvolvimento | Rodrigo Reis | Responsável por levantes requisitos, projetar, implementar e testar o sistema.
Usuários fictícios | Representados por personas desenvolvidas | Representam os papéis de expositores, visitantes e organizadores de feiras.

## 3.1. Usuários

Vamos classificar os tipos de usuários que utilizam o sistema, com base em seus perfis e responsabilidade. Esses usuários representam papéis que ajudam a dfinir a funcionalidade e usabilidade do sistema.

Tipo de usuário | Representante | Descrição | Responsabilidades
--------------- | ------------- | --------- | -----------------
Administrador | Persona simulada com acesso especial | Responsável pela gestão completa da feira e gerenciamento de expositores e ingressos. | Criar feiras, cadastrar expositores.
Expositor | Persona simulada | Representa empresas ou invíduos que desejam vender ou divulgar seus produtos. | Cadastrar produtos, atualizar e excluir.
Visitante | Persona simulada | Usuário comum interessado em visitar feiras e adquirir produtos ou ingressos. | Visualizar feiras disponíveis, adquirir ingressos.

## 4. Visão Geral do Produto
O sistema de gerenciamento de feiras é uma aplicação desenvolvida com o objetivo de auxiliar na organização, divulgação e acompanhamento de eventos do tipo feira. Ele se propõe a centralizar as principais atividades envolvidas nesse processo em uma única plataforma digital, intuitiva e acessível.

A proposta do sistema é atender a três perfis principais de usuários: organizadores, expositores e visitantes. Cada um desses perfis terá acesso a funcionalidades específicas, conforme suas responsabilidades e necessidades dentro do contexto de uma feira.

Organizadores poderão cadastrar novas feiras, gerenciar expositores e controlar os ingressos disponíveis.

Expositores poderão se associar a feiras existentes e cadastrar os produtos que pretendem apresentar ou vender.

Visitantes poderão visualizar as feiras abertas, conhecer os expositores e os produtos, além de acessar ou adquirir seus ingressos.

O sistema oferecerá funcionalidades básicas de autenticação de usuários, controle de acesso, gerenciamento de dados e exibição de informações. Seu funcionamento será guiado por regras de negócio simples, que garantem a organização e clareza na navegação.

A plataforma será desenvolvida com foco em usabilidade, clareza visual e objetividade, visando proporcionar uma boa experiência tanto para quem organiza o evento quanto para quem participa.


## 4.1 Objetivos de Negócio

O sistema de gerenciamento de feiras tem como finalidade atender às necessidades práticas dos usuários envolvidos na organização e participação de eventos.

O principal objetivo é centralizar e simplificar a gestão de feiras, substituindo processos manuais e descentralizados por uma solução digital integrada.

O sistema visa substituir processos manuais, descentralizados e sujeito a erros (**Como o uso de planilhas e e-mails**) por uma solução mais centralizada. Isso permite um melhor planejamento, uma comunicação mais clara entre as partes envolvidas e uma experiência mais profissional para os expositores e visitantes.

### **Objetivos principais**
* **Centralizar a gestão de feiras** em uma plataforma única, reduzindo o uso de ferramentas desconectadas como planilhas e e-mais.
* **Reduzir o retrabalho** e melhorar o fluxo de organização.
* **Facilitar a comunicação** entre a feira, expositores e visitantes.
* **Fornecer uma experiência** organizada e acessível para todos as entidades.

## 5. Requisitos de Alto Nível

Nesta seção vão ser apresentados os principais requisitos que o sitema deve atender, sem ainda entrar em detalhes técnicos ou funcionais. Esses requisitos representam as principais capacidades esperadas dos sitema e estão alinhas às necessidades identificadas anteriormente neste documento.

### O Sistema deve permitir:
* Autenticação e controle de acesso conforme o tipo de usuário (administrador, expositor ou visitante), garantindo que cada um tenha acesso apenas às funcionalidades que lhe são pertinentes.

* Cadastro completo de feiras, incluindo informações como nome, data e descrição, com a possibilidade de edição e exclusão.

* Gerenciamento de expositores, vinculando-os às feiras cadastradas, com informações como nome do expositor, descrição, contato e produtos oferecidos.

* Cadastro e visualização de produtos, permitindo que expositores possam incluir os produtos que serão exibidos durante o evento.

* Geração e controle de ingressos, com funcionalidades básicas para criação e vinculação a feiras, e possibilidade de visualização e exclusão.

* Visualização de feiras, expositores e produtos, mesmo para usuários não autenticados.

* Interface simples, com navegação intuitiva, que permita o uso do sistema sem necessidade de treinamento prévio.

* Restrições de edição e exclusão, garantindo que apenas o usuário que criou determinado conteúdo possa modificá-lo ou removê-lo, respeitando regras de segurança e consistência dos dados.