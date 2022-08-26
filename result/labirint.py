# Разработай свою игру в этом файле!
from pygame import* # подключаем библиотеку pygame
'''Переменные для картинок'''
#создаём переменные и подключаем к ним картинки
img_back = 'cubes.jpg'
img_hero = 'reaper.png'
img_enemy = 'zombie.png'
img_goal = 'money.png'
img_bullet = 'bullet.png'
'''Шрифт'''
#задаём шрифт и создаём надписи победы и поражения
font.init()
font = font.SysFont('Comic Sans MS',50)
win = font.render('YOU WIN!!!',True,(255,255,0))
lose = font.render('YOU LOSE:(!',True,(255,255,255))
'''Классы'''
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#создаём класс отвечающий за передвижение игрока, наследуя все методы зи класса GameSprite
class Player(GameSprite):
    def update(self): #метод передвижения
        keys = key.get_pressed() #подключаем клавиатуру
        if keys[K_a] and self.rect.x > 5: #герой движется влево
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_widht - 45: #герой движется вправо
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5: #герой движется вверх
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 45: #герой движется вниз
            self.rect.y += self.speed
    #метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.right, self.rect.centery, 15, 20, 15)
        bullets.add(bullet)
#создаём движения врагов
class Enemy(GameSprite):
    side = "left"
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_widht - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Enemy2(GameSprite):
    side = "left"
    def update(self):
        if self.rect.x <= 100:
            self.side = "right"
        if self.rect.x >= win_widht - 250:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Enemy3(GameSprite):
    side = "up"
    def update(self):
        if self.rect.y <= 130:
            self.side = "up"
        if self.rect.y >= win_height - 270:
            self.side = "down"
        if self.side == "down":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
class Wall(sprite.Sprite):
    def __init__(self, red, green, blue, wall_x, wall_y, width, height):
        super().__init__()
        self.red = red
        self.green = green
        self.blue = blue
        self.w = width
        self.h = height
        #каждый спрайт должен хранить свойство image - Surface - прямоугольная подложка
        self.image = Surface((self.w, self.h))
        self.image.fill((red,green,blue))
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
#класс спрайта-пули
class Bullet(GameSprite):
    #движение врага
    def update(self):
        self.rect.x += self.speed
        #исчезает, если дойдет до края экрана
        if self.rect.x > win_widht+10:
            self.kill()
'''Окно игры'''
#Создаём окошко
win_widht = 700 #ширина окна
win_height = 500 #высота окна
display.set_caption("Лабиринт") #название игры
window = display.set_mode((win_widht,win_height))
back = transform.scale(image.load(img_back),(win_widht,win_height)) #задний фон
'''Персонажи'''
hero = Player(img_hero, 5, win_height - 80, 40, 40, 5) #характеристики главного героя и его начальное положение
monster = Enemy(img_enemy, win_widht - 80, 280,65,65, 2)
final = GameSprite(img_goal, win_widht - 120, win_height - 80,65,65,0) #финал до которого должен дойти герой
monster2 = Enemy2(img_enemy, win_widht - 600, 35,65,65,2)
monster3 = Enemy3(img_enemy, win_widht - 600, 60,65,65,2)
'''Стены''' #добавляем стены в нашу игру
w1 = Wall(154,205,50,20,20,670,10)
w2 = Wall(154,205,50,20,480,550,10)
w3 = Wall(154,205,50,20,20,10,380)
w4 = Wall(154,205,50,225,100,10,380)
w5 = Wall(154,205,50,225,100,380,10)
w6 = Wall(154,205,50,600,100,10,110)
w7 = Wall(154,205,50,680,20,10,470)
'''Группа спрайтов''' #создаём группы для врагов, стен и пуль
walls = sprite.Group() #группа стен
monsters = sprite.Group() #группа врагов
bullets = sprite.Group() #группа пуль
'''Добавление спрайтов в группу''' #добавляем все спрайты прописанные выше в группы
monsters.add(monster)
monsters.add(monster2)
monsters.add(monster3)
walls.add(w1)
walls.add(w2)
walls.add(w3)
walls.add(w4)
walls.add(w5)
walls.add(w6)
walls.add(w7)
'''Счётчик очков''' #создаём счётчик, который будет считать поподания по врагам
points = 0
'''Игровой цикл''' #прописываем основной игровой цикл
game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT: #при нажатии на красный крестик игра закрывается
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE: #при нажатии на пробел происходит выстрел
                hero.fire()
                #fire.play()
    if finish != True:
        window.blit(back, (0,0))
        walls.draw(window)
        monsters.update()
        monsters.draw(window)
        hero.reset()
        hero.update()
        final.reset()
        bullets.draw(window)
        bullets.update()
        sprite.groupcollide(bullets, walls, True, False) #при столкновении со стеной пули пропадают
        if sprite.groupcollide(bullets, monsters, True, True): #если пуля попадает во врага засчитывается одно очко
            points+=1
        x = font.render(str(points), True, (255, 255, 255))
        window.blit(x, (20, 20)) #очки отображаются вверху слева
        #Проигрыш
        if sprite.spritecollide(hero, monsters, False): #проверка столкнулся ли герой с врагом
            finish = True #если он столкнулся игра заканчивается
            window.blit(lose, (200,200)) #пишется надпись 'YOU LOSE:(!'
        if sprite.spritecollide(hero, walls, False): #проверка столкнулся ли герой со стеной
            finish = True #если он столкнулся игра заканчивается
            window.blit(lose, (200,200)) #пишется надпись 'YOU LOSE:(!'
        #Победа
        if sprite.collide_rect(hero,final): #проверка дошёл ли герой до финала
            finish = True #если он дошёл игра заканчивается
            window.blit(win, (200,200)) #пишется надпися 'YOU WIN!!!'
    
    display.update()
    clock.tick(FPS)