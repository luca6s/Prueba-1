import time
from files_otros.store_selenium import Store_Sele

with Store_Sele() as bot:

    bot.get_url()
    bot.rellenar_form()