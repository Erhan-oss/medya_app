# medya_app

#file structure


#-medya_app
|  #->templates
|   | #->index.html
|  #->uploads
|  #app.py

--coloudflare hesabından bir tünel açıp, konsol üzerindende herhangi bir porttan (dosyalarda 8080)
oluşturulan tünele bağlanmak için kullanılan:
---------------------------------------------------
bash
cloudflared tunnel --url http://localhost:8080
---------------------------------------------------
 --cloudflareden aldığın geçici domain ile internete yayınlayabilirsin.
