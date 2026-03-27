import random
import time
from collections import Counter

class DiceGame:
    def __init__(self):
        self.categories = {
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
        
        self.players = self.setup_players()
        self.current_player_index = 0
    
    
    def setup_players(self):
        """Setup players for the game"""
        num_players = 0
        while True:
            try:
                num_players = int(input("Enter number of players (1-4): "))
                if 1 <= num_players <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        players = []
        for i in range(num_players):
            if i == 0:
                name = input("Enter player 1 name: ") or "Player 1"
            else:
                name = input(f"Enter player {i+1} name: ") or f"Player {i+1}"
            
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
        print("\nYour dice:")
        for i, die in enumerate(dice, 1):
            print(f"Die {i}: [{die}]")
        print(f"Total: {sum(dice)}")
    
    def get_dice_to_reroll(self, dice):
        """Get which dice the player wants to reroll"""
        while True:
            try:
                choice = input("Enter dice numbers to reroll (e.g., '1,3,5'), 'all' for all dice, or 'done' to keep: ")
                if choice.lower() == 'done':
                    return []
                elif choice.lower() == 'all':
                    return list(range(len(dice)))
                
                indices = [int(x.strip()) - 1 for x in choice.split(',')]
                if all(0 <= idx < len(dice) for idx in indices):
                    return indices
                else:
                    print("Invalid dice numbers. Try again.")
            except ValueError:
                print("Invalid format. Use comma-separated numbers (e.g., '1,3,5').")
    
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
    
    def display_scoreboard(self):
        """Display current scores for all players"""
        print("\n" + "="*120)
        print("SCOREBOARD")
        print("="*120)
        
        # Header (without TOTAL column)
        header = f"{'Player':<15}"
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
        print("\nCURRENT TOTAL SCORES:")
        for player in self.players:
            print(f"{player['name']}: {player['total_score']} points")
        print("="*120)
    
    def player_turn(self, player):
        """Handle a single player's turn"""
        print(f"\n{player['name']}'s turn!")
        
        # First roll
        input("Press Enter to roll 5 dice...")
        dice = self.roll_dice()
        self.display_dice(dice)
        
        # Second roll (optional)
        print("\nThrow 2 of 2:")
        choice = input("Press Enter to reroll, or 'keep' to keep current dice: ")
        if choice.lower() != 'keep':
            reroll_indices = self.get_dice_to_reroll(dice)
            if reroll_indices:
                for idx in reroll_indices:
                    dice[idx] = random.randint(1, 6)
                self.display_dice(dice)
        
        # Category selection
        available_cats = self.get_available_categories(player)
        if not available_cats:
            print("All categories used!")
            return
        
        print("\nAvailable categories:")
        for i, cat in enumerate(available_cats, 1):
            score = self.calculate_score(dice, cat)
            print(f"{i}. {self.categories[cat]} - potential score: {score}")
        
        while True:
            try:
                choice = int(input(f"Select category (1-{len(available_cats)}): ")) - 1
                if 0 <= choice < len(available_cats):
                    selected_cat = available_cats[choice]
                    score = self.calculate_score(dice, selected_cat)
                    player['scores'][selected_cat] = score
                    player['total_score'] += score
                    print(f"Scored {score} points in {self.categories[selected_cat]}")
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    def is_game_over(self):
        """Check if game is over - all categories filled for all players"""
        for player in self.players:
            if any(score is None for score in player['scores'].values()):
                return False
        return True
    
    def display_final_results(self):
        """Display final game results"""
        print("\n" + "="*80)
        print("GAME OVER!")
        print("="*80)
        
        self.display_scoreboard()
        
        # Find winner(s)
        max_score = max(player['total_score'] for player in self.players)
        winners = [player for player in self.players if player['total_score'] == max_score]
        
        if len(winners) == 1:
            print(f"\n🎉 {winners[0]['name']} wins with {max_score} points! 🎉")
        else:
            winner_names = ", ".join([w['name'] for w in winners])
            print(f"\n🤝 It's a tie between {winner_names} with {max_score} points! 🤝")
    
    def play_game(self):
        """Main game loop"""
        print("🎲 Welcome to the Advanced Dice Game! 🎲")
        print("Based on classic dice game rules with multiple scoring categories.")
        
        while not self.is_game_over():
            self.display_scoreboard()
            
            # Each player takes their turn
            for player in self.players:
                if not self.is_game_over():
                    self.player_turn(player)
            
        
        self.display_final_results()
        
        # Ask if players want to play again
        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again.lower() == 'y':
            self.__init__()
            self.play_game()
        else:
            print("Thanks for playing! 🎲")

def main():
    """Main function to start the game"""
    game = DiceGame()
    game.play_game()

if __name__ == "__main__":
    main()
