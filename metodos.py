import sys
import pygame
from pygame.locals import *
import musica


musica = [musica]



def terminar():
    pygame.quit()
    sys.exit()


def esperarTeclaJugador():
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                terminar()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:  # Sale del juego al presionar ESCAPE
                    terminar()
                return


def jugadorGolpeaVillano(rectanguloJugador, villanos):
    for v in villanos:
        if rectanguloJugador.colliderect(v['rect']):
            return True
    return False


def dibujarTexto(texto, fuente, superficie, x, y, COLORVENTANA):
    objetotexto = fuente.render(texto, 1, COLORVENTANA)
    rectangulotexto = objetotexto.get_rect()
    rectangulotexto.topleft = (x, y)
    superficie.blit(objetotexto, rectangulotexto)


def generar_menu(op_menu, superficieVentana, COLORFONDO, ANCHOVENTANA, ALTOVENTANA, fuente, relojPrincipal,
                 COLORVENTANA):
    otra_pantalla = True
    op = op_menu
    while otra_pantalla:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == ord('q'):
                    # Ocultar pantalla
                    otra_pantalla = False
                    # color del menu
                if evento.key == ord('1'):
                    op = 1
                    otra_pantalla = False
                if evento.key == ord('2'):
                    op = 2
                    otra_pantalla = False
                if evento.key == ord('0') or evento.key == K_ESCAPE:
                    terminar()

        superficieVentana.fill(COLORFONDO)
        # dibujar
        dibujarTexto('Menu:', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 4), COLORVENTANA)
        dibujarTexto('0-Salir', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3) + 50, COLORVENTANA)
        dibujarTexto('1-Primera fase', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3) + 100,
                     COLORVENTANA)
        dibujarTexto('2-Segunda fase', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3) + 150,
                     COLORVENTANA)
        pygame.display.update()
        relojPrincipal.tick(5)
    return op


def generar_menu_musica(op_menu, superficieVentana, COLORFONDO, ANCHOVENTANA, ALTOVENTANA, fuente, relojPrincipal,
                        COLORVENTANA,i):
    otra_pantalla = True
    op = op_menu
    lista = ['gobierno.mp3', 'InTE.mp3', 'CastleOG.mp3', 'Numb.mp3', 'Nigths.mp3', 'Counting.mp3', 'Demons.mp3',
             '7years.mp3']
    while otra_pantalla:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == ord('q'):
                    # Ocultar pantalla
                    otra_pantalla = False
                    # color del menu
                if evento.key == ord('1'):
                    op = 1
                    pygame.mixer.music.load(lista[i])
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play(-1, 0.0)
                    if i < 7:
                        i = i + 1
                    else:
                        i = 0
                    return i
                    otra_pantalla = False
                if evento.key == ord('2'):
                    op = 2
                    pygame.mixer.music.load('InTE.mp3')
                    pygame.mixer.music.queue('CastleOG.mp3')
                    pygame.mixer.music.queue('Numb.mp3')
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play(0, 0.0)
                    otra_pantalla = False
                if evento.key == ord('3'):
                    op = 3
                    pygame.mixer.music.load('Nigths.mp3')
                    pygame.mixer.music.queue('Counting.mp3')
                    pygame.mixer.music.queue('Demons.mp3')
                    pygame.mixer.music.queue('7years.mp3')
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play(0, 0.0)
                    otra_pantalla = False
                if evento.key == ord('0') or evento.key == K_ESCAPE:
                    terminar()

        superficieVentana.fill(COLORFONDO)
        # dibujar
        dibujarTexto('Menu:', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 4), COLORVENTANA)
        dibujarTexto('0-Salir', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3) + 50, COLORVENTANA)
        dibujarTexto('1-Siguiente canción', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3) + 100,
                     COLORVENTANA)
        dibujarTexto('2-Lista LP', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3) + 150, COLORVENTANA)
        dibujarTexto('3-Lista A', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3) + 200, COLORVENTANA)
        pygame.display.update()
        relojPrincipal.tick(5)
    return op
