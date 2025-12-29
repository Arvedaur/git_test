1. STRATEJİK VİZYON (ÖZET)

Proje 3 ana katman üzerine inşa edilir:

Layer 1: Generation & Spot Market (mevcut çekirdek)
Layer 2: Transmission & System Operation (TSO perspektifi)
Layer 3: Exchange & Financial Markets (borsa ve türevler)


Her katman:

Öncekini kullanır

Ama yeni bir oyuncu rolü ve kazanma koşulu getirir

Bu yaklaşım:

“Tek oyun, çok rol” stratejisidir.

2. FAZ 0 — MEVCUT DURUM (v0.3) ✅
Durum

Python engine

Streamlit UI

Günlük spot market simülasyonu

NPC rekabeti

Grafik dashboard

Test altyapısı

Oyuncu Rolü

Elektrik üreticisi (Generator / Asset Owner)

Temel Kazanma Koşulu

Uzun vadede pozitif nakit akışı

Düşük curtailment

Dengeli dispatch

3. FAZ 1 — CORE GAMEPLAY DERİNLEŞTİRME (v0.4 – v0.5)

🎯 Amaç:
Mevcut oyunu “öğretici prototip”ten
derin ve tekrar oynanabilir bir oyun hâline getirmek.

Planlanan Feature’lar

Battery Storage (depolama)

Negative prices

NPC personality types

Market shock events (hava, arıza)

Benchmark AI (gold standard player)

Replay & timeline slider

Difficulty presets

Extended analytics (KPIs)

Etki

Oynanabilirlik artar

Öğrenme eğrisi güçlenir

Oyuncu davranışı çeşitlenir

4. FAZ 2 — TRANSMISSION / TSO MODE (v0.6 – v0.8)

🎯 Amaç:
Oyuna iletim sistemi perspektifini eklemek
ve “üretici” bakışını sistem operatörü bakışıyla tamamlamak.

4.1 Yeni Oyuncu Rolü: TSO

Oyuncu bu modda:

Üretici değil

İletim sistemi operatörüdür (TSO)

Temel Hedef

Sistem dengesini sağlamak

Congestion ve blackout riskini minimize etmek

Redispatch maliyetlerini yönetmek

4.2 Temel Transmission Mekanikleri

Bölgesel node yapısı (A / B / C)

Hat kapasite kısıtları

Congestion oluşumu

Forced curtailment

Redispatch kararları

Sistem güvenliği metrikleri

Bu mekanikler:

Fiziksel load-flow değil

Oynanabilir bir soyutlamadır

4.3 Layer 1 ile Bağlantı

Üretici kararları → TSO problemleri yaratır

TSO kararları → üreticinin kârını etkiler

Bu çatışma:

Oyunun en güçlü dramatik noktalarından biri olur.

5. FAZ 3 — EXCHANGE / FINANCIAL MARKET MODE (v1.0+)

🎯 Amaç:
Oyunu sadece fiziksel değil,
finansal bir enerji simülatörü hâline getirmek.

5.1 Yeni Oyuncu Rolü: Trader / Portfolio Manager

Oyuncu bu modda:

Fiziksel üretim yapmaz

Ama fiziksel sonuçlardan etkilenen ürünlerle trade eder

5.2 Finansal Ürünler (Aşamalı)

Başlangıç:

Day-ahead futures

Price caps / floors

Basit hedge kontratları

İleri aşama:

Seasonal futures

Regional spreads

Volatility bazlı ürünler

5.3 Fiziksel – Finansal Bağlantı

Generation hataları → fiyat şokları

Transmission congestion → bölgesel spread

Hava olayları → volatilite

Bu bağ:

Finansal oyunu “kumar” olmaktan çıkarır.

6. MODLAR VE OYNANIŞ YAPISI
Modüler Yapı

Generation Mode

TSO Mode

Exchange Mode

Her mod:

Aynı engine’i kullanır

Farklı UI ve kazanma koşuluna sahiptir

7. ÜRÜNLEŞME & PAZAR STRATEJİSİ
7.1 Hedef Segmentler

Indie strategy oyuncuları

Üniversiteler

Enerji şirketleri

Danışmanlık & eğitim kurumları

7.2 Sunum Biçimleri

Oyun (Steam / itch.io)

Eğitim simülatörü

Kurumsal demo

Danışmanlık aracı

Aynı çekirdek, farklı ambalaj.

8. TEKNİK YOL HARİTASI

Python engine → referans model

Godot → ürün UI

Streamlit → prototip / demo

Modüler core → uzun vadeli sürdürülebilirlik

9. BİLİNÇLİ OLARAK ERTELENENLER

Gerçek zamanlı trading

Tam load-flow simülasyonu

Aşırı finansal türevler

Mikro yönetim ağırlıklı mekanikler

Sebep:

Gerçekçilik ≠ karmaşıklık

10. SON SÖZ

Bu roadmap ile proje:

Kısa vadede oynanabilir

Orta vadede derin

Uzun vadede benzersiz

bir ürün hâline gelir.

Energy Market Simulator,
Energy System Simulator’a evrilir.