# Chad Standard Recomp
### Universal Game Engineering Framework

Padrão aberto de engenharia para recomps, ports, descompilações, runtimes híbridos, emuladores e jogos originais. Não é um recompilador universal.

Consulte a [especificação](docs/STANDARD.md), [matriz de consoles](docs/PLATFORMS.md), [catálogo de ferramentas](docs/TOOLCHAINS.md) e [contrato de adaptadores](docs/ADAPTERS.md).

Execute `python tools/validate.py examples/project.json` e `python -m unittest discover -s tests -v`. Copie o manifesto de exemplo para seu projeto, adapte o pipeline e registre evidências. O pacote não contém jogos ou firmware. Versão 0.1.0: documentação e validador inicial; adaptadores reais ainda pendentes.

## Apoio de engenharia opcional

[Arquitetura](docs/ARCHITECTURE.md) · [Handoff](docs/HANDOFF.md) · [Referências NEF](docs/NEF.md). Nenhum agente de IA ou ferramenta NAVI é obrigatório para executar o validador CSR.
