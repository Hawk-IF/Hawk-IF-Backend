# Como contribuir com o Hawk-Backend 
Esse arquivo descreve as principais convenções e
praticas usadas no sistema,se vc deseja contribuir basta
seguir o que será instruido e não haverá problemas

## Como posso subir meu codigo:
Para subir seu codigo vc deve criar uma branch separada
baseada na develop seguindo os padrões do gitflow,realizar suas modificações usando
também os padrões do gitflow, e documentando o que foi feito
o minimo esperado é a modificação no changelog.md mas coisas como ferramentas
que devem ser utilizadas durante o processo de desenvolvimento também devem ser explicadas
principalmente nesse arquivo. Ao fim do processo de criação do codigo deve-se abrir um
pull request para a develop explicando oq foi feito, qual issue foi resolvida,e esperar 
o resultado final

## Praticas Aderidas
algumas praticas são recomendadas de serem seguidas, e dependendo da modificação
seu codigo não será aprovado sem seguir elas.

- testes: 
    o codigo feito deve em sua grande maioria dos casos ter testes automatizados
    para garantir a qualidade, junto a isso é recomendado usar o TDD para ajudas
- Praticas Minimas de arquitetura:
    o sistema por padrão já tem uma arquitetura definida, mas algumas praticas deve ser
    utilizadas: DRY , KISS , SOLID , YGANI são boas praticas que devem ser seguidas
- Tipagem , modulariazação e clean code:
    o codigo deve ser bem tipado, o sistema tem ferramentas que gerenciam os tipos do sistema
    e quando ha inconsistencias emitem erros, a modularizão serve como organização, e o clean code deve 
    ser algo a se seguir mesmo que seja o basico
- padronização:
    a maior parte do sistema é automaticamente padronizada por algumas 
    ferramentas como o pre-commit mas nomes de classes,funções e variaveis deve usar convenções proprias
    sendo funções,arquivos e variaveis o snake_case e as classes e modulos o camalCase

## Ferramentas

o sistema tem algumas ferramentas que é vc deve conhecer,
a primeira e mais importante é o **CI** ele é um processo automatizado
que é rodado em cada pull request e que sozinho rodas as outras ferramentas do sistema,
seu objetivo é manter uma integração continua de qualidade, então se qualquer processo falhar
o pull request não poderá ser mergiado.

### Tests:
devem ser rodados usando : 
```bash
uv run pytest
```

### pre-commit:
deve ser rodado antes de cada commit, e se algum erro for encontrado corrigido,
vc pode rodar com:
```bash
pre-commit run --all-files
```

### imports linter
serve como ferramenta de garantia de integridade da arquitetura (em partes)
ele gerencia os imports e se caso vc quebre alguma regra da arquitetura em camadas
ele irá emitir um error
```bash
uv run lint-imports
```