# Sprint__COA

Sistema Otimizado para Eletropostos com Arquitetura RISC

Integrantes

Gustavo de Souza Abreu — RM 574080

Lucas Nogueira dos Santos — RM 572592

Enzo Coppa Selingarde — RM 573393

Gabriel Carlos Barbosa — RM 574074

Problema

Atualmente, muitos sistemas utilizados em eletropostos operam com softwares de alto nível e hardwares genéricos, o que acaba gerando um consumo desnecessário de energia e menor eficiência no processamento de tarefas críticas.

Operações como autenticação de usuários, controle de carga e gerenciamento do sistema precisam acontecer de forma rápida e contínua. Porém, quando executadas em arquiteturas pouco otimizadas, exigem mais processamento do que o necessário, aumentando o gasto energético e reduzindo a eficiência do equipamento.

Justificativa

Quando falamos em mobilidade elétrica, a sustentabilidade não deve estar apenas no uso da eletricidade como combustível, mas também na eficiência tecnológica dos sistemas que tornam essa operação possível.

Quanto menor for a quantidade de instruções necessárias para executar uma tarefa, menor será o consumo de energia do sistema.

Por isso, otimizar o processamento em nível de hardware se torna um diferencial importante, contribuindo para a redução do desperdício energético, melhor aproveitamento dos recursos e maior eficiência operacional dos eletropostos.

Proposta de Solução

Nossa proposta consiste no desenvolvimento de um módulo de controle otimizado em Assembly para gerenciar operações críticas de eletropostos.

O principal objetivo é reduzir a quantidade de ciclos de CPU utilizados durante o processamento, permitindo que tarefas essenciais sejam executadas de forma mais rápida e com menor consumo energético.

Diferente de soluções tradicionais que dependem de múltiplas camadas de software, o uso de Assembly oferece maior controle sobre o hardware, permitindo uma execução mais direta e eficiente.

Arquitetura Utilizada

Para tornar o sistema mais eficiente, utilizamos uma arquitetura baseada no modelo RISC (Reduced Instruction Set Computer), conhecida por seu baixo consumo energético e alta performance em sistemas embarcados.

Além disso, o projeto utiliza o conceito de Pipeline, permitindo o processamento paralelo de instruções e reduzindo a quantidade de ciclos de clock necessários para cada operação.

O hardware pensado para a solução inclui microcontroladores e sistemas embarcados de baixo consumo, ideais para aplicações que exigem eficiência energética e estabilidade contínua.

Comparativo Técnico — Assembly vs Python

Linguagens de alto nível, como Python, oferecem maior facilidade de desenvolvimento, porém exigem mais recursos computacionais para executar tarefas simples.

Isso acontece porque essas linguagens trabalham com camadas de abstração e dependem de interpretadores, aumentando o número de instruções processadas pela CPU.

Já o código em Assembly permite acesso direto ao hardware, eliminando grande parte desse overhead e tornando a execução muito mais eficiente.

Como resultado, o sistema consegue reduzir significativamente o consumo energético por instrução executada, além de melhorar o desempenho geral do processamento.

Impactos Esperados e Sustentabilidade

Com a implementação dessa solução, os principais impactos esperados são:

Redução do consumo energético da infraestrutura de carregamento;
Diminuição da pegada de carbono dos eletropostos;
Melhor aproveitamento de fontes de energia renovável;
Maior eficiência operacional do sistema;
Redução do aquecimento dos componentes eletrônicos;
Aumento da vida útil do hardware utilizado.

Além dos benefícios técnicos, o projeto também reforça a importância da sustentabilidade tecnológica, mostrando que eficiência energética depende não apenas da fonte de energia utilizada, mas também da forma como os sistemas são desenvolvidos e executados.

Conclusão

O projeto propõe uma abordagem mais eficiente para o funcionamento de eletropostos, utilizando otimização em baixo nível para reduzir consumo energético e melhorar o desempenho do sistema.

A combinação entre arquitetura RISC, programação em Assembly e sistemas embarcados cria uma solução mais leve, rápida e sustentável, alinhada às necessidades atuais da mobilidade elétrica e da preservação de recursos tecnológicos e ambientais.
