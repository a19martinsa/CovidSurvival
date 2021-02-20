import sys
import pygame
from pygame.locals import *
import random
import var
import conexion
import metodos


def covidSurvival(self):
    anchoVen = 1920
    altoVen = 1080
    colorVen = (255, 255, 255)
    colorFondo = (0, 0, 0)
    FPS = 60
    tamMinVirus = 15
    tamMaxVirus = 90
    velMinVirus = 5
    velMaxVirus = 8
    tasaVirus = 8
    tasaMovJug = 6
    op_menu = 1
    op_musica = 1
    i = 1

    pygame.init()
    relojPrincipal = pygame.time.Clock()
    formaVen = pygame.display.set_mode((anchoVen, altoVen), FULLSCREEN)
    pygame.display.set_caption('Covid Survival')
    pygame.mouse.set_visible(False)

    font = pygame.font.SysFont("Arial", 48)

    ending = pygame.mixer.Sound('musica/ending.ogg')
    ending.set_volume(0.2)
    pygame.mixer.music.load('musica/arex.ogg')
    pygame.mixer.music.set_volume(0.2)

    imgJug = pygame.image.load('imagenes/jugador2.png')
    rectJug = imgJug.get_rect()
    imgVirus = pygame.image.load('imagenes/covid2.png')
    virus = []

    metodos.showText('Presiona cualquier tecla para comenzar.', font, formaVen, (anchoVen / 3)-120,
                         (altoVen / 3), colorVen)
    pygame.display.update()
    metodos.esperarTeclaJugador()

    puntmax = var.puntmax
    pygame.mixer.music.play(0, 0.0)
    while True:
        virus = []
        punt = 0
        rectJug.topleft = (anchoVen / 2, altoVen / 2)
        moverIzquierda = moverDerecha = moverArriba = moverAbajo = False
        pause = False
        contadorpausa = False
        contVirus = 0

        while True:  # el ciclo del juego se mantiene mientras se este jugando
            if not pause:
                punt += 1
                if 0 <= punt < 1000:
                    imgJug = pygame.image.load('imagenes/jugador2.png')
                    velMaxVirus = 8
                    tasaVirus = 6
                elif 1000 <= punt < 2000:
                    imgJug = pygame.image.load('imagenes/jugador3.png')
                    velMaxVirus = 12
                    tasaVirus = 6
                elif 2000 <= punt < 3000:
                    imgJug = pygame.image.load('imagenes/jugador4.jpg')
                    velMaxVirus = 18
                    tasaVirus = 4
                elif 3000 <= punt < 4000:
                    imgJug = pygame.image.load('imagenes/jugador5.png')
                    velMaxVirus = 24
                    tasaVirus = 4
                elif 4000 <= punt:
                    imgJug = pygame.image.load('imagenes/jugador6.jpg')
                    velMaxVirus = 28
                    tasaVirus = 2



            for evento in pygame.event.get():
                if evento.type == QUIT:
                    metodos.terminar()

                if evento.type == KEYDOWN:
                    if evento.key == K_ESCAPE:
                        metodos.terminar()
                    # menu principal
                    if evento.key == pygame.K_q:
                        op_menu = metodos.generar_menu(op_menu, formaVen, colorFondo, anchoVen,
                                                       altoVen, font, relojPrincipal, colorVen)
                    # menu musica
                    if evento.key == pygame.K_m:
                        i = metodos.generar_menu_musica(op_musica, formaVen, colorFondo, anchoVen,
                                                        altoVen, font, relojPrincipal, colorVen, i)

                    # pausar el juego con el espacio
                    if evento.key == K_SPACE:

                        conexion.Conexion.db_connect('database.db')
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
                    if evento.key == K_SPACE and contadorpausa == 0:
                        pause = False
                        contadorpausa = False
                    if evento.key == K_LEFT or evento.key == ord('a'):
                        moverIzquierda = False
                    if evento.key == K_RIGHT or evento.key == ord('d'):
                        moverDerecha = False
                    if evento.key == K_UP or evento.key == ord('w'):
                        moverArriba = False
                    if evento.key == K_DOWN or evento.key == ord('s'):
                        moverAbajo = False

                if evento.type == MOUSEMOTION:
                    rectJug.move_ip(evento.pos[0] - rectJug.centerx,
                                              evento.pos[1] - rectJug.centery)
            if op_menu == 1:
                # Añadir virus
                if not pause:
                    contVirus += 1
                if contVirus >= tasaVirus:
                    contVirus = 0
                    tamFinVirus = random.randint(tamMinVirus, tamMaxVirus)
                    nuevoVirus = {
                        'virus': pygame.Rect(random.randint(0, anchoVen - tamFinVirus),
                                             0 - tamFinVirus,tamFinVirus,tamFinVirus),
                        'velocidad': random.randint(velMinVirus, velMaxVirus),
                        'superficie': pygame.transform.scale(imgVirus, (tamFinVirus, tamFinVirus)),
                    }

                    virus.append(nuevoVirus)

                # Mover virus
                for v in virus:
                    if not pause:
                        v['virus'].move_ip(0, v['velocidad'])
                    elif pause:
                        v['virus'].move_ip(0, 0)

                # Elimina los virus que han caido por debajo.
                for v in virus:
                    if v['virus'].top > altoVen:
                        virus.remove(v)
            if op_menu == 2:
                if not pause:
                    contVirus += 1
                if contVirus >= tasaVirus:
                    contVirus = 0
                    tamFinVirus = random.randint(tamMinVirus, tamMaxVirus)
                    nuevoVirus = {
                        'virus': pygame.Rect(random.randint(0, anchoVen - tamFinVirus),
                                             altoVen + tamFinVirus,tamFinVirus, tamFinVirus),
                        'velocidad': random.randint(velMinVirus, velMaxVirus),
                        'superficie': pygame.transform.scale(imgVirus, (tamFinVirus, tamFinVirus)),
                    }
                    virus.append(nuevoVirus)
                # Mueve los virus hacia arriba.
                for v in virus:
                    if not pause:
                        v['virus'].move_ip(0, -v['velocidad'])
                    elif pause:
                        v['virus'].move_ip(0, 0)

                # Elimina los virus que tocado techo.
                for v in virus[:]:
                    if v['virus'].bottom < 0:
                        virus.remove(v)

            if moverIzquierda and rectJug.left > 0:
                rectJug.move_ip(-1 * tasaMovJug, 0)
            if moverDerecha and rectJug.right < anchoVen:
                rectJug.move_ip(tasaMovJug, 0)
            if moverArriba and rectJug.top > 0:
                rectJug.move_ip(0, -1 * tasaMovJug)
            if moverAbajo and rectJug.bottom < altoVen:
                rectJug.move_ip(0, tasaMovJug)

            # Posiciona el jugador en el lugar el cursor
            pygame.mouse.set_pos(rectJug.centerx, rectJug.centery)

            formaVen.fill(colorFondo)
            formaVen.blit(imgJug, rectJug)

            metodos.showText('Puntuación: %s' % (punt), font, formaVen, 10, 0, colorVen)
            metodos.showText('Mejor puntuación: %s' % (puntmax), font, formaVen, 10, 40,
                                 colorVen)
            metodos.showText('Menus: Q/M', font, formaVen, 10, 80,colorVen)
            metodos.showText('Pausar: Space Bar', font, formaVen, 10, 120, colorVen)
            # Dibujar virus
            for v in virus:
                formaVen.blit(v['superficie'], v['virus'])

            pygame.display.update()

            # Comprobar contactos villano-jugador
            if metodos.comprobarContacto(rectJug, virus):
                if punt > puntmax:
                    puntmax = punt  # Establece nuevo punt máximo
                    conexion.Conexion.modifJug(var.jugador, puntmax)
                break

            relojPrincipal.tick(FPS)

        pygame.mixer.music.pause()
        ending.play()


        metodos.showText('Juego Terminado', font, formaVen, (anchoVen / 3), (altoVen / 3),
                             colorVen)
        metodos.showText('Presiona cualquier tecla para jugar de nuevo.', font, formaVen,
                             (anchoVen / 3)-120,
                             (altoVen / 2), colorVen)
        pygame.display.update()

        metodos.esperarTeclaJugador()

        ending.stop()
        pygame.mixer.music.unpause()

def terminar():
    pygame.quit()
    conexion.Conexion.mostrarJugadores(None)


def esperarTeclaJugador():
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                terminar()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:  # Sale del juego al presionar ESCAPE
                    terminar()
                return


def comprobarContacto(rectJug, virus):
    for v in virus:
        if rectJug.colliderect(v['virus']):
            return True
    return False


def showText(texto, font, superficie, x, y, colorVen):
    objetotexto = font.render(texto, 1, colorVen)
    rectangulotexto = objetotexto.get_rect()
    rectangulotexto.topleft = (x, y)
    superficie.blit(objetotexto, rectangulotexto)


def generar_menu(op_menu, formaVen, colorFondo, anchoVen, altoVen, font, relojPrincipal,
                 colorVen):
    otra_pantalla = True
    op = op_menu
    while otra_pantalla:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == ord('q'):
                    otra_pantalla = False
                if evento.key == ord('1'):
                    op = 1
                    otra_pantalla = False
                if evento.key == ord('2'):
                    op = 2
                    otra_pantalla = False
                if evento.key == ord('0') or evento.key == K_ESCAPE:
                    terminar()

        formaVen.fill(colorFondo)
        showText('Menu Principal:', font, formaVen, (anchoVen / 3), (altoVen / 4), colorVen)
        showText('0-Salir de juego', font, formaVen, (anchoVen / 3), (altoVen / 3) + 50,
                     colorVen)
        showText('1-Modo caida', font, formaVen, (anchoVen / 3), (altoVen / 3) + 100,
                     colorVen)
        showText('2-Modo ascenso', font, formaVen, (anchoVen / 3), (altoVen / 3) + 150,
                     colorVen)
        pygame.display.update()
        relojPrincipal.tick(5)
    return op


def generar_menu_musica(op_menu, formaVen, colorFondo, anchoVen, altoVen, font, relojPrincipal,
                        colorVen, i):
    otra_pantalla = True
    op = op_menu
    lista = ['musica/arex.ogg', 'musica/batalla.ogg', 'musica/biological.ogg', 'musica/heroic.ogg', 'musica/planeta.ogg',
             'musica/resilience.ogg']
    while otra_pantalla:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == ord('m'):
                    otra_pantalla = False
                if evento.key == ord('1'):
                    op = 1
                    pygame.mixer.music.load(lista[i])
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1, 0.0)
                    if i < 5:
                        i = i + 1
                    else:
                        i = 0
                    return i
                    otra_pantalla = False
                if evento.key == ord('2'):
                    op = 2
                    pygame.mixer.music.load('musica/arex.ogg')
                    pygame.mixer.music.queue( 'musica/batalla.ogg')
                    pygame.mixer.music.queue('musica/biological.ogg')
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(0, 0.0)
                    otra_pantalla = False
                if evento.key == ord('3'):
                    op = 3
                    pygame.mixer.music.load('musica/ending.ogg')
                    pygame.mixer.music.queue('musica/heroic.ogg')
                    pygame.mixer.music.queue('musica/planeta.ogg')
                    pygame.mixer.music.queue('musica/resilience.ogg')
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(0, 0.0)
                    otra_pantalla = False
                if evento.key == ord('0') or evento.key == K_ESCAPE:
                    otra_pantalla = False

        formaVen.fill(colorFondo)
        showText('Menu del reproducción:', font, formaVen, (anchoVen / 3), (altoVen / 4), colorVen)
        showText('0-Salir', font, formaVen, (anchoVen / 3), (altoVen / 3) + 50, colorVen)
        showText('1-Siguiente canción', font, formaVen, (anchoVen / 3), (altoVen / 3) + 100,
                     colorVen)
        showText('2-Lista A', font, formaVen, (anchoVen / 3), (altoVen / 3) + 150, colorVen)
        showText('3-Lista B', font, formaVen, (anchoVen / 3), (altoVen / 3) + 200, colorVen)
        pygame.display.update()
        relojPrincipal.tick(5)
    return op
