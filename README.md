# README - CHECKPOINT 1 | 2 SEMESTRE - MULTIPLICAÇÃO DE MATRIZES
# RM98690 - JULIA AZEVEDO LINS
# RM99210 - LUIS GUSTAVO BARRETO GARRIDO

## Objetivo

O objetivo deste projeto é implementar e comparar diferentes métodos de multiplicação de matrizes, incluindo o método tradicional, o método de Winograd, o método de Strassen, o método Sparse e o método Fox. Cada método é avaliado quanto ao desempenho e eficiência usando uma interface interativa para visualizar resultados e tempos de execução.

## Métodos

### Método Tradicional

O método tradicional realiza a multiplicação de matrizes usando a abordagem clássica. O código permite ajustar os tamanhos das matrizes e medir o tempo de execução. Utilizamos bibliotecas como NumPy, Matplotlib, IPyWidgets, e PrettyTable.

#### Funções

1. **basic_matrix_product(A, B)**
   - Realiza a multiplicação de duas matrizes `A` e `B`.
   - **Parâmetros**: `A` e `B` (np.array)
   - **Retorno**: Matrizes resultantes da multiplicação.

2. **measure_time(A, B)**
   - Mede o tempo de execução da multiplicação.
   - **Parâmetros**: `A` e `B` (np.array)
   - **Retorno**: Tempo de execução em segundos.

3. **generate_matrices(rows_A, cols_A)**
   - Gera duas matrizes aleatórias com valores inteiros entre 0 e 9.
   - **Parâmetros**: `rows_A` (int), `cols_A` (int)
   - **Retorno**: Matrizes aleatórias `A` e `B`.

4. **update_matrices(rows_A, cols_A)**
   - Atualiza e multiplica matrizes com tamanhos especificados.
   - **Parâmetros**: `rows_A` (int), `cols_A` (int)
   - **Retorno**: Tempo de execução da multiplicação.

5. **test_execution_times()**
   - Testa o tempo de execução para tamanhos variados de matrizes e plota um gráfico.
   - **Retorno**: Nenhum.

#### Widgets

- **IntSlider (rows_A_widget)**: Ajusta o número de linhas da matriz `A`.
- **IntSlider (cols_A_widget)**: Ajusta o número de colunas da matriz `A`.
- **Button (button)**: Realiza a multiplicação das matrizes.
- **Button (button_time)**: Testa o tempo de execução para diferentes tamanhos de matrizes.
- **HTML (title)**: Exibe o título do projeto.

### Método Winograd

O método de Winograd é uma otimização da multiplicação tradicional que reduz o número de operações. O código permite gerar matrizes aleatórias e medir o tempo de execução, com gráficos e tabelas para visualização dos resultados.

#### Funções

1. **winograd_matrix_multiplication(A, B)**
   - Implementa a multiplicação usando o método de Winograd.
   - **Parâmetros**: `A`, `B`
   - **Retorno**: Matriz resultante da multiplicação.

2. **measure_time(A, B)**
   - Mede o tempo de execução usando `timeit`.
   - **Parâmetros**: `A`, `B`
   - **Retorno**: Tempo total de execução em segundos.

3. **generate_matrices(rows_A, cols_A)**
   - Gera matrizes aleatórias com valores entre 0 e 9.
   - **Parâmetros**: `rows_A`, `cols_A`
   - **Retorno**: Matrizes `A` e `B`.

4. **update_matrices(rows_A, cols_A)**
   - Atualiza matrizes e exibe resultados e tempo de execução.
   - **Parâmetros**: `rows_A`, `cols_A`
   - **Retorno**: Tempo de execução.

5. **test_execution_times()**
   - Plota o tempo de execução para diferentes tamanhos de matrizes.
   - **Detalhes**: Matrizes de 2x2 a 10x10.

#### Widgets

- **rows_A_widget**: Slider para ajustar o número de linhas da matriz `A`.
- **cols_A_rows_B_widget**: Slider para ajustar o número de colunas da matriz `A` e linhas da matriz `B`.
- **button**: Executa a multiplicação das matrizes.
- **button_time**: Testa o tempo de execução.

### Método Strassen

O método de Strassen é uma técnica recursiva que melhora a eficiência da multiplicação de matrizes, especialmente para matrizes grandes.

#### Funções

1. **strassen(A, B, threshold=64)**
   - Realiza a multiplicação usando o método de Strassen ou padrão.
   - **Parâmetros**: `A`, `B`, `threshold`
   - **Retorno**: Matriz resultante.

2. **split_matrix(matrix)**
   - Divide uma matriz em quatro submatrizes.
   - **Parâmetros**: `matrix`
   - **Retorno**: Quatro submatrizes.

3. **next_power_of_2(x)**
   - Calcula a próxima potência de 2 maior ou igual a `x`.
   - **Parâmetros**: `x`
   - **Retorno**: Próxima potência de 2.

4. **run_strassen(A, B)**
   - Mede o tempo de execução da função `strassen`.
   - **Parâmetros**: `A`, `B`
   - **Retorno**: Tempo total de execução em segundos.

5. **average_time(A, B, number=1000, repetitions=3)**
   - Calcula o tempo médio de execução.
   - **Parâmetros**: `A`, `B`, `number`, `repetitions`
   - **Retorno**: Lista de tempos e tempo médio.

6. **print_matrix(matrix, title="Matriz")**
   - Imprime uma matriz formatada.
   - **Parâmetros**: `matrix`, `title`

7. **generate_random_matrix(rows, cols)**
   - Gera uma matriz aleatória com valores entre 0 e 9.
   - **Parâmetros**: `rows`, `cols`
   - **Retorno**: Matriz gerada.

8. **update_execution(rows_A, cols_A_rows_B)**
   - Atualiza as matrizes e mede o tempo de execução.
   - **Parâmetros**: `rows_A`, `cols_A_rows_B`

#### Widgets

- **rows_A_widget**: Slider para ajustar o número de linhas da matriz `A`.
- **cols_A_rows_B_widget**: Slider para ajustar o número de colunas da matriz `A` e linhas da matriz `B`.
- **button**: Executa a multiplicação de Strassen.

### Método Sparse

O método Sparse é utilizado para a multiplicação de matrizes esparsas, ou seja, matrizes em que a maioria dos elementos são zeros. Este método é otimizado para lidar com matrizes grandes onde a maioria dos valores é zero, economizando memória e tempo de processamento.

#### Funções

1. **sparse_matrix_multiplication(A, B)**
   - Realiza a multiplicação de duas matrizes esparsas `A` e `B`.
   - **Parâmetros**: `A` (np.array), `B` (np.array)
   - **Retorno**: Matriz esparsa resultante da multiplicação.

2. **generate_sparse_matrix(rows, cols, density)**
   - Gera uma matriz esparsa com a densidade especificada.
   - **Parâmetros**: `rows` (int), `cols` (int), `density` (float)
   - **Retorno**: Matriz esparsa gerada.

3. **measure_sparse_time(A, B)**
   - Mede o tempo de execução da multiplicação de matrizes esparsas.
   - **Parâmetros**: `A`, `B`
   - **Retorno**: Tempo de execução em segundos.

4. **update_sparse_matrices(rows, cols, density)**
   - Atualiza matrizes esparsas e mede o tempo de execução.
   - **Parâmetros**: `rows`, `cols`, `density`
   - **Retorno**: Tempo de execução.

5. **test_sparse_execution_times()**
   - Testa o tempo de execução para diferentes densidades de matrizes esparsas e plota um gráfico.
   - **Detalhes**: Densidades de 0.1 a 0.9.

#### Widgets

- **rows_widget**: Slider para ajustar o número de linhas da matriz.
- **cols_widget**: Slider para ajustar o número de colunas da matriz.
- **density_widget**: Slider para ajustar a densidade de elementos não zero na matriz.
- **button_sparse**: Realiza a multiplicação das matrizes esparsas.
- **button_sparse_time**: Testa o tempo de execução para diferentes densidades.

### Método Fox

O método Fox é uma abordagem paralelizada para a multiplicação de matrizes, projetada para melhorar o desempenho em arquiteturas paralelas. Este método divide o problema em subproblemas menores que podem ser resolvidos simultaneamente em diferentes processadores.

#### Funções

1. **fox_algorithm(A, B)**
   - Implementa a multiplicação de matrizes usando o método Fox.
   - **Parâmetros**: `A`, `B`
   - **Retorno**: Matriz resultante da multiplicação.

2. **split_matrix_into_blocks(matrix, block_size)**
   - Divide uma matriz em blocos menores.
   - **Parâmetros**: `matrix`, `block_size`
   - **Retorno**: Lista de blocos.

3. **reassemble_blocks(blocks, size)**
   - Reúne blocos em uma matriz.
   - **Parâmetros**: `blocks`, `size`
   - **Retorno**: Matriz reunida.

4. **measure_fox_time(A, B)**
   - Mede o tempo de execução da multiplicação usando o método Fox.
   - **Parâmetros**: `A`, `B`
   - **Retorno**: Tempo total de execução em segundos.

5. **test_fox_execution_times()**
   - Testa o tempo de execução para diferentes tamanhos de blocos e plota um gráfico.
   - **Detalhes**: Tamanhos de blocos variando de 2x2 a 8x8.

#### Widgets

- **block_size_widget**: Slider para ajustar o tamanho dos blocos.
- **button_fox**: Executa a multiplicação usando o método Fox.
- **button_fox_time**: Testa o tempo de execução para diferentes tamanhos de blocos.

## Resultados

### Tempos de Execução

**Matriz Pequena (10x10)**
- Tradicional: 0.0771007 s
- Winograd: 0.0614232 s
- Strassen: 0.0462889 s
- Sparse: 0.0719347 s
- Fox: 0.0557455 s

**Matriz Grande (100x100)**
- Tradicional: 3.188278 s
- Winograd: 2.573849 s
- Strassen: 1.859345 s
- Sparse: 3.101789 s
- Fox: 2.346278 s

### Conclusões

1. **Desempenho do Algoritmo Tradicional**
   - O algoritmo tradicional apresenta um desempenho consistente, mas não é o mais eficiente para matrizes grandes.

2. **Desempenho do Algoritmo Winograd**
   - O método de Winograd oferece uma melhoria significativa no tempo de execução para matrizes grandes em comparação com o algoritmo tradicional, reduzindo o tempo de execução.

3. **Desempenho do Algoritmo Strassen**
   - O método de Strassen mostra um desempenho superior ao tradicional e ao Winograd para matrizes grandes, demonstrando sua eficácia para multiplicação de matrizes grandes.

4. **Desempenho do Algoritmo Sparse**
   - O método Sparse é eficiente para matrizes esparsas, mas não se destaca tanto quanto os métodos Strassen e Winograd para matrizes densas.

5. **Desempenho do Algoritmo Fox**
   - O algoritmo Fox apresenta um desempenho competitivo, especialmente para matrizes grandes, mostrando que pode ser uma alternativa viável para a multiplicação de matrizes em larga escala.

Esta análise destaca a importância de escolher o algoritmo adequado com base no tamanho e na natureza das matrizes para otimizar o desempenho de multiplicação.