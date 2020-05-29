import tkinter
import sys
import random

FILENAME='Lexicon.txt'


def main():
    canvas=make_canvas(450,650)
    hang_structure(canvas)
    error_count=0
    word=get_word(FILENAME)
    lines=print_lines(word)
    print("")
    print("Welcome to Hangman!")
    print("")
    print(lines)
    while error_count<11:
        print("")
        guess=input("Enter a letter from A to Z: ").upper()
        while (check_if_letter(guess) or check_if_one_letter(guess)):
            print("You must enter one a letter from A to Z")
            guess = input("Enter a letter from A to Z: ").upper()
        if check_if_in_word(guess,word):
            lines=print_updated_lines(lines, word,guess)
            print(lines)
            print(" ")
            if "_" not in lines:
                print("Congrats! you've guessed the word")
                sys.exit()
        else:
            print("Letter "+guess+" is not part of the word.")
            print(" ")
            print(lines)
            print(" ")
            error_count+=1
            draw_body_part(canvas,error_count)
    print("Game Over. The word was: "+word)
    canvas.mainloop()

def get_word(file):
    words_list=[]
    for line in open(file):
        line=line.strip()
        word=line.split()
        words_list+=word
    length=len(words_list)
    word=words_list.pop(random.randint(0,length-1))
    return word

def print_lines(word):
    lines=""
    for ch in word:
        lines+="_ "
    return lines

def check_if_letter(guess):
    return not guess.isalpha()

def check_if_one_letter(guess):
    return len(guess)>1

def check_if_in_word(guess, word):
    if guess in word:
        return True
    else:
        return False

def print_updated_lines(lines, word, guess):
    new_lines=""
    very_new=""
    lines=lines.replace(" ","")
    for ch in range(len(word)):
        char_word=word[ch]
        if char_word==guess:
            new_lines+=guess
        else:
            new_lines+="_"
    for char in range(len(new_lines)):
        char_lines=new_lines[char]
        ch_lines=lines[char]
        if char_lines=="_" and ch_lines=="_":
            very_new+="_ "
        elif char_lines!="_":
            very_new+=char_lines+" "
        elif ch_lines!="_":
            very_new+=ch_lines+" "
    return very_new

def draw_body_part(canvas,error):
    if error==1:
        canvas.create_oval(250,105,340,195, fill="NavajoWhite2")
    elif error==2:
        canvas.create_line(295,195,295,400)
    elif error==3:
        canvas.create_line(295,400,230,480)
    elif error==4:
        canvas.create_line(295,400,360,480)
    elif error==5:
        canvas.create_line(295,245,230,305)
    elif error==6:
        canvas.create_line(295,245,360,305)
    elif error==7:
        canvas.create_oval(275,135,290,146,fill="White")
        canvas.create_oval(283,139,288,144,fill="Black")
    elif error==8:
        canvas.create_oval(300, 135, 315, 146, fill="White")
        canvas.create_oval(308, 139, 313, 144, fill="Black")
    elif error==9:
        canvas.create_line(290,180,302,182)


def hang_structure(canvas):
    canvas.create_rectangle(50,540,400,565, fill='LightBlue4',outline='white')
    canvas.create_rectangle(125, 50, 150, 540,fill='LightBlue4',outline='white')
    canvas.create_rectangle(150, 70, 300, 85, fill='LightBlue4', outline='white')
    canvas.create_rectangle(290, 85, 300, 105, fill='LightBlue4', outline='white')



def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas

if __name__ == '__main__':
    main()