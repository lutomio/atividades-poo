#INTEGRANTES: Anderson Simioni, Lucas Tomio,  Felipe Pierotti,  Victória Rodrigues Veloso

class ship:
    def __init__(self, name, _len):
        self.name = name
        self.len = _len
    
    def get_name(self):
        return self.name
    
    def get_len(self):
        return self.len

class player:
    def __init__(self, _id, name):
        self.id = _id
        self.name = name
        self.score = 0
    
    def add_score(self, val):
        self.score += val
    
    def get_score(self):
        return self.score
    
    def get_id(self): 
        return self.id
    
    def get_name(self):
        return self.name

class table:
    def __init__(self, n):
        self.size = n
        self.posmap = {}
    
    def print_map(self):
        for x in range(self.size):
            line = ""
            for y in range(self.size):
                if x in self.posmap:
                    if y in self.posmap[x]:
                        line += (" X " if self.posmap[x][y]=='X' else ' O ')
                        continue
                line += (' O ')
                
            print(line)
                
    
    def can_put(self, _ship:ship, is_other_half, x, y, _dir):
        if x <0 or y <0: return False
        if (x+_ship.get_len())>self.size or (y+_ship.get_len())>self.size: return False
        if is_other_half and x < self.size//2: return False
        elif not is_other_half and x > self.size//2: return False
        
        if _dir in ['right', 'left']:
            dir_x = 1 if _dir == 'right' else -1
            for _x in range(x if dir_x>0 else x+_ship.get_len(), (x+_ship.get_len() if dir_x>0 else x), dir_x):
                if _x <0 or y <0: return False
                if (_x+_ship.get_len())>self.size or (y+_ship.get_len())>self.size: return False
                if _x in self.posmap:
                    if y in self.posmap[_x]:
                        return False
        else:
            dir_y = 1 if _dir == 'down' else -1
            for _y in range(x if dir_y>0 else y+_ship.get_len(), (y+_ship.get_len() if dir_y>0 else y), dir_y):
                if x <0 or _y <0: return False
                if (x+_ship.get_len())>self.size or (_y+_ship.get_len())>self.size: return False
                if x in self.posmap:
                    if _y in self.posmap[_y]:
                        return False
                    
        return True
    
    def put_ship(self, player_id, _ship:ship, x, y, _dir):
        if _dir in ['right', 'left']:
            dir_x = 1 if _dir == 'right' else -1
            for _x in range(x if dir_x>0 else x+_ship.get_len(), (x+_ship.get_len() if dir_x>0 else x), dir_x):
                if _x not in self.posmap: self.posmap[_x] = {}
                self.posmap[_x][y] = player_id
        else:
            dir_y = 1 if _dir == 'down' else -1
            for _y in range(x if dir_y>0 else y+_ship.get_len(), (y+_ship.get_len() if dir_y>0 else y), dir_y):
                if x not in self.posmap: self.posmap[x] = {}
                self.posmap[x][_y] = player_id
                
    def hit_ship(self, player_id, x,y):
        if x in self.posmap:
            if y in self.posmap[x]:
                if self.posmap[x][y] != 'X':
                    self.posmap[x][y] = 'X'
                    return 'HIT'
                else:
                    return 'X'
                
        return 'MISS'
                
class game:
    def __init__(self, player1, player2, ship_list, table_size):
        self.players = [player1, player2]
        self.ship_list = ship_list
        self.table_size = table_size
        self.table = table(table_size)
        
    def start_def_ships(self):
        other_half = True
        for player in self.players:
            other_half = not other_half
            print(f"\n{player.get_name()} put ships:")
            for _ship in self.ship_list:
                print(f"Ship: {_ship.get_name()} (size:{_ship.get_len()})")
                
                fail = True
                while fail:
                    print("Set a valid ship positions: ")
                    print(f"x y:")
                    x, y = [int(a) for a in input().split(' ')]
                    print("Directions: ")
                    print(f"right or left or up or down:")
                    _dir = input()
                    fail = not self.table.can_put(_ship, other_half, x, y, _dir)
                    if not fail: self.table.put_ship(player.get_id(), _ship, x,y,_dir)            
        return
    
    def get_player_by_id(self, id):
        for p in self.players:
            if p.get_id() == id:
                return p
    
    def check_winner(self):
        for p in self.players:
            if p.get_score() >= sum([x.get_len() for x in self.ship_list]):
                return p.get_id()
            
        return -1
    
    def play(self):
        winner_id = -1
        player1 = True
        
        while winner_id == -1:
            print("\n")
            self.table.print_map()
            _player = self.players[0 if player1 else 1]
            fail = True
            while fail:
                fail = False
                print(f"\n{_player.get_name()} time x y:")
                x, y = [int(a) for a in input().split(' ')] 
                if player1 and x < self.table_size//2: fail = True
                elif not player1 and x > self.table_size//2: fail = True 
            
            result = self.table.hit_ship(_player.get_id(), x,y)
            print("STRIKE" if result=='HIT' else result)
            if result == 'HIT': _player.add_score(1)
            winner_id = self.check_winner()
            player1 = not player1
        
        print(f"WINNER {self.get_player_by_id(winner_id).get_name()}")
        
        return
    
    def start(self):
        #self.table.print_map()
        self.start_def_ships()
        self.play()

new_game = game(
    player(1, "Player 1"), player(2, "Player 2"),
    [ship("lancha", 1), ship("barco", 2)],
    20
    )

new_game.start()
