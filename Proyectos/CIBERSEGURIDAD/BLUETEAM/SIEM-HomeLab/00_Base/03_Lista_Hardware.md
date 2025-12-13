

---

## 1️⃣ Hardware principal

### 🔹 **Servidor Firewall (OPNsense)**

#### **Partaker H15 – Mini-PC fanless para OPNsense**

**CPU elegida:**

- **Intel Core i7-1255U – 10 núcleos (2P+8E) – 12 hilos – hasta 4.7 GHz**
    

**LAN:**

- **6 × Intel i226-V 2.5 GbE**  
    → La NIC _obligatoria_ para OPNsense (evitas problemas de controladores)
    

**Memoria:**

- Hasta **64 GB DDR4 3200 MHz**
    
- Recomendado: **16 GB DDR4** (suficiente)
    

**Almacenamiento:**

- 1× **M.2 NVMe 2280**
    
- 1× **2.5″ SATA**
    

> En tu caso: **512 GB NVMe**, correcto.

**Funciones de seguridad:**

- **TPM 2.0**
    
- Arranque automático
    
- Watchdog
    
- Low-power PCH
    
- Fanless (cero ruido, cero polvo)
    

**Aplicaciones soportadas:**

- OPNsense
    
- pfSense
    
- VyOS
    
- OpenWrt
    
- Firewall + VPN + VLAN + IDS/IPS + HAProxy + WireGuard
    

**Consumo energético:**

- 10–18 W  
    (enorme ventaja para 24/7)

![[Pasted image 20251126115557.png]]
![[Pasted image 20251126115445.png]]
>https://es.aliexpress.com/item/1005009096070218.html?spm=a2g0o.productlist.main.2.6b49iNAYiNAYeM&algo_pvid=2afcc34e-f28f-4b9b-8ba2-e1f8fa899c39&algo_exp_id=2afcc34e-f28f-4b9b-8ba2-e1f8fa899c39-1&pdp_ext_f=%7B%22order%22%3A%22-1%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21EUR%21490.37%21387.39%21%21%21552.09%21436.15%21%4021038e1e17640958906224946ecb55%2112000047894443661%21sea%21ES%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3A1519af05%3Bm03_new_user%3A-29895&curPageLogUid=XylNsVmOkzid&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009096070218%7C_p_origin_prod%3A#nav-specification
---

### 🔹 **Servidor Proxmox / SIEM / Laboratorio SOC**

>No ofrece confianza los proveedores de amazon y hay que tener cuidado con amazon UK para la factura del iva
>
>ACUTALMENTE FUERA DE STOCK
![[Pasted image 20251126120251.png]]
- Modelo recomendado: **Beelink SER8 – Ryzen 7 8745HS**
    
- RAM: 32 GB DDR5
    
- SSD: 1 TB PCIe 4.0
    
- Función:
    
    - Proxmox VE
        
    - Wazuh Manager
        
    - OpenSearch
        
    - Laboratorio de ataque/defensa (VMs)
        
- Nota: Si el SER8 vuelve a desaparecer, alternativas equivalentes:
    
    - **SER8 Pro (8745HS)**
        
    - **SER7 7840HS**
        
    - **SER6 Pro 7735HS**
        

---

### 🔹 **Servidor Home Assistant (dedicado)**

- Modelo: **Beelink MINI-S13 Pro – Intel N150**
    
- RAM: 16 GB
    
- SSD: 500 GB
    
- Función: Home Assistant OS + add-ons
    
- Consumo: 8–12 W

![[Pasted image 20251126120327.png]]
>https://www.amazon.es/gp/product/B0BYZ3JC3D/ref=ox_sc_act_title_1?smid=AXH2SW380BDWO&th=1

---

## 2️⃣ Almacenamiento (NAS)

### 🔹 **NAS**

- Modelo definitivo: **QNAP TS-473A**
    
    - 4 bahías
        
    - Ryzen V1500B
        
    - 2× 2.5 GbE
        
    - Ampliable a 10 GbE
        
    - VMs ligeras, Docker, snapshots
        
    - Ideal para SIEM/HomeLab + multimedia

![[Pasted image 20251126120654.png]]
>https://www.amazon.es/TS-473A-8G-Bay-2-2-GHz-INT/dp/B092352NHY/ref=sr_1_1?crid=3PWWVT8VAIHP&dib=eyJ2IjoiMSJ9.VEEVFI3zFvUsadswf6EJ9fd8B2bIDQtrdjvO1rVth2sPK0NfyEOQzxdjq3Vzw_pTuZ6ALHS1db6mIJ6uYlFoL87RVjR6uUF0RlHnKJKeaCF9kLPjgEg_XCIlccL-Jg2COmO0ZnNd9gzHGy4VPWctDUmSjUYp2copr-JzrPiN0Cs4oYeWW6OFhHSi_VLuRG_ejv1L8xt2Cm_JB87OIQ_vpgwbtsVrqU2jadAqdiQitNLc8KvJBjkx1G4Kiap_GH4egVk5wnl3lhIOv9yCXctZRVawnuNnu0iyYWgO4IV9B88.0yGZdShCFRkVOFzGz3DlEpOxgHlrgdbIcC-GgoJse2g&dib_tag=se&keywords=NAS+QNAP+TS-473A&qid=1764155128&sprefix=nas+qnap+ts-473a%2Caps%2C121&sr=8-1
---

### 🔹 **Discos – Pool 1 (sensibles – RAID 1)**

- **2× Seagate IronWolf 8 TB – 5400 rpm – CMR – ST8000VNZ02**
    
- Uso:
    
    - Datos importantes
        
    - Backups
        
    - Configs críticas
        
    - Documentación
        
>https://www.amazon.es/gp/product/B0BM4T2L86/ref=ox_sc_act_title_3?smid=A1E49E3QWFWWKM&th=1
### 🔹 **Discos – Pool 2 (multimedia – RAID 1)**

- **2× Seagate IronWolf 12 TB – CMR – ST12000VNZ008**
    
- Uso:
    
    - Plex/Jellyfin
        
    - Series/películas
        
    - Archivos no críticos


>Fuera de stock
---

## 3️⃣ Red y cableado

### 🔹 **Switch principal**

- Modelo: **TP-Link JetStream TL-SG3210XHP-M2**
    
    - 8× 2.5 GbE PoE++
        
    - 2× 10 GbE SFP+
        
    - L2+, VLANs, ACLs, IGMP
        
    - Ideal para APs + cámaras

![[Pasted image 20251126120729.png]]
>https://www.amazon.es/gp/product/B08SJTPJH7/ref=ox_sc_act_title_2?smid=A1AT7YVPFBWXBL&psc=1
---

### 🔹 **Patch panel y keystones**

- Patch panel: **DIGITUS 24 puertos – 1U – apantallado – Keystone**

![[Pasted image 20251126120836.png]]
>https://www.amazon.es/gp/product/B004C0V29W/ref=ox_sc_act_title_21?smid=A1E49E3QWFWWKM&th=1

- Keystones: **24× DIGITUS Cat 6A blindados – versión compacta**

![[Pasted image 20251126120907.png]]
>https://www.amazon.es/gp/product/B0FTF5Z6DJ/ref=ox_sc_act_title_22?smid=A1AT7YVPFBWXBL&th=1


---

### 🔹 **Cable estructurado (vivienda)**

- Bobina: **DIGITUS Cat 6A – U-FTP – LSZH – 100 m – AWG23**

![[Pasted image 20251126120938.png]]
>https://www.amazon.es/gp/product/B00I2EOBBK/ref=ox_sc_act_title_18?smid=A1AT7YVPFBWXBL&th=1

---

### 🔹 **Cables cortos (rack)**

- **2× packs 0.5 m (20 cables)** – CAT6A S-FTP

![[Pasted image 20251126121224.png]]
>https://www.amazon.es/gp/product/B00NVL40EC/ref=ox_sc_act_title_19?smid=A38EVDLV2KVCJ3&th=1


- **1× pack 1 m (10 cables)** – CAT6A S-FTP

![[Pasted image 20251126121259.png]]
>https://www.amazon.es/gp/product/B00NVLDQ06/ref=ox_sc_act_title_12?smid=A38EVDLV2KVCJ3&th=1

---

## 4️⃣ Rack y accesorios

### 🔹 **Rack**

- **DIGITUS Unique – 19” – 16U – 600 mm – gris**

![[Pasted image 20251126121330.png]]
>https://www.amazon.es/gp/product/B000GRU070/ref=ox_sc_act_title_11?smid=A2OJM9ELVGD4BZ&th=1

---

### 🔹 **Bandejas**

- 2× bandejas **1U – 250 mm**

![[Pasted image 20251126121417.png]]
>https://www.amazon.es/gp/product/B003AOYLOE/ref=ox_sc_act_title_9?smid=A1E49E3QWFWWKM&th=1


- 1× bandeja **1U – 400 mm**

![[Pasted image 20251126121444.png]]
>https://www.amazon.es/gp/product/B003BWJAQY/ref=ox_sc_act_title_10?smid=A1E49E3QWFWWKM&th=1

---

### 🔹 **Ventilación**

- **Unidad de ventiladores DIGITUS (Dynamic Basic/Unique)**
    
    - 2 ventiladores
        
    - Termostato
        
    - Montaje superior

![[Pasted image 20251126121517.png]]
>https://www.amazon.es/gp/product/B00DMNKQ3I/ref=ox_sc_act_title_7?smid=A1AT7YVPFBWXBL&psc=1

---

### 🔹 **Gestión de cables del rack**

- 1× panel con **cepillo + 4 guías**

![[Pasted image 20251126121710.png]]
>https://www.amazon.es/gp/product/B08BPGRNZX/ref=ox_sc_act_title_8?smid=A1E49E3QWFWWKM&psc=1

- 2× **entradas de cable con cepillo** (1U cada una)

![[Pasted image 20251126121942.png]]
>https://www.amazon.es/gp/product/B0014GE7IA/ref=ox_sc_act_title_15?smid=A1E49E3QWFWWKM&psc=1

---

### 🔹 **Tornillería / montaje**

- deleyCON – **100× tuercas enjauladas M6 + tornillos**

![[Pasted image 20251126122118.png]]
>https://www.amazon.es/gp/product/B07Q4Q6BYR/ref=ox_sc_act_title_14?smid=A326X3AG3XUTK4&th=1

---

## 5️⃣ Alimentación y energía

### 🔹 **SAI / UPS**

- **Eaton 5SC 1000i IEC – rack 2U**
    
    - 1000 VA
        
    - 8× IEC C13
        
    - Software de apagado line-interactive

![[Pasted image 20251126122150.png]]
>https://www.amazon.es/gp/product/B09KNPWP2C/ref=ox_sc_act_title_6?smid=A33WZWG42W0AU5&th=1

---

### 🔹 **PDUs del rack**

- **PDU IEC C13 (9 tomas) – 1U**

![[Pasted image 20251126122326.png]]
>https://www.amazon.es/gp/product/B0BDM68G3L/ref=ox_sc_act_title_4?smid=A1AT7YVPFBWXBL&th=1

- **Regleta Schuko (7 tomas) – vertical – con protección**
![[Pasted image 20251126122302.png]]
>https://www.amazon.es/gp/product/B078KQGW4W/ref=ox_sc_act_title_5?smid=A1E49E3QWFWWKM&th=1

---

### 🔹 **Cables IEC (a comprar según necesidad)**

- Recomendación:
    
    - **6× cables C14 → C13 (50–100 cm)**
        
- Función:
    
    - SAI → PDU IEC
        
    - PDU → NAS
        
    - PDU → Mini-PCs
        
    - PDU → switch
        

---

## 6️⃣ Herramientas y organización de cableado

- Crimpadora RJ45 VCE Pro

![[Pasted image 20251126122458.png]]
>https://www.amazon.es/gp/product/B07VZTN6YK/ref=ox_sc_act_title_16?smid=A2XY2J3FRQ9IR9&psc=1

- Tester RJ45/RJ12 deleyCON

![[Pasted image 20251126122517.png]]
>https://www.amazon.es/gp/product/B08R1XV7V6/ref=ox_sc_act_title_17?smid=A326X3AG3XUTK4&th=1

- SUPVAN G15M (etiquetadora industrial)

![[Pasted image 20251126122441.png]]
>https://www.amazon.es/gp/product/B0DSFRZPTN/ref=ox_sc_act_title_13?smid=A3EDYKTGMKE2CW&th=1

- Kit de organización SOULWIT 200 pcs

![[Pasted image 20251126122542.png]]
>https://www.amazon.es/gp/product/B0928VJDZ3/ref=ox_sc_act_title_20?smid=A31OWVAP5YKVZM&th=1

---

## 7️⃣ IoT mínimo (solo lo necesario para pruebas SOC/HA)

- 2–4 enchufes inteligentes
    
- 2–3 sensores temp/humedad
    

---
