import pygame
import random
from pygame.locals import *
import metodos

ANCHOVENTANA = 1920
ALTOVENTANA = 1080
COLORVENTANA = (255, 255, 255)
COLORFONDO = (0, 0, 0)
FPS = 60
TAMANOMINVILLANO = 15
TAMANOMAXVILLANO = 60
VELOCIDADMINVILLANO = 1
VELOCIDADMAXVILLANO = 8
TASANUEVOVILLANO = 6
TASAMOVIMIENTOJUGADOR = 5
op_menu = 1
op_musica = 1
i = 1


# establece un pygame, la ventana y el cursor del ratón
pygame.init()
relojPrincipal = pygame.time.Clock()
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), FULLSCREEN)
pygame.display.set_caption('Evasor')
pygame.mouse.set_visible(False)

# establece las fuentes
fuente = pygame.font.SysFont("Arial", 48)

# establece los sonidos
sonidoJuegoTerminado = pygame.mixer.Sound('juegoterminado.wav')
sonidoJuegoTerminado.set_volume(0.1)
pygame.mixer.music.load('gobierno.mp3')
pygame.mixer.music.set_volume(0.1)

# establece las imagenes
imagenJugador = pygame.image.load('jugador2.png')
rectanguloJugador = imagenJugador.get_rect()
imagenVillano = pygame.image.load('covid2.png')

# Muestra la pantalla inicial
metodos.dibujarTexto('Esquiva el bicho', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 4), COLORVENTANA)
metodos.dibujarTexto('Presione una tecla para comenzar.', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3), COLORVENTANA)
pygame.display.update()
metodos.esperarTeclaJugador()

puntmax = 0
pygame.mixer.music.play(0, 0.0)
while True:
    # establece el comienzo del juego
    villanos = []
    punt = 0
    rectanguloJugador.topleft = (ANCHOVENTANA / 2, ALTOVENTANA / 2)
    moverIzquierda = moverDerecha = moverArriba = moverAbajo = False
    trucoReversa = trucoLento = pause = False
    contadorpausa = False
    contadorAgregarVillano = 0

    while True:  # el ciclo del juego se mantiene mientras se este jugando
        if not pause:
            punt += 1  # incrementa la puntuación

        for evento in pygame.event.get():
            if evento.type == QUIT:
                metodos.terminar()

            if evento.type == KEYDOWN:
                #menu principal
                if evento.key == pygame.K_q:
                    op_menu = metodos.generar_menu(op_menu, superficieVentana, COLORFONDO, ANCHOVENTANA, ALTOVENTANA, fuente, relojPrincipal, COLORVENTANA)
                #menu musica
                if evento.key == pygame.K_m:
                    i = metodos.generar_menu_musica(op_musica, superficieVentana, COLORFONDO, ANCHOVENTANA,
                                                   ALTOVENTANA, fuente, relojPrincipal, COLORVENTANA,i)
                # invertir el movimiento con la z
                if evento.key == ord('z'):
                    trucoReversa = True
                # ralentizar el movimiento con la z
                if evento.key == ord('x'):
                    trucoLento = True
                # pausar el juego con el espacio
                if evento.key == K_SPACE:
                    pause = True
                    if not contadorpausa:
                        contadorpausa = True
                    elif contadorpausa:
                        contadorpausa = False

                if evento.key == K_LEFT or evento.key == ord('a'):
                    moverDerecha = False
                    moverIzquierda = True
                if evento.key == K_RIGHT or evento.key == ord('d'):
                    moverIzquierda = False
                    moverDerecha = True
                if evento.key == K_UP or evento.key == ord('w'):
                    moverAbajo = False
                    moverArriba = True
                if evento.key == K_DOWN or evento.key == ord('s'):
                    moverArriba = False
                    moverAbajo = True

            if evento.type == KEYUP:
                if evento.key == ord('z'):
                    trucoReversa = False
                    punt = 0
                if evento.key == ord('x'):
                    trucoLento = False
                    punt = 0
                if evento.key == K_SPACE and contadorpausa == 0:
                    pause = False
                    contadorpausa = False
                if evento.key == K_ESCAPE:
                    metodos.terminar()

                if evento.key == K_LEFT or evento.key == ord('a'):
                    moverIzquierda = False
                if evento.key == K_RIGHT or evento.key == ord('d'):
                    moverDerecha = False
                if evento.key == K_UP or evento.key == ord('w'):
                    moverArriba = False
                if evento.key == K_DOWN or evento.key == ord('s'):
                    moverAbajo = False

            if evento.type == MOUSEMOTION:
                # Si se mueve el ratón, este se mueve al lugar donde esté el cursor.
                rectanguloJugador.move_ip(evento.pos[0] - rectanguloJugador.centerx,
                                          evento.pos[1] - rectanguloJugador.centery)
        if op_menu == 1:
            # Añade villanos en la parte superior de la pantalla, de ser necesarios.
            if not trucoReversa and not trucoLento and not pause:
                contadorAgregarVillano += 1
            if contadorAgregarVillano == TASANUEVOVILLANO:
                contadorAgregarVillano = 0
                tamanoVillano = random.randint(TAMANOMINVILLANO, TAMANOMAXVILLANO)
                nuevoVillano = {
                    'rect': pygame.Rect(random.randint(0, ANCHOVENTANA - tamanoVillano), 0 - tamanoVillano,
                                        tamanoVillano,
                                        tamanoVillano),
                    'velocidad': random.randint(VELOCIDADMINVILLANO, VELOCIDADMAXVILLANO),
                    'superficie': pygame.transform.scale(imagenVillano, (tamanoVillano, tamanoVillano)),
                }

                villanos.append(nuevoVillano)

            # Mueve los villanos hacia abajo.
            for v in villanos:
                if not trucoReversa and not trucoLento and not pause:
                    v['rect'].move_ip(0, v['velocidad'])
                elif trucoReversa:
                    v['rect'].move_ip(0, -5)
                elif trucoLento:
                    v['rect'].move_ip(0, 1)
                elif pause:
                    v['rect'].move_ip(0, 0)

            # Elimina los villanos que han caido por debajo.
            for v in villanos:
                if v['rect'].top > ALTOVENTANA:
                    villanos.remove(v)
        if op_menu == 2:
            # Añade villanos en la parte inferior de la pantalla, de ser necesarios.
            if not trucoReversa and not trucoLento and not pause:
                contadorAgregarVillano += 1
            if contadorAgregarVillano == TASANUEVOVILLANO:
                contadorAgregarVillano = 0
                tamanoVillano = random.randint(TAMANOMINVILLANO, TAMANOMAXVILLANO)
                nuevoVillano = {
                    'rect': pygame.Rect(random.randint(0, ANCHOVENTANA - tamanoVillano), ALTOVENTANA + tamanoVillano,
                                        tamanoVillano, tamanoVillano),
                    'velocidad': random.randint(VELOCIDADMINVILLANO, VELOCIDADMAXVILLANO),
                    'superficie': pygame.transform.scale(imagenVillano, (tamanoVillano, tamanoVillano)),
                }
                villanos.append(nuevoVillano)
            # Mueve los villanos hacia arriba.
            for v in villanos:
                if not trucoReversa and not trucoLento and not pause:
                    v['rect'].move_ip(0, -v['velocidad'])
                elif trucoReversa:
                    v['rect'].move_ip(0, 5)
                elif trucoLento:
                    v['rect'].move_ip(0, -1)
                elif pause:
                    v['rect'].move_ip(0, 0)

            # Elimina los villanos que tocado techo.
            for v in villanos[:]:
                if v['rect'].bottom < 0:
                    villanos.remove(v)

        # Mueve el jugador.
        if moverIzquierda and rectanguloJugador.left > 0:
            rectanguloJugador.move_ip(-1 * TASAMOVIMIENTOJUGADOR, 0)
        if moverDerecha and rectanguloJugador.right < ANCHOVENTANA:
            rectanguloJugador.move_ip(TASAMOVIMIENTOJUGADOR, 0)
        if moverArriba and rectanguloJugador.top > 0:
            rectanguloJugador.move_ip(0, -1 * TASAMOVIMIENTOJUGADOR)
        if moverAbajo and rectanguloJugador.bottom < ALTOVENTANA:
            rectanguloJugador.move_ip(0, TASAMOVIMIENTOJUGADOR)

        # Mueve el cursor del ratón hacia el jugador.
        pygame.mouse.set_pos(rectanguloJugador.centerx, rectanguloJugador.centery)

        # Dibuja el mundo del juego en la ventana.
        superficieVentana.fill(COLORFONDO)

        # Dibuja el punt y el punt máximo
        metodos.dibujarTexto('Puntuación: %s' % (punt), fuente, superficieVentana, 10, 0, COLORVENTANA)
        metodos.dibujarTexto('Mejor puntuación: %s' % (puntmax), fuente, superficieVentana, 10, 40, COLORVENTANA)

        # Dibuja el rectángulo del jugador
        superficieVentana.blit(imagenJugador, rectanguloJugador)

        # Dibuja cada villano
        for v in villanos:
            superficieVentana.blit(v['superficie'], v['rect'])

        pygame.display.update()

        # Verifica si algún villano impactó en el jugador.
        if metodos.jugadorGolpeaVillano(rectanguloJugador, villanos):
            if punt > puntmax:
                puntmax = punt  # Establece nuevo punt máximo
            break

        relojPrincipal.tick(FPS)

    # Detiene el juego y muestra "Juego Terminado"
    #pygame.mixer.music.stop()
    #sonidoJuegoTerminado.play()

    metodos.dibujarTexto('Juego Terminado', fuente, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3), COLORVENTANA)
    metodos.dibujarTexto('Presione una tecla para jugar de nuevo.', fuente, superficieVentana, (ANCHOVENTANA / 3),
                 (ALTOVENTANA / 2), COLORVENTANA)
    pygame.display.update()
    metodos.esperarTeclaJugador()

    #sonidoJuegoTerminado.stop()
