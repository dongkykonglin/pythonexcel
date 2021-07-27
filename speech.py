from gtts import gTTS

text = open('demo.txt', 'r').read()
language = 'zh-CN'
output = gTTS(text=text, lang=language, slow=False)
output.save('fileouput.mp3')
