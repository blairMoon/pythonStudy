
import string
import random

class Player:
    def __init__(self, name, hp, damage, correct_alp):
      self.name = name      
      self.hp = hp          
      self.damage = damage  
      self.correct_alp = correct_alp
      self.correct_alp = 0  


class Game:

    def __init__(self):
        self.player = []  # 캐릭터의 목록. start_game()에서 생성
        self.user_character = ""  # 사용자가 선택한 캐릭터
        self.remain_alp = list(string.ascii_uppercase)  # 남은 알파벳
        self.cur_string = ["_"] * 10  # 현재까지의 글자상태를 저장
        self.answer_string = ""  # 랜덤 10글자 단어
        self.correct_alp = 0 

    def start_game(self):
        self.player.append(Player("김용빈", 50, 20, 0))
        self.player.append(Player("김규리", 70, 25, 0))
        self.player.append(Player("이승아", 80, 30, 0))
        self.player.append(Player("윤석현", 90, 35, 0))

        self.user_character = input()
        string_pool = string.ascii_uppercase
        for i in range(10):
            self.answer_string += random.choice(string_pool)
             
    def sort_data(self, round):        
        if round == 1:
            self.player.sort(key = lambda x:x.name )
        else:  
            self.player.sort(key = lambda x:-x.hp )     
      
    def play_game(self):

        print(f"게임은 {self.player[0].name},{self.player[1].name},{self.player[2].name},{self.player[3].name} 순으로 진행됩니다.\n")

        for i in range(4):
            if self.player[i].name == self.user_character:
                print("***** 내 캐릭터 *****") 
                print(f"이름: {self.player[i].name} (HP: {self.player[i].hp})")
            else:
                print(f"***** {i+1} 캐릭터 *****")
                print(f"이름: {self.player[i].name} (HP: {self.player[i].hp})")
                
            string_pool = string.ascii_uppercase   
            alpabet = list(string_pool) 
            random_alpabet_list = random.sample(alpabet,k = 1) 
            pick_one = ''.join(map(str,random_alpabet_list))  
            print(f"선택 알파벳 : {pick_one}")  

            if pick_one in self.answer_string: 
                idx = self.answer_string.index(pick_one) 
                self.cur_string[idx] = pick_one
                self.cur_string_str = ' '.join(map(str, self.cur_string))
                self.player[i].correct_alp += 1
                print(self.cur_string_str)
                print("***** 맞았습니다 ᵔεᵔ  *****")
            else:
                damaged_hp = (self.player[i].hp) - (self.player[i].damage)
                self.player[i].hp = damaged_hp
                print("***** 틀렸습니다 (ﾟ⊿ﾟ)  ******")
                print(f"{self.player[i].name}은 틀렸기 때문에 HP가 {self.player[i].hp}입니다.")

    def game_result(self):

        print("\n\n******************* 게임이 끝났습니다 *******************")

        print("=============================")
        print("     게임 순위 - 생명력")
        print("=============================")

        self.player.sort(key = lambda x:-x.hp)
        for i in range(4):
            if self.player[i].name == self.user_character:   
                self.player[i].name = "*" + self.player[i].name + "*"  
            if self.player[i].hp <= 0:      
                self.player[i].hp = "사망"   
        print(f" 1등: {self.player[0].name} (HP:{self.player[0].hp}) \n 2등: {self.player[1].name} (HP:{self.player[1].hp}) \n 3등: {self.player[2].name} (HP:{self.player[2].hp}) \n 4등: {self.player[3].name} (HP:{self.player[3].hp})" )   

        print("=============================")
        print(" 게임 순위 - 알파벳 맞춘 횟수")
        print("=============================")
        self.player.sort(key = lambda x:-x.correct_alp)  
        for i in range(4):
            if self.player[i].name == self.user_character:   
                self.player[i].name = "*" + self.player[i].name + "*"    
        print(f" 1등: {self.player[0].name} {self.player[0].correct_alp}회\n 2등: {self.player[1].name} {self.player[1].correct_alp}회 \n 3등: {self.player[2].name} {self.player[2].correct_alp}회\n 4등: {self.player[3].name} {self.player[3].correct_alp}회" )            
    
    def game(self):
      self.start_game()

      print("******************* 게임 시작 *******************\n")

      for i in range(1, 4):
          print("===========================")
          print(f"     ROUND {i} - START")
          print("===========================")

          self.sort_data(i)
          self.play_game()

          print("===========================")
          print(f"     ROUND {i} - END")
          print("===========================")

      self.game_result()


if __name__ == '__main__':

    game = Game()
    game.game()