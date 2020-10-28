import line_notice
import voice


voice_class = voice.voiceFunctionsClass()
voice_class.voice_recode()
voice_result = voice_class.voice_recognize()
line_notice.send(voice_result)