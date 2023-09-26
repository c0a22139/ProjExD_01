import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_2 = pg.transform.flip(bg_img, True, False)
    c3_img = pg.image.load("ex01/fig/3.png")
    c3_img = pg.transform.flip(c3_img, True, False)
    c3_img_2 = pg.transform.rotozoom(c3_img, 2.5, 1.0) 
    c3_img_3 = pg.transform.rotozoom(c3_img, 5, 1.0)
    c3_img_4 = pg.transform.rotozoom(c3_img, 7.5, 1.0)
    c3_img_5 = pg.transform.rotozoom(c3_img, 10, 1.0)
    list_c3 = [c3_img, c3_img_3, c3_img_5,c3_img_3]
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr * 10 %6400
        screen.blit(bg_img,[-x,0])
        screen.blit(bg_img_2,[1600-x,0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(bg_img_2,[4800-x,0])
        screen.blit(bg_img,[6400-x, 0])
        screen.blit(list_c3[tmr%4],[300,200])
        pg.display.update()
        tmr += 1
       
           
        
        
        clock.tick(20)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()