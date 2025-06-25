# Requisitos Não Funcionais

## Qualidade do Sistema
### Usabilidade

* O sistema deve ser intuitivo e de fácil navegação, mesmo para usuários com pouco experiência em sistemas web.
* Deve possuir interface acessívell em computadores e dispositivos móveis.
* O tempo de aprendizado para novos usuários deve ser rápido.
* Textos, botões e quaisquer mensagens devem estar em português e utilizar uma linguagem clara.
* Deve seguir padrões de acessibilidade, como tamanho mínimo de fonte.

### Confiabilidade
* O sistema deve apresentar disponibilidade mínima de 99% durante o período de uso simulado.
* Em caso de falha o sistema deve exibir um alerta para evitar a perda de dados.
* O sistema deve manter consistência dos dados em todas as operações, mesmo em caso de falhas inesperadas.
* Todos os dados que forem inseridos devem ser validados antes do armazenamento no banco de dados.

### Desempenho
* As páginas devem ser carregas em no máximo 5 segundos em redes comuns.
* O sistema deve suportar ao menos 10 usuários simultâneos sem perda perceptível da performance.
* Operações de crud devem ser concluídas em menos de 2 segundos em condições normais de uso.

### Suporte e Manutenibilidade
* O sistema deve ser desenvolvido com código limpo com boas práticas de programação, para facilitar a manutenção e evolução.
* Deve ser compatível com navegadores modernos(Chrome, Firefox, Edge).
* O banco de dados e as tecnologias devem permitir escalabilidade futura.
* O sistema deve permitir fácil configuração em ambientes locais de teste.

## Interfaces do Sistema
### Interface com o Usuário
* A interface deve seguir um padrão visual consistente em todas as páginas.
* O sistema deve fornecer feedback imediato após ações do usuário (ex: criação de feira).
* Todos os elementos devem seguir padrão de cores e estilo definidos.
* O sistema deve possuir navegação clara entre as seções: Feira, Expositores, Produtos e ingressos.

### Aparência
* A interface deve apresentar um visual limpo e moderno, com destaque para os elementos principais (Nome da feira, botão de ações e etc).
* O layout deve priorizar a simplicidade.
* Devem ser utilizadas cores neutros com destaque para elementos interativos.

### Layout e Navegação
* O menu de navegação deve estar em todas as páginas.
* Páginas de CRUD devem seguir estrutura similiar.
* Listagens devem conter filtros e botões de edição/exclusão.

### Consistência 
* Os mesmos termos e padrões de interação devem ser utilizados em todas as telas (ex: "Salvar" sempre com o mesmo estilo).
* O mesmo fluxo de uso deve ser mantido entre diferentes módulos (feiras, expositores e produtos).

### Personalização
* O sistema não permitirá personalização visual ou funcional por parte do usuário, mas poderá exibir dados personalizados com base no login(ex: Feiras criadas pelo usuário).

## Interfaces com Sistemas Externos
* Nenhum sistema externo será integrado ao sistema proposto.
* O sistema não exige dispositivos específicos, sendo acessível via navegador padrão.

### Interfaces de Software
* O sistema será desenvolvido utilizando framework web padrão.
* O banco de dados será acessado por ORM ou via SQL diretamente, com camadas separadas de lógica de negócio.

### Interfaces de Hardware
* Não há exigências específicas de hardware. O sistema será acessado de um navegador web comum.
* Para o ambiente de desenvolvimento/teste, basta apenas um computador com acesso a red e um navegador instalado.

## Regras de Negócio
* Apenas o usuário que criou um registro (feira, expositor, produto, ingresso) poderá editá-lo ou excluí-lo.

* Um registro só pode ser excluído se não houver dependências (ex: uma feira só pode ser excluída se não houver expositores nela).

* Ingressos são válidos apenas para a data de emissão.

* Um usuário precisa estar autenticado para cadastrar ou modificar qualquer entidade.

* A listagem de feiras, expositores e produtos é pública, mas operações de modificação exigem login.

### Restrições do Sistema
* O sistema deve ser desenvolvidocom com framework voltado para web.

* O banco de dados a ser utilizado será SQLite.

* O sistema deve ser compatível com navegadores modernos (Chrome, Firefox, Edge).

* O sistema será utilizado apenas em ambiente acadêmico, sem necessidade de publicação pública.

## Conformidade do Sistema
### Requisitos de Licenciamento
* O sistema será de uso exclusivo acadêmico.

* Não haverá necessidade de gerenciamento de licenças ou autenticação externa.

### Avisos Legais e Direitos Autorais
* Todo o conteúdo do sistema será fictício utilizado apenas para fins acadêmicos.

* Não haverá integração com dados reias de usuários ou feiras existentes.

### Padrões Aplicáveis
* O projeto seguirá padrões básicos de desenvolvimento web.
* A estrutura e documentação seguirão modelos típicos de engenharia de software, incluindo modelos de visão, casos de uso e etc.

### Documentação do Sistema
* O sistema conterá documentação mínima voltada para o usuário.
* A documentão técnica estará disponível como parte do material do projeto, incluindo README e comentários no código.