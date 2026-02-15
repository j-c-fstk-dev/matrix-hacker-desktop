# Contributing to Matrix Hacker Desktop

Obrigado por considerar contribuir para o Matrix Hacker Desktop! 🟢

## Como Contribuir

### Reportar Bugs
- Use a aba [Issues](../../issues)
- Descreva o problema detalhadamente
- Inclua sua distribuição Linux e versão
- Adicione logs se possível

### Sugerir Melhorias
- Abra uma [Issue](../../issues) com a tag `enhancement`
- Explique sua ideia e o caso de uso
- Se possível, mostre exemplos visuais

### Fazer Pull Requests

1. **Fork** o repositório
2. **Clone** seu fork:
```bash
   git clone https://github.com/SEU_USUARIO/matrix-hacker-desktop.git
   cd matrix-hacker-desktop
```

3. **Crie uma branch** para sua feature:
```bash
   git checkout -b feature/minha-feature
```

4. **Faça suas mudanças** e commit:
```bash
   git add .
   git commit -m "Add: descrição da feature"
```

5. **Push** para seu fork:
```bash
   git push origin feature/minha-feature
```

6. Abra um **Pull Request** no repositório original

## Padrões de Código

### Shell Scripts
- Use `#!/bin/bash` no topo
- Comente código complexo
- Teste em múltiplas distros se possível

### Python
- Siga PEP 8
- Use type hints quando apropriado
- Docstrings para funções complexas

### Configurações (i3, polybar, etc)
- Mantenha comentários explicativos
- Preserve a otimização para hardware antigo
- Teste antes de submeter

## Estilo de Commits

Use prefixos claros:
- `Add:` nova funcionalidade
- `Fix:` correção de bug
- `Update:` atualização de feature existente
- `Docs:` mudanças em documentação
- `Refactor:` refatoração de código
- `Style:` mudanças visuais/tema
- `Perf:` melhorias de performance

Exemplo:
```
Add: suporte para Fedora 39 no instalador
```

## Áreas que Precisam de Ajuda

- [ ] Suporte para mais distribuições (NixOS, Gentoo)
- [ ] Widgets adicionais para Polybar
- [ ] Temas alternativos (cyberpunk, dracula, etc)
- [ ] Traduções (inglês, espanhol)
- [ ] Testes automatizados
- [ ] Documentação de troubleshooting

## Código de Conduta

- Seja respeitoso com outros contribuidores
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade
- Mantenha discussões técnicas e profissionais

## Dúvidas?

Abra uma [Issue](../../issues) com a tag `question` ou entre em contato!

---

**Obrigado por contribuir!** Cada PR, issue ou sugestão ajuda a melhorar o projeto. 🚀
