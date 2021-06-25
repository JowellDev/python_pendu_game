from random import choice
from typing import List, Tuple, Optional, Type


class WordGenerator:
    _WORDS: List[str] = [
        'bateau',
        'avion',
        'etoile',
        'ticket',
        'train',
        'guerre'
    ]

    def get(self):
        return choice(self._WORDS)


class HangmanEngine:
    lives: int = 6
    has_guessed_word: bool = False
    best_guess: Tuple[str, int] = None

    def __init__(self):
        self.word_to_guess: str = WordGenerator().get()
        self.best_guess = ' '.join(self._match_or_mask_letter()), 0

    def play(self):

        print('Bienvenue au jeu du Pendu 🙂!',
            'Vous devez deviner le mot mystère choisi par l\'ordinateur.', 'Bonne chance', sep='\n')

        print(' '.join(self.best_guess[0]))

        while not self.has_guessed_word and self.lives > 0:
            guess = input('Veuillez entrer votre suggestion: ')

            # Match
            letter_match_count = self._get_letter_match_count(guess)

            if letter_match_count > self.best_guess[1]:
                self.best_guess = ' '.join(self._match_or_mask_letter(
                    guess)), letter_match_count

            if letter_match_count == len(self.word_to_guess):
                self.has_guessed_word = True

            print(self.best_guess[0])

            self.lives -= 1
            print(f'Il ne vous reste que {self.lives} vie(s) 😬')
        else:
            self._check_state()

    def _match_or_mask_letter(self, guessed_word: Optional[str] = None) -> List[str]:
        guessed_word = guessed_word if guessed_word is not None else '_' * \
            len(self.word_to_guess)

        return ['_' if letter != match else letter for letter,
                match in zip(self.word_to_guess, guessed_word)]

    def _get_letter_match_count(self, guessed_word: str) -> int:
        if len(guessed_word) != len(self.word_to_guess):
            return 0

        if guessed_word == self.word_to_guess:
            return len(self.word_to_guess)

        matches = self._match_or_mask_letter(guessed_word)

        return len(
            list(
                filter(
                    lambda x: x != '_', matches
                )
            )
        )

    def _check_state(self):
        if self.has_guessed_word:
            print('Bravo vous avez trouvez le mot mystère 🎉!')
        else:
            print('Vous n\'avez plus de vie 💀. GAME OVER')


class Hangman:
    retry: str = 'o'

    def run(self):
        while self.retry == 'o':
            HangmanEngine().play()
            self.retry = input('Voulez-vous faire une nouvelle partie? o/n ')
        else:
            print('Fin de la partie. Merci d\'avoir jouer 👋🏾')


if __name__ == '__main__':
    Hangman().run()
