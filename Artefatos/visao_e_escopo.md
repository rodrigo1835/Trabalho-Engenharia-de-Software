# Documento de Visão e Escopo

## 1. Introdução
O documento de visão tem como objetivo definir o escopo e o propósito do sistema de gerenciamento de feiras.
Ele estabelece expectativas claras quanto às funcionalidades do produto, visando reduzir riscos no desenvolvimento e garantir um alinhamento entre as necessidades dos usuários e as soluções oferecidas. 

## 1.1. Escopo
O sistema de gerenciamento de feiras tem como objetivo principal facilitar a organização, divulgação e participação em eventos do tipo feira, permitindo que usuários realizem o gerenciamento completo de feiras, expositores, produtos e ingressos.

O sistema fornece funcionalidades, acesíveis para qualquer usuario interessados, como listar feiras cadastradas, visualizar suas informações, expositores que iram participar e produtos que estão disponíveis. Usuários autenticados terão poderes especiais como o cadastro, edição e exclusão de feiras, expositores e produtos, e também a gestão de ingressos.

Cada elemento (feira, expositor, produto ou ingresso) será vinculado ao usuário que o criou, assim garatindo que apenas o usuário que a criou possa fazer alterações ou exlusões.

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

Diante desse cenário, surge a necessidade de um sistema que centraliza e automatizes as operações relacionadas à organização e participação em feiras.

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

## 2.1.2. Partes afetadas

* **Organizadores de Feiras**: Tem dificuldade para cadastrar e controlar expositores e ingressos.

* **Expositores**: Não tem um canal prático para divulgar seus produtos e informações.

* **Visitantes**: