
class Entity(object):

    def __init__(self, stats = None):
        self.stats = {}
        '''A base set of stats when stats are not provided'''
        if(stats == None):
            self.stats['HP'] = 10
            self.stats['STR'] = 5
            self.stats['AGI'] = 5
            self.stats['DEX'] = 5
        else:
            for k, v in stats.iteritems():
                self.stats[k] = v
        self.equipped = []
        self.inventory = []

    def heal(self, points):
        self.stats['HP'] += points

    def hurt(self, points):
        self.stats['HP'] -= points

    def is_dead(self):
        if(self.stats['HP'] <= 0):
            print '{} has died.'.format(self.name)
            return True
        else:
            return False

    def is_alive(self):
        return not self.is_dead()

    def getAttack(self):
        return self.stats['STR'] * 1.3

