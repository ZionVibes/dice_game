import random
import time
from collections import Counter

class DiceGame:
    def __init__(self):
        self.language = self.select_language()
        self.translations = self.get_translations()
        self.categories = self.get_categories()
        self.players = self.setup_players()
        self.current_player_index = 0
    
    def select_language(self):
        """Let user select game language"""
        print("🎲 Welcome / Witaj! 🎲")
        print("Select language / Wybierz język:")
        print("1. English")
        print("2. Polski")
        
        while True:
            try:
                choice = input("Enter choice / Wpisz wybór (1-2): ")
                if choice == '1':
                    return 'en'
                elif choice == '2':
                    return 'pl'
                else:
                    print("Please enter 1 or 2 / Proszę wpisać 1 lub 2")
            except:
                print("Please enter 1 or 2 / Proszę wpisać 1 lub 2")
    
    def get_translations(self):
        """Get translations for selected language"""
        translations = {
            'en': {
                'welcome': "🎲 Welcome to the Advanced Dice Game! 🎲",
                'based_on': "Based on classic dice game rules with multiple scoring categories.",
                'enter_players': "Enter number of players (1-4): ",
                'invalid_players': "Please enter a number between 1 and 4.",
                'valid_number': "Please enter a valid number.",
                'player_name': "Enter player {} name: ",
                'scoreboard': "SCOREBOARD",
                'current_totals': "CURRENT TOTAL SCORES:",
                'points': "points",
                'player_turn': "{}'s turn!",
                'roll_dice': "Press Enter to roll 5 dice...",
                'your_dice': "Your dice:",
                'die': "Die {}",
                'total': "Total",
                'throw': "Throw {} of 2:",
                'reroll_prompt': "Enter dice numbers to reroll (e.g., '1,3,5'), 'all' for all dice, or press Enter to keep: ",
                'invalid_dice': "Invalid dice numbers. Try again.",
                'invalid_format': "Invalid format. Use comma-separated numbers (e.g., '1,3,5').",
                'all_categories_used': "All categories used!",
                'available_categories': "Available categories:",
                'potential_score': "- potential score: {}",
                'select_category': "Select category (1-{}): ",
                'invalid_choice': "Invalid choice. Try again.",
                'scored_points': "Scored {} points in {}",
                'game_over': "GAME OVER!",
                'final_scores': "Final Scores:",
                'congratulations': "🎉 Congratulations! You won the game! 🎉",
                'computer_wins': "🤖 Computer wins! Better luck next time! 🤖",
                'tie_game': "🤝 It's a tie game! 🤝",
                'tie_players': "It's a tie between {} with {} points! 🤝",
                'play_again': "Would you like to play again? (y/n): ",
                'thanks': "Thanks for playing! 🎲",
                'player': "Player",
                'table_header': "Player"
            },
            'pl': {
                'welcome': "🎲 Witaj w Pokerze Kościanym! 🎲",
                'based_on': "Oparta na klasycznych zasadach gry w kości z wieloma kategoriami punktacji.",
                'enter_players': "Podaj liczbę graczy (1-4): ",
                'invalid_players': "Proszę podać liczbę od 1 do 4.",
                'valid_number': "Proszę podać prawidłową liczbę.",
                'player_name': "Podaj imię gracza {}: ",
                'scoreboard': "TABELA WYNIKÓW",
                'current_totals': "AKTUALNA PUNKTACJA:",
                'points': "punktów",
                'player_turn': "Tura gracza {}!",
                'roll_dice': "Naciśnij Enter, aby rzucić 5 kośćmi...",
                'your_dice': "Twoje kości:",
                'die': "Kość {}",
                'total': "Suma",
                'throw': "Rzut {} z 2:",
                'reroll_prompt': "Podaj numery kości do ponownego rzutu (np. '1,3,5'), 'all' dla wszystkich kości, lub naciśnij Enter, aby zachować obecne: ",
                'invalid_dice': "Nieprawidłowe numery kości. Spróbuj ponownie.",
                'invalid_format': "Nieprawidłowy format. Użyj liczb oddzielonych przecinkami (np. '1,3,5').",
                'all_categories_used': "Wszystkie kategorie wykorzystane!",
                'available_categories': "Dostępne kategorie:",
                'potential_score': "- potencjalne punkty: {}",
                'select_category': "Wybierz kategorię (1-{}): ",
                'invalid_choice': "Nieprawidłowy wybór. Spróbuj ponownie.",
                'scored_points': "Zdobyto {} punktów w kategorii {}",
                'game_over': "KONIEC GRY!",
                'final_scores': "Końcowe wyniki:",
                'congratulations': "🎉 Gratulacje! Wygrałeś grę! 🎉",
                'computer_wins': "🤖 Komputer wygrał! Spróbuj następnym razem! 🤖",
                'tie_game': "🤝 Remis! 🤝",
                'tie_players': "Remis między {} z {} punktami! 🤝",
                'play_again': "Czy chcesz zagrać ponownie? (t/n): ",
                'thanks': "Dziękujemy za grę! 🎲",
                'player': "Gracz",
                'table_header': "Gracz"
            }
        }
        return translations[self.language]
    
    def get_categories(self):
        """Get category names in selected language"""
        if self.language == 'en':
            return {
                '1': 'Ones',
                '2': 'Twos', 
                '3': 'Threes',
                '4': 'Fours',
                '5': 'Fives',
                '6': 'Sixes',
                'pair': 'Pair',
                'two_pairs': 'Two Pairs',
                'three_kind': 'Three of a Kind',
                'four_kind': 'Four of a Kind',
                'poker': 'Poker',
                'full_house': 'Full House',
                'low_straight': 'Low Straight (1-5)',
                'high_straight': 'High Straight (2-6)',
                'chance': 'Chance'
            }
        else:  # Polish
            return {
                '1': 'Jedynki',
                '2': 'Dwójki', 
                '3': 'Trójki',
                '4': 'Czwórki',
                '5': 'Piątki',
                '6': 'Szóstki',
                'pair': 'Para',
                'two_pairs': 'Dwie Pary',
                'three_kind': 'Trójka',
                'four_kind': 'Kareta',
                'poker': 'Poker',
                'full_house': 'Full',
                'low_straight': 'Mały Strit',
                'high_straight': 'Duży Strit',
                'chance': 'Szansa'
            }
    
    
    def setup_players(self):
        """Setup players for game"""
        num_players = 0
        while True:
            try:
                num_players = int(input(self.translations['enter_players']))
                if 1 <= num_players <= 4:
                    break
                else:
                    print(self.translations['invalid_players'])
            except ValueError:
                print(self.translations['valid_number'])
        
        players = []
        for i in range(num_players):
            if i == 0:
                name = input(self.translations['player_name'].format(1)) or self.translations['player'] + " 1"
            else:
                name = input(self.translations['player_name'].format(i+1)) or self.translations['player'] + f" {i+1}"
            
            players.append({
                'name': name,
                'scores': {cat: None for cat in self.categories.keys()},
                'total_score': 0
            })
        
        return players
    
    def roll_dice(self, num_dice=5):
        """Roll specified number of dice"""
        return [random.randint(1, 6) for _ in range(num_dice)]
    
    def display_dice(self, dice):
        """Display dice with visual representation"""
        print("\n" + self.translations['your_dice'])
        for i, die in enumerate(dice, 1):
            print(f"{self.translations['die'].format(i)}: [{die}]")
        print(f"{self.translations['total']}: {sum(dice)}")
    
    def get_dice_to_reroll(self, dice):
        """Get which dice the player wants to reroll"""
        while True:
            try:
                choice = input(self.translations['reroll_prompt'])
                if choice.strip() == '':
                    return []
                elif choice.lower() == 'all':
                    return list(range(len(dice)))
                
                indices = [int(x.strip()) - 1 for x in choice.split(',')]
                if all(0 <= idx < len(dice) for idx in indices):
                    return indices
                else:
                    print(self.translations['invalid_dice'])
            except ValueError:
                print(self.translations['invalid_format'])
    
    def calculate_score(self, dice, category):
        """Calculate score for a given category and dice"""
        counts = Counter(dice)
        dice_sorted = sorted(dice)
        
        if category in ['1', '2', '3', '4', '5', '6']:
            # Number categories - sum of that number
            target = int(category)
            return counts.get(target, 0) * target
        
        elif category == 'pair':
            # Pair - sum of the highest pair
            pairs = [num for num, count in counts.items() if count >= 2]
            if pairs:
                return max(pairs) * 2
            return 0
        
        elif category == 'two_pairs':
            # Two pairs - sum of both pairs (4 of a kind also counts)
            pairs = [num for num, count in counts.items() if count >= 2]
            if len(pairs) >= 2:
                # Take the two highest pairs
                pairs_sorted = sorted(pairs, reverse=True)
                return pairs_sorted[0] * 2 + pairs_sorted[1] * 2
            elif any(count >= 4 for count in counts.values()):
                # Four of a kind counts as two pairs
                num = next(num for num, count in counts.items() if count >= 4)
                return num * 4
            return 0
        
        elif category == 'three_kind':
            # Three of a kind - sum of three (4 of a kind also counts)
            threes = [num for num, count in counts.items() if count >= 3]
            if threes:
                return max(threes) * 3
            elif any(count >= 4 for count in counts.values()):
                # Four of a kind counts as three of a kind
                num = next(num for num, count in counts.items() if count >= 4)
                return num * 3
            return 0
        
        elif category == 'four_kind':
            # Four of a kind - sum of four
            fours = [num for num, count in counts.items() if count >= 4]
            if fours:
                return max(fours) * 4
            return 0
        
        elif category == 'poker':
            # Poker (5 of a kind) - sum of all five
            if any(count == 5 for count in counts.values()):
                return sum(dice)
            return 0
        
        elif category == 'full_house':
            # Full house - pair + three of a kind
            has_three = any(count == 3 for count in counts.values())
            has_pair = any(count == 2 for count in counts.values())
            if has_three and has_pair:
                return sum(dice)
            return 0
        
        elif category == 'low_straight':
            # Low straight - 1,2,3,4,5
            if dice_sorted == [1, 2, 3, 4, 5]:
                return 15
            return 0
        
        elif category == 'high_straight':
            # High straight - 2,3,4,5,6
            if dice_sorted == [2, 3, 4, 5, 6]:
                return 20
            return 0
        
        elif category == 'chance':
            # Chance - sum of all dice
            return sum(dice)
        
        return 0
    
    def get_available_categories(self, player):
        """Get categories that haven't been used yet"""
        return [cat for cat, score in player['scores'].items() if score is None]
    
    def is_game_over(self):
        """Check if game is over - all categories filled for all players"""
        for player in self.players:
            if any(score is None for score in player['scores'].values()):
                return False
        return True
    
    def display_scoreboard(self):
        """Display current scores for all players"""
        print("\n" + "="*120)
        print(self.translations['scoreboard'])
        print("="*120)
        
        # Header (without TOTAL column)
        header = f"{self.translations['table_header']:<15}"
        for cat_key, cat_name in self.categories.items():
            header += f"{cat_name:<15}"
        print(header)
        print("-" * 120)
        
        # Player scores (without total in table)
        for player in self.players:
            row = f"{player['name']:<15}"
            for cat_key in self.categories.keys():
                score = player['scores'][cat_key]
                row += f"{str(score if score is not None else '-'):<15}"
            print(row)
        print("="*120)
        
        # Display total scores separately below the table
        print("\n" + self.translations['current_totals'])
        for player in self.players:
            print(f"{player['name']}: {player['total_score']} {self.translations['points']}")
        print("="*120)
    
    def player_turn(self, player):
        """Handle a single player's turn"""
        print("\n" + self.translations['player_turn'].format(player['name']))
        
        # First roll
        input(self.translations['roll_dice'])
        dice = self.roll_dice()
        self.display_dice(dice)
        
        # Second roll (optional)
        print("\n" + self.translations['throw'].format(2))
        reroll_indices = self.get_dice_to_reroll(dice)
        if reroll_indices:
            for idx in reroll_indices:
                dice[idx] = random.randint(1, 6)
            self.display_dice(dice)
        
        # Category selection
        available_cats = self.get_available_categories(player)
        if not available_cats:
            print(self.translations['all_categories_used'])
            return
        
        print("\n" + self.translations['available_categories'])
        for i, cat in enumerate(available_cats, 1):
            score = self.calculate_score(dice, cat)
            print(f"{i}. {self.categories[cat]} {self.translations['potential_score'].format(score)}")
        
        while True:
            try:
                choice = int(input(self.translations['select_category'].format(len(available_cats)))) - 1
                if 0 <= choice < len(available_cats):
                    selected_cat = available_cats[choice]
                    score = self.calculate_score(dice, selected_cat)
                    player['scores'][selected_cat] = score
                    player['total_score'] += score
                    print(self.translations['scored_points'].format(score, self.categories[selected_cat]))
                    break
                else:
                    print(self.translations['invalid_choice'])
            except ValueError:
                print(self.translations['invalid_choice'])
    
    def display_final_results(self):
        """Display final game results"""
        print("\n" + "="*80)
        print(self.translations['game_over'])
        print("="*80)
        
        self.display_scoreboard()
        
        # Find winner(s)
        max_score = max(player['total_score'] for player in self.players)
        winners = [player for player in self.players if player['total_score'] == max_score]
        
        if len(winners) == 1:
            print(f"\n{self.translations['congratulations'].replace('You', winners[0]['name'])}")
        else:
            winner_names = ", ".join([w['name'] for w in winners])
            print(f"\n{self.translations['tie_players'].format(winner_names, max_score)}")
    
    def play_game(self):
        """Main game loop"""
        print(self.translations['welcome'])
        print(self.translations['based_on'])
        
        while not self.is_game_over():
            self.display_scoreboard()
            
            # Each player takes their turn
            for player in self.players:
                if not self.is_game_over():
                    self.player_turn(player)
        
        self.display_final_results()
        
        # Ask if players want to play again
        play_again = input("\n" + self.translations['play_again'])
        if (play_again.lower() == 'y' and self.language == 'en') or (play_again.lower() == 't' and self.language == 'pl'):
            self.__init__()
            self.play_game()
        else:
            print(self.translations['thanks'])

def main():
    """Main function to start the game"""
    game = DiceGame()
    game.play_game()

if __name__ == "__main__":
    main()
