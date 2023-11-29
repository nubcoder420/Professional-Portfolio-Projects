import tkinter as tk
from datetime import datetime

test_words = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer semper tortor sed tempor semper. Aenean cursus imperdiet lacus. Ut rhoncus pretium arcu, id porttitor arcu. Vivamus dolor quam, mollis ac sapien et, tristique luctus nisi. Morbi placerat varius sapien, id aliquam dolor aliquet vel. Aliquam non ex blandit, maximus magna eget, blandit eros. Vestibulum elementum varius velit, ac interdum quam tincidunt quis. Aliquam erat volutpat.

Sed eu eros id nunc eleifend lobortis ut quis sapien. Duis vitae magna vitae augue fringilla accumsan. Nam pretium metus eros, malesuada congue mauris pulvinar id. Donec luctus enim in tellus vehicula, sit amet porttitor urna congue. Cras quam ligula, auctor vitae ante vel, mattis maximus magna. Curabitur vel maximus leo. Nullam vel velit volutpat, fermentum purus et, malesuada enim. Cras a metus sed diam rhoncus sagittis. In hac habitasse platea dictumst. Quisque dictum erat ut nisi aliquet, nec feugiat eros porta. Nunc pellentesque vehicula ultrices. Donec sollicitudin, erat sit amet volutpat suscipit, leo massa scelerisque elit, id consectetur sem enim vel turpis. Fusce congue eget ex in ultrices. Aliquam vestibulum varius laoreet. Praesent bibendum elit a orci auctor malesuada.

Proin magna risus, aliquet dapibus viverra id, vehicula at eros. Cras ac rhoncus massa. Phasellus at tellus ac nibh pharetra pretium sit amet et arcu. Vestibulum at ex rutrum leo dapibus elementum a et tortor. Fusce commodo, lacus a dictum rhoncus, lacus orci vulputate est, commodo ultrices lectus enim eu turpis. Fusce bibendum id justo eget semper. Vestibulum tincidunt quis lacus sit amet auctor. In commodo urna ex, eget fringilla felis facilisis pretium. Maecenas risus turpis, auctor id ligula vel, aliquet venenatis urna. Morbi a nibh gravida, vehicula orci sed, sagittis velit. Sed nulla nisi, finibus at cursus sed, auctor pharetra purus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam imperdiet, ligula in dapibus aliquam, erat mi placerat lacus, eu convallis elit sem ut lacus. Maecenas egestas diam non aliquam auctor.

"""

words_list = test_words.split()


class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Typing Speed Test')

        self.words_list = words_list
        self.current_word_index = 0

        self.start_time = None
        self.end_time = None
        self.timer_id = None

        self.label_text = tk.StringVar()
        self.label_text.set('Type the following text:')
        self.label = tk.Label(root, textvariable=self.label_text, font=('Arial', 12))
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(root, font=('Arial', 12))
        self.text_entry.pack(pady=30)
        self.text_entry.focus_set()

        self.start_button = tk.Button(root, text='Start Test', command=self.start_test)
        self.start_button.pack(pady=10)

        self.result_label_text = tk.StringVar()
        self.result_label = tk.Label(root, textvariable=self.result_label_text, font=('Arial', 12))
        self.result_label.pack(pady=10)  # Display the result label below the start button

    def start_test(self):
        self.words_list = words_list
        self.current_word_index = 0

        # Display the first ten words to type
        display_text = " ".join(self.words_list[:10])
        self.label_text.set(display_text)

        self.result_label_text.set('')
        self.start_button['state'] = 'disabled'
        self.text_entry.delete(0, tk.END)
        self.text_entry['state'] = 'normal'
        self.text_entry.bind('<Key>', self.check_input)

        # Start the timer
        self.start_time = datetime.now()
        # Schedule the end_test function to be called after 60 seconds
        self.timer_id = self.root.after(60000, self.end_test)

    def end_test(self):
        # User has completed 60 seconds, end the test
        self.root.after_cancel(self.timer_id)
        self.end_time = datetime.now()
        elapsed_time = self.end_time - self.start_time
        elapsed_minutes = elapsed_time.total_seconds() / 60.0
        words_per_minute = int(len(self.words_list) / elapsed_minutes)

        result_text = f'Your typing speed: {words_per_minute} words per minute'
        self.result_label_text.set(result_text)

        self.start_button['state'] = 'normal'
        self.text_entry['state'] = 'disabled'
        self.text_entry.unbind('<Key>')

    def check_input(self, event):
        entered_text = self.text_entry.get()
        entered_words = entered_text.split()

        # Determine the current set of words to display
        start_index = (len(entered_words) // 10) * 10
        current_words = self.words_list[start_index:start_index + 10]

        # Display the current set of words
        display_text = " ".join(current_words)
        self.label_text.set(display_text)

        if entered_words == self.words_list[:len(entered_words)]:
            if len(entered_words) == len(self.words_list):
                # User has completed typing all words
                self.end_test()
            elif len(entered_words) % 10 == 0:
                # User has correctly typed the current set of words, display the next set
                next_words = self.words_list[len(entered_words):len(entered_words) + 10]
                next_display_text = " ".join(next_words)
                self.label_text.set(next_display_text)
        else:
            # User has made a mistake, display the current set of words again
            self.result_label_text.set('')


if __name__ == '__main__':
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()