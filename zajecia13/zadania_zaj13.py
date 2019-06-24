# Player vs alien


class Player(object):

    def blast(self, enemy):
        print('Gracz razi wroga')
        enemy.die()


class Alien(object):

    def die(self):
        print('Mowa pozegnalna')


if __name__ == '__main__':
    print('death of the alien')
    hero = Player()
    invader = Alien()
    hero.blast(invader)
    input('wcisnij enter aby zakonczyc')

