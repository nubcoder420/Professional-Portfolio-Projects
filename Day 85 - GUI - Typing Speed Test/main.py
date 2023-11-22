import tkinter as tk
from datetime import datetime
import random


test_words = """

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer semper tortor sed tempor semper. Aenean cursus imperdiet lacus. Ut rhoncus pretium arcu, id porttitor arcu. Vivamus dolor quam, mollis ac sapien et, tristique luctus nisi. Morbi placerat varius sapien, id aliquam dolor aliquet vel. Aliquam non ex blandit, maximus magna eget, blandit eros. Vestibulum elementum varius velit, ac interdum quam tincidunt quis. Aliquam erat volutpat.

Sed eu eros id nunc eleifend lobortis ut quis sapien. Duis vitae magna vitae augue fringilla accumsan. Nam pretium metus eros, malesuada congue mauris pulvinar id. Donec luctus enim in tellus vehicula, sit amet porttitor urna congue. Cras quam ligula, auctor vitae ante vel, mattis maximus magna. Curabitur vel maximus leo. Nullam vel velit volutpat, fermentum purus et, malesuada enim. Cras a metus sed diam rhoncus sagittis. In hac habitasse platea dictumst. Quisque dictum erat ut nisi aliquet, nec feugiat eros porta. Nunc pellentesque vehicula ultrices. Donec sollicitudin, erat sit amet volutpat suscipit, leo massa scelerisque elit, id consectetur sem enim vel turpis. Fusce congue eget ex in ultrices. Aliquam vestibulum varius laoreet. Praesent bibendum elit a orci auctor malesuada.

Proin magna risus, aliquet dapibus viverra id, vehicula at eros. Cras ac rhoncus massa. Phasellus at tellus ac nibh pharetra pretium sit amet et arcu. Vestibulum at ex rutrum leo dapibus elementum a et tortor. Fusce commodo, lacus a dictum rhoncus, lacus orci vulputate est, commodo ultrices lectus enim eu turpis. Fusce bibendum id justo eget semper. Vestibulum tincidunt quis lacus sit amet auctor. In commodo urna ex, eget fringilla felis facilisis pretium. Maecenas risus turpis, auctor id ligula vel, aliquet venenatis urna. Morbi a nibh gravida, vehicula orci sed, sagittis velit. Sed nulla nisi, finibus at cursus sed, auctor pharetra purus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam imperdiet, ligula in dapibus aliquam, erat mi placerat lacus, eu convallis elit sem ut lacus. Maecenas egestas diam non aliquam auctor.

Proin mattis interdum sem eget porttitor. Mauris tempus, diam eu cursus facilisis, magna massa suscipit massa, molestie ullamcorper nisi arcu a purus. Proin turpis orci, rutrum sed mi eu, dignissim pretium magna. Aenean blandit leo et porta hendrerit. In vehicula purus vitae odio semper laoreet. Suspendisse ante lacus, finibus a auctor ac, condimentum sed lectus. Phasellus vitae ipsum non dui laoreet venenatis. Donec pharetra at ligula eu rhoncus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

Suspendisse tellus turpis, vestibulum sit amet varius at, dictum et metus. Morbi consequat sagittis purus ac pretium. Quisque semper ligula et urna facilisis, ut sodales massa volutpat. Fusce sed eros tortor. In semper quis justo eu laoreet. Nulla odio ex, iaculis sed enim ac, cursus volutpat justo. Phasellus aliquet, risus a mollis auctor, nisl urna accumsan nulla, nec gravida felis ipsum a nunc. Vivamus rhoncus pharetra urna, ut ultricies nunc condimentum a.

Proin quis ligula mauris. Ut vulputate ipsum quis augue pulvinar faucibus. Aenean tincidunt urna massa, vitae molestie mauris efficitur et. Nulla facilisi. Etiam vitae tincidunt magna. Nullam consequat aliquet lectus in tincidunt. Maecenas eget quam pulvinar, ullamcorper ipsum eget, tristique justo. Maecenas nibh nisi, pretium quis egestas sed, venenatis hendrerit eros. Nullam blandit nec velit dignissim scelerisque. Ut eu scelerisque odio. Suspendisse neque felis, venenatis quis maximus nec, laoreet vel eros. Integer blandit porta risus, sit amet lacinia risus sollicitudin non. In tristique vel leo non tincidunt. Pellentesque ornare eget arcu sit amet pretium. Pellentesque eget venenatis ante.

Vivamus luctus laoreet elit et convallis. Donec venenatis dui in maximus luctus. Quisque sed facilisis neque. Donec id augue dictum, condimentum nibh sed, aliquet urna. Nulla viverra euismod ex. Nunc id porta tellus. Nulla magna sem, commodo id sapien at, gravida rutrum leo. Nunc erat velit, mattis eu volutpat eu, rhoncus suscipit libero. Nullam ac enim tincidunt metus dapibus molestie. Curabitur et mauris rutrum, dapibus diam at, hendrerit urna. Fusce interdum eros tincidunt, eleifend turpis ac, faucibus urna. Ut sed lobortis urna. Fusce consequat urna sed erat gravida convallis. Nunc vitae magna eu nisl suscipit porta quis imperdiet lacus.

Morbi aliquam rhoncus viverra. Pellentesque dictum arcu eget est ultrices facilisis. Aliquam non nisl maximus, tincidunt neque quis, congue eros. Aliquam ut ultrices massa. Aenean feugiat bibendum massa, id consequat arcu condimentum in. Aliquam sodales urna et arcu congue, at elementum nulla elementum. Nullam a placerat lorem. Proin aliquam, nunc eget finibus interdum, quam erat euismod mi, et dictum nibh lectus id ipsum. Nullam facilisis venenatis blandit. Praesent volutpat sapien nec leo viverra tempus. Phasellus est nisl, ultricies nec vestibulum quis, commodo et purus. Praesent vel pellentesque tortor, sit amet venenatis eros. Fusce suscipit augue nisi, ut scelerisque mauris vulputate et. Integer maximus neque vitae felis tincidunt, vitae congue nulla rutrum. Pellentesque ut convallis arcu.

Proin scelerisque porta dignissim. Nulla in auctor justo. Fusce pharetra nulla risus, vitae tempus mi imperdiet in. Etiam sed libero mattis, blandit augue a, bibendum libero. Nulla felis erat, maximus eu facilisis at, dignissim et ex. Nam at rhoncus lacus. Quisque in justo et nisi eleifend placerat. Sed eget nulla erat. Aenean at lorem euismod, ultricies nisi nec, ullamcorper urna. Proin luctus nibh quis lacinia hendrerit. Curabitur vehicula eu orci eu aliquam. Sed molestie quam id tincidunt venenatis. Cras mattis sem eros, ut interdum sapien venenatis sit amet. Quisque gravida et lacus nec facilisis. Mauris dignissim molestie maximus. Vestibulum sit amet eros molestie, rhoncus turpis vel, porta ligula.

Maecenas consectetur nibh vitae nisi bibendum, consequat volutpat justo lacinia. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed hendrerit orci nec leo malesuada feugiat. Duis tempor convallis urna facilisis blandit. Quisque sollicitudin velit eget risus pellentesque ullamcorper. Suspendisse in risus nec urna iaculis varius. Donec vehicula sem at orci dignissim, ultrices bibendum nisi ornare. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla tempor fermentum risus, luctus euismod neque interdum eu. Mauris fermentum elementum risus, eget feugiat dui euismod elementum. In venenatis pretium placerat. Vestibulum odio lacus, iaculis id pulvinar id, sollicitudin vel felis. Aenean. 

"""

words_list = test_words.split()


class TypingSpeedTestApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title('Typing Speed Test')

        self.words = words_list
        self.current_word_index = 0

        self.start_time = None
        self.end_time = None

        self.label_text = tk.StringVar()
        self.label_text.set('Type the following text:')
        self.label = tk.Label(root, textvariable=self.label_text, font=('Arial', 12))
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(root, font=('Arial', 12))
        self.text_entry.pack(pady=10)
        self.text_entry.focus_set()

        self.start_button = tk.Button(root, text='Start Test', command=self.start_test)
        self.start_button.pack(pady=10)

        self.result_label_text = tk.StringVar()
        self.result_label = tk.Label(root, textvariable=self.result_label_text, font=('Arial', 12))


    def start_test(self):

        self.words = words_list
        self.current_word_index = 0

        self.start_time = datetime.now()

        self.label_text.set('Type the following text:')
        self.result_label_text.set('')
        self.start_button["state"] = 'disabled'
        self.text_entry.delete(0, tk.END)
        self.text_entry['state'] = 'normal'
        self.text_entry.bind('<Key>', self.check_input)

    
    def check_input(self, event):

        entered_text = self.text_entry.get()
        entered_words = entered_text.split()

        if entered_words == self.words[:len(entered_words)]:

            if len(entered_words) == len(self.words):
                self.end_time = datetime.now()
                elapsed_time = self.end_time - self.start_time
                elapsed_minutes = elapsed_time.total_seconds() / 60.0
                words_per_minute = int(len(self.words) / elapsed_minutes)

                result_text = f'Your typing speed: {words_per_minute} words per minute'
                self.result_label_text.set(result_text)

                self.start_button['state'] = 'normal'
                self.text_entry['state'] = 'disabled'
                self.text_entry.unbind('<Key>')

        else:
            
            self.label_text.set("Type the following text (mistakes may occur):")


if __name__ == '__main__':
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
