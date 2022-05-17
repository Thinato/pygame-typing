# Typing Game - pygame
* [English](README.md)
* **Português**
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Thinato/pygame-typing">
    <img src="assets/img/logo128.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">pygame-typing</h3>

  <p align="center">
    Um jogo de digitação feito com pygame.
    <br />
    <a href="https://github.com/Thinato/pygame-typing/blob/main/game.py"><strong>Arquivo Principal do Jogo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Thinato/pygame-typing/blob/main/demo/demo.gif">Demonstração</a>
    ·
    <a href="https://github.com/Thinato/pygame-typing/issues">Relatar Bug</a>
    ·
    <a href="https://github.com/Thinato/pygame-typing/pulls">Requisitar Recurso</a>
  </p>
</div>


## Sobre
Essa é uma implementação de um jogo de digitação, o objetivo é impedir que as palavras cheguem ao lado esquerdo, para isso, você precisa digitar a palavra e pressionar Enter. Cada palavra tem uma pontuação que é registrada abaixo (Score), essa pontuação também é usada para tornar o jogo cada vez mais difícil de acordo com o seu progesso.

Esse projeto foi, em grande parte, inspirado pelo jogo de digitação do [bisqwit](https://bisqwit.iki.fi/) ([wspeed](https://bisqwit.iki.fi/wspeed/))

![gif demonstrando o jogo sendo jogado][demo]

## Requisitos
* Python 3.10
* pygame 2.1.2

## Como iniciar o jogo
Run main.py<br/>
`$ python main.py`

## Recursos
* Sistema de pontuação
* Dificuldade aumenta de acordo com o progresso
* Sistema de Ranking
* Medidor de palavras por minuto
* Medidor de precisão
* Método simples para criação de novas palavras e listas de palavras

## Como criar listas de palavras
1. Vá até a pasta 'word_lists'
2. Crie um novo documento de texto (.txt)
3. Escreva cada palavra em cada uma das linhas
4. Salve o arquivo
5. Com o mesmo nome que foi salvo o arquivo em 'word_lists', crie um novo documento de texto vazio na pasta 'leaderboards'.

## Recursos usados
* [jsfxr](https://sfxr.me/) - Um gerador de som de 8 bits feito em JavaScript por Eric Fredricksen, a versão origial (sfxr) foi feita por DrPetter.
* Background music - É uma portação em 8 bits de J.S. Bach: [Little Fugue in G minor (BWV 578)](https://www.youtube.com/watch?v=Bbox4oi6HjA), o remix foi feito por [MajorNebula](https://www.youtube.com/channel/UCyWw_f8wEU3PIEO2LaKgoUw)

## Leitura adicional
* [pygame](https://www.pygame.org/wiki/about)
* [wspeed](https://bisqwit.iki.fi/wspeed/)
* [jsfxr](https://sfxr.me/)
* [background music](https://www.youtube.com/watch?v=ZAwYwK4Ujas)




<!-- MARKDOWN LINKS & IMAGES -->
[demo]: demo/demo.gif
