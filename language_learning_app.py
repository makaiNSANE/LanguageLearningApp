import random

words = [
    {"Portuguese": "o", "english": "the"},
    {"Portuguese": "de", "english": "of/from"},
    {"Portuguese": "que", "english": "that/which"},
    {"Portuguese": "e", "english": "and"},
    {"Portuguese": "a", "english": "the"},
    {"Portuguese": "do", "english": "of the"},
    {"Portuguese": "da", "english": "of the"},
    {"Portuguese": "em", "english": "in"},
    {"Portuguese": "um", "english": "a"},
    {"Portuguese": "para", "english": "for"},
    {"Portuguese": "é", "english": "is"},
    {"Portuguese": "com", "english": "with"},
    {"Portuguese": "não", "english": "not"},
    {"Portuguese": "uma", "english": "a"},
    {"Portuguese": "os", "english": "the"},
    {"Portuguese": "no", "english": "in"},
    {"Portuguese": "por", "english": "by"},
    {"Portuguese": "mais", "english": "more"},
    {"Portuguese": "como", "english": "like"},
    {"Portuguese": "mas", "english": "but"},
]

def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['Portuguese']}'?")
        user_answer = input("Your Answer: ").strip() .lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct, Great!\n!")
            score +=1
        else:
            print(f"Wrong, dummy! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")



def main():
    print("Welcome to the Language Learning Flashcards App")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()