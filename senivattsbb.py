import pyttsx4

engine = pyttsx4.init('sapi5')
# voices = engine.getProperty('voices')
# for voice in voices:
#     print(voice.id)
engine.setProperty('voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Dünýä')
rate = engine.getProperty('rate')
# print(rate)
engine.setProperty('rate', 120)

# ssml = '''
# <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="de-DE">
#     <voice name="en-US-JennyNeural">
#         <prosody rate="-20%" pitch="0%">
#             <phoneme alphabet="ipa" ph="nuzɔ bɛnubɛfanɔ jɔnɔ jɛnɔ ladɔ jɛbɛnɔ nuza bɛn a zɛvɔ"> tomato </phoneme>
#         </prosody>
#     </voice>
# </speak>
# '''
# ssml = 'nuzo benubefano jono jeno lado jebeno nuza ben a zevo SianhGheln, linove u Borifatovone a Sig e fatove a nuzo vog. u fatove, Engusinzim lopike a lopove u zugove e rede loz zu hake a zugiken a Sig. Engusinzim hok ke, du nuzo e zevo Sig ruvag zugi, zogen ju jehe tur, e tence Huriputo so flasove Devideriploda so fene poj zugi.'
# ssml = 'nuzo'
ssml = 'engusynzym hok ke devideriploda'
engine.say(ssml)
# engine.say('''<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="sr-RS">
#         <voice name="Dragana">
#             <mstts:express-as   >
#                 <prosody rate="0%" pitch="0%">
#                     <phoneme alphabet="ipa" ph="neːs pataka"></phoneme>
#                 </prosody>
#             </mstts:express-as>
#         </voice>
#     </speak>
#     ''')
engine.runAndWait()